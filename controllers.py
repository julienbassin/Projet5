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

        request = CollectingDataOFF()
        request.menu()
        final_json = request.connect_and_harvest()
        products = request.get_info_products(final_json)


        database = DataBaseCreator()
        database.menu()
        database.create_tables()

        database.insert_rows(products)


        affichage =  View()
        affichage.menu()
        database.disconnect_sql()

if __name__ == "__main__":
    app = Controller()
    app.run()




