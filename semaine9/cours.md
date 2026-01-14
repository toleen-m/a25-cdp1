# Exercices sur les Imports en Python

## Exercice 1 : Module `random`

### 1.1 : Lancer de dés

```python
# Écrivez un programme qui simule:
# 1. Le lancer de 2 dés à 6 faces
# 2. Affiche chaque résultat
# 3. Calcule et affiche la somme
# 4. Si c'est un double, affiche "DOUBLE!"

# Import nécessaire
import random

# Votre code ici
```

### 1.2 : Tirage au sort

```python
# Créez un tirage au sort pour une liste d'étudiants
etudiants = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# 1. Mélangez la liste aléatoirement
# 2. Choisissez un gagnant au hasard
# 3. Choisissez 2 gagnants différents
# 4. Affichez l'ordre de passage aléatoire

import random

# Votre code ici
```

## Exercice 2 : Module `math`

### 2.1 : Calculs géométriques

```python
# Écrivez un programme qui calcule:
# 1. L'aire d'un cercle (π × r²)
# 2. Le périmètre d'un cercle (2 × π × r)
# 3. L'hypoténuse d'un triangle rectangle (√(a² + b²))
# 4. Arrondissez π à 2 décimales

import math

rayon = 5
cote_a = 3
cote_b = 4

# Votre code ici
```

### 2.2 : Conversions

```python
# Convertissez:
# 1. 180 degrés en radians
# 2. π radians en degrés
# 3. Calculez sin(90°)
# 4. Calculez cos(π)

import math

# Votre code ici
```

## Exercice 3 : Module `json`

### 3.1 : Sauvegarde de données

```python
# Créez un programme qui:
# 1. Crée un dictionnaire d'étudiant
# 2. Le sauvegarde dans un fichier JSON
# 3. Le relit depuis le fichier
# 4. Affiche les données lues

import json

etudiant = {
    "nom": "Alice",
    "age": 20,
    "notes": [15, 18, 12],
    "present": True
}

# Votre code ici
```

### 3.2 : Journal d'événements

```python
# Créez un journal qui:
# 1. Ajoute des événements à un fichier JSON
# 2. Chaque événement a: date, type, message
# 3. Peut lire tout l'historique
# 4. Compte le nombre d'événements

import json
import datetime

# Votre code ici
```

## Exercice 4 : Module `os`

### 4.1 : Vérificateur de fichiers

```python
# Écrivez un programme qui:
# 1. Vérifie si un fichier existe
# 2. Si oui, affiche sa taille
# 3. Si non, le crée avec du contenu
# 4. Liste les fichiers du dossier courant

import os

fichier = "test.txt"

# Votre code ici
```

### 4.2 : Gestionnaire de projets

```python
# Créez un gestionnaire qui:
# 1. Crée un dossier pour un projet
# 2. Crée des fichiers README.md et main.py dans le dossier
# 3. Vérifie que le dossier a été créé
# 4. Nettoie en supprimant le dossier (optionnel)

import os

# Votre code ici
```

## Exercice 5 : Module `copy`

### 5.1 : Copies de listes

```python
# Montrez la différence entre:
# 1. Une référence (l1 = l2)
# 2. Une copie superficielle
# 3. Une copie profonde

import copy

originale = [[1, 2], [3, 4]]

# Votre code ici
# Modifiez une sous-liste et observez les effets
```

### 5.2 : Système de sauvegarde

```python
# Créez un système qui:
# 1. Garde une copie de sauvegarde des données
# 2. Permet de restaurer la version précédente
# 3. Montre la différence entre les versions

import copy

donnees = {
    "utilisateurs": ["Alice", "Bob"],
    "config": {"theme": "sombre", "langue": "fr"}
}

# Votre code ici
```

## Exercice 6 : Combinaisons d'imports

### 6.1 : Jeu de dés amélioré

```python
# Créez un jeu qui:
# 1. Lance 3 dés (random)
# 2. Calcule les statistiques (math)
# 3. Sauvegarde les résultats (json)
# 4. Vérifie si le fichier de scores existe (os)

import random
import math
import json
import os

# Votre code ici
```

### 6.2 : Système de configuration

```python
# Créez un système de configuration qui:
# 1. Lit un fichier JSON de configuration
# 2. Si non existant, crée une config par défaut
# 3. Sauvegarde une copie de backup
# 4. Génère des IDs aléatoires pour les utilisateurs

import json
import os
import random
import copy

# Votre code ici
```
