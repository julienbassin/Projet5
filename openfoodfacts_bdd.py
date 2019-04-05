import mysql.connector
from mysql.connector import errorcode
from openfoodfacts_requests import OpenFoodFactsRequest
import logging

class OpenFoodFactsBdd:

    def __init__(self, user, password, sqlserver):
        """
            Dans init, initialiser les params pour les credentials à utiliser

        """
        self.user = user
        self.password = password
        self.server = sqlserver
        self.tables = ["users","products","categories","stores","product_users"]
        self.tables.users = {}

    def connexion_sql(self):
        """
        Dans connexion_mysql, se connecter la bdd en tant qu'user ou root ?

        """

        try:
            self.conn = mysql.connector.connect(host=self.server,user=self.user,passwd=self.password)
        except mysql.connector.Error as err:
            logging.log("Something went wrong: {}".format(err))

    def req_sql(self, req):
        try:
            if req not none:
                mycursor = self.conn.cursor()
                mycursor.execute(req)
                mycursor.commit()
        except  mysql.connector.Error as err:
            logging.log("Something went wrong: {}".format(err))

    def create_sql_db(self, database="pur_beurre"):
        """
        Dans create_mysql_db, initialiser les params pour créer la bdd

        """
        req_sql("CREATE DATABASE {}".format(database))


    def create_sql_tables(self):
        for table in self.tables:
            req_sql("CREATE {}".format(table))

    #ajouter les informations sur les tables avec un dictionnaire
    #stocker les informations de bdd afin d'automatiser les requetes
    #attention, chaque possède des données differentes. l unpacking doit pouvoir être utilisé


    def info_products_to_bdd(self):
            req_sql(self.info_products)

