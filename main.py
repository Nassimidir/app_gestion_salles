from data.dao_salle import DataSalle
from models.salle import Salle

data_salle = DataSalle()

salle1 = Salle("A101", "Salle informatique", "laboratoire", 30)
data_salle.insert_salle(salle1)

print("Salle ajoutee avec succes")