import requests

class Pilote:

    def __init__(self, base_url, api_key) -> None:
        self.base_url = base_url
        self.api_key = api_key
        return

    def get_donnees_indicateur(self, chantier_id, indicateur_id):
        endpoint_url="/".join(["chantier", chantier_id, "indicateur", indicateur_id, "donnees"])
        
        res = requests.get(
            "/".join([self.base_url, endpoint_url]),
            headers= {"Authorization":"Bearer "+self.api_key}
        ).json()

        return res
