import mysql.connector
class openfoodfacts_mysql:


    def __init__(self, user, password):
        """
            Dans init, initialiser les params pour les credentials à utiliser

        """
        self.user = user
        self.password = password

    def connexion_mysql(self, sqlserver):
        """
        Dans connexion_mysql, se connecter la bdd

        """
        try:
            myconn = mysql.connector.connect(
            host=sqlserver,
            user=self.user,
            passwd=self.password
            )
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        self.conn = myconn

    def create_mysql_db(self, database):
        """
        Dans create_mysql_db, initialiser les params pour créer la bdd

        """
        try:
            mycursor = self.conn.cursor()
            mycursor.execute("CREATE DATABASE " + database)
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    def create_users_bdd():
        """
        create_users_bdd permet de créer des utilisateurs et d'octroyer des droits

        """
        pass

    def get_info_bdd():
        """
        get_info_bdd permet de récuperer les informations en bdd

        """
        pass


    def write_info_bdd():
        """
        Dans init, initialiser les params pour créer la bdd

        """
        pass

    def update_info_bdd():
        """
        update_info_bdd permet de mettre à jour les informations de la bdd

        """
        pass


    def delete_info_bdd():
        """
        delete_info_bdd permet de supprimer les informations de la bdd

        """
        pass
