URL = "https://ssl-api.openfoodfacts.org/cgi/search.pl"
CAT_PRODUCTS = ('riz', 'pates','patates_douces')

PARAMS = {
                "search_simple" : '1',
                "action"        :'process',
                "json"          : '1',
                "number"        : 20
        }