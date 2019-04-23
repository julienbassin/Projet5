from view import Tree

import logging
import json
from openfoodfacts_requests import OpenFoodFactsRequest
#from openfoodfacts_bdd import openfoodfacts_mysql
from config import URL,PARAMS, CAT_PRODUCTS


for CatProducts in CAT_PRODUCTS:
        PARAMS["search_terms"] = CatProducts
        PARAMS["tag_0"] = CatProducts
        print(PARAMS["search_terms"])

        request = OpenFoodFactsRequest(PARAMS)
        final_json = request.Connect(URL)
        #print(final_json)
        print(request.GetInfoProducts(final_json))






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