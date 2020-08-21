#=============================================================#
# Copyright   : ©BANAS Yann 
# Projet      : Annuaire Telephonique dynamique
# entreprise  : Mairie le creusot
# Date        : 03/08/2020
# Description : Permet de creer un site web (un annuaire telephonique)
# design avec une base de donner et responsive avec python-flask-sqlite3
# pour l'intranet de la mairie du creusot
#=============================================================#

#=============================================================#
#                       SECTION DES IMPORT                    #
#=============================================================#
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3

#indique au serveur flask les fichier a envoyer au clien 
app = Flask(__name__,template_folder='./frontend/templates',static_folder='./frontend/static')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///annuairedb.sqlite3'


#=============================================================#
#                  CREATION DATABASE TABLE                    #
#=============================================================#

#ce code permet de initialiser le fichier sqlite a cette application web
db = SQLAlchemy(app)
con = sqlite3.connect('C:\\Users\\ybanas\\Desktop\\flask_Annuaire_template\\dist\\annuairedb.sqlite3') #mettre emplacement de ta base de donner generer avec python

#ce code permet de creer les table de la base de donner
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100))
    prenom = db.Column(db.String(100))
    nom = db.Column(db.String(100))
    mail = db.Column(db.String(100))
    tel = db.Column(db.String(100))
    telportable = db.Column(db.String(100))


class ServiceA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100))
    prenom = db.Column(db.String(100))
    nom = db.Column(db.String(100))
    mail = db.Column(db.String(100))
    tel = db.Column(db.String(100))
    telportable = db.Column(db.String(100))

class ServiceB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100))
    prenom = db.Column(db.String(100))
    nom = db.Column(db.String(100))
    mail = db.Column(db.String(100))
    tel = db.Column(db.String(100))
    telportable = db.Column(db.String(100))

class ServiceC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100))
    prenom = db.Column(db.String(100))
    nom = db.Column(db.String(100))
    mail = db.Column(db.String(100))
    tel = db.Column(db.String(100))
    telportable = db.Column(db.String(100))



#ce code permet de creer le fichier sqlite3
db.drop_all() #detruie le fichier precedent
db.create_all()#build la fichier sqlite3

#=============================================================#
#                           API                               #
#=============================================================#

#ce code fournie la page par default
@app.route('/')#<== cette ligne permet de creer une route html (ce quon tape ou redirige dans la barre url)
def index():
    con = sqlite3.connect('C:\\Users\\ybanas\\Desktop\\flask_Annuaire_template\\dist\\annuairedb.sqlite3')
    db = con.cursor()
    res = db.execute('select * from user')
    return render_template("index.html",title='Annuaire', users=res.fetchall())#renvoie la meme page html car les info s'adapte en fonction de res

@app.route('/A')
def page_A():
    con = sqlite3.connect('C:\\Users\\ybanas\\Desktop\\flask_Annuaire_template\\dist\\annuairedb.sqlite3')
    db = con.cursor()
    res = db.execute('select * from serviceA')
    return render_template("index.html",title='Annuaire', users=res.fetchall())#renvoie la meme page html car les info s'adapte en fonction de res

@app.route('/B')
def page_B():
    con = sqlite3.connect('C:\\Users\\ybanas\\Desktop\\flask_Annuaire_template\\dist\\annuairedb.sqlite3')
    db = con.cursor()
    res = db.execute('select * from serviceB')
    return render_template("index.html",title='Annuaire', users=res.fetchall())#renvoie la meme page html car les info s'adapte en fonction de res

@app.route('/C')
def page_C():
    con = sqlite3.connect('C:\\Users\\ybanas\\Desktop\\flask_Annuaire_template\\dist\\annuairedb.sqlite3')
    db = con.cursor()
    res = db.execute('select * from serviceC')
    return render_template("index.html",title='Annuaire', users=res.fetchall())#renvoie la meme page html car les info s'adapte en fonction de res

#ce code est une fonction de test qui renvoie HELLO
@app.route('/hello')
def hello():
   return "<h1>HELLO</h1>"

#ce code permet quand un fait une requet web de type /informatique/yann/banas/yann.banas@ville-lecreusot.fr/5925
#de creer un utilisateur grace a la fonction AddUser
@app.route('/<service>/<prenom>/<nom>/<mail>/<tel>/<telportable>')
def AddUser(service,prenom,nom,mail,tel,telportable):
    NewUser = User(service=service,prenom=prenom,nom=nom,mail=mail,tel=tel,telportable=telportable)
    db.session.add(NewUser)
    db.session.commit()
    return f'<h1><br><br> L\'utilisateur {prenom} {nom} à été Ajouter!</h1>'

#=============================================================#
#                    AddNewUserToDATABASE                     #
#=============================================================#
def AddLastNameA(service,prenom,nom,mail,tel,telportable):
    NewLastNameA = ServiceA(service=service,prenom=prenom,nom=nom,mail=mail,tel=tel,telportable=telportable)
    db.session.add(NewLastNameA)
    db.session.commit()
    print("Un nouvelle utilisateur à été inserer dans la table ServiceA")

def AddLastNameB(service,prenom,nom,mail,tel,telportable):
    NewLastNameB = ServiceB(service=service,prenom=prenom,nom=nom,mail=mail,tel=tel,telportable=telportable)
    db.session.add(NewLastNameB)
    db.session.commit()
    print("Un nouvelle utilisateur à été inserer dans la table ServiceB")

def AddLastNameC(service,prenom,nom,mail,tel,telportable):
    NewLastNameC = ServiceC(service=service,prenom=prenom,nom=nom,mail=mail,tel=tel,telportable=telportable)
    db.session.add(NewLastNameC)
    db.session.commit()
    print("Un nouvelle utilisateur à été inserer dans la table ServiceC")


#Pour ajouter d'autre autilisateur avec d'autre service utiliser ce code
#def AddNomDuService(les parametre de la table class defini plus haut)
#   VariableStockeNewUSer = NomClassDeLaDbDefiniPlusHAut(parametre=value,...)
#   db.session.Add(VariableStockeNewUSer) permet de creer object
#   db.session.commit() permet d'ajouter object dans la db


#=============================================================#
#                    Annuaire DATABASE                        #
#=============================================================#

#permet de recreer a chaque fois car il n'y a pas outils graphique pour editer en
#temps reel le fichier sqlite3 comme avec phpmyadmin avec base de donner mysql
AddLastNameA("service A   ","BANAS    ","Yann    ",     "yannbanas@gmail.com",        "5925  ","0711223344")

AddLastNameB("service B  ","trou  "    ,"ducul  ",     "trou.ducul@ville-lecreusot.fr",         "5934  ","0711223344")

AddLastNameC("service C  ","alie  ","gator       ",     "alie.gator@ville-lecreusot.fr",         "5973  ","0711223344")

AddUser("service A   ","BANAS    ","Yann    ",     "yannbanas@gmail.com",        "5925  ","0711223344")
AddUser("service B  ","trou  "    ,"ducul  ",     "trou.ducul@ville-lecreusot.fr",         "5934  ","0711223344")
AddUser("service C  ","alie  ","gator       ",     "alie.gator@ville-lecreusot.fr",         "5973  ","0711223344")
#=============================================================#
#                    RUN MAIN PROGRAMME                       #
#=============================================================#
if __name__ == "__main__":
    #Initialise le fichier sqlite3
    db.init_app(app)
    #demarer le serveur web (framework flask) sur le port 1024 sur hote 172.16.13.88
    app.run(host= '172.16.13.88', port=1024, debug=False)