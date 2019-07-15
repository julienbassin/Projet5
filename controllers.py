from openfoodfacts_bdd import DataBaseCreator
from openfoodfacts_requests import CollectingDataOFF
from view import View


class Controller:

    """
        This class is dedicated to the controller
    """
    def __init__(self):
        pass

    def run(self):
        """
            This method is dedicated to run all the actions
        """
        request = CollectingDataOFF()
        request.menu()
        final_json = request.connect_and_harvest()
        products = request.get_info_products(final_json)
        database = DataBaseCreator()
        database.menu()
        database.create_tables()
        database.insert_products_informations(products)
        affichage = View()
        affichage.menu()

