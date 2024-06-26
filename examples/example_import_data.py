from dotenv import load_dotenv
from pylote import Pylote
from os import environ

load_dotenv()

pylote_dev = Pylote(environ.get("BASE_URL"), environ.get("API_KEY"))


data_to_import = [
    {"identifiant_indic": "IND-208", "zone_id": "D01", "zone_nom": None, "date_valeur": "2024-07-15", "type_valeur": "va", "valeur": 12.64},
    {"identifiant_indic": "IND-208", "zone_id": "D01", "zone_nom": None, "date_valeur": "2022-12-01", "type_valeur": "vi", "valeur": 11.17},
]

res = pylote_dev.import_donnees_indicateur_array("CH-047", "IND-208", data_to_import)

print(res)
