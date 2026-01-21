### **Exercices de Programmation Fonctionnelle en Python**

**Objectif :** Comprendre et pratiquer les concepts de la programmation fonctionnelle : pureté des fonctions, `map()`, `filter()`, `zip()`, `reduce()`, et expressions lambda.

---

## **Partie 1 : Fonctions Pures vs Non Pures**

### **Exercice 1.1 : Identifier la Pureté**

Pour chaque fonction ci-dessous, déterminez si elle est **pure** ou **non pure** et expliquez pourquoi.

```python
# Fonction A
def ajouter_pure(a, b):
    return a + b

# Fonction B
total = 0
def ajouter_impure(a):
    global total
    total += a
    return total

# Fonction C
def formater_message(nom):
    return f"Bonjour, {nom} !"

# Fonction D
import random
def lancer_de():
    return random.randint(1, 6)

# Fonction E
liste_resultats = []
def traiter_liste(lst):
    resultat = []
    for x in lst:
        resultat.append(x * 2)
    liste_resultats.extend(resultat)
    return resultat
```

### **Exercice 1.2 : Transformer en Fonction Pure**

Transformez cette fonction non pure en une fonction pure :

```python
# Version non pure
compteur = 0

def incrementer_impur():
    global compteur
    compteur += 1
    return compteur

# Votre version pure ici :
def incrementer_pur(valeur_actuelle):
    # À compléter
    pass

# Test
print(incrementer_pur(5))  # Devrait retourner 6
print(incrementer_pur(10)) # Devrait retourner 11
```

---

## **Partie 2 : Expressions Lambda**

### **Exercice 2.1 : Convertir en Lambda**

Convertissez ces fonctions normales en expressions lambda :

```python
# 1. Fonction qui double un nombre
def doubler(x):
    return x * 2

# Version lambda :
doubler_lambda = # À écrire

# 2. Fonction qui vérifie si un nombre est pair
def est_pair(x):
    return x % 2 == 0

# Version lambda :
est_pair_lambda = # À écrire

# 3. Fonction qui concatène deux chaînes avec un espace
def concatener(a, b):
    return a + " " + b

# Version lambda :
concatener_lambda = # À écrire
```

### **Exercice 2.2 : Utilisation avec Tri**

Utilisez une expression lambda pour trier cette liste de tuples par le deuxième élément :

```python
etudiants = [("Alice", 85), ("Bob", 72), ("Charlie", 93), ("Diana", 68)]

# Trier par note (du plus bas au plus haut) avec lambda
etudiants_tries = # À écrire

print(etudiants_tries)  # [('Diana', 68), ('Bob', 72), ('Alice', 85), ('Charlie', 93)]
```

---

## **Partie 3 : La fonction `map()`**

### **Exercice 3.1 : Application Simple**

Utilisez `map()` pour appliquer différentes transformations à une liste de nombres :

```python
nombres = [1, 2, 3, 4, 5]

# 1. Calculer les carrés
carres = # À écrire avec map() et lambda
print(list(carres))  # [1, 4, 9, 16, 25]

# 2. Convertir en chaîne avec préfixe "Nombre: "
chaines = # À écrire avec map() et lambda
print(list(chaines))  # ['Nombre: 1', 'Nombre: 2', ...]
```

### **Exercice 3.2 : Map avec Fonction Personnalisée**

Créez une fonction pure `celsius_vers_fahrenheit()` et utilisez-la avec `map()` :

```python
temperatures_c = [0, 20, 37, 100]

def celsius_vers_fahrenheit(c):
    # Conversion: F = C × 9/5 + 32
    # À compléter
    pass

# Utiliser map() avec votre fonction
temperatures_f = # À écrire
print(list(temperatures_f))  # [32.0, 68.0, 98.6, 212.0]
```

---

## **Partie 4 : La fonction `filter()`**

### **Exercice 4.1 : Filtrage Basique**

Utilisez `filter()` pour sélectionner des éléments selon des critères :

```python
nombres = range(1, 21)  # Nombres de 1 à 20

# 1. Nombres pairs
pairs = # À écrire avec filter() et lambda
print(list(pairs))  # [2, 4, 6, ..., 20]

# 2. Nombres divisibles par 3
div_par_3 = # À écrire
print(list(div_par_3))  # [3, 6, 9, 12, 15, 18]

# 3. Nombres > 10
grands = # À écrire
print(list(grands))  # [11, 12, ..., 20]
```

### **Exercice 4.2 : Filtrage Complexe**

Filtrez cette liste de mots selon deux critères :

```python
mots = ["python", "java", "functional", "programming", "lambda", "map", "filter", "reduce"]

# 1. Mots de plus de 5 caractères
longs_mots = # À écrire
print(list(longs_mots))  # ['python', 'functional', 'programming', 'lambda', 'filter', 'reduce']

# 2. Mots qui contiennent la lettre 'a'
avec_a = # À écrire
print(list(avec_a))  # ['java', 'functional', 'programming', 'lambda', 'map']
```

---

## **Partie 5 : La fonction `zip()`**

### **Exercice 5.1 : Combinaison de Listes**

Utilisez `zip()` pour combiner plusieurs listes :

```python
noms = ["Alice", "Bob", "Charlie"]
notes = [85, 72, 93]
matieres = ["Math", "Python", "Physique"]

# 1. Créer des tuples (nom, note)
combinaison1 = # À écrire
print(list(combinaison1))  # [('Alice', 85), ('Bob', 72), ('Charlie', 93)]

# 2. Créer des tuples (nom, note, matière)
combinaison2 = # À écrire
print(list(combinaison2))  # [('Alice', 85, 'Math'), ...]

# 3. Créer un dictionnaire nom -> note
dictionnaire = dict(# À écrire)
print(dictionnaire)  # {'Alice': 85, 'Bob': 72, 'Charlie': 93}
```

### **Exercice 5.2 : Dézipper et Transposer**

Utilisez `zip()` avec l'opérateur `*` pour "dézipper" :

```python
# Liste de coordonnées (x, y)
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Dézipper en deux listes : xs et ys
xs, ys = # À écrire avec zip(*points)

print("Xs:", xs)  # [1, 3, 5, 7]
print("Ys:", ys)  # [2, 4, 6, 8]

# Vérification : re-zip doit redonner les points originaux
points_reconstruits = list(zip(xs, ys))
print(points_reconstruits)  # [(1, 2), (3, 4), (5, 6), (7, 8)]
```

---

## **Partie 6 : La fonction `reduce()`**

_Note : `reduce()` se trouve dans le module `functools`_

### **Exercice 6.1 : Opérations de Réduction**

Utilisez `reduce()` pour effectuer différentes opérations de réduction :

```python
from functools import reduce

nombres = [1, 2, 3, 4, 5]

# 1. Somme des nombres
somme = reduce(# À écrire avec lambda)
print("Somme:", somme)  # 15

# 2. Produit des nombres (factorielle de 5)
produit = reduce(# À écrire)
print("Produit:", produit)  # 120

# 3. Plus grand nombre
maximum = reduce(# À écrire)
print("Maximum:", maximum)  # 5

# 4. Concaténation de chaînes
mots = ["Programmation", " ", "Fonctionnelle", " ", "Python"]
phrase = reduce(# À écrire)
print("Phrase:", phrase)  # "Programmation Fonctionnelle Python"
```

### **Exercice 6.2 : Réduction Complexe**

Créez une fonction de réduction personnalisée :

```python
from functools import reduce

# Liste de transactions (nom, montant)
transactions = [
    ("dépôt", 100),
    ("retrait", 30),
    ("dépôt", 50),
    ("retrait", 20),
    ("frais", 5)
]

def calculer_solde(solde_actuel, transaction):
    operation, montant = transaction
    # À compléter:
    # - Ajouter pour "dépôt"
    # - Soustraire pour "retrait" et "frais"
    # Retourner le nouveau solde
    pass

# Utiliser reduce() avec votre fonction
solde_final = reduce(# À écrire)
print("Solde final:", solde_final)  # Devrait être 95
```

---

## **Partie 7 : Combinaison des Concepts**

### **Exercice 7.1 : Pipeline Fonctionnel**

Créez un pipeline qui traite une liste de données en utilisant plusieurs fonctions fonctionnelles :

```python
from functools import reduce

donnees = [12, 7, 14, 9, 21, 18, 5, 16]

# Pipeline:
# 1. Filtrer pour garder seulement les nombres > 10
# 2. Multiplier chaque nombre par 2
# 3. Calculer la moyenne des résultats

etape1 = filter(# À écrire)  # Nombres > 10
etape2 = map(# À écrire)     # Multiplier par 2
resultats = list(etape2)

# Calcul de la moyenne avec reduce
if resultats:
    somme_totale = reduce(# À écrire)  # Somme des résultats
    moyenne = # À écrire  # Diviser par le nombre d'éléments
    print("Résultats:", resultats)
    print("Moyenne:", moyenne)
```

### **Exercice 7.2 : Traitement de Données Réelles**

Traitez ces données d'étudiants avec une approche fonctionnelle :

```python
etudiants = [
    {"nom": "Alice", "notes": [85, 90, 78]},
    {"nom": "Bob", "notes": [72, 68, 74]},
    {"nom": "Charlie", "notes": [93, 95, 91]},
    {"nom": "Diana", "notes": [68, 72, 65]}
]

# Objectif: Calculer la moyenne de chaque étudiant, puis la moyenne de la classe

# 1. Calculer la moyenne de chaque étudiant (map)
moyennes_individuelles = list(map(
    # À écrire: fonction qui prend un étudiant et retourne sa moyenne
    # lambda ou fonction définie séparément
    lambda etudiant: # À compléter,
    etudiants
))

print("Moyennes individuelles:", moyennes_individuelles)

# 2. Calculer la moyenne de la classe (reduce)
if moyennes_individuelles:
    moyenne_classe = reduce(# À écrire)
    print("Moyenne de classe:", moyenne_classe)
```

---

## **Partie 8 : Défi Final**

### **Exercice 8.1 : Analyse de Textes**

Écrivez un programme fonctionnel qui analyse une liste de phrases :

```python
phrases = [
    "La programmation fonctionnelle est intéressante.",
    "Python supporte plusieurs paradigmes.",
    "Les fonctions pures n'ont pas d'effets de bord.",
    "map, filter et reduce sont des fonctions d'ordre supérieur."
]

# Objectif: Trouver le mot le plus fréquent (hors mots communs)

mots_communs = {"la", "le", "les", "est", "sont", "de", "des", "et", "d'"}

# Étapes suggérées:
# 1. Diviser chaque phrase en mots (map)
# 2. Mettre en minuscule et filtrer les mots communs (map + filter)
# 3. Aplatir la liste de listes en une seule liste
# 4. Compter les occurrences de chaque mot
# 5. Trouver le mot avec le plus d'occurrences (reduce)

# Écrivez votre solution ici en utilisant autant que possible
# une approche fonctionnelle avec map, filter, reduce, lambda
```

---

## **Solutions Guide (Indications)**

### **Pour l'Exercice 1.1 :**

- **Fonction A** : Pure (mêmes entrées → mêmes sorties, pas d'effets de bord)
- **Fonction B** : Non pure (modifie une variable globale)
- **Fonction C** : Pure (déterministe, pas d'effets de bord)
- **Fonction D** : Non pure (utilise random, résultat imprévisible)
- **Fonction E** : Non pure (modifie `liste_resultats`)

### **Pour l'Exercice 3.1 :**

```python
# 1. Calculer les carrés
carres = map(lambda x: x ** 2, nombres)

# 2. Convertir en chaîne
chaines = map(lambda x: f"Nombre: {x}", nombres)
```

### **Pour l'Exercice 5.1 :**

```python
# 1. Créer des tuples (nom, note)
combinaison1 = zip(noms, notes)

# 3. Créer un dictionnaire
dictionnaire = dict(zip(noms, notes))
```

### **Pour l'Exercice 6.1 :**

```python
# 1. Somme des nombres
somme = reduce(lambda x, y: x + y, nombres)

# 3. Plus grand nombre
maximum = reduce(lambda x, y: x if x > y else y, nombres)
```
