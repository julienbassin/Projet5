import requests
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)

class OpenFoodFactsRequest:

    """
        This class retrieve all data with Openfoodfacts API
    """

    def __init__(self, params):
        self.params = params
        self.products = {}
        self.categories = None
        self.stores = None

    def Connect(self, url):

        """
            This method allows you to connect using the Openfoodfacts API
        """
        try:
            search_result = requests.get(url, params=self.params, timeout=3)
            search_result.raise_for_status()
            result_json = search_result.json()
        except requests.exceptions.HTTPError as errh:
            logging.log("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            logging.log("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            logging.log("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            logging.log("OOps: Something Else",err)
        return result_json['products']

    def GetInfoProducts(self, object_json):

        """
        This method retrieve needed informations based on:
            -  Name of the product (FR) -> key: countries_tags
            -  Nutriscore               -> key: nutrition_grades
            -  Stores                   -> key: stores
            -  URL                      -> key : image_nutrition_url
        """
        list_products = []
        for products in object_json:
            try:
                if products.get('nutrition_grades') and products.get('product_name_fr') and products.get('stores'):
                    self.info_products = {
                    'code' : products['code'],
                    'product_name_fr': products['product_name_fr'],
                    'categories' : products['categories_tags'],
                    'countries': products['countries_tags'],
                    'nutrition': products['nutrition_grades'],
                    'stores': products['stores'],
                    'url': products['url']
                }
            except KeyError as key_error:
                print("key does not exist {}".format(key_error))
            list_products.append(self.info_products)
        return list_products
