import requests
import json
import logging

class OpenFoodFactsRequest:

    """
        This class retrieve all data with Openfoodfacts API
    """

    def __init__(self, params):
        self.params = params
        self.info_products = None

    def Connexion(self, url):

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

    def GetProducts(self, object_json):

        """
        This method retrieve needed informations based on:
            -  Name of the product (FR) -> key: countries_tags
            -  Nutriscore               -> key: nutrition_grades
            -  Stores                   -> key: stores
            -  URL                      -> key : image_nutrition_url
        """

        for products in object_json:
            if products.get('countries_tags') and products.get('nutrition_grades') and products.get('stores') and products.get('image_nutrition_url'):
                self.info_products = {
                    'product_name_fr': products['product_name_fr'],
                    'countries': products['countries_tags'],
                    'nutrition': products['nutrition_grades'],
                    'stores': products['stores_tags'],
                    'url': products['url']
                }
            return self.info_products
        #utiliser la clé qui récupère 20 items puis traiter les objets afin d'avoir 10 items contenant tous les éléments.

class GetCategories:
    """
        This class retrieves the categories of the products are available

        key -> categories_tags

    """

    pass

class GetStores:
    """

        This class retrieves the stores where the products are available

    """


    pass

