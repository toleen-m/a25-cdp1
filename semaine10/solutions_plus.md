## **Niveau 1 : Récursivité Fondamentale**

### **Exercice 1.1 : Somme des n premiers nombres**

```python
def somme(n):
    """Calcule récursivement la somme de 1 à n."""
    if n <= 0:  # Cas de base
        return 0
    return n + somme(n - 1)  # Appel récursif

# Test
print(somme(5))   # 15
print(somme(10))  # 55
```

**Explication** :

- Cas de base : `n <= 0` retourne 0
- Réduction : `somme(n)` = `n + somme(n-1)`
- Trace pour `somme(3)` : `3 + somme(2)` → `3 + (2 + somme(1))` → `3 + (2 + (1 + somme(0)))` → `3 + (2 + (1 + 0))` = 6

### **Exercice 1.2 : Factorielle**

```python
def factorielle(n):
    """Calcule n! de façon récursive."""
    if n <= 1:  # Cas de base : 0! = 1 et 1! = 1
        return 1
    return n * factorielle(n - 1)

# Test
print(factorielle(5))   # 120
print(factorielle(0))   # 1
print(factorielle(1))   # 1
```

### **Exercice 1.3 : Puissance**

```python
def puissance(x, n):
    """Calcule x^n récursivement."""
    if n == 0:  # Cas de base : x^0 = 1
        return 1
    if n < 0:   # Gestion des exposants négatifs
        return 1 / puissance(x, -n)
    return x * puissance(x, n - 1)  # x^n = x * x^(n-1)

# Version optimisée (exponentiation rapide)
def puissance_rapide(x, n):
    """Version optimisée avec exponentiation rapide."""
    if n == 0:
        return 1
    if n < 0:
        return 1 / puissance_rapide(x, -n)

    if n % 2 == 0:  # n est pair
        temp = puissance_rapide(x, n // 2)
        return temp * temp
    else:           # n est impair
        return x * puissance_rapide(x, n - 1)

# Test
print(puissance(2, 3))     # 8
print(puissance(5, 0))     # 1
print(puissance(2, -3))    # 0.125
print(puissance_rapide(2, 10))  # 1024
```

---

## **Niveau 2 : Récursivité sur les Chaînes**

### **Exercice 2.1 : Inverser une chaîne**

```python
def inverser(chaine):
    """Inverse récursivement une chaîne de caractères."""
    if len(chaine) <= 1:  # Cas de base
        return chaine

    # Prendre le dernier caractère + inverser(le reste)
    return chaine[-1] + inverser(chaine[:-1])

# Version avec indices
def inverser_indices(chaine, debut=0, fin=None):
    """Version avec indices pour éviter les slices coûteuses."""
    if fin is None:
        fin = len(chaine) - 1

    if debut >= fin:  # Cas de base
        return chaine

    # Convertir en liste pour pouvoir modifier
    liste_chars = list(chaine)
    # Échanger les caractères aux extrémités
    liste_chars[debut], liste_chars[fin] = liste_chars[fin], liste_chars[debut]
    # Appel récursif sur le reste
    return inverser_indices(''.join(liste_chars), debut + 1, fin - 1)

# Test
print(inverser("python"))      # "nohtyp"
print(inverser("recursif"))    # "fisrucer"
print(inverser(""))            # ""
```

### **Exercice 2.2 : Compter les occurrences**

```python
def compter_occurrences(chaine, caractere, index=0):
    """Compte récursivement les occurrences d'un caractère."""
    if index >= len(chaine):  # Cas de base
        return 0

    # Compter 1 si le caractère correspond, 0 sinon
    compteur = 1 if chaine[index] == caractere else 0
    # Ajouter le compte du reste de la chaîne
    return compteur + compter_occurrences(chaine, caractere, index + 1)

# Version avec slices (moins efficace)
def compter_occurrences_slice(chaine, caractere):
    if not chaine:  # Chaîne vide
        return 0

    premier = 1 if chaine[0] == caractere else 0
    return premier + compter_occurrences_slice(chaine[1:], caractere)

# Test
print(compter_occurrences("programmation", 'm'))  # 2
print(compter_occurrences("recursivite", 'r'))    # 2
print(compter_occurrences("", 'a'))               # 0
```

### **Exercice 2.3 : Vérifier palindrome**

```python
def est_palindrome(chaine):
    """Vérifie récursivement si une chaîne est un palindrome."""
    # Nettoyer la chaîne (enlever espaces, mettre en minuscule)
    chaine = ''.join(c.lower() for c in chaine if c.isalnum())

    def verifier(debut, fin):
        if debut >= fin:  # Cas de base
            return True

        if chaine[debut] != chaine[fin]:
            return False

        return verifier(debut + 1, fin - 1)

    return verifier(0, len(chaine) - 1)

# Version simple avec slices
def est_palindrome_simple(chaine):
    if len(chaine) <= 1:
        return True

    if chaine[0] != chaine[-1]:
        return False

    return est_palindrome_simple(chaine[1:-1])

# Test
print(est_palindrome("radar"))           # True
print(est_palindrome("python"))          # False
print(est_palindrome(""))                # True
print(est_palindrome("A man a plan a canal Panama"))  # True
```

---

## **Niveau 3 : Récursivité sur les Listes**

### **Exercice 3.1 : Somme d'une liste**

```python
def somme_liste(liste, index=0):
    """Calcule récursivement la somme d'une liste."""
    if index >= len(liste):  # Cas de base
        return 0
    return liste[index] + somme_liste(liste, index + 1)

# Version avec slices
def somme_liste_slice(liste):
    if not liste:  # Liste vide
        return 0
    return liste[0] + somme_liste_slice(liste[1:])

# Test
print(somme_liste([1, 2, 3, 4, 5]))      # 15
print(somme_liste([10, -2, 8]))         # 16
print(somme_liste([]))                  # 0
```

### **Exercice 3.2 : Maximum d'une liste**

```python
def maximum_liste(liste, index=0):
    """Trouve récursivement le maximum d'une liste."""
    if index >= len(liste):
        return float('-inf')  # Pour les listes vides

    if index == len(liste) - 1:  # Dernier élément
        return liste[index]

    max_restant = maximum_liste(liste, index + 1)
    return liste[index] if liste[index] > max_restant else max_restant

# Version élégante avec deux cas de base
def maximum_liste_v2(liste):
    if len(liste) == 0:
        return None  # Ou lever une exception
    if len(liste) == 1:  # Cas de base
        return liste[0]

    max_restant = maximum_liste_v2(liste[1:])
    return liste[0] if liste[0] > max_restant else max_restant

# Test
print(maximum_liste([3, 7, 2, 9, 1]))    # 9
print(maximum_liste([-5, -2, -10]))     # -2
print(maximum_liste([]))                # -inf (ou None pour v2)
```

### **Exercice 3.3 : Recherche dans une liste**

```python
def rechercher(liste, element, index=0):
    """Recherche récursive d'un élément dans une liste."""
    if index >= len(liste):  # Cas de base : non trouvé
        return False
    if liste[index] == element:  # Cas de base : trouvé
        return True
    return rechercher(liste, element, index + 1)

# Version qui retourne l'index
def rechercher_index(liste, element, index=0):
    if index >= len(liste):
        return -1  # Non trouvé
    if liste[index] == element:
        return index
    return rechercher_index(liste, element, index + 1)

# Test
print(rechercher([1, 2, 3, 4, 5], 3))   # True
print(rechercher([1, 2, 3, 4, 5], 6))   # False
print(rechercher_index([1, 2, 3, 4, 5], 3))  # 2
```

---

## **Niveau 4 : Récursivité Mathématique Avancée**

### **Exercice 4.1 : Suite de Fibonacci**

```python
def fibonacci(n):
    """Calcule le n-ième nombre de Fibonacci."""
    if n <= 0:  # F(0) = 0
        return 0
    if n == 1:  # F(1) = 1
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

# Version avec mémoïsation (optimisation)
cache_fibonacci = {}

def fibonacci_memo(n):
    """Fibonacci avec mémoïsation pour éviter les calculs répétés."""
    if n in cache_fibonacci:
        return cache_fibonacci[n]

    if n <= 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

    cache_fibonacci[n] = result
    return result

# Test
print(fibonacci(0))   # 0
print(fibonacci(1))   # 1
print(fibonacci(6))   # 8
print(fibonacci_memo(50))  # 12586269025 (rapide avec mémoïsation)
```

### **Exercice 4.2 : PGCD (Algorithme d'Euclide)**

```python
def pgcd(a, b):
    """Calcule le PGCD avec l'algorithme d'Euclide récursif."""
    if b == 0:  # Cas de base
        return abs(a)
    return pgcd(b, a % b)

# Version étendue (retourne aussi les coefficients de Bézout)
def pgcd_etendu(a, b):
    """Retourne (pgcd, x, y) tels que ax + by = pgcd(a,b)."""
    if b == 0:
        return (abs(a), 1 if a >= 0 else -1, 0)

    pgcd_rest, x1, y1 = pgcd_etendu(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (pgcd_rest, x, y)

# Test
print(pgcd(48, 18))      # 6
print(pgcd(1071, 462))   # 21
print(pgcd(17, 13))      # 1 (nombres premiers entre eux)

pgcd_val, x, y = pgcd_etendu(48, 18)
print(f"PGCD(48,18)={pgcd_val}, coefficients: 48*{x} + 18*{y} = {pgcd_val}")
```

### **Exercice 4.3 : Tours de Hanoï**

```python
def hanoi(n, depart, intermediaire, arrivee):
    """
    Résout le problème des Tours de Hanoï.
    n: nombre de disques
    depart: tour de départ
    intermediaire: tour intermédiaire
    arrivee: tour d'arrivée
    """
    if n == 1:  # Cas de base : déplacer un seul disque
        print(f"Déplacer disque 1 de {depart} vers {arrivee}")
        return

    # Étape 1 : Déplacer n-1 disques de départ vers intermédiaire
    hanoi(n - 1, depart, arrivee, intermediaire)

    # Étape 2 : Déplacer le plus grand disque vers l'arrivée
    print(f"Déplacer disque {n} de {depart} vers {arrivee}")

    # Étape 3 : Déplacer les n-1 disques de intermédiaire vers arrivée
    hanoi(n - 1, intermediaire, depart, arrivee)

def compter_deplacements_hanoi(n):
    """Calcule le nombre minimal de déplacements nécessaires."""
    if n == 1:
        return 1
    return 2 * compter_deplacements_hanoi(n - 1) + 1

# Formule fermée : 2^n - 1
def compter_deplacements_formule(n):
    return 2**n - 1

# Test
print("=== Tours de Hanoï avec 3 disques ===")
hanoi(3, 'A', 'B', 'C')
print(f"\nNombre de déplacements pour 3 disques: {compter_deplacements_hanoi(3)}")
print(f"Vérification: {compter_deplacements_formule(3)}")

print("\n=== Tours de Hanoï avec 4 disques ===")
hanoi(4, 'A', 'B', 'C')
```

---

## **Niveau 5 : Récursivité sur les Structures Arborescentes**

### **Exercice 5.1 : Profondeur d'une structure imbriquée**

```python
def profondeur(structure):
    """Calcule la profondeur maximale d'une liste imbriquée."""
    if not isinstance(structure, list) or not structure:
        return 1  # Une liste vide ou non-liste a profondeur 1

    profondeurs_sous_listes = []
    for element in structure:
        if isinstance(element, list):
            profondeurs_sous_listes.append(profondeur(element))
        else:
            profondeurs_sous_listes.append(1)  # Élément non-liste

    return 1 + max(profondeurs_sous_listes)

# Version plus concise
def profondeur_v2(structure):
    if not isinstance(structure, list):
        return 0
    if not structure:
        return 1
    return 1 + max((profondeur_v2(elem) for elem in structure), default=0)

# Test
print(profondeur([1, [2, [3, 4], 5], 6]))  # 3
print(profondeur([1, 2, 3]))               # 1
print(profondeur([]))                      # 1
print(profondeur([[[[]]]]))                # 4
```

### **Exercice 5.2 : Aplatir une liste**

```python
def aplatir(liste_imbriquee):
    """Aplatit récursivement une liste contenant d'autres listes."""
    resultat = []

    for element in liste_imbriquee:
        if isinstance(element, list):
            # Étendre avec la version aplatie de la sous-liste
            resultat.extend(aplatir(element))
        else:
            # Ajouter l'élément simple
            resultat.append(element)

    return resultat

# Version avec générateur (plus efficace pour les grandes listes)
def aplatir_generateur(liste_imbriquee):
    for element in liste_imbriquee:
        if isinstance(element, list):
            yield from aplatir_generateur(element)
        else:
            yield element

# Test
liste_test = [1, [2, [3, 4], 5], 6]
print(aplatir(liste_test))  # [1, 2, 3, 4, 5, 6]

# Utilisation du générateur
print(list(aplatir_generateur(liste_test)))  # [1, 2, 3, 4, 5, 6]

# Test avec structure complexe
complexe = [1, [2, [3, [4, 5], 6]], 7, [8, 9]]
print(aplatir(complexe))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### **Exercice 5.3 : Parcours d'arbre binaire**

```python
class Noeud:
    def __init__(self, valeur, gauche=None, droite=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite

# Parcours préfixe (racine, gauche, droite)
def parcours_prefixe(noeud):
    if noeud is None:
        return []

    resultat = [noeud.valeur]
    resultat.extend(parcours_prefixe(noeud.gauche))
    resultat.extend(parcours_prefixe(noeud.droite))
    return resultat

# Parcours infixe (gauche, racine, droite)
def parcours_infixe(noeud):
    if noeud is None:
        return []

    resultat = []
    resultat.extend(parcours_infixe(noeud.gauche))
    resultat.append(noeud.valeur)
    resultat.extend(parcours_infixe(noeud.droite))
    return resultat

# Parcours postfixe (gauche, droite, racine)
def parcours_postfixe(noeud):
    if noeud is None:
        return []

    resultat = []
    resultat.extend(parcours_postfixe(noeud.gauche))
    resultat.extend(parcours_postfixe(noeud.droite))
    resultat.append(noeud.valeur)
    return resultat

# Hauteur de l'arbre
def hauteur_arbre(noeud):
    if noeud is None:
        return 0
    return 1 + max(hauteur_arbre(noeud.gauche), hauteur_arbre(noeud.droite))

# Test
arbre = Noeud(1,
              Noeud(2,
                    Noeud(4),
                    Noeud(5)),
              Noeud(3))

print("Préfixe:", parcours_prefixe(arbre))  # [1, 2, 4, 5, 3]
print("Infixe:", parcours_infixe(arbre))    # [4, 2, 5, 1, 3]
print("Postfixe:", parcours_postfixe(arbre)) # [4, 5, 2, 3, 1]
print("Hauteur:", hauteur_arbre(arbre))      # 3
```

---

## **Quelques solutions des niveaux avancés**

### **Exercice 6.1 : Sous-ensembles**

```python
def sous_ensembles(liste):
    """Génère tous les sous-ensembles d'une liste."""
    if not liste:  # Cas de base : ensemble vide
        return [[]]

    premier = liste[0]
    restant = liste[1:]

    # Sous-ensembles sans le premier élément
    sous_sans_premier = sous_ensembles(restant)

    # Sous-ensembles avec le premier élément
    sous_avec_premier = []
    for sous_ensemble in sous_sans_premier:
        sous_avec_premier.append([premier] + sous_ensemble)

    # Combiner les deux
    return sous_sans_premier + sous_avec_premier

# Test
resultat = sous_ensembles([1, 2, 3])
print("Nombre de sous-ensembles:", len(resultat))  # 2^3 = 8
for sous in sorted(resultat, key=len):
    print(sous)
```

### **Exercice 7.1 : Fibonacci avec mémoïsation améliorée**

```python
from functools import lru_cache

# Utilisation du décorateur standard de Python
@lru_cache(maxsize=None)
def fibonacci_cache(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)

# Test
print(fibonacci_cache(100))  # 354224848179261915075 (instantané)
```

### **Exercice 7.2 : Combinaisons avec mémoïsation**

```python
cache_combinaison = {}

def combinaison(n, k):
    """Calcule C(n, k) = n! / (k! * (n-k)!) récursivement."""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

    # Vérifier le cache
    if (n, k) in cache_combinaison:
        return cache_combinaison[(n, k)]

    # Formule de récurrence: C(n,k) = C(n-1,k-1) + C(n-1,k)
    result = combinaison(n - 1, k - 1) + combinaison(n - 1, k)

    # Mettre en cache
    cache_combinaison[(n, k)] = result
    return result

# Test
print(combinaison(5, 2))   # 10
print(combinaison(10, 3))  # 120
print(combinaison(50, 25)) # 126410606437752 (calcul rapide grâce au cache)
```

---

## **Conseils pour la Pratique**

1. **Toujours identifier le(s) cas de base** : C'est la condition d'arrêt
2. **Réduire le problème** : Chaque appel récursif doit se rapprocher du cas de base
3. **Visualiser avec des `print()`** : Pour comprendre l'ordre d'exécution
4. **Tester avec des petites valeurs** : Vérifiez manuellement les résultats
5. **Attention à la profondeur de récursion** : Python a une limite (~1000)

**Exemple de débuggage avec traces** :

```python
def somme_trace(n, profondeur=0):
    indent = "  " * profondeur
    print(f"{indent}somme_trace({n})")

    if n <= 0:
        print(f"{indent}→ retourne 0")
        return 0

    resultat = n + somme_trace(n - 1, profondeur + 1)
    print(f"{indent}→ retourne {resultat}")
    return resultat

somme_trace(3)
```
