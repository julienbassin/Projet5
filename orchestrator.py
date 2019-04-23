from view import Tree

a_node = Tree("Vue utilisateur")
a_node.insert_right("menu-a")

b_node = a_node.right_child
b_node.insert_right("sous-menu-a")

c_node = b_node.right_child
c_node.insert_right("item-sous-menu-a")

d_node = c_node.right_child

print(a_node.value)
print(b_node.value)
print(c_node.value)
print(d_node.value)