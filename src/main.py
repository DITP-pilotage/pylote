from dotenv import load_dotenv
from utils.api_pilote import Pilote
from os import environ



pylote_dev = Pilote(environ.get("BASE_URL"), environ.get("API_KEY"))


res1 = pylote_dev.get_donnees_indicateur("CH-047", "IND-208")

print({
    "indic_id": res1['indic_id'],
    "est_barometre": res1['est_barometre'],
    "chantier_id": res1['chantier_id'],
    "donnees_territoires": len(res1['donnees_territoires']),
})
