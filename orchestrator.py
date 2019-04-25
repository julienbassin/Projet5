from view import Menu, MenuItem

import logging
import json
from openfoodfacts_requests import OpenFoodFactsRequest
#from openfoodfacts_bdd import openfoodfacts_mysql
from config import URL,PARAMS, CAT_PRODUCTS


for CatProducts in CAT_PRODUCTS:
        PARAMS["search_terms"] = CatProducts
        PARAMS["tag_0"] = CatProducts
        print(PARAMS["search_terms"])

        request = OpenFoodFactsRequest(PARAMS)
        final_json = request.Connect(URL)
        print(request.GetInfoProducts(final_json))

if __name__ == '__main__':
    main_menu = Menu("Projet 5 - OpenfoodFacts")
    main_menu.add_item(MenuItem("1 - Quel aliment souhaitez-vous remplacer ?", lambda : MenuItem.press_enter("1")))
    main_menu.add_item(MenuItem("2 - Retrouver mes aliments substitués", lambda : MenuItem.press_enter("2")))
    sub_menu = Menu('Submenu')
    sub_menu.add_item(MenuItem('Sub D', lambda : MenuItem.press_enter('D')))
    sub_menu.add_item(MenuItem('Sub E', lambda : MenuItem.press_enter('E')))
    main_menu.add_item(sub_menu)
    main_menu.show_menu()


