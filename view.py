import logging
import config

class View:

    def __init__(self):
        pass

    def menu(self):
        """ This function allows to direct the user """
        print('\n', conf.DECO, '\n',
              "***  Bonjour et bienvenue au ° Substitute Factory ° ***",
              '\n', conf.DECO, '\n')
        print("Tapez:", '\n',
              " |-'1': Quel aliment souhaitez-vous remplacer ?" '\n',
              " |-'2': Retrouver mes aliments substitués" '\n',
              " |-'Q': Pour quitter", '\n')
        user = input()
        key_list = ['1', '2', 'Q']
        if user not in key_list:
            print('\n', conf.SPACE_ADJUST,  conf.INDEX_ERROR, '\n')
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
        category = self.value_error(self.choice_category_action)
        print('\n', conf.SPACE_ADJUST,
              "|*** vous avez choisis ***| : ",
              category.capitalize(), '\n')
        self.choice_product(category)

    def choice_category_action(self):
        for i, categorie in enumerate(config.CATEGORIES):
            print("*", i+1, "-", categorie)
        user_input = input('\n'
                     " |*** Pour choisir une catégorie, "
                     "tapez le chiffre associé et appuyer sur ENTREE ***| "
                     '\n')
        return config.CATEGORIES[user_input-1]

    def product_store(self, category):
        pass

    def exit(self):
        print('\n', conf.DECO, '\n', conf.SPACE_ADJUST,
              "*** ° Au revoir et à bientot ° ***",
              '\n', conf.DECO, '\n')
        quit()

    def choice_product(self,category):
        product = self.database.get_all_products(category)



#categories
                #1 - riz
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