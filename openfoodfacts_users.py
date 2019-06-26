import mysql.connector
import logging
import records

from mysql.connector import errorcode
from logging.handlers import RotatingFileHandler

class DataBaseUsers:
    """
        Class which handle any users
    """
    def __init__(self, connection):
        """
            constructor
        """
        self.conn_user = connection
        self.logger = logging.getLogger()

    def get_all_products_per_category(self, category):
        """
            method which get all products of different categories
        """
        cat = self.conn_user.query(""" SELECT product.barcode, product.name_product, product.grade, product.web_site
                                       FROM products as product
                                       JOIN products_categories as pc
                                            ON pc.product_id = product.barcode
                                       JOIN categories as cat
                                            ON pc.category_id = cat.id
                                       WHERE cat.category= :user_cat;

                             """, user_cat=category, fetchall=True).as_dict()
        return cat

    def get_favorite_table(self):
        """
            Method which get all favorite product from user
        """

        self.conn_user.query()

    def substitute_product(self):
        """
            Method which substitute any product from user
        """

        self.conn_user.query()

    def check_product(self, product_user):

        self.conn_user.query()

    def add_product_into_favorties(self, product, substitute):

        self.conn_user.query()
