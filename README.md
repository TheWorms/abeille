# 🐝 Abeille — le store d'addons de Panda

Abeille est le dépôt d'addons du kiosk domestique **Panda**. Chaque addon apporte une tuile et une vue dédiée à un service de la maison (cuisine, médias, monitoring, quotidien…). Les tuiles arborent le **logo officiel** de chaque application (SVG embarqué, rendu net à toute taille et disponible hors-ligne).

## Installation du store

Dans Panda : **⚙ Réglages → Store**. Le store officiel est préconfiguré ; les addons s'installent et se mettent à jour en un tap depuis l'onglet Store. Les mises à jour disponibles sont signalées par un badge **⬆ MISE À JOUR** et une pastille sur l'icône du Store.

L'index du store est **signé** (Ed25519) : Panda vérifie la signature avant d'accepter tout catalogue, garantissant que les addons proviennent bien de cette source.

## Configuration des addons

📖 **[Voir la page complète de configuration des addons »](CONFIGURATION.md)** — tous les réglages, champ par champ.

Après installation, chaque addon se configure depuis sa tuile via l'icône **⚙** (URL du service, identifiants ou clés API). Le bouton **Tester** valide la connexion avant d'enregistrer. La configuration est relue à chaud, sans redémarrage.


## Catalogue — 37 addons

| | Addon | Version | Catégorie | Description |
|---|---|---|---|---|
| 🧊 | Congélateur | 0.2.4 | Maison |  |
| 🛒 | Courses | 0.2.4 | Maison |  |
| 🥘 | Hub KitchenOwl | 0.2.5 | Maison |  |
| 🌱 | Jardin | 0.3.1 | Maison |  |
| 📖 | Recettes | 0.2.4 | Maison |  |
| 📅 | Repas semaine | 0.3.3 | Maison |  |
| 📦 | Stock cuisine | 0.2.4 | Maison |  |
| 🐜 | Abonnements | 0.4.3 | Quotidien | Abonnements via Wallos (Fourmi) : budget du mois (dû/prélevé/restant), tous les abonnements en cartes, répartition par… |
| 📆 | Agenda | 0.3.2 | Quotidien | Agenda CalDAV (Infomaniak, Nextcloud, Baïkal, Radicale, Fastmail, Google…) : événements à venir, notifications, ajout… |
| 💶 | Budget | 0.2.3 | Quotidien |  |
| 🌊 | Marée | 0.3.2 | Quotidien |  |
| 🌙 | Soleil & Lune | 1.0.2 | Quotidien | Lever et coucher du soleil, durée du jour, phase et illumination de la lune — calculés localement, sans connexion. |
| 🚆 | Transport | 0.2.2 | Quotidien |  |
| 🐳 | Arcane | 0.3.3 | Services | Conteneurs Docker via Arcane, tous environnements agrégés (badge machine) : stats, liste ou cartes avec ports et état, actions… |
| 🗂️ | Forgejo | 0.3.1 | Services | Dépôts Forgejo — cartes ou liste, recherche, historique des derniers commits. |
| 🐙 | GitHub | 0.1.1 | Services | GitHub : tes dépôts publics et privés (étoiles, issues, dernier push), notifications non lues, issues et pull requests… |
| 📊 | Grafana | 0.3.2 | Services | Supervision Grafana : santé et version, sources de données et leur état, alertes actives, liste des dashboards, et rendu à la… |
| 🔴 | Hetzner | 0.5.1 | Services | Hetzner : serveurs Cloud multi-projets (jusqu'à 8 projets, un token par projet), état/type/IP/datacenter/coût mensuel,… |
| 🌐 | Infomaniak | 0.6.1 | Services | Infomaniak multi-organisations : balaie automatiquement tous tes comptes (Koody, ES Production…) et agrège domaines,… |
| ✉️ | Mail | 0.1.2 | Services | Boîte mail IMAP (Infomaniak, Gmail, Proton Bridge…) : lire les messages, marquer lu/non lu, supprimer. |
| 🐕 | Malinois | 0.1.2 | Services | Trackers privés via tracker-autovisit (Malinois) : état des visites automatiques (OK / échec), dernière visite, alertes, et… |
| ☁️ | Nextcloud | 0.4.2 | Services | . Explorateur avec bascule liste / cartes (vignettes en grille). |
| ☁️ | OVH | 0.2.1 | Services | OVHcloud : domaines (expiration, offre, DNSSEC), hébergements web, VPS, serveurs dédiés et projets Public Cloud. Sections… |
| 📄 | Paperless | 0.3.2 | Services | Paperless-ngx (Méduse) : statistiques (documents, réception, correspondants, types, tags), recherche plein-texte, boîte de… |
| 🛡️ | Pi-hole | 0.7.1 | Services | Supervision Pi-hole v6 multi-instances : ajoute autant de nœuds que tu veux, statistiques détaillées (top domaines/clients,… |
| 🖥️ | Proxmox | 0.2.2 | Services |  |
| 🎬 | Radarr | 0.2.6 | Services | Radarr : statistiques (films, disponibles, manquants, file), téléchargements en cours, prochaines sorties et films récemment… |
| 💾 | Sauvegardes | 0.4.2 | Services | Liste des sauvegardes vzdump présentes sur les stockages Proxmox, regroupées par VM/CT : dernière sauvegarde, nombre, taille… |
| 📺 | Sonarr | 0.2.7 | Services | Sonarr : statistiques (séries, épisodes, file, manquants), téléchargements en cours, épisodes à venir et séries récemment… |
| 🟢 | Uptime Kuma | 0.3.2 | Services | Uptime Kuma (Faucon) : statistiques (en ligne, hors ligne, ping moyen), moniteurs en liste ou cartes avec uptime 24 h, temps… |
| 📡 | WatchYourLAN | 0.3.3 | Services | Hôtes du réseau via WatchYourLAN (Furet) : nom, IP, MAC, matériel et statut en ligne. Bascule liste / cartes, hôtes hors ligne… |
| 📚 | Wiki.js | 0.3.3 | Services | Wiki.js (Hibou) : statistiques (pages, publiées, brouillons, dossiers), recherche, pages récemment modifiées et arborescence… |
| 🎞️ | Emby | 0.2.2 | Médias | Emby : statistiques (films, séries, épisodes, lectures en cours), ce qui est en lecture maintenant, reprise (continuer à… |
| 📸 | Instagram | 0.4.2 | Médias |  |
| 📺 | Kodi | 0.3.2 | Médias | Kodi (Cormoran/Ours) : télécommande complète (lecture, navigation, volume) et bibliothèque — films et épisodes récemment… |
| 📚 | Livres | 0.4.2 | Médias | Kavita (Hérisson) : bibliothèques, lectures en cours, nouveautés, recherche et LISEUSE intégrée — lecture des BD page par page… |
| 🎵 | Musique | 0.2.2 | Médias |  |


---

_Catalogue généré automatiquement depuis l'index signé du store. Panda & Abeille — The Worm's._

