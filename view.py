import logging


class Tree:
    """
        Class qui gère l'affichage du menu
    """

    def __init__(self, name="root"):
        self.node_parent = name
        self.node_child = []
        if node_child is not None:
            for child in node_child:
                self.add_node(child)

    def add_node(self, node):
        assert isinstance(node, Tree):
             self.node_child.append(node)


    def __repr__(self):
        return self.node_parent