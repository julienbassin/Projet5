import records
from openfoodfacts_users import DataBaseUsers
import config


class DataBaseCreator:

    def __init__(self):
        """
            Dans init, initialiser les params pour les credentials à utiliser

        """
        self.user = config.DB_CONF['user']
        self.Pass = config.DB_CONF['password']
        self.host = config.DB_CONF['host']
        self.db_info = f"{self.user}:{self.Pass}@{self.host}/pur_beurre"
        self.db = records.Database(f"mysql+mysqlconnector://{self.db_info}")
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
                          name VARCHAR(150),
                          grade CHAR(1),
                          url VARCHAR(255));
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

        barcode = product['barcode']
        name = product['name']
        url = product['url']
        grade = product['grade']
        self.db.query(""" INSERT INTO `products`
                                   (barcode, name,grade,url)
                                   VALUES
                                  (:barcode, :name, :grade, :url)
                                  ON DUPLICATE KEY UPDATE barcode=:barcode
                               """, barcode=barcode, name=name, url=url, grade=grade)

    def insert_categories(self, product):
        """
            Method which is insert categories into the table
        """
        barcode = product['barcode']
        category = product['category']

        self.db.query(""" INSERT INTO `categories`
                          (category)
                          VALUES
                          (:category)
                          ON DUPLICATE KEY UPDATE category=:category
                      """, category=category)

        self.db.query(""" INSERT INTO Products_categories
                          (product_id, category_id)
                          VALUES
                          (:barcode, (SELECT id FROM Categories
                           WHERE category=:category_id));
                      """, barcode=barcode, category_id=category)

    def insert_stores(self, product):
        """
            Method which is insert stores into the table
        """
        barcode = product['barcode']
        all_stores = []
        for store in product['store'].split(","):
            store.strip()
            all_stores.append(store)

        for store_final in all_stores:
            self.db.query(""" INSERT INTO stores (store)
                              VALUES (:store)
                              ON DUPLICATE KEY UPDATE store=:store
                          """, store=store_final)

            self.db.query("""INSERT INTO Products_stores
                              (product_id, store_id) VALUES (:barcode,
                              (SELECT id FROM Stores WHERE store=:store_id))
                          """, barcode=barcode, store_id=store_final)

    def insert_products_informations(self, products):
        """
            Method which call all the methods below
        """

        for product in products:
            self.insert_products(product)
            self.insert_stores(product)
            self.insert_categories(product)
        return True
