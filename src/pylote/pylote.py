from urllib.parse import urljoin

import requests

class Pylote:

    def __init__(self, base_url, api_key) -> None:
        self.base_url = base_url
        self.api_key = api_key
        return

    @property
    def headers(self):
        return {"Authorization": f"Bearer {self.api_key}"}

    def get_donnees_indicateur(self, chantier_id, indicateur_id):
        endpoint_url="/".join(["chantier", chantier_id, "indicateur", indicateur_id, "donnees"])
        full_url = urljoin(self.base_url, endpoint_url)

        res = requests.get(
            full_url,
            headers=self.headers
        ).json()

        return res
