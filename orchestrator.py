import logging
import json
from openfoodfacts_requests import OpenFoodFactsRequest
#from openfoodfacts_bdd import openfoodfacts_mysql
from config import URL,PARAMS, CAT_PRODUCTS


for CatProducts in CAT_PRODUCTS:
        PARAMS["search_terms"] = CatProducts
        print(PARAMS["search_terms"])
        request = OpenFoodFactsRequest(PARAMS)
        final_json = request.Connexion(URL)
        with open('datas.json', 'w') as file:
                json.dump(final_json, file, indent=4)

        #print(final_json)

        #print(request.parsing_json_object(final_json))





