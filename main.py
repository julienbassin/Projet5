from openfoodfacts_requests import OpenFoodFactsRequest
from openfoodfacts_bdd import openfoodfacts_mysql

PARAMS = {
        "search_terms"  :'riz',
        "search_simple" : '1',
        "action"        :'process',
        "json"          : '1'
}

a = OpenFoodFactsRequest(PARAMS)
b = a.Connexion("https://ssl-api.openfoodfacts.org/cgi/search.pl")
a.parsing_json_object(b)

c = openfoodfacts_mysql("julien","Passw0rd+","localhost")
c.connexion_sql()




