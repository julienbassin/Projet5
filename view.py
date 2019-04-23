import logging


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
