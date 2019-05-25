import mysql.connector
import config

def main():
    try:
        connexion = mysql.connector.connect(
            host=config.DATABASE_CONFIG['host'],
            user=config.DATABASE_CONFIG['user'],
            passwd=config.DATABASE_CONFIG['password'])
    except mysql.connector.Error as err:
        print(err)
        exit(1)
    try:

        cursor = connexion.cursor()
        sql_select_database_req = "USE pur_beurre"
        sql_insert_products = "INSERT INTO `product` (name,barcode,store,url,grade,category) VALUES ('Filet de Poulet Rôti (4 Tranches Épaisses)',3095752126013,'Casino','https://fr.openfoodfacts.org/produit/3095752126013/filet-de-poulet-roti-4-tranches-epaisses-fleury-michon','c','titi')"
        print(sql_insert_products)
        cursor.execute(sql_select_database_req)
        cursor.execute(sql_insert_products)
        connexion.commit()
    except mysql.connector.Error as err:
        print(err)


if __name__ == '__main__':
    main()

