import mysql.connector
import logging

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

    def request_sql(self, req):
        """
            Method which is used for the request
        """

        try:
            with self.conn_user as cursor:
                cursor.execute(req)
                self.conn_user.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                self.logger.debug("already exists.")
            else:
                self.logger.debug(err.msg)

    def get_all_products(self):
        """
            method which get all products from user
        """

        pass

    def get_favorite_product(self):
        """
            Method which get all favorite product from user
        """

        pass

    def substitute_product(self):
        """
            Method which substitute any product from user
        """

        pass