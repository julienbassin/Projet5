import records


class DataBaseUsers:
    """
        Class which handle any users
    """
    def __init__(self, connection):
        """
            constructor
        """
        self.conn_user = connection

    def get_all_products_per_category(self, category):
        """
            method which get all products of different categories
        """
        cat = self.conn_user.query(""" SELECT p.barcode, p.name, p.grade, p.url
                                       FROM products as p
                                       JOIN products_categories as pc
                                            ON pc.product_id = p.barcode
                                       JOIN categories as cat
                                            ON pc.category_id = cat.id
                                       WHERE cat.category= :user_cat
                                       ORDER BY p.barcode;

                             """, user_cat=category, fetchall=True).as_dict()
        return cat

    def get_all_favorites_product(self):
        """
            Method which get all favorite product from user
        """

        favorites = self.conn_user.query(""" Select p.barcode, p.name, p.grade, p.url
                                             FROM Products as p
                                             JOIN favorites as fav
                                             ON fav.id_substitute = p.barcode
                                             ORDER BY p.barcode""").as_dict()

        return favorites

    def choose_product_from_category(self, category, product):
        """
            Method which is check product with another product
        """
        product = self.conn_user.query("""SELECT p.barcode, p.name, MIN(p.grade), p.url, c.category
                                                FROM products as p
                                                JOIN products_categories as pc
                                                ON pc.product_id = p.barcode
                                                JOIN categories as c
                                                ON pc.category_id = c.id
                                                WHERE p.grade < :grade AND c.category= :cat
                                                ORDER BY p.grade """, grade='c', cat=category, fetchall=True).as_dict()
        return product

    def add_product_into_favorites(self, product, substitute):
        """
            method which is add a product into favorites table

        """
        product_favorite = self.conn_user.query("""
                                INSERT into favorites
                                (id_product, id_substitute)
                                VALUES
                                (:id_product, :id_substitute)

                             """, id_product=product, id_substitute=substitute)
        return product_favorite
