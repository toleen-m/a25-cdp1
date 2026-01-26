## **Partie 1 : Compréhensions de listes**

### **Exercice 1 : Transformations basiques**

```python
# 1.1
nombres = list(range(1, 11))
triples = [n * 3 for n in nombres]
# Résultat: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# 1.2
mots = ["python", "est", "puissant"]
longueurs = [len(mot) for mot in mots]
# Résultat: [6, 3, 8]
```

### **Exercice 2 : Filtrage simple**

```python
# 2.1
nombres = list(range(1, 16))
divisibles_par_3 = [n for n in nombres if n % 3 == 0]
# Résultat: [3, 6, 9, 12, 15]

# 2.2
temperatures = [23, 17, 30, 15, 28, 10, 5]
chaud = [t for t in temperatures if t > 20]
# Résultat: [23, 30, 28]
```

### **Exercice 3 : Conditions complexes**

```python
# 3.1
nombres = list(range(1, 11))
parite = ["Pair" if n % 2 == 0 else "Impair" for n in nombres]
# Résultat: ['Impair', 'Pair', 'Impair', 'Pair', 'Impair', 'Pair', 'Impair', 'Pair', 'Impair', 'Pair']

# 3.2
notes = [12, 8, 17, 5, 14, 20, 9]
au_dessus_moyenne = [note >= 10 for note in notes]
# Résultat: [True, False, True, False, True, True, False]
```

### **Exercice 4 : Boucles imbriquées**

```python
# 4.1
paires = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
# Résultat: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]

# 4.2
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplatie = [element for ligne in matrice for element in ligne]
# Résultat: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### **Exercice 5 : Mise en pratique**

```python
# 5.1
phrase = "Le Python est un langage de programmation"
mots_avec_o = [mot.lower() for mot in phrase.split() if 'o' in mot.lower()]
# Résultat: ['python', 'langage', 'programmation']

# 5.2
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
sommes = [x + y for x, y in zip(liste1, liste2)]
# Résultat: [5, 7, 9]
```

---

## **Partie 2 : Compréhensions de dictionnaires**

### **Exercice 1 : Création basique**

```python
# 1.1
carres_dict = {x: x**2 for x in range(1, 6)}
# Résultat: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 1.2
noms = ["Alice", "Bob", "Charlie"]
longueur_noms = {nom: len(nom) for nom in noms}
# Résultat: {'Alice': 5, 'Bob': 3, 'Charlie': 7}
```

### **Exercice 2 : Transformations et filtrage**

```python
# 2.1
inventaire = {"pommes": 5, "bananes": 8, "oranges": 3}
stock_suffisant = {fruit: qte for fruit, qte in inventaire.items() if qte > 4}
# Résultat: {'pommes': 5, 'bananes': 8}

# 2.2
coordonnees = [("x", 10), ("y", 20), ("z", 30)]
coord_dict = {cle: valeur for cle, valeur in coordonnees}
# Résultat: {'x': 10, 'y': 20, 'z': 30}
```

### **Exercice 3 : Inversion et manipulation**

```python
# 3.1
d = {"a": 1, "b": 2, "c": 3}
inverse = {valeur: cle for cle, valeur in d.items()}
# Résultat: {1: 'a', 2: 'b', 3: 'c'}

# 3.2
cles = ["id", "nom", "age"]
valeurs = [101, "Alice", 25]
dictionnaire = {cles[i]: valeurs[i] for i in range(len(cles))}
# Alternative: dict(zip(cles, valeurs))
# Résultat: {'id': 101, 'nom': 'Alice', 'age': 25}
```

### **Exercice 4 : Conditions avec if-else**

```python
notes = {"Alice": 15, "Bob": 8, "Charlie": 12, "David": 17}
resultats = {nom: "Admis" if note >= 10 else "Recalé" for nom, note in notes.items()}
# Résultat: {'Alice': 'Admis', 'Bob': 'Recalé', 'Charlie': 'Admis', 'David': 'Admis'}
```

---

## **Partie 3 : Compréhensions d'ensembles (sets)**

### **Exercice 1 : Création et dédoublonnage**

```python
# 1.1
donnees = [1, 2, 2, 3, 4, 4, 4, 5]
carres_uniq = {x**2 for x in donnees}
# Résultat: {1, 4, 9, 16, 25} (le 16 n'apparaît qu'une fois même si 4^2 est calculé 3 fois)

# 1.2
phrase = "hello world"
consonnes = {lettre for lettre in phrase if lettre.isalpha() and lettre.lower() not in 'aeiou'}
# Résultat: {'h', 'l', 'r', 'w', 'd'}
```

### **Exercice 2 : Filtrage**

```python
# 2.1
nombres = [12, 7, 15, 3, 20, 8, 10]
div_2_et_3 = {n for n in nombres if n % 2 == 0 and n % 3 == 0}
# Résultat: {12} (seul 12 est divisible par 2 et 3)

# 2.2
mots = ["python", "java", "python", "c++", "java"]
long_mots = {mot for mot in mots if len(mot) > 4}
# Résultat: {'python'}
```

### **Exercice 3 : Opérations avancées**

```python
# 3.1
ensemble = {1, 2, 3}
paires = {(x, y) for x in ensemble for y in ensemble if x != y}
# Résultat: {(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)}

# 3.2
phrases = ["le chat dort", "le chien court", "le chat mange"]
mots_uniques = {mot for phrase in phrases for mot in phrase.split()}
# Résultat: {'le', 'chat', 'dort', 'chien', 'court', 'mange'}
```

---

## **Partie 4 : Exercices de synthèse**

### **Exercice 1 : Analyse de texte**

```python
texte = "Les compréhensions de liste en Python offrent une syntaxe concise pour créer des listes."

# 1. Liste des mots sans ponctuation, en minuscules
import string
mots = [mot.strip(string.punctuation).lower() for mot in texte.split()]
# Résultat: ['les', 'compréhensions', 'de', 'liste', 'en', 'python', 'offrent', 'une', 'syntaxe', 'concisé', 'pour', 'créer', 'des', 'listes']

# 2. Dictionnaire mot -> nombre de voyelles
def compter_voyelles(mot):
    voyelles = 'aeiouéèêàâôûù'
    return sum(1 for lettre in mot.lower() if lettre in voyelles)

voyelles_par_mot = {mot: compter_voyelles(mot) for mot in mots}
# Exemple de résultat: {'les': 1, 'compréhensions': 4, 'de': 1, ...}

# 3. Ensemble des mots avec plus de 3 consonnes
def compter_consonnes(mot):
    consonnes = 'bcdfghjklmnpqrstvwxyz'
    return sum(1 for lettre in mot.lower() if lettre in consonnes)

mots_3plus_consonnes = {mot for mot in mots if compter_consonnes(mot) > 3}
# Résultat probable: {'compréhensions', 'syntaxe'}
```

### **Exercice 2 : Traitement de données**

```python
etudiants = [
    {"nom": "Alice", "notes": [14, 12, 16]},
    {"nom": "Bob", "notes": [8, 10, 7]},
    {"nom": "Charlie", "notes": [18, 15, 17]}
]

# 1. Liste des noms
noms = [etud["nom"] for etud in etudiants]
# Résultat: ['Alice', 'Bob', 'Charlie']

# 2. Dictionnaire nom:moyenne
moyennes = {etud["nom"]: sum(etud["notes"])/len(etud["notes"]) for etud in etudiants}
# Résultat: {'Alice': 14.0, 'Bob': 8.333..., 'Charlie': 16.666...}

# 3. Ensemble des notes uniques > 15
notes_elevees = {note for etud in etudiants for note in etud["notes"] if note > 15}
# Résultat: {16, 17, 18}
```

### **Exercice 3 : Combinaison de structures**

```python
# 1. Liste de dictionnaires pour les carrés
carres = [{"côté": x, "aire": x**2} for x in range(1, 6)]
# Résultat: [{'côté': 1, 'aire': 1}, {'côté': 2, 'aire': 4}, ..., {'côté': 5, 'aire': 25}]

# 2. Ensemble des aires multiples de 4
aires_multiples_4 = {carre["aire"] for carre in carres if carre["aire"] % 4 == 0}
# Résultat: {4, 16} (car 1, 9, 25 ne sont pas multiples de 4)
```
