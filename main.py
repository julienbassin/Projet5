from openfoodfacts_requests import OpenFoodFactsRequest
from openfoodfacts_bdd import openfoodfacts_mysql

# -tc- ne pas mettre de code hors d'une fonction, d'une méthode ou d'une classe, ou exceptionnellement

# -tc- J'utiliserais la recherche par catégories avec tagtype_*, tag_contains_* et tag_*
PARAMS = {
    "search_terms"  :'riz',
    "search_simple" : '1',
    "action"        :'process',
    "json"          : '1'
}

# -tc- les variables a, b et c ne sont pas descriptives
a = OpenFoodFactsRequest(PARAMS)
b = a.Connexion("https://ssl-api.openfoodfacts.org/cgi/search.pl")
a.parsing_json_object(b)

c = openfoodfacts_mysql("julien","Passw0rd+","localhost")
c.connexion_sql()




