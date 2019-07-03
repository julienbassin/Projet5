import logging
import config

from openfoodfacts_bdd import DataBaseCreator
from openfoodfacts_users import DataBaseUsers

class View:

    def __init__(self):
        self.database = DataBaseCreator()
        self.db_user = DataBaseUsers(self.database.db)

    def menu(self):
        """
            Method which display the main menu
        """

        """ This function allows to direct the user """
        print('\n', config.DECO, '\n',
              "***  Welcome to ° Substitute Factory ° ***",
              '\n', config.DECO, '\n')
        print("Tapez:", '\n',
              " |-'1': Quel aliment souhaitez-vous remplacer ?" '\n',
              " |-'2': Retrouver mes aliments substitués" '\n',
              " |-'Q': Pour quitter", '\n')
        user = input()
        key_list = ['1', '2', 'Q']
        if user not in key_list:
            print('\n', config.SPACE_ADJUST,  config.INDEX_ERROR, '\n')
            self.menu()
        else:
            if user == '1':
                self.choice_category()
                self.product_store()
            elif user == '2':
                #table subsitué
                #check if a product is present via check_products (row present ?)
                self.product_store()
            elif user == 'Q':
                self.exit()

    def choice_category(self):
        """
            Method which allow to display you category
        """
        category = self.choice_category_action()
        print('\n',"|*** vous avez choisis la catégorie ***| : ",category.capitalize(), '\n')
        self.choice_product(category)

    def choice_category_action(self):
        """
            Method which allow to choose your category
        """
        for i, categorie in enumerate(config.CATEGORIES):
            print(i+1, "-", categorie)
        user_input = input('\n'
                     " |*** Pour choisir une catégorie, "
                     "tapez le chiffre associé et appuyer sur ENTREE ***| "
                     '\n\n')
        return config.CATEGORIES[int(user_input)-1]

    def product_store(self):
        """
            Method which display all substitued products
        """
        print("voici vos produits")
        favorites_products = self.db_user.get_all_favorites_product()
        for i, favorite in enumerate(favorites_products):
            print("\n {} - {}\n".format(i+1, favorite))

    def exit(self):
        """
            Method which permit to exit the main program
        """
        print('\n', config.DECO, '\n', config.SPACE_ADJUST,
              "*** ° Au revoir et à bientot ° ***",
              '\n', config.DECO, '\n')
        quit()

    def choice_product(self, category):
        """
            Method which shows all available products
        """
        product = self.choice_product_action(category)
        print("Vous avez choisi {}".format(product['name_product'].capitalize()))
        self.choice_substitute(category, product)


    def choice_product_action(self, category):
        """
            Method which puts all action for products
        """
        products = self.db_user.get_all_products_per_category(category)
        for i, product in enumerate(products):
            print("{} - {}".format(i+1, product['name_product']))
        choice_product = input("\nVeuillez sélectionner le produit de votre choix\n")
        return products[int(choice_product)-1]


    def choice_substitute(self, category, product):
        """
            Method which use method action
        """
        self.choice_substitute_action(category, product)


    def choice_substitute_action(self, category,product):
        """
            Method which permit to substitute
        """
        substitutes = self.db_user.choose_product_from_category(category, product)
        for i, select_substitute in enumerate(substitutes):
            print("{} - {}".format(i+1, select_substitute['name_product']))

        user_choice = input("\nveuillez selectionner un produit de substition\n")
        if user_choice.isdigit():
            substitute = substitutes[int(user_choice) -1]
            print("{}".format(substitute))
            self.choose_product_final(category,product,substitute)
        else:
            if user_choice not in ["C", "H", "Q"]:
                self.choice_substitute_action(category, product)
            elif user_choice == "C":
                self.choice_substitute_action(category, product)
            elif user_choice == "H":
                self.menu()
            elif user_choice == "Q":
                self.exit()

    def choose_product_final(self, category, product, substitute):
        """
            Method which select your product
        """
        print("le produit de substitution {}\n".format(product['name_product']))
        user_save = input("\nSouhaitez-vous l'enregistrer ?\n")
        if user_save.isdigit():
            self.choose_product_final(category, product, substitute)
        else:
            if user_save not in ["O","N","C","Q"]:
                self.choose_product_final(category, product, substitute)
            if user_save == "O" or user_save == "o":
                id_product = product['barcode']
                id_substitute = substitute['barcode']
                self.db_user.add_product_into_favorites(id_product, id_substitute)
                self.menu()
            elif user_save == "N":
                self.db_user.choose_product_from_category(category,product)
            elif user_save == "C":
                self.choice_substitute(category,product)
            elif user_save == "Q":
                self.exit()
