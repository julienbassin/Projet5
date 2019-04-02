import mysql.connector
from mysql.connector import errorcode
from openfoodfacts_requests import *

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
            print("Something went wrong: {}".format(err))

    def req_sql(self, req):
        try:
            if req not none:
                mycursor = self.conn.cursor()
                mycursor.execute(req)
                mycursor.commit()
        except  mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    def create_sql_db(self, database="pur_beurre"):
        """
        Dans create_mysql_db, initialiser les params pour créer la bdd

        """
        req_sql("CREATE DATABASE {}".format(database))


    def create_sql_tables(self):
        for table in self.tables:
            req_sql("CREATE {}".format(table))

    def create_users_bdd(self):

        """
        create_users_bdd permet de créer des utilisateurs et d'octroyer des droits

        """
        statement = """CREATE USER 'exemplar'@'localhost' IDENTIFIED BY 'MoreSecurity'"""
        req_sql(statement)

    def info_products_to_bdd(self, products):
            req_sql(products)

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
