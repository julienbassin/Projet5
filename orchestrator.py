from openfoodfacts_requests import OpenFoodFactsRequest
from openfoodfacts_bdd import openfoodfacts_mysql
from config import URL,PARAMS, CAT_PRODUCTS


for cat_product in CAT_PRODUCTS:
        PARAMS["search_terms"] = cat_product

        a = OpenFoodFactsRequest(PARAMS)
        b = a.Connexion("https://ssl-api.openfoodfacts.org/cgi/search.pl")
        a.parsing_json_object(b)

c = openfoodfacts_mysql("julien","Passw0rd+","localhost")
c.connexion_sql()
c.create_sql_db()
c.create_sql_tables()




