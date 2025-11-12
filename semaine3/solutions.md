# Solutions Complètes

## Solutions Exercice 1 : Calculs avec précédence

```python
# Expression 1
resultat1 = 10 + 3 * 2  # 10 + 6 = 16

# Expression 2
resultat2 = (10 + 3) * 2  # 13 * 2 = 26

# Expression 3
resultat3 = 15 - 4 / 2  # 15 - 2 = 13

# Expression 4
resultat4 = (15 - 4) / 2  # 11 / 2 = 5.5

# Expression 5
resultat5 = 2 ** 3 * 2  # 8 * 2 = 16

# Expression 6
resultat6 = 2 ** (3 * 2)  # 2 ** 6 = 64

print("Exercice 1 résultats:")
print(f"10 + 3 * 2 = {resultat1}")
print(f"(10 + 3) * 2 = {resultat2}")
print(f"15 - 4 / 2 = {resultat3}")
print(f"(15 - 4) / 2 = {resultat4}")
print(f"2 ** 3 * 2 = {resultat5}")
print(f"2 ** (3 * 2) = {resultat6}")
```

## Solutions Exercice 2 : Associativité des opérateurs

```python
# Expression 1 (associativité gauche-droite)
resultat1 = 15 - 4 - 3  # (15-4)-3 = 11-3 = 8

# Expression 2 (associativité droite-gauche)
resultat2 = 2 ** 3 ** 2  # 2**(3**2) = 2**9 = 512

# Expression 3
resultat3 = 20 / 4 / 2  # (20/4)/2 = 5/2 = 2.5

# Expression 4
resultat4 = not True or False  # (not True) or False = False or False = False

print("\nExercice 2 résultats:")
print(f"15 - 4 - 3 = {resultat1}")
print(f"2 ** 3 ** 2 = {resultat2}")
print(f"20 / 4 / 2 = {resultat3}")
print(f"not True or False = {resultat4}")
```

## Solutions Exercice 3 : Expressions complexes

```python
# Expression 1
a = 5
b = 3
c = 2
resultat1 = a + b * c ** 2  # 5 + 3*(2**2) = 5 + 3*4 = 5 + 12 = 17

# Expression 2
resultat2 = (a + b) * c ** 2  # (5+3)*2**2 = 8*4 = 32

# Expression 3
resultat3 = a * b // c + 1  # (5*3)//2 + 1 = 15//2 + 1 = 7 + 1 = 8

# Expression 4
resultat4 = a % b + c * 3  # 5%3 + 2*3 = 2 + 6 = 8

print("\nExercice 3 résultats:")
print(f"a + b * c ** 2 = {resultat1}")
print(f"(a + b) * c ** 2 = {resultat2}")
print(f"a * b // c + 1 = {resultat3}")
print(f"a % b + c * 3 = {resultat4}")
```

## Solutions Exercice 4 : Conversions de base

```python
# Conversion de string vers entier
texte_nombre = "123"
nombre_entier = int(texte_nombre)

# Conversion de string vers float
texte_decimal = "45.67"
nombre_decimal = float(texte_decimal)

# Conversion de float vers entier
prix = 99.99
prix_entier = int(prix)  # 99 (troncature)

# Conversion de booléen vers entier
vrai = True
faux = False
vrai_entier = int(vrai)  # 1
faux_entier = int(faux)  # 0

print("\nExercice 4 résultats:")
print(f"int('123') = {nombre_entier}")
print(f"float('45.67') = {nombre_decimal}")
print(f"int(99.99) = {prix_entier}")
print(f"int(True) = {vrai_entier}")
print(f"int(False) = {faux_entier}")
```

## Solutions Exercice 5 : Conversions avec input

```python
# Demander deux nombres
nombre1 = input("Entrez le premier nombre : ")
nombre2 = input("Entrez le deuxième nombre : ")

# Convertir en entiers et calculer la somme
somme = int(nombre1) + int(nombre2)

# Convertir en floats et calculer la moyenne
moyenne = (float(nombre1) + float(nombre2)) / 2

# Convertir en strings et créer un message
message = "Nombres: " + nombre1 + " et " + nombre2

print("\nExercice 5 résultats:")
print(f"Somme: {somme}")
print(f"Moyenne: {moyenne}")
print(f"Message: {message}")
```

## Solutions Exercice 6 : Gestion des erreurs de conversion

```python
# Essayer de convertir différentes valeurs
valeurs = ["123", "45.67", "abc", "789", "12.34.56"]

print("\nExercice 6 résultats:")
for valeur in valeurs:
    try:
        # Essayer de convertir en float
        resultat = float(valeur)
        print(f"Conversion réussie: {valeur} -> {resultat}")
    except ValueError:
        print(f"Erreur: impossible de convertir '{valeur}' en nombre")
```

## Solutions Exercice 7 : Identification des types

```python
# Liste de variables
a = 10          # int - immuable
b = "hello"     # str - immuable
c = [1, 2, 3]   # list - mutable
d = (4, 5, 6)   # tuple - immuable
e = {"nom": "Alice", "age": 25}  # dict - mutable
f = 3.14        # float - immuable
g = True        # bool - immuable
h = {1, 2, 3}   # set - mutable

print("\nExercice 7 résultats:")
print(f"int (10): immuable")
print(f"str ('hello'): immuable")
print(f"list ([1,2,3]): mutable")
print(f"tuple ((4,5,6)): immuable")
print(f"dict ({{'nom': 'Alice'}}): mutable")
print(f"float (3.14): immuable")
print(f"bool (True): immuable")
print(f"set ({{1,2,3}}): mutable")
```

## Solutions Exercice 8 : Manipulation des types mutables

```python
# Liste (mutable)
liste1 = [1, 2, 3]
liste2 = liste1
liste2.append(4)

print("\nExercice 8 résultats:")
print("Liste1 après modification de liste2:", liste1)  # [1, 2, 3, 4]

# Dictionnaire (mutable)
dict1 = {"a": 1, "b": 2}
dict2 = dict1
dict2["c"] = 3

print("Dict1 après modification de dict2:", dict1)  # {'a': 1, 'b': 2, 'c': 3}
```

## Solutions Exercice 9 : Comportement des types immuables

```python
# String (immuable)
texte1 = "hello"
texte2 = texte1
texte2 = texte2 + " world"

print("\nExercice 9 résultats:")
print("Texte1 après opération sur texte2:", texte1)  # "hello"

# Tuple (immuable)
tuple1 = (1, 2, 3)
tuple2 = tuple1
# tuple2[0] = 4  # Cette ligne générera une erreur

print("Tuple1 inchangé:", tuple1)  # (1, 2, 3)
```

## Solutions Exercice 10 : Copie de types mutables

```python
import copy

# Liste originale
originale = [1, 2, [3, 4]]

# Référence
reference = originale

# Copie superficielle
copie_superficielle = originale.copy()

# Modification
copie_superficielle[0] = 100
copie_superficielle[2][0] = 300

print("\nExercice 10 résultats:")
print("Originale après modifications:", originale)  # [1, 2, [300, 4]]
print("Référence après modifications:", reference)  # [1, 2, [300, 4]]
print("Copie superficielle après modifications:", copie_superficielle)  # [100, 2, [300, 4]]
```

## Solutions Exercice 11 : Opérateurs de comparaison

```python
# Comparaisons numériques
a = 10
b = 5
c = 10

resultat1 = a > b    # True
resultat2 = a == c   # True
resultat3 = a != b   # True
resultat4 = a <= c   # True
resultat5 = b >= a   # False

# Comparaisons de strings
texte1 = "abc"
texte2 = "abd"
texte3 = "abc"

resultat6 = texte1 == texte3  # True
resultat7 = texte1 < texte2   # True ('abc' < 'abd')
resultat8 = texte1 != texte2  # True

print("\nExercice 11 résultats:")
print(f"10 > 5: {resultat1}")
print(f"10 == 10: {resultat2}")
print(f"10 != 5: {resultat3}")
print(f"10 <= 10: {resultat4}")
print(f"5 >= 10: {resultat5}")
print(f"'abc' == 'abc': {resultat6}")
print(f"'abc' < 'abd': {resultat7}")
print(f"'abc' != 'abd': {resultat8}")
```

## Solutions Exercice 12 : Opérateurs d'identité

```python
# Cas 1 : Même valeur, même objet
a = 100
b = 100
resultat1 = a == b  # True
resultat2 = a is b  # True (interning des petits entiers)

# Cas 2 : Même valeur, objets différents
c = [1, 2, 3]
d = [1, 2, 3]
resultat3 = c == d  # True
resultat4 = c is d  # False

# Cas 3 : Petits entiers (interning)
e = 5
f = 5
resultat5 = e is f  # True

# Cas 4 : Gros entiers
g = 1000
h = 1000
resultat6 = g is h  # False (dépend de l'implémentation)

print("\nExercice 12 résultats:")
print(f"100 == 100: {resultat1}")
print(f"100 is 100: {resultat2}")
print(f"[1,2,3] == [1,2,3]: {resultat3}")
print(f"[1,2,3] is [1,2,3]: {resultat4}")
print(f"5 is 5: {resultat5}")
print(f"1000 is 1000: {resultat6}")
```

## Solutions Exercice 13 : Expressions booléennes complexes

```python
x = 10
y = 5
z = 10

# Expression 1
resultat1 = x > y and x == z  # True and True = True

# Expression 2
resultat2 = x < y or x == z   # False or True = True

# Expression 3
resultat3 = not (x == y)      # not False = True

# Expression 4
resultat4 = x > y and x != z or y < z  # True and False or True = False or True = True

# Expression 5
resultat5 = (x > y and x != z) or y < z  # (True and False) or True = False or True = True

print("\nExercice 13 résultats:")
print(f"x > y and x == z: {resultat1}")
print(f"x < y or x == z: {resultat2}")
print(f"not (x == y): {resultat3}")
print(f"x > y and x != z or y < z: {resultat4}")
print(f"(x > y and x != z) or y < z: {resultat5}")
```

## Solutions Exercice 14 : Programme de validation

```python
# Données d'un utilisateur
age = 25
salaire = 45000
experience = 3
diplome = True

# Conditions pour un prêt
condition1 = age >= 18 and salaire >= 40000  # True and True = True
condition2 = experience >= 2 or diplome     # True or True = True
condition3 = salaire >= 50000 or (diplome and experience >= 1)  # False or (True and True) = False or True = True

# Validation finale
pret_approuve = condition1 and condition2 and condition3  # True and True and True = True

print("\nExercice 14 résultats:")
print(f"Condition 1 (âge >= 18 et salaire >= 40000): {condition1}")
print(f"Condition 2 (expérience >= 2 ou diplôme): {condition2}")
print(f"Condition 3 (salaire >= 50000 ou (diplôme et expérience >= 1)): {condition3}")
print(f"Prêt approuvé: {pret_approuve}")
```
