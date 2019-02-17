import mysql.connector

try:
    print("Connexion à la base de donnée !")
    db_connexion = mysql.connector.connect(user='root', password='toor', host='127.0.0.1')
    print("Fermeture de la connexion SQL !")
    db_connexion.close()
except print(0):
    pass







