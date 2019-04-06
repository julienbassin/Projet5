URL = "https://ssl-api.openfoodfacts.org/cgi/search.pl"
CAT_PRODUCTS = ('riz',
                'pates',
                'pizzas',
                'patates douces', 
                'haricots verts', 
                'haricots rouges', 
                'lentilles',
                'quinoa',
                'boeuf',
                'poulet')

PARAMS = {
                "search_simple" : '1',
                "action"        :'process',
                "json"          : '1'
        }