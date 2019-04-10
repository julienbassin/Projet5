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
        self.tables.users = [(name VARCHAR(255), user_name VARCHAR(255)]


    def ConnexionSQL(self):
        """
        Dans connexion_mysql, se connecter la bdd en tant qu'user ou root ?

        """

        try:
            self.conn = mysql.connector.connect(host=self.server,user=self.user,passwd=self.password)
        except mysql.connector.Error as err:
            logger.error("Something went wrong: {}".format(err))

    def RequestSQL(self, req):
        try:
            if req is not None:
                mycursor = self.conn.cursor()
                mycursor.execute(req)
                mycursor.commit()
        except  mysql.connector.Error as err:
            logger.error("Something went wrong: {}".format(err))

    def CreateSQLBDD(self, database="pur_beurre"):
        """
        Dans create_mysql_db, initialiser les params pour créer la bdd

        """
        self.RequestSQL("CREATE DATABASE {}".format(database))
        databases = cursor.fetchall()
            for database in databases:
                print(database)


    def CreateSQLTables(self):
        for table in self.tables:
            self.RequestSQL("CREATE {}".format(table))
        tables = cursor.fetchall()
        for table in tables:
            print(table)

#ajouter les informations sur les tables avec un dictionnaire
#stocker les informations de bdd afin d'automatiser les requetes
#attention, chaque possède des données differentes. l unpacking doit pouvoir être utilisé