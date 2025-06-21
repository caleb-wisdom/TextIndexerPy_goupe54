TextIndexerPy

est une application indexeur de texte en ligne de commande écrite en Python, conçu par les membres du groupe 54, suivant les instructions données par le professeur, elle permet d'analyser un ensemble de fichiers texte, les indexer, et permettre la recherche rapide de mots ou expressions.

## Structure du projet


TextIndexerPy/
├── document_loader.py   # Chargement et prétraitement des fichiers texte
├── indexer.py           # Construction de l'index inversé
├── search_engine.py     # Recherche de mots et calcul de pertinence
├── retrieval.py         # Tri et affichage des résultats
├── stats.py             # Statistiques sur les textes
└── main_cli.py          # Interface principale (point d'entrée du programme)


## Comment exécuter le projet

1. **Préparer les fichiers texte** : Crée un dossier contenant des fichiers `.txt`.

2. **Exécuter le programme** :

- fichier-python: main_cli.py


3. **Suivre le menu** :
- `1` → Recherche de mots-clés
- `2` → Affichage des statistiques
- `3` → Quitter

##  Fonctionnalités principales

- Chargement de plusieurs fichiers texte.
- Nettoyage automatique : minuscules, suppression de ponctuation.
- Construction d’un index inversé.
- Recherche simple de mots ou expressions.
- Classement des documents par fréquence des mots (TF).
- Affichage d’extraits contextuels (snippets).
- Statistiques globales (mots uniques, plus fréquents, etc.).

## Dépendances

Aucune dépendance externe. Utilise uniquement la bibliothèque standard Python 3.

## Rapport de projet

- le rapport du projet serra soumis sous format imprimé 

## Auteurs 
- ngoie katota caleb
- ngoie bakafwa elvic
- ngoie pascaline christelle
- ngoie gamboa arcel
- ngoie ndaie gad

## Apprentissage
Ce projet a été conçu pour un apprentissage pratique autour :
- Des chaînes de caractères,
- des boucles et fonctions
- Des dictionnaires et listes en Python,
- De la conception d’algorithmes simples de recherche textuelle.

---

© UDBL - GROUPE 54, 2025
