import logging
import mysql.connector

from openfoodfacts_bdd import DataBaseCreator

from openfoodfacts_requests import CollectingDataOFF
import config


request = CollectingDataOFF()
final_json = request.connect_and_harvest()
products = request.get_info_products(final_json)

connection = mysql.connector.connect(host=config.DATABASE_CONFIG['host'],
                                        user=config.DATABASE_CONFIG['user'],
                                        passwd=config.DATABASE_CONFIG['password'])


database = DataBaseCreator(connection, "request.sql")
database.create_database()
database.select_database()
database.create_tables()

database.insert_rows(products)

# database.disconnect_sql()



