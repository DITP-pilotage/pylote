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

    def build_url_indicateur(self, chantier_id_, indicateur_id_):
        endpoint_url = "/".join(
            ["chantier", chantier_id_, "indicateur", indicateur_id_, "donnees"]
        )
        full_url = urljoin(self.base_url, endpoint_url)
        return full_url

    def build_url_chantier(self, chantier_id_):
        endpoint_url = "/".join(["chantier", chantier_id_, "donnees"])
        return urljoin(self.base_url, endpoint_url)

    def get_donnees_indicateur(self, chantier_id, indicateur_id):
        return requests.get(
            self.build_url_indicateur(chantier_id, indicateur_id), headers=self.headers
        ).json()

    def import_donnees_indicateur_array(
        self, chantier_id, indicateur_id, donnees_array
    ):
        return requests.post(
            self.build_url_indicateur(chantier_id, indicateur_id),
            json={"donnees": donnees_array},
            headers={**self.headers, **{"Content-Type": "application/json"}},
        ).json()

    def import_donnees_indicateur_file(
        self, chantier_id, indicateur_id, filepath, is_excel=False
    ):
        # Default type is CSV, otherwise Excel
        filetype = "application/vnd.ms-excel" if is_excel else "application/csv"
        filename = "import.xls" if is_excel else "import.csv"

        return requests.post(
            self.build_url_indicateur(chantier_id, indicateur_id),
            headers=self.headers,
            files={
                "file": (filename, open(filepath, "rb"), filetype, {"Expires": "0"})
            },
        ).json()

    def get_donnees_chantier(self, chantier_id):
        return requests.get(
            self.build_url_chantier(chantier_id), headers=self.headers
        ).json()
