# Veillllllle

## PARTIE 0 : veille sur la data 

### 1. Types de données : description

Les données peuvent être classées en plusieurs catégories :

    Données structurées : Ce sont des données organisées sous forme de tableaux (lignes et colonnes). Elles sont facilement lisibles par les machines. Exemples :
        Données dans des bases SQL (noms, âges, adresses)
        Logs de capteurs
        Données financières (transactions)

    Données non structurées : Données qui ne suivent pas un format préétabli. Elles sont plus complexes à traiter et à analyser. Exemples :
        Texte brut (articles, commentaires)
        Images, vidéos
        Audio (podcasts, enregistrements vocaux)

    Données semi-structurées : Données partiellement structurées, mais qui ne suivent pas un format rigide. Exemples :
        Fichiers XML, JSON
        Emails (structure de l’entête, corps du message libre)


### 2. Formats de données : exemples

Les formats des données varient en fonction du type de données. Voici quelques exemples courants :

    Données structurées :
        CSV (Comma-Separated Values)
        SQL (langage pour interagir avec des bases de données relationnelles)
        Excel (.xls, .xlsx)

    Données non structurées :
        Texte (.txt)
        Vidéos (.mp4, .avi)
        Images (.jpg, .png)
        Audio (.mp3, .wav)

    Données semi-structurées :
        JSON (JavaScript Object Notation)
        XML (Extensible Markup Language)
        YAML (Yet Another Markup Language)


### 3. Où trouver les données ?

Les sources de données sont multiples, et leur localisation dépend du domaine d’intérêt :

    Sources internes (données propres à une organisation) :
        Bases de données internes (ERP, CRM)
        Historique des transactions
        Données d’inventaire

    Sources externes :
        Open Data : Portails de données publiques (data.gouv.fr, OpenStreetMap)
        Réseaux sociaux : Twitter, Facebook
        Sources commerciales : Bases de données payantes (Statista, Bloomberg)
        IoT : Capteurs, dispositifs connectés
        Web Scraping : Extraction de données à partir de sites internet publics

### 4. Bonnes pratiques : Comment la stocker ?

    Sécurité des données :
        Chiffrement : Utiliser des techniques de chiffrement pour protéger les données sensibles, tant au repos qu’en transit.
        Contrôle d'accès : Définir des autorisations spécifiques pour limiter l'accès aux données en fonction des rôles.

    Formats de stockage adaptés :
        Bases de données relationnelles (SQL) pour les données structurées.
        Bases de données NoSQL (MongoDB, Cassandra) pour les données semi-structurées ou non structurées.
        Stockage en cloud (Amazon S3, Google Cloud Storage) pour les gros volumes de données non structurées (vidéos, images).

    Normes de qualité des données :
        Assurer la cohérence (éviter les doublons).
        Maintenir une traçabilité des données (d’où proviennent-elles, comment ont-elles été modifiées).

    Backup et récupération :
        Mettre en place des stratégies de sauvegarde régulière (quotidiennes, hebdomadaires).
        Tester les procédures de récupération de données pour minimiser les pertes en cas d’incident.

    Organisation et indexation :
        Cataloguer les données pour les rendre facilement accessibles (métadonnées, index).
        Utiliser des outils de gestion de version (Git) pour le suivi des changements sur les jeux de données.
