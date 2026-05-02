# Rapport de Projet : Système de Gestion de Refuge Animalier (SafeHaven)

## 1. Présentation du Projet
SafeHaven est une application web conçue pour répondre aux besoins spécifiques d'un refuge ou d'une association de protection animale. Elle permet de gérer efficacement les pensionnaires, de suivre leur état de santé et d'organiser les adoptions.

L'application a été développée en Python en utilisant le framework **Django**, avec une interface utilisateur stylisée grâce à **Bootstrap 5**.

## 2. Architecture et Modèles de Données

L'application s'articule autour de trois modèles principaux, stockés dans une base de données SQLite :

### A. Modèle `Espece`
Ce modèle permet de catégoriser les animaux.
- **Champs** : `nom_espece` (Chien, Chat, NAC, etc.), `besoins_specifiques` (texte).

### B. Modèle `Animal`
Le cœur de l'application. Il contient toutes les informations d'un pensionnaire.
- **Informations générales** : Nom, Espèce (Clé étrangère), Race, Sexe, Date de naissance estimée.
- **Santé** : Statut vaccinal (booléen), Stérilisation (booléen).
- **Compatibilités (Ententes)** : Ok Chats, Ok Chiens, Ok Enfants. *Ces champs sont cruciaux pour le système de filtrage et pour s'assurer du bon placement de l'animal.*
- **Séjour** : Date d'arrivée, Statut (Disponible, En soin, Adopté, En famille d'accueil).

### C. Modèle `Adoption`
Gère l'historique des départs.
- **Champs** : Animal (OneToOne), Nom de l'adoptant, Date d'adoption, Frais de participation.

## 3. Fonctionnalités Implémentées

### Espace Public (Visiteurs)
- **Catalogue des pensionnaires** : Affichage sous forme de cartes (cards) interactives.
- **Moteur de recherche avancé** : Filtrage par nom, espèce, sexe, compatibilités (chats, chiens, enfants), et par durée de séjour au refuge (récent, moyen, long).
- **Fiches détaillées** : Visualisation claire des informations de santé et du statut de l'animal avec des badges colorés (Bleu = Disponible, Gris = En soin, Rouge avec cœur = Adopté, Jaune = En FA).

### Espace Bénévole / Admin
- **Authentification sécurisée** : Accès restreint via un système de login.
- **Gestion des fiches** : Ajout et modification des animaux depuis l'interface publique (réservé aux utilisateurs connectés).
- **Panel d'Administration Django** : Interface backend (`/admin`) permettant une gestion poussée (CRUD complet) de toutes les tables (Animaux, Espèces, Adoptions, Utilisateurs).

## 4. Choix Techniques

- **Backend** : Django (Python) a été choisi pour sa robustesse, son ORM intégré facilitant les requêtes complexes (ex: le filtrage multicritère), et son interface d'administration générée automatiquement.
- **Frontend** : L'utilisation de Bootstrap 5 permet d'obtenir une interface *responsive* (adaptée aux mobiles) rapidement. L'utilisation de badges et d'icônes (FontAwesome) améliore l'expérience utilisateur et la lisibilité des statuts.
- **Base de données** : SQLite (par défaut dans Django) est utilisé pour simplifier le déploiement de ce projet. Il peut facilement être migré vers PostgreSQL pour une mise en production à grande échelle.

## 5. Déploiement et Utilisation locale

Pour lancer le projet localement :
1. Installer Python et Django (`pip install django`).
2. Cloner ou extraire le dossier du projet.
3. Se placer dans le dossier `safehaven` et exécuter : `python manage.py runserver`.
4. Accéder à l'application via `http://127.0.0.1:8000/`.
5. Accéder à l'administration via `http://127.0.0.1:8000/admin/`.
