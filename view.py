import config
from openfoodfacts_bdd import DataBaseCreator
from openfoodfacts_users import DataBaseUsers


class View:

    def __init__(self):
        self.database = DataBaseCreator()
        self.user = DataBaseUsers(self.database.db)

    def menu(self):
        """
            Method which display the main menu
        """

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
            print('\n', config.SPACE_ADJUST, '\n')
            self.menu()
        else:
            if user == '1':
                self.choice_category()
            elif user == '2':
                self.check_rows()
            elif user == 'Q':
                self.exit()

    def choice_category(self):
        """
            Method which allow to display you category
        """
        category = self.choice_category_action()
        print('\n', "La catégorie choisis: ", category.capitalize(), '\n')
        self.choice_product(category)

    def choice_category_action(self):
        """
            Method which allow to choose your category
        """
        for i, categorie in enumerate(config.CATEGORIES):
            print(i+1, "-", categorie)

        user_input = input("""\n
                           |*** Choisir une catégorie,
                           tapez le chiffre associé et appuyer sur ENTREE ***|
                            \n""")
        return config.CATEGORIES[int(user_input)-1]

    def product_store(self):
        """
            Method which display all substitued products
        """
        print("voici vos produits")
        favorites_products = self.user.get_all_favorites_product()
        for i, favorite in enumerate(favorites_products):
            print(f"""
            Barcode: {favorite['barcode']}
            Product Name: {favorite['name']}
            Grade: {favorite['grade']}
            Url: {favorite['url']}
                 """)

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
        print(f"Produit choisi: {product['name'].capitalize()}")
        self.choice_substitute(category, product)

    def choice_product_action(self, category):
        """
            Method which puts all action for products
        """
        products = self.user.get_all_products_per_category(category)
        for i, product in enumerate(products):
            print(f"{i+1} - {product['name']}")
        choice_product = input("\nSélectionner un produit de votre choix\n")
        return products[int(choice_product)-1]

    def choice_substitute(self, category, product):
        """
            Method which use method action
        """
        self.choice_substitute_action(category, product)

    def choice_substitute_action(self, category, product):
        """
            Method which permit to substitute
        """
        substitutes = self.user.choose_product_from_category(category, product)
        for i, select_substitute in enumerate(substitutes):
            print(f"{i+1} - {select_substitute['name']}")

        user_choice = input("\n Sélectionner un produit de substition\n")
        if user_choice.isdigit():
            substitute = substitutes[int(user_choice)-1]
            print(f"""
            Barcode: {substitute['barcode']}
            Product Name: {substitute['name']}
            Grade: {substitute['MIN(p.grade)']}
            Url: {substitute['url']}
            Category: {substitute['category']}
            """)
            self.choose_product_final(category, product, substitute)
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
        user_save = input("\nSouhaitez-vous l'enregistrer ?\n")
        if user_save.isdigit():
            self.choose_product_final(category, product, substitute)
        else:
            if user_save not in ["O", "N", "C", "Q"]:
                self.choose_product_final(category, product, substitute)
            if user_save == "O" or user_save == "o":
                id_product = product['barcode']
                id_substitute = substitute['barcode']
                self.user.add_product_into_favorites(id_product, id_substitute)
                self.menu()
            elif user_save == "N":
                self.user.choose_product_from_category(category, product)
            elif user_save == "C":
                self.choice_substitute(category, product)
            elif user_save == "Q":
                self.exit()

    def check_rows(self):
        """
            Method which checks if something is present into favorite table
        """
        FavIsPresent = self.user.get_all_favorites_product
        # if self.user.get_all_favorites_product:
        #     print("[+] something here")
        #     self.product_store()
        # else:
        #     print("[-] something missing")
