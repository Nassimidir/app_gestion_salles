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