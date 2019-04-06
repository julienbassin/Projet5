import requests
import json
import logging

class OpenFoodFactsRequest:

    """
        initialiser des params pour requeter l'API openfoodfacts
    """

    def __init__(self, params):
        self.params = params
        self.info_products = None

    def Connexion(self, url):

        """
            connexion permet de se connecter à l'API openfoodfacts
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

    def parsing_json_object(self, object_json):

        """
        parsing_json_object permet de récupérer seulement les informations nécessaires:
            -   Le nom du produit (FR) -> key: countries_tags
            -   son nutriscore -> key: nutrition_grades
            -   l'enseigne qui le propose (carrefour par exemple) -> key: stores
            -   l'url -> key : image_nutrition_url
        """

        for products in object_json:
            if products.get('countries_tags') and products.get('nutrition_grades') and products.get('stores') and products.get('image_nutrition_url'):
                self.info_products = {
                    'product_name_fr': products['product_name_fr'],
                    'countries': products['countries_tags'],
                    'nutrition': products['nutrition_grades'],
                    'stores': products['stores'],
                    'url': products['image_nutrition_url']
                }
            return self.info_products
        #utiliser la clé qui récupère 20 items puis traiter les objets afin d'avoir 10 items contenant tous les éléments.

