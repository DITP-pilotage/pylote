from dotenv import load_dotenv
from pylote import Pylote
from os import environ

load_dotenv()

pylote_dev = Pylote(environ.get("BASE_URL_DEV"), environ.get("API_KEY_DEV"))


donnees_208 = pylote_dev.get_donnees_indicateur("CH-047", "IND-208")

print({
    "indic_id": donnees_208['indic_id'],
    "est_barometre": donnees_208['est_barometre'],
    "chantier_id": donnees_208['chantier_id'],
    "donnees_territoires": len(donnees_208['donnees_territoires']),
})
