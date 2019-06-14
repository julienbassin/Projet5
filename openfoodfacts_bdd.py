import mysql.connector
import logging

from mysql.connector import errorcode
from logging.handlers import RotatingFileHandler

from openfoodfacts_users import DataBaseUsers
import config


class DataBaseCreator:

    def __init__(self):
        """
            Dans init, initialiser les params pour les credentials à utiliser

        """
        self.conn = mysql.connector.connect(host=config.DATABASE_CONFIG['host'],
                                        user=config.DATABASE_CONFIG['user'],
                                        passwd=config.DATABASE_CONFIG['password'])
        self.file = "request.sql"
        self.logger = logging.getLogger()
        self.database = DataBaseUsers(self.conn)

    def request_sql(self, req):
        """
            Method which is used for the request
        """

        try:
            cursor = self.conn.cursor()
            cursor.execute(req)
            self.conn.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                self.logger.debug("already exists.")
            else:
                self.logger.debug(err.msg)
        finally:
            cursor.close()

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
        sql_insert_products = """INSERT INTO `product` (name,barcode,url,grade)
                                VALUES ('{}','{}','{}','{}')""".format(
                                product['name'],
                                product['barcode'],
                                product['url'],
                                product['grade'])
        print(sql_insert_products)
        self.request_sql(sql_insert_products)

    def insert_stores(self, product):
        """
            Method which is insert stores into the table
        """

        sql_insert_store = "INSERT INTO `store` (name) VALUES ('{}')".format(product['store'])
        self.request_sql(sql_insert_store)

    def insert_categories(self, product):
        """
            Method which is insert categories into the table
        """
        for category in product['category']:
             sql_insert_category = "INSERT INTO `category` (name) VALUES ('{}')".format(category)
             sql_insert_favorites = "INSERT INTO `favorite` (substitute_product_id, substituted_product_id) VALUES ('{}','{}')".format(product['barcode'], product['barcode'])
             self.request_sql(sql_insert_category)
             self.request_sql(sql_insert_favorites)



    def insert_rows(self, products):
        """
            Method which call all the methods below
        """

        for product in products:
            self.insert_products(product)
            self.insert_stores(product)
            self.insert_categories(product)
        return True

    def disconnect_sql(self):
        """
            Method to disconnect from the database
        """
        try:
            if self.conn.is_connected():
                self.conn.close()
                print("Connection closed !")
        except mysql.connector.Error as err:
            self.logger.debug(err)
