import mysql.connector
from openfoodfacts_requests import *

class openfoodfacts_mysql:

    def __init__(self, user, password, sqlserver):
        """
            Dans init, initialiser les params pour les credentials à utiliser

        """
        self.user = user
        self.password = password
        self.server = sqlserver

    def connexion_sql(self, ):
        """
        Dans connexion_mysql, se connecter la bdd en tant qu'user ou root ?

        """
        try:
            self.conn = mysql.connector.connect(host=self.server,user=self.user,passwd=self.password)
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    def create_sql_db(self, database):
        """
        Dans create_mysql_db, initialiser les params pour créer la bdd

        """
        try:
            mycursor = self.conn.cursor()
            mycursor.execute("CREATE DATABASE" + database)
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    def create_sql_tables(self):
        pass

    def create_users_bdd():
        """
        create_users_bdd permet de créer des utilisateurs et d'octroyer des droits

        """
        pass

    def info_products_to_bdd(self, products):
            #check if sqlconnexion is not broken
            try:
            mycursor = self.conn.cursor()
            mycursor.commit(products)
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    def get_info_bdd():
        """
        get_info_bdd permet de récuperer les informations en bdd

        """
        pass


    def write_info_bdd():
        """
        Dans init, initialiser les params pour créer la bdd

        """
        pass

    def update_info_bdd():
        """
        update_info_bdd permet de mettre à jour les informations de la bdd

        """
        pass


    def delete_info_bdd():
        """
        delete_info_bdd permet de supprimer les informations de la bdd

        """
        pass
