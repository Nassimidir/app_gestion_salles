import json
import mysql.connector
from models.salle import Salle


class DataSalle:
    def get_connection(self):
        with open("data/config.json", "r") as file:
            config = json.load(file)

        connection = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )

        return connection

    def insert_salle(self, salle):
        connection = self.get_connection()
        cursor = connection.cursor()

        requete = """
        INSERT INTO salle (code, description, categorie, capacite)
        VALUES (%s, %s, %s, %s)
        """
        valeurs = (salle.code, salle.description, salle.categorie, salle.capacite)

        cursor.execute(requete, valeurs)
        connection.commit()

        cursor.close()
        connection.close()