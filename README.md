# Pylote

Ce code permet d'interroger l'API de Pilote pour exporter et importer des données.

## Installation

Installer les dépendences dans un environnement virtuel avec `pip install .`.

## Usage

Exemple d'utilisation:

```python

# [init] Initialisation de l'objet Pylote
pylote_dev = Pylote(environ.get("BASE_URL"), environ.get("API_KEY"))

# [export]
## [export] Export des données de IND-208
donnees_208 = pylote_dev.get_donnees_indicateur("CH-047", "IND-208")


# [import]
## [import] Import de données d'une liste Python
data_to_import = [
    {"identifiant_indic": "IND-208", "zone_id": "D01", "zone_nom": None, "date_valeur": "2024-07-15", "type_valeur": "va", "valeur": 12.64},
    {"identifiant_indic": "IND-208", "zone_id": "D01", "zone_nom": None, "date_valeur": "2022-12-01", "type_valeur": "vi", "valeur": 11.17},
]
pylote_dev.import_donnees_indicateur_array("CH-047", "IND-208", data_to_import)

# [import] Import de données d'un fichier CSV
pylote_dev.import_donnees_indicateur_file("CH-047", "IND-208", "./data-ind208-import-sample.csv", is_excel=False)
```

## Exemples

Des fichiers d'exemple fonctionnels sont mis à disposition dans le dossier [examples](./examples). Plus de détails dans README correspondant [examples/README.md](./examples/README.md).
