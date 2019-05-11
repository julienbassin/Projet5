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
                mycursor = self.conn.cursor()
                mycursor.execute(req)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    def create_database(self, database="pur_beurre"):
        """
        Dans create_mysql_db, initialiser les params pour créer la bdd

        """
        sql_database_req = "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(database)
        self.request_sql(sql_database_req)

    def select_database(self,database="pur_beurre"):
        print("**** Use Database Pur Beurre ****", end='')
        sql_select_database_req = "USE {}".format(database)
        self.request_sql(sql_select_database_req)

    def create_table_products(self):
        """
            Method to create table products
        """
        self.tables['products'] = (
            "CREATE TABLE `product` ("
            "  `product_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `name` varchar(255) NOT NULL,"
            "  `barcode` varchar(255) NOT NULL,"
            "  `grade` varchar(255) NOT NULL,"
            "  `store` varchar(255) NOT NULL,"
            "   `category` varchar(255) NOT NULL,"
            "  PRIMARY KEY (`product_id`)"
            ") ENGINE=InnoDB")
        self.request_sql(self.tables['products'])

    def create_table_favorites(self):
        """
            Method to create table stores
        """
        self.tables['favorites'] = (
           "CREATE TABLE IF NOT EXISTS `mydb`.`product` ("
            "`product_id` INT NOT NULL AUTO_INCREMENT,"
            "`name` VARCHAR(255) NOT NULL,"
            "`category` VARCHAR(255) NOT NULL,"
            "`store` VARCHAR(255) NOT NULL,"
            "`website` VARCHAR(255) NOT NULL,"
            "`grade` VARCHAR(1) NOT NULL,"
            "`barcode` INT NOT NULL,"
            "PRIMARY KEY (`product_id`))"
            "ENGINE = InnoDB")
        self.request_sql(self.tables['store'])

    def create_table_product_favorite(self):
        """
            this method create a table for favorites products
        """
        self.tables['products_favorites'] = (
            "CREATE TABLE IF NOT EXISTS `mydb`.`Product_has_favorite_product` ("
            "`Product_product_id` INT NOT NULL,"
            "`favorite_product_favorite_id` INT NOT NULL,"
            "PRIMARY KEY (`Product_product_id`, `favorite_product_favorite_id`),"
            "INDEX `fk_Product_has_favorite_product_favorite_product1_idx` (`favorite_product_favorite_id` ASC) VISIBLE,"
            "INDEX `fk_Product_has_favorite_product_Product_idx` (`Product_product_id` ASC) VISIBLE,"
            "CONSTRAINT `fk_Product_has_favorite_product_Product`"
                "FOREIGN KEY (`Product_product_id`)"
                "REFERENCES `mydb`.`product` (`product_id`)"
                "ON DELETE NO ACTION"
                "ON UPDATE NO ACTION,"
            "CONSTRAINT `fk_Product_has_favorite_product_favorite_product1`"
                "FOREIGN KEY (`favorite_product_favorite_id`)"
                "REFERENCES `mydb`.`favorite_product` (`favorite_id`)"
                "ON DELETE NO ACTION"
                "ON UPDATE NO ACTION)"
            "ENGINE = InnoDB")
        self.request_sql(self.tables['products_favorites'])

    def drop_tables(self):
        """
            Method to drop all tables
        """
        self.tables['drop_tables'] = (
                "DROP TABLE IF EXISTS "
                "category, product"
                "store, favorite;")
        self.request_sql(self.tables['drop_tables'])

    def create_tables(self):
        """
            Method to create all the tables for OpenfoodfactsBdd
        """
        print("**** Deleting tables success ****")
        self.drop_tables()
        print("**** Creating tables ****", end='')
        self.create_table_products()
        self.create_table_favorites()
        self.create_table_product_favorite()

    def insert_products(self, product):
        pass

    def insert_favorites(self):
        pass

    def insert_products_favorites(self):
        pass

    def insert_rows(self, product):
        pass

    def disconnect_sql(self):
        """
            Method to disconnect from the database
        """
        try:
            self.conn.close()
            print("Connexion closed !")
        except mysql.connector.Error as err:
            print(err)
