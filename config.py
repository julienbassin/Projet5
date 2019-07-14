URL = "https://fr.openfoodfacts.org/cgi/search.pl"

CATEGORIES = ('riz', 'pates', 'pizzas', 'patates douces', 'haricots verts', 'haricots rouges', 'lentilles', 'quinoa', 'boeuf', 'poulet')

PARAMS = {
                "search_simple" : '1',
                "action"        :'process',
                "tagtype_0"     : "categories",
                "tag_contains_0": "contains",
                "json"          : '1',
                "page_size"     : 20
        }

DB_CONF = {
                "host"          : "localhost",
                "user"          : "root",
                "password"      : "Passw0rd+"
                }


DECO = "***-------------------------------------------------***"
SPACE_ADJUST = "          "