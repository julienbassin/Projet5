import logging
import config

from openfoodfacts_bdd import DataBaseCreator
from openfoodfacts_users import DataBaseUsers

class View:

    def __init__(self):
        self.database = DataBaseCreator()
        self.db_user = DataBaseUsers(self.database.db)

    def menu(self):
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
                self.product_store()
            elif user == 'Q':
                self.exit()

    def choice_category(self):
        category = self.choice_category_action()
        print('\n',"|*** vous avez choisis la catégorie ***| : ",category.capitalize(), '\n')
        self.choice_product(category)

    def choice_category_action(self):
        for i, categorie in enumerate(config.CATEGORIES):
            print(i+1, "-", categorie)
        user_input = input('\n'
                     " |*** Pour choisir une catégorie, "
                     "tapez le chiffre associé et appuyer sur ENTREE ***| "
                     '\n\n')
        return config.CATEGORIES[int(user_input)-1]

    def product_store(self):
        #print("\n Select your product \n")
        #user_product_input = eval(input())
        #print("vous avez choisi: ", user_product_input)

        #montrer la carte d'identité du produit
        pass

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
        self.db_user.choose_product_from_category(category, product)

    def choice_product_action(self, category):
        """
            Method which puts all action for products
        """
        products = self.db_user.get_all_products_per_category(category)
        for i, product in enumerate(products):
            print("{} - {}".format(i+1, product['name_product']))
        choice_product = input("\n Veuillez sélectionner le produit de votre choix\n")
        return products[int(choice_product)-1]


#categories
                #1 - riz
                    #table de correspondance a faire
                    #riz basmati - codebar - description - note (c)
                    #application -> verification si le produit pris possede la meilleure note?
                        #si produit a une bonne note
                            #tu enregistres dans tes favoris
                        #else
                            #voici le produit avec la meilleure note codebar - description - note (c)
                            #application -> etes vous sur de conserver le produit selectionné ou le substitué ?(y/n)
                                #if oui
                                    #tu enregistres dans tes favoris
                                #else
                                    #je change le produit subsitué
                                    #je l'enregistre dans les favoris
                #2 - pates