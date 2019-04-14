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





