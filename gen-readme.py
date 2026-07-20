#!/usr/bin/env python3
"""Génère README.md d'abeille-public depuis index.json (catalogue à jour).
Usage : python3 gen-readme.py [chemin_index.json] > README.md

La partie haute (intro, install, config) est un gabarit fixe ; seul le
catalogue (tableau récapitulatif) est régénéré depuis l'index signé.
"""
import json, sys

INDEX = sys.argv[1] if len(sys.argv) > 1 else "index.json"
CAT_ORDER = ["Maison", "Quotidien", "Services", "Médias", "Outils"]

HEADER = """# 🐝 Abeille — le store d'addons de Panda

Abeille est le dépôt d'addons du kiosk domestique **Panda**. Chaque addon apporte une tuile et une vue dédiée à un service de la maison (cuisine, médias, monitoring, quotidien…). Les tuiles arborent le **logo officiel** de chaque application (SVG embarqué, rendu net à toute taille et disponible hors-ligne).

## Installation du store

Dans Panda : **⚙ Réglages → Store**. Le store officiel est préconfiguré ; les addons s'installent et se mettent à jour en un tap depuis l'onglet Store. Les mises à jour disponibles sont signalées par un badge **⬆ MISE À JOUR** et une pastille sur l'icône du Store.

L'index du store est **signé** (Ed25519) : Panda vérifie la signature avant d'accepter tout catalogue, garantissant que les addons proviennent bien de cette source.

## Configuration des addons

📖 **[Voir la page complète de configuration des addons »](CONFIGURATION.md)** — tous les réglages, champ par champ.

Après installation, chaque addon se configure depuis sa tuile via l'icône **⚙** (URL du service, identifiants ou clés API). Le bouton **Tester** valide la connexion avant d'enregistrer. La configuration est relue à chaud, sans redémarrage.
"""

FOOTER = """

---

_Catalogue généré automatiquement depuis l'index signé du store. Panda & Abeille — The Worm's._
"""

def anchor(id_):
    return id_.lower().replace(" ", "-")

def main():
    d = json.load(open(INDEX, encoding="utf-8"))
    addons = d.get("addons", [])
    by_cat = {}
    for a in addons:
        by_cat.setdefault(a.get("category", "Autres"), []).append(a)

    out = [HEADER]
    out.append(f"\n## Catalogue — {len(addons)} addons\n")
    out.append("| | Addon | Version | Catégorie | Description |")
    out.append("|---|---|---|---|---|")

    cats = [c for c in CAT_ORDER if c in by_cat] + [c for c in sorted(by_cat) if c not in CAT_ORDER]
    for cat in cats:
        for a in sorted(by_cat[cat], key=lambda x: x.get("name", "").lower()):
            aid = a.get("id", "")
            logo = a.get("logo")
            if logo:
                icon = f'<img src="logos/{aid}.svg" width="22" alt="">'
            else:
                icon = a.get("icon", "") or "📦"
            name = a.get("name", a.get("id"))
            ver = a.get("version", "?")
            desc = (a.get("description", "") or "").strip().replace("\n", " ")
            # tronquer les descriptions très longues pour le tableau
            if len(desc) > 130:
                desc = desc[:127].rsplit(" ", 1)[0] + "…"
            out.append(f"| {icon} | {name} | {ver} | {cat} | {desc} |")

    out.append(FOOTER)
    print("\n".join(out))

if __name__ == "__main__":
    main()
