from data.dao_salle import DataSalle

data_salle = DataSalle()

connexion = data_salle.get_connection()
if connexion.is_connected():
    print("Connexion a la base de donnees reussie")
    connexion.close()
else:
    print("Echec de la connexion")