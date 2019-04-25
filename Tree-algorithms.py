class Tree:
    """
        Class qui gere l'affichage du menu
    """

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = Tree(value)
        else:
            new_node = Tree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = Tree(value)
        else:
            new_node = Tree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

menu_principal = Tree("P5 - Menu")
menu_principal.insert_right("1 - Quel aliment souhaitez-vous remplacer ?")
menu_principal.insert_left("2 - Retrouver mes aliments substitués")

select_category = menu_principal.right_child
select_category.insert_right("Selectionner la categorie")

select_food = menu_principal.right_child
select_food = menu_principal.insert_right("Sélectionnez l'aliment")

#sous menu pour selectionner l'aliment
select_food.right_child = menu_principal.right_child
select_food = Tree("choix de l'aliment")

#choix pour les aliments



find_substitued_foods = menu_principal.left_child
find_substitued_foods.insert_left("")

c_node = b_node.right_child
c_node.insert_right("item-sous-menu-a")

d_node = c_node.right_child

print(a_node.value)
print(b_node.value)
print(c_node.value)
print(d_node.value)