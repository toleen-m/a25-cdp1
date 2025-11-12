# Exercices Python pour Débutants

## Exercices sur les Opérateurs, Précédence et Associativité

### Exercice 1 : Calculs avec précédence

Calcule mentalement le résultat de ces expressions, puis vérifie avec Python :

```python
# Expression 1
resultat1 = 10 + 3 * 2

# Expression 2
resultat2 = (10 + 3) * 2

# Expression 3
resultat3 = 15 - 4 / 2

# Expression 4
resultat4 = (15 - 4) / 2

# Expression 5
resultat5 = 2 ** 3 * 2

# Expression 6
resultat6 = 2 ** (3 * 2)
```

### Exercice 2 : Associativité des opérateurs

Trouve le résultat de ces expressions en tenant compte de l'associativité :

```python
# Expression 1 (associativité gauche-droite)
resultat1 = 15 - 4 - 3

# Expression 2 (associativité droite-gauche)
resultat2 = 2 ** 3 ** 2

# Expression 3
resultat3 = 20 / 4 / 2

# Expression 4
resultat4 = not True or False
```

### Exercice 3 : Expressions complexes

Évalue ces expressions complexes :

```python
# Expression 1
a = 5
b = 3
c = 2
resultat1 = a + b * c ** 2

# Expression 2
resultat2 = (a + b) * c ** 2

# Expression 3
resultat3 = a * b // c + 1

# Expression 4
resultat4 = a % b + c * 3
```

## Exercices sur la Conversion Simple et Cast

### Exercice 4 : Conversions de base

Complète le code suivant avec les conversions appropriées :

```python
# Conversion de string vers entier
texte_nombre = "123"
nombre_entier = # À compléter

# Conversion de string vers float
texte_decimal = "45.67"
nombre_decimal = # À compléter

# Conversion de float vers entier
prix = 99.99
prix_entier = # À compléter

# Conversion de booléen vers entier
vrai = True
faux = False
vrai_entier = # À compléter
faux_entier = # À compléter
```

### Exercice 5 : Conversions avec input

Écris un programme qui demande deux nombres à l'utilisateur et effectue différentes conversions :

```python
# Demander deux nombres
nombre1 = input("Entrez le premier nombre : ")
nombre2 = input("Entrez le deuxième nombre : ")

# Convertir en entiers et calculer la somme
somme = # À compléter

# Convertir en floats et calculer la moyenne
moyenne = # À compléter

# Convertir en strings et créer un message
message = # À compléter
```

### Exercice 6 : Gestion des erreurs de conversion

Écris un programme qui gère les erreurs de conversion :

```python
# Essayer de convertir différentes valeurs
valeurs = ["123", "45.67", "abc", "789", "12.34.56"]

for valeur in valeurs:
    try:
        # Essayer de convertir en float
        resultat = # À compléter
        print(f"Conversion réussie: {valeur} -> {resultat}")
    except ValueError:
        print(f"Erreur: impossible de convertir '{valeur}' en nombre")
```

## Exercices sur les Types Mutables et Immuables

### Exercice 7 : Identification des types

Pour chaque variable, indique si son type est mutable ou immuable :

```python
# Liste de variables
a = 10
b = "hello"
c = [1, 2, 3]
d = (4, 5, 6)
e = {"nom": "Alice", "age": 25}
f = 3.14
g = True
h = {1, 2, 3}
```

### Exercice 8 : Manipulation des types mutables

Observe le comportement des types mutables :

```python
# Liste (mutable)
liste1 = [1, 2, 3]
liste2 = liste1
liste2.append(4)

print("Liste1 après modification de liste2:", liste1)

# Dictionnaire (mutable)
dict1 = {"a": 1, "b": 2}
dict2 = dict1
dict2["c"] = 3

print("Dict1 après modification de dict2:", dict1)
```

### Exercice 9 : Comportement des types immuables

Observe le comportement des types immuables :

```python
# String (immuable)
texte1 = "hello"
texte2 = texte1
texte2 = texte2 + " world"

print("Texte1 après opération sur texte2:", texte1)

# Tuple (immuable)
tuple1 = (1, 2, 3)
tuple2 = tuple1
# tuple2[0] = 4  # Cette ligne générera une erreur
```

### Exercice 10 : Copie de types mutables

Écris un programme qui montre la différence entre copie superficielle et référence :

```python
# Liste originale
originale = [1, 2, [3, 4]]

# Référence
reference = originale

# Copie superficielle
copie_superficielle = # À compléter

# Modification
copie_superficielle[0] = 100
copie_superficielle[2][0] = 300

print("Originale après modifications:", originale)
print("Référence après modifications:", reference)
print("Copie superficielle après modifications:", copie_superficielle)
```

## Exercices sur les Opérateurs de Comparaison et d'Identité

### Exercice 11 : Opérateurs de comparaison

Prédit le résultat de ces comparaisons :

```python
# Comparaisons numériques
a = 10
b = 5
c = 10

resultat1 = a > b
resultat2 = a == c
resultat3 = a != b
resultat4 = a <= c
resultat5 = b >= a

# Comparaisons de strings
texte1 = "abc"
texte2 = "abd"
texte3 = "abc"

resultat6 = texte1 == texte3
resultat7 = texte1 < texte2
resultat8 = texte1 != texte2
```

### Exercice 12 : Opérateurs d'identité

Comprends la différence entre == et is :

```python
# Cas 1 : Même valeur, même objet
a = 100
b = 100
resultat1 = a == b
resultat2 = a is b

# Cas 2 : Même valeur, objets différents
c = [1, 2, 3]
d = [1, 2, 3]
resultat3 = c == d
resultat4 = c is d

# Cas 3 : Petits entiers (interning)
e = 5
f = 5
resultat5 = e is f

# Cas 4 : Gros entiers
g = 1000
h = 1000
resultat6 = g is h
```

### Exercice 13 : Expressions booléennes complexes

Évalue ces expressions complexes :

```python
x = 10
y = 5
z = 10

# Expression 1
resultat1 = x > y and x == z

# Expression 2
resultat2 = x < y or x == z

# Expression 3
resultat3 = not (x == y)

# Expression 4
resultat4 = x > y and x != z or y < z

# Expression 5
resultat5 = (x > y and x != z) or y < z
```

### Exercice 14 : Programme de validation

Écris un programme qui valide des conditions complexes :

```python
# Données d'un utilisateur
age = 25
salaire = 45000
experience = 3
diplome = True

# Conditions pour un prêt
condition1 = age >= 18 and salaire >= 40000
condition2 = experience >= 2 or diplome
condition3 = salaire >= 50000 or (diplome and experience >= 1)

# Validation finale
pret_approuve = condition1 and condition2 and condition3

print("Prêt approuvé:", pret_approuve)
```
