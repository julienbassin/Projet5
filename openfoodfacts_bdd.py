import mysql.connector
import logging

from mysql.connector import errorcode
from logging.handlers import RotatingFileHandler
from openfoodfacts_requests import OpenFoodFactsRequest

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)

class OpenFoodFactsBdd:

    def __init__(self, user, password, sqlserver):
        """
            Dans init, initialiser les params pour les credentials à utiliser

        """
        self.user = user
        self.password = password
        self.server = sqlserver
        self.conn = None
        self.tables = ["users","products","categories","stores","favorites"]


    def connect_sql(self):
        """
        Dans connexion_mysql, se connecter la bdd en tant qu'user ou root ?

        """
        try:
            self.conn = mysql.connector.connect(host=self.server,user=self.user,passwd=self.password)
            print("connexion bdd successfully ! ")
        except mysql.connector.Error as err:
            logger.error("Something went wrong: {}".format(err))
        return self.conn

    def request_sql(self, req):
        try:
            if req is not None:
                mycursor = self.conn.cursor()
                mycursor.execute(req)
        except  mysql.connector.Error as err:
            logger.error("Something went wrong: {}".format(err))
            mycursor.rollback()


    def create_database(self, database="pur_beurre"):
        """
        Dans create_mysql_db, initialiser les params pour créer la bdd

        """
        sql_database_req = "CREATE DATABASE IF NOT EXISTS {}".format(database)
        self.request_sql(sql_database_req)

    def create_tables_products(self):
        pass

    def create_tables(self):
        #acceuillera toutes les methodes pour créer toutes les tables
        self.drop_tables()
        print("**** Deleting tables success ****")



    def drop_tables(self):
        sql_drop_tables_req = """ DROP TABLE IF EXISTS
                          Categories, Categories_summary,
                          Products, Products_categories_key,
                          Products_categories_summary_key,
                          Products_stores, Stores, Favorites;
                      """
        self.request_sql(sql_drop_tables_req)


    def disconnect_sql(self):
        try:
            self.conn.close()
            print("Connexion closed !")
        except mysql.connector.Error as err:
            print(err)

#ajouter les informations sur les tables avec un dictionnaire
#stocker les informations de bdd afin d'automatiser les requetes
#attention, chaque possède des données differentes. l unpacking doit pouvoir être utilisé