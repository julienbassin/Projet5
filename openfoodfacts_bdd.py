# -tc- Ajouter une docstring au module

import mysql.connector
from mysql.connector import errorcode
# -tc- ne jamais utiliser * dans un import
from openfoodfacts_requests import *

# -tc- éviter dans la mesure du possible (== pratiquement toujours) les noms de modules avec
# -tc- des underscores. Utiliser de préférence un seule mot en minuscules.

# -tc- Les noms de classe doivent commencer avec une majuscule et ne doivent pas contenir de _
class openfoodfacts_mysql:

    def __init__(self, user, password, sqlserver):
        """
            Dans init, initialiser les params pour les credentials à utiliser

        """
        self.user = user
        self.password = password
        self.server = sqlserver
        self.tables = ["users","products","categories","stores","product_users","product_stores","product_categories"]

    def connexion_sql(self):
        """
        Dans connexion_mysql, se connecter la bdd en tant qu'user ou root ?

        """

        try:
            self.conn = mysql.connector.connect(host=self.server,user=self.user,passwd=self.password)
        except mysql.connector.Error as err:
            # -tc- depuis python 3.6, tu peux remplacer tes format par des fstrings, plus lisible. Eviter les print, préférer
            # -tc- l'usage de logging qui est fait pour cela.
            print("Something went wrong: {}".format(err))

    def create_sql_db(self, database="pur_beurre"):
        """
        Dans create_mysql_db, initialiser les params pour créer la bdd

        """
        try:
            mycursor = self.conn.cursor()
            # -tc- Ne pas utiliser la concaténation de chaine ou le format pour construire une requête sql. Ou alors il faut 
            # -tc- s'assurer du contenu de database.
            # -tc- Laisser à l'utilisateur le soin de créer sa base de base données.
            mycursor = self.conn.cursor()
            mycursor.execute("CREATE DATABASE" + database)
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    def create_sql_tables(self):
        mycursor = self.conn.cursor()
        try:
            for table in self.tables:
                mycursor.execute("CREATE {}".format(table))
                mycursor.commit()
                mycursor.close()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    def create_users_bdd(self):
        """
        create_users_bdd permet de créer des utilisateurs et d'octroyer des droits

        """
        mycursor = self.conn.cursor()
        # -tc- l'utilisateur que j'utilise pour le tests des projets d'étudiants n'a pas le droit de créer des utilisateurs.
        statement = """CREATE USER 'exemplar'@'localhost' IDENTIFIED BY 'MoreSecurity'"""
        try:
            mycursor.execute(statement)
            mycursor.commit()
            mycursor.close()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    # -tc- Beaucoup de méthodes pas nécessairement utiles au projet.
    def info_products_to_bdd(self, products):
            #check if sqlconnexion is not broken
            mycursor = self.conn.cursor()
        try:
            mycursor.execute(products)
            mycursor.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    def get_info_bdd(self):

        """
        get_info_bdd permet de recuperer les informations en bdd

        """
        try:
            print(0)
        except print(0):
            pass


    def write_info_bdd(self):
        """
        Dans init, initialiser les params pour créer la bdd

        """
        try:
            print(0)
        except print(0):
            pass

    def update_info_bdd(self):
        """
        update_info_bdd permet de mettre à jour les informations de la bdd

        """
        try:
            print(0)
        except print(0):
            pass


    def delete_info_bdd():
        """
        delete_info_bdd permet de supprimer les informations de la bdd

        """
        try:
            print(0)
        except print(0):
            pass
