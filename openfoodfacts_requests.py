import requests
import json
class openfoodfacts_request:

    """
        initialiser des params pour requeter l'API openfoodfacts
    """
    def __init__(self,url):
        self.url = url

    """
        connexion permet de se connecter à l'API openfoodfacts
    """
    def connexion(self, **params):
        try:
            search_result = requests.get(self.url, params=params, timeout=3)
            search_result.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)

    """
        parsing_json_object permet de récupérer seulement les informations nécessaires:
            -   Le nom du produit (FR)
            -   son nutriscore
            -   l'enseigne qui le propose (carrefour par exemple)
            -   l'url
    """
    def parsing_json_object(self):
        pass

    """
        write_file_json permet d'ecrire les 10 produits dans 10 fichiers differents
    """
    def write_file_json(self):
        pass

