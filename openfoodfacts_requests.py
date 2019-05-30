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
                result = response.json()
                products_section = result['products']
                # for product in products_section:
                #     product['main_category'] = category
                #     all_products.update(product)
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
        for products in products_final:
            if products.get('nutrition_grades') and products.get('product_name_fr') and products.get('stores'):
                    self.products = {
                        'barcode' : products['id'],
                        'name': products['product_name_fr'],
                        'category' : products['categories'].upper().split(","),
                        #'sub_category' : products['main_products'].upper(),
                        'grade': products['nutrition_grades'],
                        'store': products['stores'],
                        'url': products['url']
                }
            list_products.append(self.products)
        return list_products
