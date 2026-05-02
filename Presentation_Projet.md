# Présentation du Projet SafeHaven
*(Plan pour le fichier PowerPoint)*

---

## Slide 1 : Titre
**SafeHaven**
*Système de Gestion de Refuge Animalier*
Projet développé avec Python et Django

---

## Slide 2 : Le Besoin
**Pourquoi SafeHaven ?**
- Les refuges manquent souvent d'outils numériques adaptés.
- **Objectif** : Créer une application centralisée pour gérer les animaux, leur santé et les adoptions.
- **Cibles** : 
  - Les responsables de refuge (Admin).
  - Les bénévoles / soigneurs sur le terrain.
  - Le public cherchant à adopter.

---

## Slide 3 : Architecture des Données
**Structure de la Base de Données**
Trois tables principales (Modèles Django) :
1. **Espèce** : Catégorisation biologique (Chiens, Chats, NAC) et besoins.
2. **Animal** : Fiche complète (Nom, Race, Sexe, Santé, Compatibilités, Statut).
3. **Adoption** : Registre des départs (Adoptant, Date, Frais).

---

## Slide 4 : Fonctionnalités Clés
**Ce que permet l'application :**
- 🐶 **Fiches détaillées** : Suivi médical (vaccin, stérilisation) et comportemental (ententes).
- 🔍 **Moteur de Recherche** : Filtres avancés par durée de séjour, espèce, sexe et compatibilités.
- 🎨 **Interface visuelle claire** : Utilisation de badges Bootstrap (Bleu = Disponible, Rouge = Adopté, Gris = En soin).
- 🔒 **Espaces sécurisés** : Ajout et modification restreints aux bénévoles connectés.

---

## Slide 5 : Démonstration Technique
**Stack Technique :**
- **Backend** : Django (Python) pour la logique métier, l'ORM et la sécurité.
- **Frontend** : HTML5, CSS3, Bootstrap 5 pour un design responsive.
- **Base de Données** : SQLite (évolutif vers PostgreSQL).
- **Administration** : Interface `/admin` native de Django pour la gestion globale.

---

## Slide 6 : Conclusion & Perspectives
**Bilan du projet :**
- L'application répond à l'intégralité du cahier des charges.
- Le code est propre, structuré (MVC/MVT) et prêt à être déployé.

**Perspectives d'évolution :**
- Ajout d'un système de dons en ligne.
- Gestion des plannings des bénévoles.
- Intégration d'une API pour partager les annonces sur les réseaux sociaux.
