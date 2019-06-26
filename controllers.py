import logging
import mysql.connector

from openfoodfacts_bdd import DataBaseCreator

from openfoodfacts_requests import CollectingDataOFF
from view import View
import config


class Controller:

    """
        This class is dedicated to the controller

    """
    def __init__(self):
        pass

    def run(self):
        pass




request = CollectingDataOFF()
final_json = request.connect_and_harvest()
products = request.get_info_products(final_json)


database = DataBaseCreator()
#database.create_database()
#database.select_database()
database.create_tables()

database.insert_rows(products)
#database.insert_products_categories()
#database.disconnect_sql()

affichage =  View()
affichage.menu()

