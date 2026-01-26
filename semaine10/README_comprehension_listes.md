### **Partie 1 : Compréhensions de listes**

**Exercice 1 : Transformations basiques**

1. Créez une liste `nombres` contenant les entiers de 1 à 10. Ensuite, utilisez une compréhension de liste pour créer une nouvelle liste où chaque nombre est multiplié par 3.
2. À partir d'une liste `mots = ["python", "est", "puissant"]`, créez une nouvelle liste contenant la longueur de chaque mot.

**Exercice 2 : Filtrage simple**

1. À partir de la liste `nombres` de 1 à 15, créez une liste ne contenant que les nombres divisibles par 3.
2. À partir d'une liste `temperatures = [23, 17, 30, 15, 28, 10, 5]`, créez une liste contenant seulement les températures supérieures à 20.

**Exercice 3 : Conditions complexes**

1. À partir de la liste `nombres` de 1 à 10, créez une liste de chaînes de caractères qui indique "Pair" pour les nombres pairs et "Impair" pour les impairs.
2. À partir de `notes = [12, 8, 17, 5, 14, 20, 9]`, créez une liste de booléens où `True` indique une note supérieure ou égale à la moyenne (10) et `False` l'inverse.

**Exercice 4 : Boucles imbriquées**

1. Créez une liste de tuples `(x, y)` pour tous les `x` dans `[1, 2, 3]` et tous les `y` dans `['a', 'b']`.
2. Aplatissez une liste de listes `matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]` en une liste simple.

**Exercice 5 : Mise en pratique**

1. Étant donné une phrase `phrase = "Le Python est un langage de programmation"`, créez une liste des mots de la phrase qui contiennent la lettre 'o', en minuscules.
2. À partir de deux listes `liste1 = [1, 2, 3]` et `liste2 = [4, 5, 6]`, créez une liste des sommes des paires `(1+4, 2+5, 3+6)` en utilisant `zip` dans une compréhension.

---

### **Partie 2 : Compréhensions de dictionnaires**

**Exercice 1 : Création basique**

1. Créez un dictionnaire où les clés sont les nombres de 1 à 5 et les valeurs sont leurs carrés.
2. À partir de `noms = ["Alice", "Bob", "Charlie"]`, créez un dictionnaire ayant ces noms comme clés et la longueur de chaque nom comme valeur.

**Exercice 2 : Transformations et filtrage**

1. À partir du dictionnaire `inventaire = {"pommes": 5, "bananes": 8, "oranges": 3}`, créez un nouveau dictionnaire contenant seulement les fruits dont la quantité est supérieure à 4.
2. À partir d'une liste de tuples `coordonnees = [("x", 10), ("y", 20), ("z", 30)]`, créez un dictionnaire.

**Exercice 3 : Inversion et manipulation**

1. Inverser le dictionnaire `d = {"a": 1, "b": 2, "c": 3}` pour obtenir `{1: "a", 2: "b", 3: "c"}`.
2. À partir de deux listes `cles = ["id", "nom", "age"]` et `valeurs = [101, "Alice", 25]`, créez un dictionnaire en les associant.

**Exercice 4 : Conditions avec `if-else`**

1. À partir de `notes = {"Alice": 15, "Bob": 8, "Charlie": 12, "David": 17}`, créez un nouveau dictionnaire avec les mêmes clés, mais où la valeur est "Admis" si la note >= 10, sinon "Recalé".

---

### **Partie 3 : Compréhensions d'ensembles (sets)**

**Exercice 1 : Création et dédoublonnage**

1. À partir d'une liste `donnees = [1, 2, 2, 3, 4, 4, 4, 5]`, créez un ensemble contenant les carrés de ces nombres. Observez l'effet de dédoublonnage.
2. À partir d'une chaîne `phrase = "hello world"`, créez un ensemble des lettres consonnes qu'elle contient (ignorez les espaces).

**Exercice 2 : Filtrage**

1. À partir d'une liste `nombres = [12, 7, 15, 3, 20, 8, 10]`, créez un ensemble contenant seulement les nombres divisibles par 2 **et** par 3.
2. À partir d'une liste de mots `mots = ["python", "java", "python", "c++", "java"]`, créez un ensemble des mots qui ont plus de 4 lettres.

**Exercice 3 : Opérations avancées**

1. Générez un ensemble des paires `(x, y)` où `x` et `y` sont tous deux dans l'ensemble `{1, 2, 3}` et `x` != `y`.
2. À partir d'une liste de phrases `["le chat dort", "le chien court", "le chat mange"]`, créez un ensemble de tous les mots uniques présents.

---

### **Partie 4 : Exercices de synthèse**

**Exercice 1 : Analyse de texte**
À partir de la chaîne suivante :
`texte = "Les compréhensions de liste en Python offrent une syntaxe concise pour créer des listes."`

1. Créez une liste des mots (sans ponctuation, en minuscules).
2. À partir de cette liste, créez un dictionnaire où chaque mot est une clé et sa valeur est le nombre de voyelles qu'il contient.
3. Créez un ensemble des mots qui ont plus de 3 consonnes.

**Exercice 2 : Traitement de données**
Vous avez une liste de dictionnaires représentant des étudiants :

```python
etudiants = [
    {"nom": "Alice", "notes": [14, 12, 16]},
    {"nom": "Bob", "notes": [8, 10, 7]},
    {"nom": "Charlie", "notes": [18, 15, 17]}
]
```

1. Créez une liste des noms des étudiants.
2. Créez un dictionnaire `{nom: moyenne}` contenant la moyenne de chaque étudiant.
3. Créez un ensemble des notes uniques supérieures à 15 présentes dans toutes les listes.

**Exercice 3 : Combinaison de structures**

1. En une seule ligne de code, générez une liste de dictionnaires. Chaque dictionnaire représente un carré et a les clés `"côté"` (un entier de 1 à 5) et `"aire"` (le carré de `"côté"`).
2. À partir de la liste générée, créez un ensemble des aires qui sont des multiples de 4.

---

### **Corrections suggérées (à ne consulter qu'après avoir essayé)**

**Partie 1 - Exercice 1.1**

```python
nombres = list(range(1, 11))
triples = [n * 3 for n in nombres]
```

**Partie 2 - Exercice 1.1**

```python
carres_dict = {x: x**2 for x in range(1, 6)}
```

**Partie 3 - Exercice 1.1**

```python
donnees = [1, 2, 2, 3, 4, 4, 4, 5]
carres_uniq = {x**2 for x in donnees}
```

**Partie 4 - Exercice 2.2**

```python
moyennes = {etud["nom"]: sum(etud["notes"])/len(etud["notes"]) for etud in etudiants}
```
