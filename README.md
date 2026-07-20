# 🐝 Abeille — le store d'addons de Panda

Abeille est le dépôt d'addons du kiosk domestique **Panda**. Chaque addon apporte une tuile et une vue dédiée à un service de la maison (cuisine, médias, monitoring, quotidien…).

## Installation du store

Dans Panda : **⚙ Réglages → Store**. Le store officiel est préconfiguré ; les addons s'installent et se mettent à jour en un tap depuis l'onglet Store. Les mises à jour disponibles sont signalées par un badge **⬆ MISE À JOUR** et une pastille sur l'icône du Store.

## Configuration des addons

Après installation, chaque addon se configure depuis sa tuile via l'icône **⚙** (URL du service, identifiants ou clés API). Le bouton **Tester** valide la connexion avant d'enregistrer. Les champs de chaque addon sont détaillés ci-dessous, avec un lien vers la documentation du service pour obtenir les clés.

## Catalogue — 32 addons

| | Addon | Version | Catégorie | Description |
|---|---|---|---|---|
| 🧊 | [Congélateur](#-congelateur) | 0.2.2 | Maison | Inventaire du congélateur — façade du hub cuisine KitchenOwl |
| 🛒 | [Courses](#-courses) | 0.2.2 | Maison | Liste de courses partagée — façade du hub cuisine KitchenOwl |
| 🥘 | [Hub KitchenOwl](#-kitchenowl) | 0.2.3 | Maison | Hub cuisine : connexion KitchenOwl partagée par les addons courses, stock, congélateur, recettes et repas |
| 🌱 | [Jardin](#-jardin) | 0.3.0 | Maison | Suivi du jardin — calculs locaux, sans service externe |
| 📖 | [Recettes](#-recettes) | 0.2.2 | Maison | Recettes de cuisine — façade du hub cuisine KitchenOwl |
| 📅 | [Repas semaine](#-repas) | 0.3.1 | Maison | Planification des repas de la semaine — façade du hub cuisine KitchenOwl |
| 📦 | [Stock cuisine](#-stock) | 0.2.2 | Maison | Stock du garde-manger — façade du hub cuisine KitchenOwl |
| 🐜 | [Abonnements](#-wallos) | 0.4.1 | Quotidien | Abonnements via Wallos (Fourmi) : budget du mois (dû/prélevé/restant), tous les abonnements en cartes, répartition par catégorie (donut) et prévisionnel des prochains mois |
| 📆 | [Agenda](#-agenda) | 0.3.0 | Quotidien | Agenda CalDAV (Infomaniak, Nextcloud, Baïkal, Radicale, Fastmail, Google…) : événements à venir, notifications, ajout d'événements |
| 💶 | [Budget](#-budget) | 0.2.1 | Quotidien | Budget personnel via Actual Budget (actual-http-api) |
| 🌊 | [Marée](#-maree) | 0.3.0 | Quotidien | Horaires et coefficients de marée via api-maree |
| 🌙 | [Soleil & Lune](#-soleil-lune) | 1.0.0 | Quotidien | Lever et coucher du soleil, durée du jour, phase et illumination de la lune — calculés localement, sans connexion |
| 🚆 | [Transport](#-transport) | 0.2.0 | Quotidien | Prochains passages des transports via l'API Navitia (SNCF) |
| 🐳 | [Arcane](#-arcane) | 0.3.1 | Services | Conteneurs Docker via Arcane, tous environnements agrégés (badge machine) : stats, liste ou cartes avec ports et état, actions démarrer / arrêter / redémarrer |
| 🗂️ | [Forgejo](#-forgejo) | 0.2.1 | Services | Dépôts Forgejo — cartes ou liste, recherche, historique des derniers commits |
| 📊 | [Grafana](#-grafana) | 0.3.1 | Services | Supervision Grafana : santé et version, sources de données et leur état, alertes actives, liste des dashboards, et rendu à la demande d'un panel (image PNG via le renderer) |
| ✉️ | [Mail](#-mail) | 0.1.0 | Services | Boîte mail IMAP (Infomaniak, Gmail, Proton Bridge…) : lire les messages, marquer lu/non lu, supprimer |
| ☁️ | [Nextcloud](#-nextcloud) | 0.4.0 | Services | Nextcloud |
| 📄 | [Paperless](#-paperless) | 0.3.0 | Services | Paperless-ngx (Méduse) : statistiques (documents, réception, correspondants, types, tags), recherche plein-texte, boîte de réception et documents récents avec vignettes |
| 🛡️ | [Pi-hole](#-pihole) | 0.7.0 | Services | Supervision Pi-hole v6 multi-instances : ajoute autant de nœuds que tu veux, statistiques détaillées (top domaines/clients, amont DNS, types de requêtes, historique 24 h), couleurs Pi-hole |
| 🖥️ | [Proxmox](#-proxmox) | 0.2.1 | Services | État de l'hyperviseur Proxmox : nœuds, VMs et conteneurs |
| 🎬 | [Radarr](#-radarr) | 0.1.0 | Services | Radarr : file de téléchargements, sorties à venir, films suivis, manquants, taille de bibliothèque, espace disque, santé et activité récente |
| 💾 | [Sauvegardes](#-backups) | 0.4.0 | Services | Liste des sauvegardes vzdump présentes sur les stockages Proxmox, regroupées par VM/CT : dernière sauvegarde, nombre, taille cumulée, fichiers protégés |
| 📺 | [Sonarr](#-sonarr) | 0.1.0 | Services | Sonarr : file de téléchargements, calendrier des sorties, séries suivies, épisodes manquants, espace disque, santé et activité récente |
| 🟢 | [Uptime Kuma](#-kuma) | 0.3.0 | Services | Uptime Kuma (Faucon) : statistiques (en ligne, hors ligne, ping moyen), moniteurs en liste ou cartes avec uptime 24 h, temps de réponse et historique récent |
| 📡 | [WatchYourLAN](#-wyl) | 0.3.0 | Services | Hôtes du réseau via WatchYourLAN (Furet) : nom, IP, MAC, matériel et statut en ligne |
| 📚 | [Wiki.js](#-wikijs) | 0.3.1 | Services | Wiki |
| 🎞️ | [Emby](#-emby) | 0.1.0 | Médias | Emby : sessions en cours (qui regarde quoi), bibliothèques et compteurs, derniers ajouts, activité serveur et comptes utilisateurs |
| 📸 | [Instagram](#-instagram) | 0.4.0 | Médias | Instagram |
| 📺 | [Kodi](#-kodi) | 0.3.0 | Médias | Kodi (Cormoran/Ours) : télécommande complète (lecture, navigation, volume) et bibliothèque — films et épisodes récemment ajoutés avec affiches |
| 📚 | [Livres](#-livres) | 0.4.0 | Médias | Kavita (Hérisson) : bibliothèques, lectures en cours, nouveautés, recherche et LISEUSE intégrée — lecture des BD page par page au tactile (zones gauche/droite/centre, curseur, progression synchronisée avec Kavita) |
| 🎵 | [Musique](#-musique) | 0.2.1 | Médias | Lecteur audio branché sur Navidrome (lecture persistante en fond) |


## Maison

### 🧊 congelateur

**Congélateur** · v0.2.2

Inventaire du congélateur — façade du hub cuisine KitchenOwl.

**Configuration :**

| Champ | Description |
|---|---|
| `category` | Catégorie « congélateur » (optionnel) — ex. `Congélateur` |

### 🛒 courses

**Courses** · v0.2.2

Liste de courses partagée — façade du hub cuisine KitchenOwl.

_Aucune configuration requise._

### 🥘 kitchenowl

**Hub KitchenOwl** · v0.2.3

Hub cuisine : connexion KitchenOwl partagée par les addons courses, stock, congélateur, recettes et repas.

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL KitchenOwl — ex. `http://kitchenowl.example.com:8080` |
| `token` | Jeton KitchenOwl — secret |
| `household` | Maison (id ou nom, si plusieurs) — ex. `1` |

📖 Obtenir les identifiants : [KitchenOwl — API](https://docs.kitchenowl.org/)

### 🌱 jardin

**Jardin** · v0.3.0

Suivi du jardin — calculs locaux, sans service externe.

_Aucune configuration requise._

### 📖 recettes

**Recettes** · v0.2.2

Recettes de cuisine — façade du hub cuisine KitchenOwl.

_Aucune configuration requise._

### 📅 repas

**Repas semaine** · v0.3.1

Planification des repas de la semaine — façade du hub cuisine KitchenOwl.

_Aucune configuration requise._

### 📦 stock

**Stock cuisine** · v0.2.2

Stock du garde-manger — façade du hub cuisine KitchenOwl.

_Aucune configuration requise._


## Quotidien

### 🐜 wallos

**Abonnements** · v0.4.1

Abonnements via Wallos (Fourmi) : budget du mois (dû/prélevé/restant), tous les abonnements en cartes, répartition par catégorie (donut) et prévisionnel des prochains mois. Disposition (onglets ou page unique) et horizon configurables.

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL Wallos — ex. `http://wallos.example.com:8282` |
| `apikey` | Clé API (Paramètres → API) — secret |
| `layout` | Disposition — choix : Onglets (Ce mois · Tous · Catégories · Prévisionnel) / Page unique (tout empilé) |
| `forecast` | Prévisionnel — nombre de mois — choix : 6 mois / 3 mois / 12 mois (année) |

📖 Obtenir les identifiants : [Wallos — API](https://github.com/ellite/Wallos)

### 📆 agenda

**Agenda** · v0.3.0

Agenda CalDAV (Infomaniak, Nextcloud, Baïkal, Radicale, Fastmail, Google…) : événements à venir, notifications, ajout d'événements.

**Configuration :**

| Champ | Description |
|---|---|
| `url` | Serveur CalDAV — ex. `https://exemple.com/dav (ou https://sync.infomaniak.com)` |
| `user` | Identifiant / e-mail |
| `pass` | Mot de passe (d'application si dispo) — secret |
| `calendar` | Calendrier par défaut (nouveaux événements) — ex. `Perso` |
| `notif` | Notifications dans le bandeau — choix : Activées / Désactivées |

📖 Obtenir les identifiants : [CalDAV — serveurs compatibles](https://en.wikipedia.org/wiki/CalDAV)

### 💶 budget

**Budget** · v0.2.1

Budget personnel via Actual Budget (actual-http-api).

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL actual-http-api — ex. `http://budget.example.com:5007` |
| `apikey` | Clé API — secret |
| `budget` | ID de synchronisation du budget — ex. `laisser vide pour lister` |

📖 Obtenir les identifiants : [actual-http-api](https://github.com/jhonderson/actual-http-api)

### 🌊 maree

**Marée** · v0.3.0

Horaires et coefficients de marée via api-maree.fr.

**Configuration :**

| Champ | Description |
|---|---|
| `site` | Port (api-maree.fr) — ex. `trehiguier` |
| `apikey` | Clé api-maree.fr (inscription gratuite) — secret |

📖 Obtenir les identifiants : [api-maree.fr](https://api-maree.fr/)

### 🌙 soleil-lune

**Soleil & Lune** · v1.0.0

Lever et coucher du soleil, durée du jour, phase et illumination de la lune — calculés localement, sans connexion.

**Configuration :**

| Champ | Description |
|---|---|
| `lat` | Latitude — ex. `48.8566` |
| `lon` | Longitude — ex. `2.3522` |
| `tz` | Décalage horaire (heures, ex. 2 en été) — ex. `2` |

### 🚆 transport

**Transport** · v0.2.0

Prochains passages des transports via l'API Navitia (SNCF).

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL de l'API — ex. `https://api.sncf.com/v1` |
| `token` | Jeton d'API — secret |
| `coverage` | Couverture — ex. `sncf (ou fr-ne, fr-nw… sur navitia.io)` |

📖 Obtenir les identifiants : [Navitia](https://navitia.io/)


## Services

### 🐳 arcane

**Arcane** · v0.3.1

Conteneurs Docker via Arcane, tous environnements agrégés (badge machine) : stats, liste ou cartes avec ports et état, actions démarrer / arrêter / redémarrer. Arrêtés grisés, mises à jour signalées.

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL Arcane — ex. `http://arcane.example.com:3552` |
| `apikey` | Clé API (arc_...) — secret |

📖 Obtenir les identifiants : [Arcane — clé API (Settings → API Keys)](https://getarcane.app/docs)

### 🗂️ forgejo

**Forgejo** · v0.2.1

Dépôts Forgejo — cartes ou liste, recherche, historique des derniers commits.

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL Forgejo — ex. `https://forgejo.example.com:3000` |
| `token` | Token d'accès (Paramètres → Applications) — secret |
| `view` | Affichage des dépôts — choix : Cartes / Liste |
| `hist` | Historique des commits (panneau de droite) — choix : 10 derniers / 5 derniers / 20 derniers / Masqué |

📖 Obtenir les identifiants : [Forgejo — API](https://forgejo.org/docs/latest/user/api-usage/)

### 📊 grafana

**Grafana** · v0.3.1

Supervision Grafana : santé et version, sources de données et leur état, alertes actives, liste des dashboards, et rendu à la demande d'un panel (image PNG via le renderer).

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL Grafana — ex. `http://grafana.local:3000` |
| `apikey` | Clé API (service account token) — secret |
| `theme` | Thème du rendu des panels — choix : Sombre / Clair |

📖 Obtenir les identifiants : [Grafana — Service account token (Administration → Service accounts)](https://grafana.com/docs/grafana/latest/administration/service-accounts/)

### ✉️ mail

**Mail** · v0.1.0

Boîte mail IMAP (Infomaniak, Gmail, Proton Bridge…) : lire les messages, marquer lu/non lu, supprimer.

**Configuration :**

| Champ | Description |
|---|---|
| `host` | Serveur IMAP — ex. `mail.infomaniak.com` |
| `port` | Port IMAPS — ex. `993` |
| `user` | Adresse e-mail |
| `pass` | Mot de passe d'application — secret |
| `folder` | Dossier — ex. `INBOX` |

📖 Obtenir les identifiants : [Mail — mot de passe d'application](https://www.infomaniak.com/fr/support/faq/2299/creer-un-mot-de-passe-dapplication)

### ☁️ nextcloud

**Nextcloud** · v0.4.0

. Explorateur avec bascule liste / cartes (vignettes en grille).

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL Nextcloud — ex. `http://nextcloud.example.com` |
| `user` | Utilisateur |
| `pass` | Mot de passe d'application — secret |

📖 Obtenir les identifiants : [Nextcloud — mots de passe d'application](https://docs.nextcloud.com/server/latest/user_manual/en/session_management.html)

### 📄 paperless

**Paperless** · v0.3.0

Paperless-ngx (Méduse) : statistiques (documents, réception, correspondants, types, tags), recherche plein-texte, boîte de réception et documents récents avec vignettes. Bascule liste / cartes ; clic pour ouvrir le document.

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL Paperless — ex. `http://paperless.example.com:8010` |
| `token` | Jeton API (Paramètres → Jeton API) — secret |

📖 Obtenir les identifiants : [Paperless-ngx — Jeton API (Paramètres → Jeton API)](https://docs.paperless-ngx.com/api/)

### 🛡️ pihole

**Pi-hole** · v0.7.0

Supervision Pi-hole v6 multi-instances : ajoute autant de nœuds que tu veux, statistiques détaillées (top domaines/clients, amont DNS, types de requêtes, historique 24 h), couleurs Pi-hole.

**Configuration :**

| Champ | Description |
|---|---|
| `name1` | — Pi-hole 1 — Nom — ex. `Principal` |
| `url1` | URL 1 — ex. `http://pihole.local:80` |
| `pass1` | Mot de passe d'application 1 — secret |
| `name2` | — Pi-hole 2 — Nom — ex. `Secondaire` |
| `url2` | URL 2 — ex. `http://pihole.local:80` |
| `pass2` | Mot de passe d'application 2 — secret |
| `name3` | — Pi-hole 3 — Nom — ex. `Pi-hole 3` |
| `url3` | URL 3 — ex. `http://pihole.local:80` |
| `pass3` | Mot de passe d'application 3 — secret |
| `name4` | — Pi-hole 4 — Nom — ex. `Pi-hole 4` |
| `url4` | URL 4 — ex. `http://pihole.local:80` |
| `pass4` | Mot de passe d'application 4 — secret |
| `name5` | — Pi-hole 5 — Nom — ex. `Pi-hole 5` |
| `url5` | URL 5 — ex. `http://pihole.local:80` |
| `pass5` | Mot de passe d'application 5 — secret |

📖 Obtenir les identifiants : [Pi-hole — créer un mot de passe d'application](https://docs.pi-hole.net/api/)

### 🖥️ proxmox

**Proxmox** · v0.2.1

État de l'hyperviseur Proxmox : nœuds, VMs et conteneurs.

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL Proxmox — ex. `https://proxmox.example.com:8006` |
| `token` | Token API — secret |

📖 Obtenir les identifiants : [Proxmox — API tokens](https://pve.proxmox.com/wiki/Proxmox_VE_API)

### 🎬 radarr

**Radarr** · v0.1.0

Radarr : file de téléchargements, sorties à venir, films suivis, manquants, taille de bibliothèque, espace disque, santé et activité récente.

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL Radarr — ex. `http://radarr.local:7878` |
| `apikey` | Clé API — secret |

📖 Obtenir les identifiants : [Radarr — clé API (Settings → General)](https://wiki.servarr.com/radarr/settings#security)

### 💾 backups

**Sauvegardes** · v0.4.0

Liste des sauvegardes vzdump présentes sur les stockages Proxmox, regroupées par VM/CT : dernière sauvegarde, nombre, taille cumulée, fichiers protégés.

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL Proxmox — ex. `https://proxmox.local:8006` |
| `token` | Token API (USER@REALM!ID=UUID) — secret |

📖 Obtenir les identifiants : [Proxmox — token API (Datacenter → API Tokens)](https://pve.proxmox.com/wiki/Proxmox_VE_API)

### 📺 sonarr

**Sonarr** · v0.1.0

Sonarr : file de téléchargements, calendrier des sorties, séries suivies, épisodes manquants, espace disque, santé et activité récente.

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL Sonarr — ex. `http://sonarr.local:8989` |
| `apikey` | Clé API — secret |

📖 Obtenir les identifiants : [Sonarr — clé API (Settings → General)](https://wiki.servarr.com/sonarr/settings#security)

### 🟢 kuma

**Uptime Kuma** · v0.3.0

Uptime Kuma (Faucon) : statistiques (en ligne, hors ligne, ping moyen), moniteurs en liste ou cartes avec uptime 24 h, temps de réponse et historique récent.

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL Kuma — ex. `http://uptime-kuma.example.com:3001` |
| `slug` | Slug page de statut (vue Infra) — ex. `maison` |
| `apikey` | Clé API (bandeau : flotte complète) — secret |
| `label` | Nom de la flotte (bandeau) — ex. `Ménagerie` |
| `format` | Format du bandeau — choix : Total — En ligne / Total / Pastille — En ligne / Hors ligne / Texte — En ligne / Hors ligne |

📖 Obtenir les identifiants : [Uptime Kuma — API keys](https://github.com/louislam/uptime-kuma/wiki/API-Documentation)

### 📡 wyl

**WatchYourLAN** · v0.3.0

Hôtes du réseau via WatchYourLAN (Furet) : nom, IP, MAC, matériel et statut en ligne. Bascule liste / cartes, hôtes hors ligne grisés.

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL WatchYourLAN — ex. `http://watchyourlan.example.com:8840` |

### 📚 wikijs

**Wiki.js** · v0.3.1

Wiki.js (Hibou) : statistiques (pages, publiées, brouillons, dossiers), recherche, pages récemment modifiées et arborescence par dossier. Bascule liste / cartes ; clic pour ouvrir la page.

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL Wiki.js — ex. `http://wikijs.example.com:3000` |
| `token` | Token API (Administration → API) — secret |

📖 Obtenir les identifiants : [Wiki.js — Token API (Administration → API)](https://docs.requarks.io/dev/api)


## Médias

### 🎞️ emby

**Emby** · v0.1.0

Emby : sessions en cours (qui regarde quoi), bibliothèques et compteurs, derniers ajouts, activité serveur et comptes utilisateurs.

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL Emby — ex. `http://emby.local:8096` |
| `apikey` | Clé API — secret |

📖 Obtenir les identifiants : [Emby — clé API (Dashboard → Advanced → API Keys)](https://github.com/MediaBrowser/Emby/wiki/Api-Key-Authentication)

### 📸 instagram

**Instagram** · v0.4.0

Galerie des derniers posts Instagram, synchronisés en local par instaloader (service insta-sync sur Panda).

**Configuration :**

| Champ | Description |
|---|---|
| `path` | Dossier des médias — ex. `~/instagram` |
| `login` | Identifiant Instagram (pseudo — pour la synchro) — ex. `ton_pseudo` |
| `targets` | À télécharger — choix : Publications sauvegardées / Mon profil (mes publications) |
| `media` | Type de médias — choix : Photos et vidéos / Photos uniquement / Vidéos uniquement |
| `profile` | Profil affiché par défaut — ex. `(auto : le plus fourni)` |

### 📺 kodi

**Kodi** · v0.3.0

Kodi (Cormoran/Ours) : télécommande complète (lecture, navigation, volume) et bibliothèque — films et épisodes récemment ajoutés avec affiches. Deux onglets : Lecture et Bibliothèque.

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL Kodi (JSON-RPC) — ex. `http://kodi.example.com:8080` |
| `user` | Utilisateur |
| `pass` | Mot de passe — secret |

### 📚 livres

**Livres** · v0.4.0

Kavita (Hérisson) : bibliothèques, lectures en cours, nouveautés, recherche et LISEUSE intégrée — lecture des BD page par page au tactile (zones gauche/droite/centre, curseur, progression synchronisée avec Kavita).

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL Kavita — ex. `http://kavita.example.com` |
| `apikey` | Clé API (Compte → Clé API) — secret |

📖 Obtenir les identifiants : [Kavita — Clé API (Compte → Clé API)](https://wiki.kavitareader.com/guides/settings/account/)

### 🎵 musique

**Musique** · v0.2.1

Lecteur audio branché sur Navidrome (lecture persistante en fond).

**Configuration :**

| Champ | Description |
|---|---|
| `url` | URL Navidrome — ex. `http://navidrome.example.com` |
| `user` | Utilisateur |
| `pass` | Mot de passe — secret |

📖 Obtenir les identifiants : [Navidrome](https://www.navidrome.org/docs/)


---

_Page générée depuis les manifests des addons. Panda & Abeille — The Worm's._