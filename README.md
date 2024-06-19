# Pylote

Ce code permet d'interroger l'API de Pilote pour exporter et importer des données.

## Installation

Installer les dépendences dans un environnement virtuel avec `pip install .`.

## Exemples

Vous pouvez installer l’exemple après avoir installé les dépendences avec `pip install .[example]` avec `python example/main.py`

## Mettre à jour les dépendences

Après avoir installé les dépendences de développement vous pouvez upgrader les mises à jour avec

```bash
pip-compile --upgrade requirements.in
pip-compile --upgrade example-requirements.in
```

Puis les mettre à jour avec

```bash
pip-compile requirements.in
pip-compile example-requirements.in
```
