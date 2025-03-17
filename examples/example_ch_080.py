from dotenv import load_dotenv
from pylote import Pylote
from os import environ

load_dotenv()

pylote_dev = Pylote(environ.get("BASE_URL_DEV"), environ.get("API_KEY_DEV"))

chantier_080_json = pylote_dev.get_donnees_chantier("CH-080")

print(
    {
        "chantier_id": chantier_080_json.get("chantier_id"),
        "nom": chantier_080_json.get("nom"),
        "axe": chantier_080_json.get("axe"),
        "ministere": chantier_080_json.get("ministere"),
        "est_barometre": chantier_080_json.get("est_barometre"),
        "est_territorialise": chantier_080_json.get("est_territorialise"),
        "directeurs_projet": chantier_080_json.get("directeurs_projet"),
        "directeurs_projet_mails": chantier_080_json.get("directeurs_projet_mails"),
        "donnees_territoires": ["voir documentation"],
        # "donnees_territoires": chantier_080_json.get("donnees_territoires"),
    }
)
