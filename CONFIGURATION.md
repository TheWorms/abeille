# ⚙️ Configuration des addons

Cette page décrit les réglages de chaque addon du store. La configuration se fait depuis l'écran tactile de Panda via le bouton **⚙** de chaque addon, ou à distance avec l'outil `panda-cfg.py` depuis Gypaete (`ssh -t theworms@panda.lan 'python3 ~/panda-cfg.py'`).

Les champs marqués **secret 🔒** (clés, jetons, mots de passe) sont saisis en invisible : leur valeur n'apparaît pas à l'écran.


## Sommaire

- 🏠 **Maison** — Congélateur, Courses, Hub KitchenOwl, Jardin, Recettes, Repas semaine, Stock cuisine
- 📅 **Quotidien** — Abonnements, Agenda, Budget, Marée, Soleil & Lune, Transport
- 🔧 **Services** — Arcane, Forgejo, Grafana, Mail, Nextcloud, Paperless, Pi-hole, Proxmox, Radarr, Sauvegardes, Sonarr, Uptime Kuma, WatchYourLAN, Wiki.js
- 🎬 **Médias** — Emby, Instagram, Kodi, Livres, Musique


## 🏠 Maison

### Congélateur  

| Champ | Type | À renseigner |
|---|---|---|
| `category` | texte | Catégorie |


### Courses  

_Aucun réglage — cet addon fonctionne sans configuration._


### Hub KitchenOwl  

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `token` | secret 🔒 | Jeton d'accès / API token |
| `household` | texte | Identifiant du foyer (KitchenOwl) |


### Jardin  

_Aucun réglage — cet addon fonctionne sans configuration._


### Recettes  

_Aucun réglage — cet addon fonctionne sans configuration._


### Repas semaine  

_Aucun réglage — cet addon fonctionne sans configuration._


### Stock cuisine  

_Aucun réglage — cet addon fonctionne sans configuration._



## 📅 Quotidien

### Abonnements  

Abonnements via Wallos (Fourmi) : budget du mois (dû/prélevé/restant), tous les abonnements en cartes, répartition par catégorie (donut) et prévisionnel des prochains mois. Disposition (onglets ou page unique) et horizon configurables.

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `apikey` | secret 🔒 | Clé API du service |
| `layout` | liste | Disposition |
| `forecast` | liste | Prévisionnel — nombre de mois |


### Agenda  

Agenda CalDAV (Infomaniak, Nextcloud, Baïkal, Radicale, Fastmail, Google…) : événements à venir, notifications, ajout d'événements.

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `user` | texte | Nom d'utilisateur |
| `pass` | secret 🔒 | Mot de passe |
| `calendar` | texte | Calendrier à afficher |
| `notif` | liste | Notifications |


### Budget  

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `apikey` | secret 🔒 | Clé API du service |
| `budget` | texte | Budget mensuel |


### Marée  

| Champ | Type | À renseigner |
|---|---|---|
| `site` | texte | Site / station |
| `apikey` | secret 🔒 | Clé API du service |


### Soleil & Lune  

Lever et coucher du soleil, durée du jour, phase et illumination de la lune — calculés localement, sans connexion.

| Champ | Type | À renseigner |
|---|---|---|
| `lat` | texte | Latitude |
| `lon` | texte | Longitude |
| `tz` | texte | Fuseau horaire |


### Transport  

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `token` | secret 🔒 | Jeton d'accès / API token |
| `coverage` | texte | Zone de couverture |



## 🔧 Services

### Arcane  

Conteneurs Docker via Arcane, tous environnements agrégés (badge machine) : stats, liste ou cartes avec ports et état, actions démarrer / arrêter / redémarrer. Arrêtés grisés, mises à jour signalées.

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `apikey` | secret 🔒 | Clé API du service |


### Forgejo  

Dépôts Forgejo — cartes ou liste, recherche, historique des derniers commits.

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `token` | secret 🔒 | Jeton d'accès / API token |
| `view` | liste | Affichage des dépôts |
| `hist` | liste | Historique des commits (panneau de droite) |


### Grafana  

Supervision Grafana : santé et version, sources de données et leur état, alertes actives, liste des dashboards, et rendu à la demande d'un panel (image PNG via le renderer).

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `apikey` | secret 🔒 | Clé API du service |
| `theme` | liste | Thème d'affichage |


### Mail  

Boîte mail IMAP (Infomaniak, Gmail, Proton Bridge…) : lire les messages, marquer lu/non lu, supprimer.

| Champ | Type | À renseigner |
|---|---|---|
| `host` | texte | Hôte IMAP/SMTP |
| `port` | texte | Port |
| `user` | texte | Nom d'utilisateur |
| `pass` | secret 🔒 | Mot de passe |
| `folder` | texte | Dossier à surveiller |


### Nextcloud  

. Explorateur avec bascule liste / cartes (vignettes en grille).

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `user` | texte | Nom d'utilisateur |
| `pass` | secret 🔒 | Mot de passe |


### Paperless  

Paperless-ngx (Méduse) : statistiques (documents, réception, correspondants, types, tags), recherche plein-texte, boîte de réception et documents récents avec vignettes. Bascule liste / cartes ; clic pour ouvrir le document.

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `token` | secret 🔒 | Jeton d'accès / API token |


### Pi-hole  

Supervision Pi-hole v6 multi-instances : ajoute autant de nœuds que tu veux, statistiques détaillées (top domaines/clients, amont DNS, types de requêtes, historique 24 h), couleurs Pi-hole.

| Champ | Type | À renseigner |
|---|---|---|
| `name1` | texte | — Pi-hole 1 — Nom |
| `url1` | texte | URL nœud 1 |
| `pass1` | secret 🔒 | Mot de passe nœud 1 |
| `name2` | texte | — Pi-hole 2 — Nom |
| `url2` | texte | URL nœud 2 |
| `pass2` | secret 🔒 | Mot de passe nœud 2 |
| `name3` | texte | — Pi-hole 3 — Nom |
| `url3` | texte | URL 3 |
| `pass3` | secret 🔒 | Mot de passe d'application 3 |
| `name4` | texte | — Pi-hole 4 — Nom |
| `url4` | texte | URL 4 |
| `pass4` | secret 🔒 | Mot de passe d'application 4 |
| `name5` | texte | — Pi-hole 5 — Nom |
| `url5` | texte | URL 5 |
| `pass5` | secret 🔒 | Mot de passe d'application 5 |


### Proxmox  

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `token` | secret 🔒 | Jeton d'accès / API token |


### Radarr  

Radarr : statistiques (films, disponibles, manquants, file), téléchargements en cours, prochaines sorties et films récemment ajoutés avec affiches. Bascule liste / cartes ; clic pour la fiche détail (résumé, statut, qualité).

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `apikey` | secret 🔒 | Clé API du service |


### Sauvegardes  

Liste des sauvegardes vzdump présentes sur les stockages Proxmox, regroupées par VM/CT : dernière sauvegarde, nombre, taille cumulée, fichiers protégés.

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `token` | secret 🔒 | Jeton d'accès / API token |


### Sonarr  

Sonarr : statistiques (séries, épisodes, file, manquants), téléchargements en cours, épisodes à venir et séries récemment ajoutées avec affiches. Bascule liste / cartes ; clic pour la fiche détail (progression, saisons, statut).

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `apikey` | secret 🔒 | Clé API du service |


### Uptime Kuma  

Uptime Kuma (Faucon) : statistiques (en ligne, hors ligne, ping moyen), moniteurs en liste ou cartes avec uptime 24 h, temps de réponse et historique récent.

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `slug` | texte | Identifiant de la page de statut |
| `apikey` | secret 🔒 | Clé API du service |
| `label` | texte | Libellé |
| `format` | liste | Format |


### WatchYourLAN  

Hôtes du réseau via WatchYourLAN (Furet) : nom, IP, MAC, matériel et statut en ligne. Bascule liste / cartes, hôtes hors ligne grisés.

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |


### Wiki.js  

Wiki.js (Hibou) : statistiques (pages, publiées, brouillons, dossiers), recherche, pages récemment modifiées et arborescence par dossier. Bascule liste / cartes ; clic pour ouvrir la page.

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `token` | secret 🔒 | Jeton d'accès / API token |



## 🎬 Médias

### Emby  

Emby : statistiques (films, séries, épisodes, lectures en cours), ce qui est en lecture maintenant, reprise (continuer à regarder), bibliothèques et ajouts récents avec jaquettes. Bascule liste / cartes ; fiche détail avec résumé, genres et bouton « Lire dans Emby ».

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `apikey` | secret 🔒 | Clé API du service |


### Instagram  

| Champ | Type | À renseigner |
|---|---|---|
| `path` | texte | Chemin |
| `login` | texte | Identifiant |
| `targets` | liste | Comptes ciblés |
| `media` | liste | Médias |
| `profile` | texte | Profil |


### Kodi  

Kodi (Cormoran/Ours) : télécommande complète (lecture, navigation, volume) et bibliothèque — films et épisodes récemment ajoutés avec affiches. Deux onglets : Lecture et Bibliothèque.

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `user` | texte | Nom d'utilisateur |
| `pass` | secret 🔒 | Mot de passe |


### Livres  

Kavita (Hérisson) : bibliothèques, lectures en cours, nouveautés, recherche et LISEUSE intégrée — lecture des BD page par page au tactile (zones gauche/droite/centre, curseur, progression synchronisée avec Kavita).

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `apikey` | secret 🔒 | Clé API du service |


### Musique  

| Champ | Type | À renseigner |
|---|---|---|
| `url` | texte | URL du service (http://ip:port ou domaine) |
| `user` | texte | Nom d'utilisateur |
| `pass` | secret 🔒 | Mot de passe |



---

_Page générée à partir des manifestes des 32 addons. 27 nécessitent une configuration._
