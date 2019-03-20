import requests
import json

class OpenFoodFactsRequest:

    """
        initialiser des params pour requeter l'API openfoodfacts
    """


    """
        connexion permet de se connecter à l'API openfoodfacts
    """
    def Connexion(self, url, p):
        try:
            search_result = requests.get(url, params=p, timeout=3)
            search_result.raise_for_status()
            result_json = search_result.json()
            print(result_json['products'])
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
        return result_json["products"]

    """
        parsing_json_object permet de récupérer seulement les informations nécessaires:
            -   Le nom du produit (FR) -> key: countries_tags
            -   son nutriscore -> key: nutrition_grades
            -   l'enseigne qui le propose (carrefour par exemple) -> key: uploader
            -   l'url -> key : image_nutrition_url
    """
    def parsing_json_object(self, object_json):
        info_produits = {}

        for o in object_json:
            print(o)


    """
        write_file_json permet d'ecrire les 10 produits dans 10 fichiers differents
    """
    def write_file_json(self, parsed_object_json):
        with open("datas.json", "w") as write_file:
            write_file.write(parsed_object_json)

