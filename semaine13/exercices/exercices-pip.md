# Exercice 1 — Installer son premier package (PyPI)

## Objectif

Installer un package simple.

## Instructions

Installer le package :

```
pip install colorama
```

## Vérifier installation

```
pip list
```

Le package `colorama` doit apparaître.

---

# Exercice 3 — Utiliser un package installé

## Objectif

Utiliser un package PyPI dans un programme.

Créer le fichier :

```
test_colorama.py
```

Exécuter :

```
python test_colorama.py
```

---

# Exercice 4 — Découvrir PyPI

## Instructions

Aller sur :

[https://pypi.org](https://pypi.org)

Trouver un package nommé :

```
emoji
```

Installer :

```
pip install emoji
```

Créer :

```python
import emoji

print(emoji.emojize("Python est amusant :snake:"))
```

---

# Exercice 5 — Comprendre le problème global

## Instructions

Afficher tous les packages installés :

```
pip list
```

Question :

Pourquoi est-ce problématique si tous les projets utilisent les mêmes packages ?

---

# Exercice 6 — Créer un environnement virtuel

Créer un environnement :

Windows :

```
python -m venv env
```

Mac/Linux :

```
python3 -m venv env
```

---

# Exercice 7 — Activer l’environnement

Windows :

```
env\Scripts\activate
```

Mac/Linux :

```
source env/bin/activate
```

Résultat attendu :

Le terminal affiche :

```
(env) C:\Users\...
```

---

# Exercice 8 — Installer un package dans l’environnement

Installer :

```
pip install colorama
```

Puis :

```
pip list
```

Vous verrez seulement quelques packages.

---

# Exercice 9 — Vérifier l’isolation

Désactiver :

```
deactivate
```

Puis :

```
pip list
```

Comparer avec l’environnement actif.

---

# Exercice 10 — Mini projet : programme coloré

## Objectif

Utiliser pip + environnement + package

Créer :

```
projet/
│
├── env/
└── main.py
```

Installer :

```
pip install colorama emoji
```

Code attendu :

```python
from colorama import Fore
import emoji

print(Fore.BLUE + emoji.emojize("Bonjour :smile:"))
```

---

# Exercice 11 — requirements.txt

## Objectif

Sauvegarder les dépendances

Commande :

```
pip freeze > requirements.txt
```

Fichier attendu :

```
colorama==0.4.6
emoji==2.8.0
```

---

# Exercice 12 — Reproduire un environnement

Supprimer env

Puis recréer :

```
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

---

# Exercice bonus

Installer :

```
pip install pyfiglet
```

Code :

```python
import pyfiglet

print(pyfiglet.figlet_format("Python"))
```

Résultat : texte ASCII géant.

# Exercice final — TP complet

Créer :

```
mon_projet/
│
├── env/
├── main.py
└── requirements.txt
```

Utiliser :

- colorama
- emoji
- pyfiglet

Afficher :

- texte coloré
- emoji
- ASCII art
