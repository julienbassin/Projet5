import requests
import json

class OpenFoodFactsRequest:

    """
        initialiser des params pour requeter l'API openfoodfacts
    """

    def __init__(self, params):
        self.params = params
        self.info_products = {}

    def Connexion(self, url, p):
        """
            connexion permet de se connecter à l'API openfoodfacts
        """
        try:
            search_result = requests.get(url, params=self.params, timeout=3)
            search_result.raise_for_status()
            result_json = search_result.json()
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
        return result_json["products"]

    def parsing_json_object(self,object_json):
        """
        parsing_json_object permet de récupérer seulement les informations nécessaires:
            -   Le nom du produit (FR) -> key: countries_tags
            -   son nutriscore -> key: nutrition_grades
            -   l'enseigne qui le propose (carrefour par exemple) -> key: stores
            -   l'url -> key : image_nutrition_url
        """
        for products in object_json:
            if products['countries_tags'] and products['nutrition_grades'] and products['stores'] and products['image_nutrition_url']:
                    self.info_products['countries'] = products['countries_tags']
                    self.info_products['nutrition'] = products['nutrition_grades']
                    self.info_products['stores'] = products['stores']
                    self.info_products['url'] = products['image_nutrition_url']

    def __repr__(self):
        return self.info_products
