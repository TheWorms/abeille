#!/usr/bin/env python3
"""Génère CONFIGURATION.md depuis les manifests des addons (groupé par catégorie).
Usage : python3 gen-config-doc.py [chemin_addons-src] > CONFIGURATION.md
"""
import json, os, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
CAT_ORDER = ["Maison", "Quotidien", "Médias", "Services", "Outils"]
TYPE_FR = {"text": "texte", "password": "secret (masqué)", "toggle": "interrupteur",
           "select": "liste déroulante", "number": "nombre", None: "texte", "": "texte"}

def load_addons():
    addons = []
    for d in sorted(os.listdir(ROOT)):
        mp = os.path.join(ROOT, d, "manifest.json")
        if os.path.isfile(mp):
            try:
                addons.append(json.load(open(mp, encoding="utf-8")))
            except Exception:
                pass
    return addons

def field_line(f):
    typ = TYPE_FR.get(f.get("type"), "texte")
    label = f.get("label") or f.get("key")
    extra = ""
    if f.get("type") == "select" and f.get("options"):
        opts = " / ".join(o[1] if isinstance(o, list) and len(o) > 1 else str(o) for o in f["options"])
        extra = f" — choix : {opts}"
    if f.get("placeholder"):
        ph = f["placeholder"]
        prefix = "" if ph.lower().startswith("ex") else "ex. "
        extra += f" — {prefix}`{ph}`"
    return f"| `{f.get('key')}` | {label} | {typ}{extra} |"

def main():
    addons = load_addons()
    by_cat = {}
    for a in addons:
        by_cat.setdefault(a.get("category", "Autres"), []).append(a)

    out = []
    out.append("# Configuration des addons\n")
    out.append("Cette page décrit les réglages de chaque addon du store. "
               "La configuration se fait depuis l'écran tactile via le bouton **⚙** de chaque addon, "
               "ou à distance avec l'outil `panda-cfg.py` en SSH.\n")
    out.append(f"*{len(addons)} addons au total. Document généré automatiquement depuis les manifests.*\n")

    cats = [c for c in CAT_ORDER if c in by_cat] + [c for c in sorted(by_cat) if c not in CAT_ORDER]
    for cat in cats:
        out.append(f"\n## {cat}\n")
        for a in sorted(by_cat[cat], key=lambda x: x.get("name", "").lower()):
            icon = a.get("icon") or (a.get("tiles", [{}])[0].get("icon") if a.get("tiles") else "") or ""
            aid = a.get("id", "")
            logo = a.get("logo")
            icon_html = f'<img src="logos/{aid}.svg" width="20" alt=""> ' if logo else ((icon + " ") if icon else "")
            out.append(f"\n### {icon_html}{a.get('name')} — v{a.get('version','?')}\n")
            desc = a.get("description", "").strip()
            if desc:
                out.append(desc + "\n")
            fields = (a.get("config") or {}).get("fields", [])
            if not fields:
                out.append("*Aucun réglage nécessaire (configuration héritée ou automatique).*\n")
            else:
                out.append("\n| Champ | Libellé | Type |")
                out.append("|---|---|---|")
                for f in fields:
                    out.append(field_line(f))
                out.append("")
    print("\n".join(out))

if __name__ == "__main__":
    main()
