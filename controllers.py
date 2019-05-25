import logging

import mysql.connector

from view import Menu, MenuItem
from openfoodfacts_bdd import OpenFoodFactsBdd

from openfoodfacts_requests import OpenFoodFactsRequest
from config import URL,PARAMS, CAT_PRODUCTS

for CatProducts in CAT_PRODUCTS:
        PARAMS["search_terms"] = CatProducts
        PARAMS["tag_0"] = CatProducts
        #print(PARAMS["search_terms"])
        request = OpenFoodFactsRequest(PARAMS)
        final_json = request.Connect(URL)
        products = request.GetInfoProducts(final_json)

database = OpenFoodFactsBdd("request.sql")

database.connect_sql()
database.create_database()
database.select_database()
database.create_tables()

database.insert_rows(products)

database.disconnect_sql()

"""
Menu princpal de l'application
"""
main_menu = Menu('Projet 5 - OpenfoodFacts')
sub_menu_replace_food = Menu("Quel aliment souhaitez-vous remplacer ?")
"""
Sub-Menu of category
"""
#essyer de boucle sur les categories puis permettre l'envoie d'un nombre
#effectuer une action qui va récupérer les informations en bdd
# for idx, cat in enumerate(len(CAT_PRODUCTS)):
#     sub_menu_replace_food.add_item(MenuItem(cat, lambda: MenuItem.press_enter(idx)))

sub_menu_replace_food_category = Menu("Retrouver mes aliments substitués")
sub_menu_replace_food_category.add_item(MenuItem('Selectionner une catégorie', lambda : MenuItem.press_enter('1')))
sub_menu_replace_food_category.add_item(MenuItem('Riz',  MenuItem.press_enter('1')))
sub_menu_replace_food_category.add_item(MenuItem('Pates', lambda: MenuItem.press_enter('2')))
sub_menu_replace_food_category.add_item(MenuItem('Pizzas', lambda: MenuItem.press_enter('3')))
sub_menu_replace_food_category.add_item(MenuItem('Patates douces', lambda: MenuItem.press_enter('4')))
sub_menu_replace_food_category.add_item(MenuItem('Haricots verts', lambda: MenuItem.press_enter('5')))
sub_menu_replace_food_category.add_item(MenuItem('Haricots rouges', lambda: MenuItem.press_enter('6')))
sub_menu_replace_food_category.add_item(MenuItem('Lentilles', lambda: MenuItem.press_enter('7')))
sub_menu_replace_food_category.add_item(MenuItem('Quinoa', lambda: MenuItem.press_enter('8')))
sub_menu_replace_food_category.add_item(MenuItem('Boeuf', lambda: MenuItem.press_enter('9')))
sub_menu_replace_food_category.add_item(MenuItem('Poulet', lambda: MenuItem.press_enter('10')))
sub_menu_replace_food_category.add_item(MenuItem('Selectionner un aliment', lambda : MenuItem.press_enter('2')))
sub_menu_replace_food.add_item(sub_menu_replace_food_category)

"""
Sub-Menu of substitued foods
"""
sub_menu_substitued_food = Menu("Retrouver mes favoris")
sub_menu_substitued_food.add_item(MenuItem('Sub D', lambda : MenuItem.press_enter('D')))
sub_menu_substitued_food.add_item(MenuItem('Sub E', lambda : MenuItem.press_enter('E')))

"""
    Main Menu
"""
main_menu.add_item(sub_menu_replace_food)
main_menu.add_item(sub_menu_substitued_food)
main_menu.show_menu()

