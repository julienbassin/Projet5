import mysql.connector
import logging


from mysql.connector import errorcode
from logging.handlers import RotatingFileHandler

import config

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)

class OpenFoodFactsBdd:

    def __init__(self):
        """
            Dans init, initialiser les params pour les credentials à utiliser

        """
        self.conn = None
        self.file = "request.sql"

    def connect_sql(self):
        """
        Dans connexion_mysql, se connecter la bdd en tant qu'user ou root ?

        """
        try:
            self.conn = mysql.connector.connect(host=config.DATABASE_CONFIG['host'],user=config.DATABASE_CONFIG['user'],passwd=config.DATABASE_CONFIG['password'])
            print("connexion bdd successfully ! ")
        except mysql.connector.Error as err:
            logger.error("Something went wrong: {}".format(err))
            exit(1)
        return self.conn

    def request_sql(self, req):
        """
            Method which is used for the request
        """

        try:
            if req is not None:
                mycursor = self.conn.cursor()
                mycursor.execute(req)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)

    def create_database(self, database="pur_beurre"):
        """
        Dans create_mysql_db, initialiser les params pour créer la bdd

        """
        sql_database_req = "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(database)
        self.request_sql(sql_database_req)

    def select_database(self, database="pur_beurre"):
        """
            Method
        """
        print("**** Use Database Pur Beurre ****", end='')
        sql_select_database_req = "USE {}".format(database)
        self.request_sql(sql_select_database_req)

    def create_sql_tables(self):
        """
            Method
        """
        with open(self.file) as sql_file:
            object_sql = sql_file.read()
            sql_commands = object_sql.split(";")
            for command in sql_commands:
                print(command)
            sql_file.close()

    def drop_tables(self):
        """
            Method to drop all tables
        """
        sql_table_drop_req = (
                "SET FOREIGN_KEY_CHECKS = 0;"
                "DROP TABLE IF EXISTS "
                "Product,Favorite, Store"
                "Product_Category, Product_Store;")
        self.request_sql(sql_table_drop_req)

    def create_tables(self):
        """
            Method to create all the tables for OpenfoodfactsBdd
        """
        print("**** Deleting tables success ****")
        self.drop_tables()
        print("**** Creating tables ****", end='')
        self.create_sql_tables()

    def insert_products(self, id, name, category, barcode, store, url, grade):
        """
            Method to insert all the products into the product's table
        """

        sql_insert_products = "INSERT INTO product VALUES ({}, {}, {}, {}, {}, {})".format(name, category, barcode, store, url, grade)
        self.request_sql(sql_insert_products)

    def insert_favorites(self):
        pass

    def insert_products_favorites(self):
        pass

    def insert_rows(self, products):
        for product in products:
            self.insert_products(*product)
            self.insert_products_favorites(*product)

    def disconnect_sql(self):
        """
            Method to disconnect from the database
        """
        try:
            self.conn.close()
            print("Connexion closed !")
        except mysql.connector.Error as err:
            print(err)
