# Solutions Complètes

## Solutions Exercice 1 : Décomposition d'expressions complexes

```python
print("=== EXERCICE 1 SOLUTIONS ===")

# Expression 1
# Étapes : 2**3=8 → 4*8=32 → 32//2=16 → 3+16=19 → 19-1=18
resultat1 = 3 + 4 * 2 ** 3 // 2 - 1
print(f"3 + 4 * 2 ** 3 // 2 - 1 = {resultat1}")

# Expression 2
a, b, c = 5, 3, 2
# Étapes : a//b=1 → 1**c=1 → c*1=2 → a%b=2 → 2+2=4
resultat2 = a % b + c * (a // b) ** c
print(f"5 % 3 + 2 * (5 // 3) ** 2 = {resultat2}")

# Expression 3
x, y, z = 8, 3, 2
# Étapes : x>y=True, y<z=False → True and False=False
# y*z=6 → x==6=False → False or False=False
resultat3 = (x > y and y < z) or (x == y * z)
print(f"(8 > 3 and 3 < 2) or (8 == 3 * 2) = {resultat3}")
```

## Solutions Exercice 2 : Réécriture avec parenthèses

```python
print("\n=== EXERCICE 2 SOLUTIONS ===")

# Variables pour les tests
a, b, c, d, e, f = 1, 2, 3, 4, 5, 6
x, y, z = True, False, True
p, q, r, s = 2, 3, 2, 4

# Expression 1 - Parenthèses implicites
expr1_original = a + b * c - d / e % f
expr1_parentheses = a + (b * c) - ((d / e) % f)
print(f"a + b * c - d / e % f = {expr1_original}")
print(f"a + (b * c) - ((d / e) % f) = {expr1_parentheses}")

# Expression 2 - Parenthèses implicites
expr2_original = not x or y and z
expr2_parentheses = (not x) or (y and z)
print(f"not x or y and z = {expr2_original}")
print(f"(not x) or (y and z) = {expr2_parentheses}")

# Expression 3 - Parenthèses implicites
expr3_original = p ** q ** r * s
expr3_parentheses = (p ** (q ** r)) * s
print(f"p ** q ** r * s = {expr3_original}")
print(f"(p ** (q ** r)) * s = {expr3_parentheses}")
```

## Solutions Exercice 3 : Correction d'expressions

```python
print("\n=== EXERCICE 3 SOLUTIONS ===")

# Correction 1
resultat_erreur1 = 15 / 2 * 3      # 7.5 * 3 = 22.5
resultat_correction1 = (15 / 2) * 3 # Même résultat, parenthèses inutiles
print(f"15 / 2 * 3 = {resultat_erreur1}")
print(f"(15 / 2) * 3 = {resultat_correction1}")

# Correction 2
resultat_erreur2 = 2 ** 3 ** 2      # 2 ** 9 = 512
resultat_correction2 = (2 ** 3) ** 2 # 8 ** 2 = 64
print(f"2 ** 3 ** 2 = {resultat_erreur2}")
print(f"(2 ** 3) ** 2 = {resultat_correction2}")

# Correction 3
resultat_erreur3 = 10 - 5 + 3      # 5 + 3 = 8
resultat_correction3 = 10 - (5 + 3) # 10 - 8 = 2
print(f"10 - 5 + 3 = {resultat_erreur3}")
print(f"10 - (5 + 3) = {resultat_correction3}")
```

## Solutions Exercice 4 : Conversions imbriquées

```python
print("\n=== EXERCICE 4 SOLUTIONS ===")

# Conversions chainées
valeur1 = int(float("12.75"))  # float("12.75")=12.75 → int(12.75)=12
valeur2 = str(int(8.999))      # int(8.999)=8 → str(8)="8"
valeur3 = bool(int("0"))       # int("0")=0 → bool(0)=False
valeur4 = float(str(3 + 4.5))  # 3+4.5=7.5 → str(7.5)="7.5" → float("7.5")=7.5

print(f'int(float("12.75")) = {valeur1}')
print(f'str(int(8.999)) = "{valeur2}"')
print(f'bool(int("0")) = {valeur3}')
print(f'float(str(3 + 4.5)) = {valeur4}')

# Conversions complexes
texte = "15.5 euros"
prix = float(texte.split()[0])  # split()=["15.5", "euros"] → [0]="15.5" → float=15.5
quantite = 3
total = prix * quantite  # 15.5 * 3 = 46.5

print(f"Prix extrait: {prix}")
print(f"Total: {total}")
```

## Solutions Exercice 5 : Programme de conversion universelle

```python
print("\n=== EXERCICE 5 SOLUTIONS ===")

def detecter_et_convertir(valeur):
    resultats = {"original": valeur, "type_original": type(valeur).__name__}

    # Essayer les conversions
    try:
        resultats["vers_int"] = int(valeur)
    except (ValueError, TypeError):
        resultats["vers_int"] = "Impossible"

    try:
        resultats["vers_float"] = float(valeur)
    except (ValueError, TypeError):
        resultats["vers_float"] = "Impossible"

    try:
        resultats["vers_bool"] = bool(valeur)
    except (ValueError, TypeError):
        resultats["vers_bool"] = "Impossible"

    try:
        resultats["vers_str"] = str(valeur)
    except (ValueError, TypeError):
        resultats["vers_str"] = "Impossible"

    return resultats

# Tests
test_values = ["123", "45.67", "True", "hello", "0", True, 42]

for valeur in test_values:
    resultat = detecter_et_convertir(valeur)
    print(f"\n{valeur} ({type(valeur).__name__}):")
    for conv_type, conv_val in resultat.items():
        if conv_type not in ["original", "type_original"]:
            print(f"  {conv_type}: {conv_val}")
```

## Solutions Exercice 6 : Gestion des arrondis et troncatures

```python
print("\n=== EXERCICE 6 SOLUTIONS ===")

import math

valeurs = [12.3, 12.7, -12.3, -12.7, "12.3", "12.7"]

print(f"{'Valeur':<10} {'int()':<8} {'round()':<8} {'math.floor()':<12} {'math.ceil()':<10}")
print("-" * 55)

for val in valeurs:
    # Conversion en float si c'est un string
    if isinstance(val, str):
        val_float = float(val)
    else:
        val_float = val

    int_val = int(val_float)
    round_val = round(val_float)
    floor_val = math.floor(val_float)
    ceil_val = math.ceil(val_float)

    print(f"{str(val):<10} {int_val:<8} {round_val:<8} {floor_val:<12} {ceil_val:<10}")
```

## Solutions Exercice 7 : Effets de bord complexes

```python
print("\n=== EXERCICE 7 SOLUTIONS ===")

def modifier_data(data1, data2):
    data1[0] = 100  # Modifie l'original car liste est mutable
    data2 = "modifié"  # Ne modifie pas l'original car string est immuable
    return data2

# Données initiales
liste_originale = [1, 2, 3]
texte_original = "original"

print("Avant appel:")
print(f"Liste: {liste_originale}")
print(f"Texte: {texte_original}")

# Appel de fonction
resultat = modifier_data(liste_originale, texte_original)

print("\nAprès appel:")
print(f"Liste après appel: {liste_originale}")  # [100, 2, 3] - modifiée
print(f"Texte après appel: {texte_original}")   # "original" - inchangé
print(f"Résultat fonction: {resultat}")         # "modifié"
```

## Solutions Exercice 8 : Copies profondes vs superficielles

```python
print("\n=== EXERCICE 8 SOLUTIONS ===")

import copy

# Structure complexe
donnees_complexes = [
    [1, 2, 3],
    {"a": 10, "b": [4, 5]},
    (6, 7, [8, 9])
]

# Différentes copies
ref = donnees_complexes
copie_simple = donnees_complexes.copy()
copie_profonde = copy.deepcopy(donnees_complexes)

print("Avant modifications:")
print(f"Original: {donnees_complexes[0][0]}, {donnees_complexes[1]['b'][0]}")
print(f"Copie simple: {copie_simple[0][0]}, {copie_simple[1]['b'][0]}")
print(f"Copie profonde: {copie_profonde[0][0]}, {copie_profonde[1]['b'][0]}")

# Modifications
ref[0][0] = 100
ref[1]["b"][0] = 400

print("\nAprès modifications:")
print(f"Original: {donnees_complexes[0][0]}, {donnees_complexes[1]['b'][0]}")
print(f"Copie simple: {copie_simple[0][0]}, {copie_simple[1]['b'][0]}")  # Affectée
print(f"Copie profonde: {copie_profonde[0][0]}, {copie_profonde[1]['b'][0]}")  # Inchangée

print("\nExplication:")
print("- La référence modifie l'original directement")
print("- La copie simple partage les sous-objets mutables")
print("- La copie profonde crée une vraie copie indépendante")
print("- Le tuple est immuable, donc ses éléments ne peuvent être modifiés")
```

## Solutions Exercice 9 : Performance des types

```python
print("\n=== EXERCICE 9 SOLUTIONS ===")

import sys

# Création de différentes structures
entier = 1000000
chaine = "A" * 1000
liste = ["A"] * 1000
tuple_data = ("A",) * 1000

print("Comparaison de taille mémoire:")
print(f"Int (1000000): {sys.getsizeof(entier)} octets")
print(f"String ('A'*1000): {sys.getsizeof(chaine)} octets")
print(f"Liste (['A']*1000): {sys.getsizeof(liste)} octets")
print(f"Tuple (('A',)*1000): {sys.getsizeof(tuple_data)} octets")

print("\nObservations:")
print("- Les tuples sont plus légers que les listes")
print("- Les strings sont efficaces pour le texte répété")
print("- Les entiers ont une taille fixe quelle que soit leur valeur")
```

## Solutions Exercice 10 : Tables de vérité complexes

```python
print("\n=== EXERCICE 10 SOLUTIONS ===")

# Pour a = True, b = False, c = True
a, b, c = True, False, True

expression1 = not a or b and c
# Étapes: not a=False, b and c=False, False or False=False

expression2 = (not a) or (b and c)
# Même calcul que expression1

expression3 = not (a or b) and c
# Étapes: a or b=True, not True=False, False and c=False

expression4 = a != b == c
# Étapes: a != b=True, b == c=False, True == False=False

print(f"not a or b and c = {expression1}")
print(f"(not a) or (b and c) = {expression2}")
print(f"not (a or b) and c = {expression3}")
print(f"a != b == c = {expression4}")
```

## Solutions Exercice 11 : Comparaisons chainées

```python
print("\n=== EXERCICE 11 SOLUTIONS ===")

a, b, c, d = 5, 10, 5, 20

resultat1 = a < b < c < d
# Étapes: 5<10=True, 10<5=False, donc False

resultat2 = a == c != b < d
# Étapes: a==c=True, c!=b=True, b<d=True, True and True and True=True

resultat3 = a <= c == 5 != b
# Étapes: a<=c=True, c==5=True, 5!=b=True, True and True and True=True

print(f"5 < 10 < 5 < 20 = {resultat1}")
print(f"5 == 5 != 10 < 20 = {resultat2}")
print(f"5 <= 5 == 5 != 10 = {resultat3}")
```

## Solutions Exercice 12 : Programme de validation d'identité

```python
print("\n=== EXERCICE 12 SOLUTIONS ===")

def verifier_identite(obj1, obj2, nom1, nom2):
    egalite = obj1 == obj2
    identite = obj1 is obj2
    type_identique = type(obj1) == type(obj2)

    return {
        "égalité": egalite,
        "identité": identite,
        "même_type": type_identique,
        "id_obj1": id(obj1),
        "id_obj2": id(obj2)
    }

# Tests avec différents cas
cas_test = [
    (100, 100, "a", "b"),
    (1000, 1000, "c", "d"),
    ([1,2], [1,2], "liste1", "liste2"),
    ("hello", "hello", "str1", "str2")
]

for obj1, obj2, nom1, nom2 in cas_test:
    resultat = verifier_identite(obj1, obj2, nom1, nom2)
    print(f"\n{nom1} vs {nom2}:")
    print(f"  Égalité (==): {resultat['égalité']}")
    print(f"  Identité (is): {resultat['identité']}")
    print(f"  Même type: {resultat['même_type']}")
    print(f"  ID {nom1}: {resultat['id_obj1']}")
    print(f"  ID {nom2}: {resultat['id_obj2']}")
```

## Solutions Exercice 13 : Expressions de priorité mixte

```python
print("\n=== EXERCICE 13 SOLUTIONS ===")

# Données de test
x, y, z = 10, 5, 10
a, b = True, False

# Expression 1
expr1 = x > y and y < z or a and not b
# Étapes: x>y=True, y<z=True → True and True=True
# not b=True → a and True=True
# True or True=True

# Expression 2
expr2 = (x == z) != (y == z) and a or b
# Étapes: x==z=True, y==z=False → True != False=True
# True and a=True → True or b=True

# Expression 3
expr3 = not (x > y) or (y < z and a) == b
# Étapes: x>y=True → not True=False
# y<z=True → True and a=True → True == b=False
# False or False=False

print(f"x > y and y < z or a and not b = {expr1}")
print(f"(x == z) != (y == z) and a or b = {expr2}")
print(f"not (x > y) or (y < z and a) == b = {expr3}")

print("\nPriorités des opérateurs dans l'ordre:")
print("1. ** (exponentiation)")
print("2. +x, -x, ~x (unaire)")
print("3. *, /, //, %")
print("4. +, - (binaire)")
print("5. <, <=, >, >=, ==, !=")
print("6. not x")
print("7. and")
print("8. or")
```
