import requests
import json
import logging

import config

class CollectingDataOFF:

    """
        This class retrieve all data with Openfoodfacts API
    """

    def __init__(self):
        self.params = config.PARAMS
        self.logger = logging.getLogger()

    def connect_and_harvest(self):

        """
            This method allows you to connect using the Openfoodfacts API
        """
        try:
            for category in config.CATEGORIES:
                self.params['tag_0'] = category
                response = requests.get(config.URL, params=self.params, timeout=3)
                print(category)
                result = response.json()
                products_section = result['products']
                # for product in products_section:
                #     product['main_category'] = category
                #     all_products.update(product)
                print(products_section)
        except requests.exceptions.HTTPError as errh:
            self.logger.debug("Http Error")
        except requests.exceptions.ConnectionError as errc:
            self.logger.debug("Error Connecting")
        except requests.exceptions.Timeout as errt:
            self.logger.debug("Timeout Error")
        except requests.exceptions.RequestException as err:
            self.logger.debug("Oops: Something Else")
        return products_section

    def get_info_products(self, products_final):

        """
        This method retrieve needed informations based on:
            -  Name of the product (FR) -> key: countries_tags
            -  Nutriscore               -> key: nutrition_grades
            -  Stores                   -> key: stores
            -  URL                      -> key : image_nutrition_url
        """
        list_products = []
        for product in products_final:
            if product.get('nutrition_grades') and product.get('product_name') and product.get('stores'):
                product_final = {
                        'barcode' : product['id'],
                        'name': product['product_name'],
                        'category' : product['categories'].upper().split(","),
                        'grade': product['nutrition_grades'],
                        'store': product['stores'],
                        'url': product['url']
                }
                list_products.append(product_final)
        return list_products
