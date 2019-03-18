import requests
import json

class OpenFoodFactsRequest:

    """
        initialiser des params pour requeter l'API openfoodfacts
    """
    def __init__(self, file_json):
        self.file = file_json


    """
        connexion permet de se connecter à l'API openfoodfacts
    """
    def connexion(self, url, **params):
        try:
            search_result = requests.get(url, params=params, timeout=3)
            search_result.raise_for_status()
            result_json = search_result.json()
            print(result_json)
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
        return result_json["Products"]

    """
        parsing_json_object permet de récupérer seulement les informations nécessaires:
            -   Le nom du produit (FR)
            -   son nutriscore
            -   l'enseigne qui le propose (carrefour par exemple)
            -   l'url
    """
    def parsing_json_object(self, object_json):
        pass

    """
        write_file_json permet d'ecrire les 10 produits dans 10 fichiers differents
    """
    def write_file_json(self, parsed_object_json):
        with open(self.file, "w") as write_file:
            write_file.write(parsed_object_json)

