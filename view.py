import logging


class Display:
    """
        Class qui gère l'affichage du menu
    """

    def __init__(self):
        self.running = True

    def menu(self):
        while self.running:
            print("1 - Quel aliment souhaitez-vous remplacer ? \
                2 - Retrouver mes aliments substitués.")
        #design pattern composite