# 🐝 Abeille — store d'addons pour Panda

Abeille est le dépôt d'applications du kiosk [Panda](https://github.com/TheWorms/panda).
Un dépôt git **est** le store : `index.json` décrit le catalogue, `zips/`
contient les paquets versionnés. Le kiosk consomme le tout via les URLs
« raw » — aucun serveur à déployer.

## Utiliser ce store depuis un kiosk Panda

Dans **⚙ Réglages → URL du store** :

    https://raw.githubusercontent.com/TheWorms/abeille/main/

(bouton **Tester**, puis ouvrez le Store depuis l'accueil).

Variante auto-hébergée : poussez ce dépôt sur votre Gitea/Forgejo et
utilisez son URL raw (`https://<hôte>/<user>/abeille/raw/branch/main/`),
avec un jeton d'accès si le dépôt est privé.

## Publier ou mettre à jour un addon

Prérequis : les sources de l'addon dans un dossier (`manifest.json`,
`ui.js`, `backend.py`…), un clone de ce dépôt.

    ./publish-addon.sh <chemin/vers/sources/mon-addon>

Le script : vérifie le manifeste (`kiosk_api`, catégorie, version), refuse
d'écraser une version déjà publiée (**les versions sont immuables** —
incrémentez `version` pour republier), construit `zips/<id>-<version>.zip`,
calcule son sha256, met à jour `index.json`, et committe. Il ne reste qu'à
`git push`.

## Format d'index (résumé)

```json
{
  "store": "abeille",
  "updated": "2026-07-16T10:00:00Z",
  "addons": [
    {
      "id": "soleil-lune",
      "name": "Soleil & Lune",
      "version": "1.0.0",
      "kiosk_api": "^1.3",
      "category": "Quotidien",
      "description": "Éphémérides du jour…",
      "zip": "zips/soleil-lune-1.0.0.zip",
      "sha256": "…"
    }
  ]
}
```

Détails complets : [docs/format.md](docs/format.md). Contrat du SDK :
voir `docs/sdk-addons.md` du dépôt Panda.

## Licence

GPL-3.0 — voir [LICENSE](LICENSE). Chaque addon porte ses propres crédits
dans sa fiche (`manifest.json` → `credits`).
