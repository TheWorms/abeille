#!/usr/bin/env bash
# Publie (ou met à jour) un addon dans le store Abeille.
#   ./publish-addon.sh <dossier-sources-de-l-addon>
# Vérifie le manifeste, construit zips/<id>-<version>.zip, met à jour
# index.json et committe. Les versions publiées sont immuables.
set -euo pipefail
SRC="${1:?usage: ./publish-addon.sh <dossier-sources>}"
HERE="$(cd "$(dirname "$0")" && pwd)"
[[ -f "$SRC/manifest.json" ]] || { echo "❌ $SRC/manifest.json introuvable"; exit 1; }

read -r ID VER API CAT NAME DESC < <(python3 - "$SRC/manifest.json" <<'PY'
import json,sys,re
m=json.load(open(sys.argv[1],encoding="utf-8"))
for k in ("id","version","kiosk_api","category","name"):
    if not m.get(k): sys.exit(f"manifest: champ manquant '{k}'")
if not re.fullmatch(r"[a-z0-9-]+", m["id"]): sys.exit("manifest: id invalide")
if m["category"] not in ("Maison","Quotidien","Services","Médias","Outils"):
    sys.exit("manifest: catégorie hors liste")
print(m["id"], m["version"], m["kiosk_api"], m["category"],
      m["name"].replace(" ","\u00a0"), (m.get("description") or "").replace(" ","\u00a0")[:400])
PY
) || { echo "❌ manifeste invalide"; exit 1; }
NAME="${NAME//$'\u00a0'/ }"; DESC="${DESC//$'\u00a0'/ }"

ZIP="zips/${ID}-${VER}.zip"
[[ -f "$HERE/$ZIP" ]] && { echo "❌ $ZIP existe déjà — les versions sont immuables, incrémente 'version'"; exit 1; }

echo "== $ID $VER ($CAT) =="
[[ -f "$SRC/ui.js" ]] && node --check "$SRC/ui.js"
[[ -f "$SRC/backend.py" ]] && python3 -m py_compile "$SRC/backend.py"
# le kiosk exige un préfixe <id>/ dans le zip : staging au nom de l'id
STG=$(mktemp -d); mkdir -p "$STG/$ID"
cp -r "$SRC"/. "$STG/$ID/"
( cd "$STG" && zip -rq "$HERE/$ZIP" "$ID" -x '*__pycache__*' -x '*.pyc' )
rm -rf "$STG"
SHA=$(sha256sum "$HERE/$ZIP" | cut -d' ' -f1)

python3 - "$HERE/index.json" "$ID" "$NAME" "$VER" "$API" "$CAT" "$DESC" "$ZIP" "$SHA" "$SRC/manifest.json" <<'PY'
import json,sys,datetime
idx_p,aid,name,ver,api,cat,desc,zp,sha,man_p=sys.argv[1:]
idx=json.load(open(idx_p,encoding="utf-8"))
man=json.load(open(man_p,encoding="utf-8"))
entry={"id":aid,"name":name,"version":ver,"kiosk_api":api,"category":cat,
       "description":desc or man.get("description",""),"zip":zp,"sha256":sha}
for opt in ("requires","credits"):
    if man.get(opt): entry[opt]=man[opt]
idx["addons"]=[a for a in idx.get("addons",[]) if a.get("id")!=aid]+[entry]
idx["addons"].sort(key=lambda a:a["id"])
idx["updated"]=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
json.dump(idx,open(idx_p,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("index.json mis à jour")
PY

cd "$HERE" && git add "$ZIP" index.json && git commit -m "abeille: $ID $VER" >/dev/null
echo "✅ $ID $VER publié — reste : git push"
