## **Partie 1 : Fonctions Pures vs Non Pures**

### **Exercice 1.1 : Identifier la Pureté**

```python
# Fonction A - PURE
def ajouter_pure(a, b):
    return a + b
# Raison : Toujours le même résultat pour les mêmes arguments, pas d'effets de bord.

# Fonction B - NON PURE
total = 0
def ajouter_impure(a):
    global total
    total += a
    return total
# Raison : Modifie la variable globale 'total' (effet de bord).

# Fonction C - PURE
def formater_message(nom):
    return f"Bonjour, {nom} !"
# Raison : Déterministe, pas d'effets de bord.

# Fonction D - NON PURE
import random
def lancer_de():
    return random.randint(1, 6)
# Raison : Utilise une source externe (random), résultat imprévisible.

# Fonction E - NON PURE
liste_resultats = []
def traiter_liste(lst):
    resultat = []
    for x in lst:
        resultat.append(x * 2)
    liste_resultats.extend(resultat)  # Effet de bord
    return resultat
# Raison : Modifie la liste externe 'liste_resultats'.
```

### **Exercice 1.2 : Transformer en Fonction Pure**

```python
# Version non pure
compteur = 0

def incrementer_impur():
    global compteur
    compteur += 1
    return compteur

# Version pure
def incrementer_pur(valeur_actuelle):
    return valeur_actuelle + 1  # Pas de modification d'état externe

# Test
print(incrementer_pur(5))   # 6
print(incrementer_pur(10))  # 11
print(incrementer_pur(5))   # 6 (toujours le même résultat pour la même entrée)

# Usage dans une boucle (approche fonctionnelle)
valeurs = [5, 10, 5]
resultats = [incrementer_pur(v) for v in valeurs]
print(resultats)  # [6, 11, 6]
```

---

## **Partie 2 : Expressions Lambda**

### **Exercice 2.1 : Convertir en Lambda**

```python
# 1. Fonction qui double un nombre
def doubler(x):
    return x * 2

# Version lambda :
doubler_lambda = lambda x: x * 2

# 2. Fonction qui vérifie si un nombre est pair
def est_pair(x):
    return x % 2 == 0

# Version lambda :
est_pair_lambda = lambda x: x % 2 == 0

# 3. Fonction qui concatène deux chaînes avec un espace
def concatener(a, b):
    return a + " " + b

# Version lambda :
concatener_lambda = lambda a, b: a + " " + b

# Tests
print(doubler_lambda(5))          # 10
print(est_pair_lambda(4))         # True
print(concatener_lambda("Hello", "World"))  # "Hello World"
```

### **Exercice 2.2 : Utilisation avec Tri**

```python
etudiants = [("Alice", 85), ("Bob", 72), ("Charlie", 93), ("Diana", 68)]

# Trier par note (du plus bas au plus haut) avec lambda
etudiants_tries = sorted(etudiants, key=lambda x: x[1])

# Alternative: tri en place
# etudiants.sort(key=lambda x: x[1])

print(etudiants_tries)
# [('Diana', 68), ('Bob', 72), ('Alice', 85), ('Charlie', 93)]

# Trier par note décroissante
etudiants_tries_desc = sorted(etudiants, key=lambda x: x[1], reverse=True)
print(etudiants_tries_desc)
# [('Charlie', 93), ('Alice', 85), ('Bob', 72), ('Diana', 68)]
```

---

## **Partie 3 : La fonction `map()`**

### **Exercice 3.1 : Application Simple**

```python
nombres = [1, 2, 3, 4, 5]

# 1. Calculer les carrés
carres = map(lambda x: x ** 2, nombres)
print(list(carres))  # [1, 4, 9, 16, 25]

# 2. Convertir en chaîne avec préfixe "Nombre: "
chaines = map(lambda x: f"Nombre: {x}", nombres)
print(list(chaines))  # ['Nombre: 1', 'Nombre: 2', 'Nombre: 3', 'Nombre: 4', 'Nombre: 5']

# 3. Utiliser map avec une fonction définie séparément
def ajouter_un(x):
    return x + 1

plus_un = map(ajouter_un, nombres)
print(list(plus_un))  # [2, 3, 4, 5, 6]
```

### **Exercice 3.2 : Map avec Fonction Personnalisée**

```python
temperatures_c = [0, 20, 37, 100]

# Fonction pure de conversion
def celsius_vers_fahrenheit(c):
    return c * 9/5 + 32

# Utiliser map() avec votre fonction
temperatures_f = map(celsius_vers_fahrenheit, temperatures_c)
print(list(temperatures_f))  # [32.0, 68.0, 98.6, 212.0]

# Version avec lambda
temperatures_f_lambda = map(lambda c: c * 9/5 + 32, temperatures_c)
print(list(temperatures_f_lambda))  # [32.0, 68.0, 98.6, 212.0]
```

---

## **Partie 4 : La fonction `filter()`**

### **Exercice 4.1 : Filtrage Basique**

```python
nombres = range(1, 21)  # Nombres de 1 à 20

# 1. Nombres pairs
pairs = filter(lambda x: x % 2 == 0, nombres)
print(list(pairs))  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 2. Nombres divisibles par 3
div_par_3 = filter(lambda x: x % 3 == 0, nombres)
print(list(div_par_3))  # [3, 6, 9, 12, 15, 18]

# 3. Nombres > 10
grands = filter(lambda x: x > 10, nombres)
print(list(grands))  # [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# 4. Nombres pairs ET > 10 (combinaison de conditions)
pairs_grands = filter(lambda x: x % 2 == 0 and x > 10, nombres)
print(list(pairs_grands))  # [12, 14, 16, 18, 20]
```

### **Exercice 4.2 : Filtrage Complexe**

```python
mots = ["python", "java", "functional", "programming", "lambda", "map", "filter", "reduce"]

# 1. Mots de plus de 5 caractères
longs_mots = filter(lambda mot: len(mot) > 5, mots)
print(list(longs_mots))  # ['python', 'functional', 'programming', 'lambda', 'filter', 'reduce']

# 2. Mots qui contiennent la lettre 'a'
avec_a = filter(lambda mot: 'a' in mot.lower(), mots)
print(list(avec_a))  # ['java', 'functional', 'programming', 'lambda', 'map']

# 3. Mots qui commencent par 'p' ou 'f'
pf_mots = filter(lambda mot: mot.lower().startswith(('p', 'f')), mots)
print(list(pf_mots))  # ['python', 'functional', 'programming', 'filter']
```

---

## **Partie 5 : La fonction `zip()`**

### **Exercice 5.1 : Combinaison de Listes**

```python
noms = ["Alice", "Bob", "Charlie"]
notes = [85, 72, 93]
matieres = ["Math", "Python", "Physique"]

# 1. Créer des tuples (nom, note)
combinaison1 = zip(noms, notes)
print(list(combinaison1))  # [('Alice', 85), ('Bob', 72), ('Charlie', 93)]

# 2. Créer des tuples (nom, note, matière)
combinaison2 = zip(noms, notes, matieres)
print(list(combinaison2))  # [('Alice', 85, 'Math'), ('Bob', 72, 'Python'), ('Charlie', 93, 'Physique')]

# 3. Créer un dictionnaire nom -> note
dictionnaire = dict(zip(noms, notes))
print(dictionnaire)  # {'Alice': 85, 'Bob': 72, 'Charlie': 93}

# 4. Afficher chaque association
for nom, note, matiere in zip(noms, notes, matieres):
    print(f"{nom} a eu {note} en {matiere}")
```

### **Exercice 5.2 : Dézipper et Transposer**

```python
# Liste de coordonnées (x, y)
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Dézipper en deux listes : xs et ys
xs, ys = zip(*points)  # L'astérisque * "dépaquette" la liste de tuples

print("Xs:", xs)  # (1, 3, 5, 7)
print("Ys:", ys)  # (2, 4, 6, 8)

# Vérification : re-zip doit redonner les points originaux
points_reconstruits = list(zip(xs, ys))
print(points_reconstruits)  # [(1, 2), (3, 4), (5, 6), (7, 8)]

# Application : calculer les distances par rapport à l'origine
import math
distances = map(lambda point: math.sqrt(point[0]**2 + point[1]**2), points)
print("Distances:", list(distances))  # [2.236..., 5.0, 7.810..., 10.630...]

# Avec zip pour plus de clarté
distances_clair = map(lambda xy: math.sqrt(xy[0]**2 + xy[1]**2), zip(xs, ys))
print("Distances (clair):", list(distances_clair))
```

---

## **Partie 6 : La fonction `reduce()`**

### **Exercice 6.1 : Opérations de Réduction**

```python
from functools import reduce

nombres = [1, 2, 3, 4, 5]

# 1. Somme des nombres
somme = reduce(lambda x, y: x + y, nombres)
print("Somme:", somme)  # 15

# 2. Produit des nombres (factorielle de 5)
produit = reduce(lambda x, y: x * y, nombres)
print("Produit:", produit)  # 120

# 3. Plus grand nombre
maximum = reduce(lambda x, y: x if x > y else y, nombres)
print("Maximum:", maximum)  # 5

# 4. Plus petit nombre
minimum = reduce(lambda x, y: x if x < y else y, nombres)
print("Minimum:", minimum)  # 1

# 5. Concaténation de chaînes
mots = ["Programmation", " ", "Fonctionnelle", " ", "Python"]
phrase = reduce(lambda a, b: a + b, mots)
print("Phrase:", phrase)  # "Programmation Fonctionnelle Python"

# 6. Avec valeur initiale
somme_avec_init = reduce(lambda x, y: x + y, nombres, 10)  # 10 + 1 + 2 + 3 + 4 + 5
print("Somme avec initial 10:", somme_avec_init)  # 25
```

### **Exercice 6.2 : Réduction Complexe**

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

    if operation == "dépôt":
        return solde_actuel + montant
    elif operation in ["retrait", "frais"]:
        return solde_actuel - montant
    else:
        return solde_actuel  # Opération inconnue

# Utiliser reduce() avec votre fonction
solde_final = reduce(calculer_solde, transactions, 0)
print("Solde final:", solde_final)  # 95

# Version avec lambda (moins lisible mais possible)
solde_final_lambda = reduce(
    lambda solde, trans: solde + trans[1] if trans[0] == "dépôt" else solde - trans[1],
    transactions,
    0
)
print("Solde final (lambda):", solde_final_lambda)  # 95
```

---

## **Partie 7 : Combinaison des Concepts**

### **Exercice 7.1 : Pipeline Fonctionnel**

```python
from functools import reduce

donnees = [12, 7, 14, 9, 21, 18, 5, 16]

# Pipeline:
# 1. Filtrer pour garder seulement les nombres > 10
# 2. Multiplier chaque nombre par 2
# 3. Calculer la moyenne des résultats

# Version décomposée
etape1 = filter(lambda x: x > 10, donnees)           # [12, 14, 21, 18, 16]
etape2 = map(lambda x: x * 2, etape1)               # [24, 28, 42, 36, 32]
resultats = list(etape2)

# Calcul de la moyenne avec reduce
if resultats:
    somme_totale = reduce(lambda x, y: x + y, resultats)  # 24+28+42+36+32 = 162
    moyenne = somme_totale / len(resultats)
    print("Résultats:", resultats)     # [24, 28, 42, 36, 32]
    print("Somme totale:", somme_totale)  # 162
    print("Moyenne:", moyenne)         # 32.4

# Version en une seule expression (plus avancée)
moyenne_one_line = (
    reduce(lambda x, y: x + y,
           map(lambda x: x * 2,
               filter(lambda x: x > 10, donnees)))
    / len(list(filter(lambda x: x > 10, donnees)))
) if any(x > 10 for x in donnees) else 0

print("Moyenne (one-line):", moyenne_one_line)  # 32.4
```

### **Exercice 7.2 : Traitement de Données Réelles**

```python
from functools import reduce

etudiants = [
    {"nom": "Alice", "notes": [85, 90, 78]},
    {"nom": "Bob", "notes": [72, 68, 74]},
    {"nom": "Charlie", "notes": [93, 95, 91]},
    {"nom": "Diana", "notes": [68, 72, 65]}
]

# 1. Calculer la moyenne de chaque étudiant (map)
def moyenne_etudiant(etudiant):
    notes = etudiant["notes"]
    return sum(notes) / len(notes) if notes else 0

moyennes_individuelles = list(map(moyenne_etudiant, etudiants))

print("Moyennes individuelles:", moyennes_individuelles)
# [84.333..., 71.333..., 93.0, 68.333...]

# Version avec lambda (un peu moins lisible)
moyennes_lambda = list(map(
    lambda e: sum(e["notes"]) / len(e["notes"]),
    etudiants
))

# 2. Calculer la moyenne de la classe (reduce)
if moyennes_individuelles:
    somme_moyennes = reduce(lambda x, y: x + y, moyennes_individuelles)
    moyenne_classe = somme_moyennes / len(moyennes_individuelles)
    print("Somme des moyennes:", somme_moyennes)  # 317.0
    print("Moyenne de classe:", moyenne_classe)   # 79.25

# 3. Trouver la meilleure moyenne (reduce)
meilleure_moyenne = reduce(
    lambda x, y: x if x > y else y,
    moyennes_individuelles
)
print("Meilleure moyenne:", meilleure_moyenne)  # 93.0

# 4. Associer chaque étudiant avec sa moyenne
etudiants_avec_moyenne = list(map(
    lambda e: (e["nom"], moyenne_etudiant(e)),
    etudiants
))
print("Étudiants avec moyenne:", etudiants_avec_moyenne)
# [('Alice', 84.333...), ('Bob', 71.333...), ...]
```

---

## **Partie 8 : Défi Final**

### **Exercice 8.1 : Analyse de Textes**

```python
from functools import reduce
from collections import Counter

phrases = [
    "La programmation fonctionnelle est intéressante.",
    "Python supporte plusieurs paradigmes.",
    "Les fonctions pures n'ont pas d'effets de bord.",
    "map, filter et reduce sont des fonctions d'ordre supérieur."
]

mots_communs = {"la", "le", "les", "est", "sont", "de", "des", "et", "d'", "pas", "n'ont"}

# 1. Diviser chaque phrase en mots et mettre en minuscule
mots_bruts = map(lambda phrase: phrase.lower().replace(',', '').replace('.', '').split(), phrases)

# 2. Aplatir la liste de listes en une seule liste
# Première méthode: double map
mots_aplatiss = []
for liste_mots in mots_bruts:
    mots_aplatiss.extend(liste_mots)

# Deuxième méthode: plus fonctionnelle (avec itertools.chain)
from itertools import chain
mots_bruts = map(lambda phrase: phrase.lower().replace(',', '').replace('.', '').split(), phrases)
mots_aplatiss = list(chain.from_iterable(mots_bruts))

print("Mots bruts:", mots_aplatiss)

# 3. Filtrer les mots communs
mots_filtres = filter(lambda mot: mot not in mots_communs, mots_aplatiss)
mots_filtres_liste = list(mots_filtres)

print("Mots filtrés:", mots_filtres_liste)

# 4. Compter les occurrences (méthode simple avec Counter)
comptage = Counter(mots_filtres_liste)
print("Comptage:", comptage)

# 5. Trouver le mot le plus fréquent
if comptage:
    mot_plus_frequent = reduce(
        lambda x, y: x if comptage[x] > comptage[y] else y,
        comptage.keys()
    )
    print(f"Mot le plus fréquent: '{mot_plus_frequent}' ({comptage[mot_plus_frequent]} occurrences)")
    # Résultat: 'fonctions' (2 occurrences)

# Version alternative sans Counter (plus "pure" fonctionnelle)
def incrementer_compteur(compteur, mot):
    compteur[mot] = compteur.get(mot, 0) + 1
    return compteur

comptage_manuel = reduce(incrementer_compteur, mots_filtres_liste, {})
print("Comptage manuel:", comptage_manuel)

# Trouver le maximum sans Counter
if comptage_manuel:
    mot_max = reduce(
        lambda x, y: x if comptage_manuel[x] > comptage_manuel[y] else y,
        comptage_manuel.keys()
    )
    print(f"Mot le plus fréquent (manuel): '{mot_max}'")
```

---

## **Points Clés à Retenir**

1. **Fonctions pures** : Même entrée → même sortie, pas d'effets de bord
2. **`map(func, iterable)`** : Applique `func` à chaque élément
3. **`filter(predicat, iterable)`** : Garde les éléments où `predicat` est `True`
4. **`zip(*iterables)`** : Combine plusieurs itérables élément par élément
5. **`reduce(func, iterable, init)`** : Réduit l'itérable à une valeur unique
6. **`lambda args: expression`** : Fonction anonyme courte
