import mysql.connector
import logging
import time
import records

from mysql.connector import errorcode
from logging.handlers import RotatingFileHandler

from openfoodfacts_users import DataBaseUsers
import config


class DataBaseCreator:

    def __init__(self):
        """
            Dans init, initialiser les params pour les credentials à utiliser

        """
        self.db = records.Database("mysql+mysqlconnector://{}:{}@{}/pur_beurre".format(
                                                                                config.DATABASE_CONFIG['user'],
                                                                                config.DATABASE_CONFIG['password'],
                                                                                config.DATABASE_CONFIG['host']))
        self.logger = logging.getLogger()
        self.database = DataBaseUsers(self.db)

    def menu(self):
        print('\n', config.DECO, '\n',
              "***  Configuration of the databse PUR_BEURRE ° ***",
              '\n', config.DECO, '\n')

    def drop_tables(self):
        """
            Method to drop all tables
        """
        sql_table_drop_req = ("""drop table if EXISTS
                                 products,favorites,
                                 categories,stores,
                                 products_categories,products_stores""")
        self.db.query(sql_table_drop_req)

    def create_table_product(self):
        """ Create table Products """
        self.db.query(""" CREATE TABLE IF NOT EXISTS Products (
                          barcode BIGINT UNSIGNED UNIQUE PRIMARY KEY,
                          name_product VARCHAR(150),
                          grade CHAR(1),
                          web_site VARCHAR(255));
                       """)

    def create_table_category(self):
        """ Create table category """
        self.db.query(""" CREATE TABLE IF NOT EXISTS Categories (
                          id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          category VARCHAR(125) UNIQUE);
                      """)

    def create_table_store(self):
        """ Create table stores """
        self.db.query(""" CREATE TABLE IF NOT EXISTS Stores (
                          id MEDIUMINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          store VARCHAR(150) UNIQUE);
                      """)

    def create_association_table(self):
        """ Creating to the associate index table """
        self.db.query(""" CREATE TABLE IF NOT EXISTS Products_categories (
                          id MEDIUMINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          product_id BIGINT REFERENCES Products(barcode),
                          category_id MEDIUMINT REFERENCES Category(id));
                       """)


        self.db.query(""" CREATE TABLE IF NOT EXISTS Products_stores (
                          id MEDIUMINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          product_id BIGINT REFERENCES Products(barcode),
                          store_id MEDIUMINT REFERENCES Stores(id));
                      """)

    def create_favorites_table(self):
        """ Create the favorites table """
        self.db.query(""" CREATE TABLE IF NOT EXISTS Favorites (
                          id_product BIGINT REFERENCES Products(barcode),
                          id_substitute BIGINT REFERENCES Products(barcode),
                          PRIMARY KEY (id_product, id_substitute));
                      """)

    def create_sql_tables(self):
        """
            Method
        """
        self.create_table_product()
        self.create_table_category()
        self.create_table_store()
        self.create_association_table()
        self.create_favorites_table()

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
        self.db.query(""" INSERT INTO `products`
                                   (barcode, name_product,grade,web_site)
                                   VALUES
                                  (:barcode, :name, :grade, :web_site)
                                  ON DUPLICATE KEY UPDATE barcode=:barcode;
                               """, barcode=product['barcode'],
                                    name=product['name'],
                                    web_site=product['url'],
                                    grade=product['grade'])

    def insert_categories(self, product):
        """
            Method which is insert categories into the table
        """
        self.db.query(""" INSERT INTO `categories`
                          (category)
                          VALUES
                          (:category)
                          ON DUPLICATE KEY UPDATE category=:category

                      """, category=product['category'])

        self.db.query(""" INSERT INTO Products_categories
                          (product_id, category_id)
                          VALUES
                          (:barcode, (SELECT id FROM Categories
                           WHERE category=:category_id));
                      """, barcode=product['barcode'], category_id=product['category'])

    def insert_stores(self, product):
        """
            Method which is insert stores into the table
        """
        all_stores = []
        for store in product['store'].split(","):
            store.strip()
            all_stores.append(store)

        for store_final in all_stores:
            self.db.query(""" INSERT INTO stores (store)
                              VALUES (:store)
                              ON DUPLICATE KEY UPDATE store=:store;
                          """, store=store_final)

            self.db.query("""INSERT INTO Products_stores
                              (product_id, store_id) VALUES (:barcode,
                              (SELECT id FROM Stores WHERE store=:store_id));
                          """, barcode=product['barcode'], store_id=store_final)

    def insert_products_informations(self, products):
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
            if self.db.open:
                self.db.close()
                print("Connection closed !")
        except mysql.connector.Error as err:
            self.logger.debug(err)
