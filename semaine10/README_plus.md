## **Exercices de Récursivité en Python**

### **Niveau 1 : Récursivité Fondamentale**

**Exercice 1.1 : Somme des n premiers nombres**
Écrivez une fonction récursive `somme(n)` qui calcule la somme des nombres de 1 à n.

```python
# Test
print(somme(5))   # 15 (1+2+3+4+5)
print(somme(10))  # 55
```

**Exercice 1.2 : Factorielle**
Implémentez la fonction factorielle de façon récursive.

```python
# Test
print(factorielle(5))   # 120 (5*4*3*2*1)
print(factorielle(0))   # 1 (par définition)
```

**Exercice 1.3 : Puissance**
Créez une fonction récursive `puissance(x, n)` qui calcule x^n.

```python
# Test
print(puissance(2, 3))   # 8
print(puissance(5, 0))   # 1
```

---

### **Niveau 2 : Récursivité sur les Chaînes**

**Exercice 2.1 : Inverser une chaîne**
Écrivez une fonction récursive qui inverse une chaîne de caractères.

```python
# Test
print(inverser("python"))    # "nohtyp"
print(inverser("recursif"))  # "fisrucer"
```

**Exercice 2.2 : Compter les occurrences**
Comptez récursivement le nombre d'occurrences d'un caractère dans une chaîne.

```python
# Test
print(compter_occurrences("programmation", 'm'))  # 2
print(compter_occurrences("recursivite", 'r'))    # 2
```

**Exercice 2.3 : Vérifier palindrome**
Vérifiez si une chaîne est un palindrome (se lit pareil dans les deux sens).

```python
# Test
print(est_palindrome("radar"))    # True
print(est_palindrome("python"))   # False
print(est_palindrome(""))         # True
```

---

### **Niveau 3 : Récursivité sur les Listes**

**Exercice 3.1 : Somme d'une liste**
Calculez récursivement la somme des éléments d'une liste.

```python
# Test
print(somme_liste([1, 2, 3, 4, 5]))      # 15
print(somme_liste([10, -2, 8]))         # 16
print(somme_liste([]))                  # 0
```

**Exercice 3.2 : Maximum d'une liste**
Trouvez le maximum d'une liste de façon récursive.

```python
# Test
print(maximum_liste([3, 7, 2, 9, 1]))    # 9
print(maximum_liste([-5, -2, -10]))     # -2
```

**Exercice 3.3 : Recherche dans une liste**
Recherchez récursivement si un élément est présent dans une liste.

```python
# Test
print(rechercher([1, 2, 3, 4, 5], 3))   # True
print(rechercher([1, 2, 3, 4, 5], 6))   # False
```

---

### **Niveau 4 : Récursivité Mathématique Avancée**

**Exercice 4.1 : Suite de Fibonacci**
Générez le n-ième terme de la suite de Fibonacci.

```python
# Test
print(fibonacci(0))   # 0
print(fibonacci(1))   # 1
print(fibonacci(6))   # 8 (0,1,1,2,3,5,8)
```

**Exercice 4.2 : PGCD (Algorithme d'Euclide)**
Calculez le PGCD de deux nombres avec l'algorithme d'Euclide récursif.

```python
# Test
print(pgcd(48, 18))    # 6
print(pgcd(1071, 462)) # 21
```

**Exercice 4.3 : Tours de Hanoï**
Résolvez le problème des Tours de Hanoï pour n disques.

```python
# Test
def hanoi(n, depart, intermediaire, arrivee):
    # À compléter
    pass

hanoi(3, 'A', 'B', 'C')
# Doit afficher les déplacements nécessaires
```

---

### **Niveau 5 : Récursivité sur les Structures Arborescentes**

**Exercice 5.1 : Profondeur d'une structure imbriquée**
Calculez la profondeur maximale d'une liste pouvant contenir d'autres listes.

```python
# Test
print(profondeur([1, [2, [3, 4], 5], 6]))  # 3
print(profondeur([1, 2, 3]))               # 1
print(profondeur([]))                      # 1
```

**Exercice 5.2 : Aplatir une liste**
Aplatissez récursivement une liste contenant potentiellement d'autres listes.

```python
# Test
print(aplatir([1, [2, [3, 4], 5], 6]))
# [1, 2, 3, 4, 5, 6]
```

**Exercice 5.3 : Parcours d'arbre binaire**
Créez une fonction qui retourne tous les éléments d'un arbre binaire.

```python
# Structure de nœud
class Noeud:
    def __init__(self, valeur, gauche=None, droite=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite

# Test
arbre = Noeud(1, Noeud(2, Noeud(4), Noeud(5)), Noeud(3))
print(parcours_prefixe(arbre))  # [1, 2, 4, 5, 3]
```

---

### **Niveau 6 : Défis Récursifs**

**Exercice 6.1 : Sous-ensembles**
Générez tous les sous-ensembles d'un ensemble donné.

```python
# Test
print(sous_ensembles([1, 2, 3]))
# [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
```

**Exercice 6.2 : Permutations**
Générez toutes les permutations d'une liste.

```python
# Test
print(permutations([1, 2, 3]))
# [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
```

**Exercice 6.3 : Retour sur trace (Backtracking)**
Résolvez le problème des N reines sur un échiquier N×N.

```python
def n_reines(n):
    # À compléter : retourne toutes les solutions
    pass

solutions = n_reines(4)
print(f"Nombre de solutions pour 4 reines: {len(solutions)}")
```

---

### **Niveau 7 : Optimisation et Mémoïsation**

**Exercice 7.1 : Fibonacci avec mémoïsation**
Améliorez la fonction Fibonacci avec un dictionnaire pour stocker les résultats intermédiaires.

```python
# Test
print(fibonacci_memo(50))  # Doit être rapide
```

**Exercice 7.2 : Combinaisons (Coefficient binomial)**
Calculez C(n, k) = n!/(k!(n-k)!) de façon récursive avec mémoïsation.

```python
# Test
print(combinaison(5, 2))   # 10
print(combinaison(10, 3))  # 120
```

---

### **Exercice Final : Interpréteur d'Expressions Arithmétiques**

**Exercice 8.1 : Évaluer une expression**
Écrivez un évaluateur récursif pour des expressions arithmétiques simples.

```python
# Test
print(evaluer("(2 + 3) * 4"))        # 20
print(evaluer("2 + 3 * 4"))          # 14
print(evaluer("((1+2)*(3+4))/2"))    # 10.5
```

---

## **Indications et Bonnes Pratiques**

### **Structure Générale d'une Fonction Récursive**

```python
def fonction_recursive(parametre):
    # 1. CAS DE BASE (condition d'arrêt)
    if condition_simple:
        return valeur_simple

    # 2. APPEL RÉCURSIF (cas général)
    #    Réduire le problème vers le cas de base
    resultat_partiel = fonction_recursive(parametre_reduit)

    # 3. COMBINAISON DES RÉSULTATS
    return combiner(parametre, resultat_partiel)
```

### **Exemple Guidé : Exercice 1.1 (Somme des n premiers nombres)**

```python
def somme(n):
    # Cas de base
    if n <= 0:
        return 0

    # Appel récursif + combinaison
    return n + somme(n - 1)

# Traces d'exécution pour somme(3):
# somme(3) = 3 + somme(2)
# somme(2) = 2 + somme(1)
# somme(1) = 1 + somme(0)
# somme(0) = 0  ← Cas de base
# Remontée: 1+0=1, 2+1=3, 3+3=6
```

### **Pièges Courants à Éviter**

1. **Oublier le cas de base** → récursion infinie
2. **Ne pas réduire suffisamment le problème** → récursion infinie
3. **Récursion trop profonde** → `RecursionError` (limite ~1000 appels)
4. **Duplication de calculs** → utiliser la mémoïsation

### **Conversion Itérative ↔ Récursive**

Pour l'exercice 1.1 :

```python
# Version itérative
def somme_iterative(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

# Version récursive
def somme_recursive(n):
    if n <= 0:
        return 0
    return n + somme_recursive(n-1)
```

---

## **Pour Aller Plus Loin**

### **Analyse de Complexité**

Pour chaque exercice, essayez de déterminer :

- Complexité temporelle (O(n), O(2^n), etc.)
- Complexité spatiale (pile d'appels)
- Possibilité d'optimisation (tail recursion, mémoïsation)

### **Débuggage Récursif**

Ajoutez des `print()` pour tracer l'exécution :

```python
def somme_debug(n, profondeur=0):
    indentation = "  " * profondeur
    print(f"{indentation}somme({n}) appelé")

    if n <= 0:
        print(f"{indentation}→ retourne 0")
        return 0

    resultat = n + somme_debug(n-1, profondeur+1)
    print(f"{indentation}→ retourne {resultat}")
    return resultat

somme_debug(3)
```
