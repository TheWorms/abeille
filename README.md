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
| <img src="logos/congelateur.svg" width="22" alt=""> | Congélateur | 0.2.4 | Maison |  |
| <img src="logos/courses.svg" width="22" alt=""> | Courses | 0.2.4 | Maison |  |
| <img src="logos/kitchenowl.svg" width="22" alt=""> | Hub KitchenOwl | 0.2.5 | Maison |  |
| <img src="logos/jardin.svg" width="22" alt=""> | Jardin | 0.3.1 | Maison |  |
| <img src="logos/recettes.svg" width="22" alt=""> | Recettes | 0.2.4 | Maison |  |
| <img src="logos/repas.svg" width="22" alt=""> | Repas semaine | 0.3.3 | Maison |  |
| <img src="logos/stock.svg" width="22" alt=""> | Stock cuisine | 0.2.4 | Maison |  |
| <img src="logos/wallos.svg" width="22" alt=""> | Abonnements | 0.4.3 | Quotidien | Abonnements via Wallos (Fourmi) : budget du mois (dû/prélevé/restant), tous les abonnements en cartes, répartition par… |
| <img src="logos/agenda.svg" width="22" alt=""> | Agenda | 0.3.2 | Quotidien | Agenda CalDAV (Infomaniak, Nextcloud, Baïkal, Radicale, Fastmail, Google…) : événements à venir, notifications, ajout… |
| <img src="logos/budget.svg" width="22" alt=""> | Budget | 0.2.3 | Quotidien |  |
| <img src="logos/maree.svg" width="22" alt=""> | Marée | 0.3.2 | Quotidien |  |
| <img src="logos/soleil-lune.svg" width="22" alt=""> | Soleil & Lune | 1.0.2 | Quotidien | Lever et coucher du soleil, durée du jour, phase et illumination de la lune — calculés localement, sans connexion. |
| <img src="logos/transport.svg" width="22" alt=""> | Transport | 0.2.2 | Quotidien |  |
| <img src="logos/arcane.svg" width="22" alt=""> | Arcane | 0.3.3 | Services | Conteneurs Docker via Arcane, tous environnements agrégés (badge machine) : stats, liste ou cartes avec ports et état, actions… |
| <img src="logos/forgejo.svg" width="22" alt=""> | Forgejo | 0.3.1 | Services | Dépôts Forgejo — cartes ou liste, recherche, historique des derniers commits. |
| <img src="logos/github.svg" width="22" alt=""> | GitHub | 0.1.4 | Services | GitHub : tes dépôts publics et privés (étoiles, issues, dernier push), notifications non lues, issues et pull requests… |
| <img src="logos/grafana.svg" width="22" alt=""> | Grafana | 0.3.5 | Services | Supervision Grafana : santé et version, sources de données et leur état, alertes actives, liste des dashboards, et rendu à la… |
| <img src="logos/hetzner.svg" width="22" alt=""> | Hetzner | 0.5.1 | Services | Hetzner : serveurs Cloud multi-projets (jusqu'à 8 projets, un token par projet), état/type/IP/datacenter/coût mensuel,… |
| <img src="logos/infomaniak.svg" width="22" alt=""> | Infomaniak | 0.6.1 | Services | Infomaniak multi-organisations : balaie automatiquement tous tes comptes (Koody, ES Production…) et agrège domaines,… |
| <img src="logos/mail.svg" width="22" alt=""> | Mail | 0.1.2 | Services | Boîte mail IMAP (Infomaniak, Gmail, Proton Bridge…) : lire les messages, marquer lu/non lu, supprimer. |
| <img src="logos/malinois.svg" width="22" alt=""> | Malinois | 0.1.2 | Services | Trackers privés via tracker-autovisit (Malinois) : état des visites automatiques (OK / échec), dernière visite, alertes, et… |
| <img src="logos/nextcloud.svg" width="22" alt=""> | Nextcloud | 0.4.2 | Services | . Explorateur avec bascule liste / cartes (vignettes en grille). |
| <img src="logos/ovh.svg" width="22" alt=""> | OVH | 0.2.1 | Services | OVHcloud : domaines (expiration, offre, DNSSEC), hébergements web, VPS, serveurs dédiés et projets Public Cloud. Sections… |
| <img src="logos/paperless.svg" width="22" alt=""> | Paperless | 0.3.2 | Services | Paperless-ngx (Méduse) : statistiques (documents, réception, correspondants, types, tags), recherche plein-texte, boîte de… |
| <img src="logos/pihole.svg" width="22" alt=""> | Pi-hole | 0.7.1 | Services | Supervision Pi-hole v6 multi-instances : ajoute autant de nœuds que tu veux, statistiques détaillées (top domaines/clients,… |
| <img src="logos/proxmox.svg" width="22" alt=""> | Proxmox | 0.2.2 | Services |  |
| <img src="logos/radarr.svg" width="22" alt=""> | Radarr | 0.2.9 | Services | Radarr : statistiques (films, disponibles, manquants, file), téléchargements en cours, prochaines sorties et films récemment… |
| <img src="logos/backups.svg" width="22" alt=""> | Sauvegardes | 0.4.2 | Services | Liste des sauvegardes vzdump présentes sur les stockages Proxmox, regroupées par VM/CT : dernière sauvegarde, nombre, taille… |
| <img src="logos/sonarr.svg" width="22" alt=""> | Sonarr | 0.2.7 | Services | Sonarr : statistiques (séries, épisodes, file, manquants), téléchargements en cours, épisodes à venir et séries récemment… |
| <img src="logos/kuma.svg" width="22" alt=""> | Uptime Kuma | 0.3.2 | Services | Uptime Kuma (Faucon) : statistiques (en ligne, hors ligne, ping moyen), moniteurs en liste ou cartes avec uptime 24 h, temps… |
| <img src="logos/wyl.svg" width="22" alt=""> | WatchYourLAN | 0.3.3 | Services | Hôtes du réseau via WatchYourLAN (Furet) : nom, IP, MAC, matériel et statut en ligne. Bascule liste / cartes, hôtes hors ligne… |
| <img src="logos/wikijs.svg" width="22" alt=""> | Wiki.js | 0.3.3 | Services | Wiki.js (Hibou) : statistiques (pages, publiées, brouillons, dossiers), recherche, pages récemment modifiées et arborescence… |
| <img src="logos/emby.svg" width="22" alt=""> | Emby | 0.2.2 | Médias | Emby : statistiques (films, séries, épisodes, lectures en cours), ce qui est en lecture maintenant, reprise (continuer à… |
| <img src="logos/instagram.svg" width="22" alt=""> | Instagram | 0.4.2 | Médias |  |
| <img src="logos/kodi.svg" width="22" alt=""> | Kodi | 0.3.2 | Médias | Kodi (Cormoran/Ours) : télécommande complète (lecture, navigation, volume) et bibliothèque — films et épisodes récemment… |
| <img src="logos/livres.svg" width="22" alt=""> | Livres | 0.4.2 | Médias | Kavita (Hérisson) : bibliothèques, lectures en cours, nouveautés, recherche et LISEUSE intégrée — lecture des BD page par page… |
| <img src="logos/musique.svg" width="22" alt=""> | Musique | 0.2.2 | Médias |  |


---

_Catalogue généré automatiquement depuis l'index signé du store. Panda & Abeille — The Worm's._

