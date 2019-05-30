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

    def __init__(self, file):
        """
            Dans init, initialiser les params pour les credentials à utiliser

        """
        self.conn = None
        self.file = file

    def connect_sql(self):
        """
        Dans connexion_mysql, se connecter la bdd en tant qu'user ou root ?

        """
        try:
            self.conn = mysql.connector.connect(host=config.DATABASE_CONFIG['host'],
                                                user=config.DATABASE_CONFIG['user'],
                                                passwd=config.DATABASE_CONFIG['password'])
            print("connexion bdd successfully ! ")
        except mysql.connector.Error as err:
            logger.error("Something went wrong: {}".format(err))
        return self.conn

    def request_sql(self, req):
        """
            Method which is used for the request
        """

        try:
            with self.conn as cursor:
                cursor.execute(req)
                self.conn.commit()
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
        print("**** Use Database Pur Beurre ****\n", end='')
        sql_select_database_req = "USE {}".format(database)
        self.request_sql(sql_select_database_req)

    def create_sql_tables(self):
        """
            Method
        """
        with open(self.file) as sql_file:
            self.request_sql(sql_file.read())

    def drop_tables(self):
        """
            Method to drop all tables
        """
        sql_table_drop_req = "drop table if exists Product,Favorite,Category, Store, Product_Category, Product_store;"
        self.request_sql(sql_table_drop_req)

    def create_tables(self):
        """
            Method to create all the tables for OpenfoodfactsBdd
        """
        print("**** Deleting tables success ****\n")
        self.drop_tables()
        print("**** Creating tables ****\n", end='')
        self.create_sql_tables()

    def insert_products(self, product):
        """
            Method to insert all the products into the product's table
        """
        sql_insert_products = """INSERT INTO `product` (name,barcode,store,url,grade,category)
                                VALUES ({},{},{},{},{},{})""".format(
                                product['name'],
                                product['barcode'],
                                product['store'],
                                product['url'],
                                product['grade'],
                                product['category'])
        self.request_sql(sql_insert_products)

    def insert_favorites(self):
        """
            Method which is insert favorites products into the table
        """
        pass

    def insert_stores(self, product):
        """
            Method which is insert stores into the table
        """

        sql_insert_store = "INSERT INTO `store` (store) VALUES ({})".format(product['store'])
        self.request_sql(sql_insert_store)

    def insert_categories(self, product):
        """
            Method which is insert categories into the table
        """

        sql_insert_category = "INSERT INTO `category` (category) VALUES ({})".format(product['category'])
        self.request_sql(sql_insert_category)

    def insert_products_categories(self):
        """
            Method which is insert products_categories into the table
        """

        pass

    def insert_products_stores(self):
        """
            Method which is insert favorites products into the table
        """

        pass


    def insert_rows(self, products):
        """
            Method which call all the methods below
        """

        for product in products:
            self.insert_products(product)
            self.insert_stores(product)
            self.insert_categories(product)
			#self.insert_favorites(*product)
            #self.insert_products_categories(*product)
			#self.insert_products_stores(*product)

    def disconnect_sql(self):
        """
            Method to disconnect from the database
        """
        try:
            if self.conn.is_connected():
                self.conn.close()
                print("Connexion closed !")
        except mysql.connector.Error as err:
            print(err)
