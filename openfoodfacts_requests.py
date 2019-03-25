import requests
import json

class OpenFoodFactsRequest():

    """
        initialiser des params pour requeter l'API openfoodfacts
    """

    def __init__(self, params):
        self.params = params

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
        info_products = {}

        for products in object_json:
            if products['countries_tags'] and products['nutrition_grades'] and products['stores']:
                #if products['countries_tags'] not in info_products:
                    info_products['countries'] = products['countries_tags']
                    info_products['nutrition'] = products['nutrition_grades']
                    info_products['stores'] = products['stores']
                    info_products['url'] = products['image_nutrition_url']
            print(info_products)

    def write_file_json(self, parsed_object_json):
        """
            write_file_json permet d'ecrire les 10 produits dans 10 fichiers differents
        """
        with open("datas.json", "w") as write_file:
            write_file.write(parsed_object_json)

