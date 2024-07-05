## Mettre à jour les dépendences

Après avoir installé les dépendences de développement vous pouvez upgrader les mises à jour avec

```bash
pip-compile --upgrade requirements.in
```

Puis les mettre à jour avec

```bash
pip-compile requirements.in
```
