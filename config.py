import logging
from logging.config import dictConfig

URL = "https://fr.openfoodfacts.org/cgi/search.pl"

CATEGORIES = ('riz',
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
                "tagtype_0"     : "categories",
                "tag_contains_0": "contains",
                "json"          : '1',
                "page_size"     : 20
        }

DATABASE_CONFIG = {
                "host"          : "localhost",
                "user"          : "root",
                "password"      : "Passw0rd+"
                }



logging_config = dict(
    version = 1,
    formatters = {
        'f': {'format':
              '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
        },
    handlers = {
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.DEBUG}
        },
    root = {
        'handlers': ['h'],
        'level': logging.DEBUG,
        },
)

dictConfig(logging_config)