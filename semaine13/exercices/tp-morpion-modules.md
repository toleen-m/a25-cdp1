# ÉNONCÉ 1 — Morpion avec modules et packages

## Objectif

Vous devez transformer un jeu de morpion écrit dans un seul fichier en un projet structuré utilisant **des modules et un package Python**.

Ce travail vous permettra de comprendre :

- comment créer un module Python
- comment créer un package Python
- comment importer des fonctions depuis d'autres fichiers
- comment organiser un projet Python proprement

---

## Résultat attendu

Le jeu doit fonctionner exactement comme avant :

- deux joueurs jouent à tour de rôle
- chaque joueur entre un nombre entre 1 et 9
- le jeu affiche la grille
- le jeu détecte une victoire
- le jeu détecte une égalité

Exemple :

```
 .  .  .
 .  .  .
 .  .  .

Joueur 1 [1-9] ? > 5

 .  .  .
 .  O  .
 .  .  .
```

---

## Structure obligatoire du projet

Vous devez utiliser cette structure :

```
morpion/
│
├── main.py
│
└── tictactoe/
    ├── __init__.py
    ├── board.py
    ├── rules.py
    └── ui.py
```

---

## Rôle de chaque module

### board.py

Ce module doit contenir les fonctions :

- créer la grille
- convertir une position (1-9) en ligne et colonne
- vérifier si une case est vide
- placer un symbole

---

### rules.py

Ce module doit contenir les fonctions :

- vérifier si un joueur a gagné
- vérifier s'il y a une égalité

---

### ui.py

Ce module doit contenir les fonctions :

- afficher la grille
- demander une position au joueur
- afficher un message

---

### main.py

Ce fichier doit :

- importer les modules
- contenir la boucle principale du jeu
- gérer le joueur courant

---

## Contraintes importantes

Vous devez utiliser des imports comme :

```python
from tictactoe.board import create_board
```

et NON :

```python
import board
```

---

## Critères de réussite

Votre programme doit :

- fonctionner sans erreur
- utiliser plusieurs modules
- utiliser un package
- utiliser des imports corrects
- avoir un code clair et organisé

---

## Bonus (optionnel)

Ajouter :

- une vérification si la case est déjà prise
- un message d'erreur si l'utilisateur entre une mauvaise valeur
