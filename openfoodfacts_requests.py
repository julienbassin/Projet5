# -tc- Ajouter une docstring au module

import requests
import json

# -tc- éviter dans la mesure du possible (== pratiquement toujours) les noms de modules avec
# -tc- des underscores. Utiliser de préférence un seule mot en minuscules.

class OpenFoodFactsRequest:

    """
        initialiser des params pour requeter l'API openfoodfacts
    """

    def __init__(self, params):
        # -tc- ajouter une docstring à la méthode
        self.params = params
        self.info_products = {}

    def Connexion(self, url):
        # -tc- ne pas séparer l'entête de la méthode et la docstring par un espace
        """
            connexion permet de se connecter à l'API openfoodfacts
        """
        try:
            search_result = requests.get(url, params=self.params, timeout=3)
            search_result.raise_for_status()
            result_json = search_result.json()
        except requests.exceptions.HTTPError as errh:
            # -tc- éviter les prints. Utiliser logging
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
        return result_json["products"]

    def parsing_json_object(self, object_json):
        # -tc- ne pas séparer l'entête de la méthode et la docstring par un espace
        """
        parsing_json_object permet de récupérer seulement les informations nécessaires:
            -   Le nom du produit (FR) -> key: countries_tags
            -   son nutriscore -> key: nutrition_grades
            -   l'enseigne qui le propose (carrefour par exemple) -> key: stores
            -   l'url -> key : image_nutrition_url
        """

        # -tc- Pas très logique, je renommerais object_json en products et écrirais for product in products
        for products in object_json:
            # -tc- si l'une de ces clés n'existe pas, ton code produira une KeyError
            if products['countries_tags'] and products['nutrition_grades'] and products['stores'] and products['image_nutrition_url']:
                # -tc- plutôt que de fabriquer un autre dictionnaire, pourquoi pas un objet Product. Il manque l'info sur la ou
                # -tc- les catégories.
                self.info_products['countries'] = products['countries_tags']
                self.info_products['nutrition'] = products['nutrition_grades']
                self.info_products['stores'] = products['stores']
                self.info_products['url'] = products['image_nutrition_url']

    def __repr__(self):
        # -tc- self.info_products n'est pas une chaine de caractères
        return self.info_products

