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
        self.tables = {}

    def connect_sql(self):
        """
        Dans connexion_mysql, se connecter la bdd en tant qu'user ou root ?

        """
        try:
            self.conn = mysql.connector.connect(host=self.server,user=self.user,passwd=self.password)
            print("connexion bdd successfully ! ")
        except mysql.connector.Error as err:
            logger.error("Something went wrong: {}".format(err))
            exit(1)
        return self.conn

    def request_sql(self, req):
        try:
            if req is not None:
                print("**** Creating tables ****, end='')
                mycursor = self.conn.cursor()
                mycursor.execute(req)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")



    def create_user_sql(self):
        pass

    def create_database(self, database="pur_beurre"):
        """
        Dans create_mysql_db, initialiser les params pour créer la bdd

        """
        sql_database_req = "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(database)
        self.request_sql(sql_database_req)

    def create_table_products(self):
        """
            Method to create table products
        """
        self.tables['product'] = (
            "CREATE TABLE `product` ("
            "  `product_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `name` date NOT NULL,"
            "  `barcode` varchar(14) NOT NULL,"
            "  `grade` varchar(16) NOT NULL,"
            "  `website` enum('M','F') NOT NULL,"
            "  `store` date NOT NULL,"
            "   `category` varchar(255) NOT NULL,"
            "  PRIMARY KEY (`product`)"
            ") ENGINE=InnoDB")
        self.request_sql(self.tables['product'])

    def create_table_categories(self):
        """
            Method to create table categories
        """
        self.tables['category'] = (
            "CREATE TABLE `category` ("
            "  `category_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `name` date NOT NULL,"
            "   `category` varchar(255) NOT NULL,"
            "  PRIMARY KEY (`category`)"
            ") ENGINE=InnoDB")
        self.request_sql(self.tables['category'])

    def create_table_stores(self):
        """
            Method to create table stores
        """
        self.tables['store'] = (
            "CREATE TABLE `product` ("
            "  `store_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `name` date NOT NULL,"
            "  PRIMARY KEY (`store`)"
            ") ENGINE=InnoDB")
        self.request_sql(self.tables['store'])

    def create_tables(self):
        """
            Method to create all the tables for OpenfoodfactsBdd
        """
        self.drop_tables()
        print("**** Deleting tables success ****")

    def insert_products(self):
        pass

    def insert_categories(self):
        pass

    def drop_tables(self):
        """
            Method to drop all tables
        """
        sql_drop_tables_req = """ DROP TABLE IF EXISTS
                          Categories, Categories_summary,
                          Products, Products_categories_key,
                          Products_categories_summary_key,
                          Products_stores, Stores, Favorites;
                      """
        self.request_sql(sql_drop_tables_req)


    def disconnect_sql(self):
        """
        """
        try:
            self.conn.close()
            print("Connexion closed !")
        except mysql.connector.Error as err:
            print(err)
