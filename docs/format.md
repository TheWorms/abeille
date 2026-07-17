# Format du store Abeille

## Arborescence

    index.json          # catalogue (source de vérité)
    zips/<id>-<ver>.zip # paquets, un par version, immuables

## index.json

Champs par addon :

| Champ | Obligatoire | Rôle |
|---|---|---|
| `id` | ✓ | identifiant `[a-z0-9-]+`, unique |
| `name` | ✓ | nom affiché |
| `version` | ✓ | semver ; toute republication l'incrémente |
| `kiosk_api` | ✓ | contrainte SDK, ex. `"^1.3"` |
| `category` | ✓ | Maison, Quotidien, Services, Médias ou Outils |
| `description` | ✓ | une à deux phrases, affichées sur la fiche |
| `zip` | ✓ | chemin relatif du paquet |
| `sha256` | ✓ | empreinte du zip, vérifiée à l'installation |
| `requires` | — | ids à installer avant (ordre d'installation) |
| `credits` | — | sources de données, licences tierces |

## Un paquet (zip)

Le zip contient le dossier de l'addon à plat : `manifest.json` obligatoire,
plus `ui.js`, `backend.py` et tout fichier statique (servi par le kiosk sur
`/addons/<id>/ui/<fichier>` — extensions autorisées : js, css, svg, png,
webp, woff2).

## Règles

1. **Immutabilité** : un `zips/<id>-<ver>.zip` publié ne change jamais.
2. Le `sha256` de l'index doit correspondre au zip — le kiosk refuse sinon.
3. `version` de l'index = `version` du manifest embarqué.
4. Publiez les dépendances (`requires`) avant les dépendants.
