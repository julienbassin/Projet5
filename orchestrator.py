import logging

from openfoodfacts_requests import OpenFoodFactsRequest
#from openfoodfacts_bdd import openfoodfacts_mysql
from config import URL,PARAMS, CAT_PRODUCTS


for cat_product in CAT_PRODUCTS:
        PARAMS["search_terms"] = cat_product
        print(PARAMS["search_terms"])
        request = OpenFoodFactsRequest(PARAMS)
        final_json = request.Connexion(URL)
        print(final_json)
        #print(request.parsing_json_object(final_json))




