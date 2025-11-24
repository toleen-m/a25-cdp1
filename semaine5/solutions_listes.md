# Solutions des Exercices

## Solution Exercice 1

### 1.1 : Accès par index

```python
nombres = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(f"Premier: {nombres[0]}")
print(f"Dernier: {nombres[-1]}")
print(f"Cinquième: {nombres[4]}")
print(f"Avant-dernier: {nombres[-2]}")
```

### 1.2 : Slicing de liste

```python
nombres = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(f"3 premiers: {nombres[:3]}")
print(f"3 derniers: {nombres[-3:]}")
print(f"Du 3ème au 7ème: {nombres[2:7]}")
print(f"Un sur deux: {nombres[::2]}")
print(f"Inversée: {nombres[::-1]}")
```

### 1.3 : Modification par index

```python
fruits = ["pomme", "banane", "orange"]

fruits[1] = "kiwi"
fruits[-1] = "ananas"
fruits.append("fraise")

print(fruits)  # ['pomme', 'kiwi', 'ananas', 'fraise']
```

## Solution Exercice 2

### 2.1 : Décompactage basique

```python
coordonnees = [45.5, -73.5, 100]
latitude, longitude, altitude = coordonnees

print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
print(f"Altitude: {altitude}")
```

### 2.2 : Décompactage partiel

```python
donnees = ["Alice", 25, "Paris", "ingénieure", "python"]
nom, age, *reste = donnees

print(f"Nom: {nom}")
print(f"Âge: {age}")
print(f"Reste: {reste}")
```

### 2.3 : Échange de variables

```python
a = 5
b = 10

print(f"Avant: a={a}, b={b}")
a, b = b, a
print(f"Après: a={a}, b={b}")
```

## Solution Exercice 3

### 3.1 : Concaténation et répétition

```python
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

concatenee = liste1 + liste2
repetee = liste1 * 3
liste1.extend(liste2)

print(f"Concaténée: {concatenee}")
print(f"Répétée: {repetee}")
print(f"Liste1 étendue: {liste1}")
```

### 3.2 : Copies de listes

```python
originale = [[1, 2], [3, 4]]
reference = originale
copie_superficielle = originale.copy()

reference[0][0] = 100
copie_superficielle[1] = [300, 400]

print(f"Originale: {originale}")    # [[100, 2], [3, 4]]
print(f"Référence: {reference}")    # [[100, 2], [3, 4]]
print(f"Copie: {copie_superficielle}")  # [[1, 2], [300, 400]]
```

### 3.3 : Comparaison de listes

```python
liste_a = [1, 2, 3]
liste_b = [3, 2, 1]
liste_c = [1, 2, 3]

print(f"a == b: {liste_a == liste_b}")  # False
print(f"a == c: {liste_a == liste_c}")  # True
print(f"a is c: {liste_a is liste_c}")  # False
```

## Solution Exercice 4

### 4.1 : Fonctions de base

```python
valeurs = [15, 2, 8, 20, 5]

print(f"Longueur: {len(valeurs)}")
print(f"Maximum: {max(valeurs)}")
print(f"Minimum: {min(valeurs)}")
print(f"Somme: {sum(valeurs)}")
print(f"Triée: {sorted(valeurs)}")
print(f"Originale inchangée: {valeurs}")
```

### 4.2 : Ajout d'éléments

```python
liste = ["a", "b"]

liste.append("c")
liste.insert(1, "x")
liste.extend(["d", "e"])

print(liste)  # ['a', 'x', 'b', 'c', 'd', 'e']
```

### 4.3 : Conversion depuis string

```python
mot = "python"
liste_caracteres = list(mot)
print(f"Caractères: {liste_caracteres}")

chiffres_str = "1,2,3,4,5"
liste_chiffres = [int(x) for x in chiffres_str.split(",")]
print(f"Chiffres: {liste_chiffres}")
```

## Solution Exercice 5

### 5.1 : Suppression par valeur et index

```python
elements = ["a", "b", "c", "d", "e", "a"]

elements.remove("a")  # Supprime le premier "a"
del elements[2]       # Supprime l'élément à l'index 2 (maintenant "d")
elements.pop()        # Supprime le dernier élément

print(elements)  # ['b', 'c', 'e']
```

### 5.2 : Nettoyage de liste

```python
donnees = [1, None, "texte", 0, "", [], 42, False]
donnees_nettoyees = [x for x in donnees if x]

print(f"Originale: {donnees}")
print(f"Nettoyée: {donnees_nettoyees}")
```

### 5.3 : Vidage et extraction

```python
liste = [10, 20, 30, 40, 50]

dernier = liste.pop()
premier = liste.pop(0)
liste.clear()

print(f"Dernier élément: {dernier}")
print(f"Premier élément: {premier}")
print(f"Liste vidée: {liste}")
```

## Solution Exercice 6

### 6.1 : Recherche basique

```python
nombres = [15, 8, 23, 42, 8, 15, 8]

print(f"Premier index de 8: {nombres.index(8)}")
print(f"Occurrences de 15: {nombres.count(15)}")
print(f"42 dans la liste: {42 in nombres}")
```

### 6.2 : Recherche conditionnelle

```python
ages = [25, 17, 30, 16, 22, 19]

majeurs = [age for age in ages if age >= 18]
premier_majeur_index = next((i for i, age in enumerate(ages) if age >= 18), -1)

print(f"Majeurs: {majeurs}")
print(f"Index premier majeur: {premier_majeur_index}")
```

### 6.3 : Recherche d'extremums

```python
temperatures = [22, 18, 25, 20, 17, 23, 19]

temp_max = max(temperatures)
index_max = temperatures.index(temp_max)
temp_min = min(temperatures)
index_min = temperatures.index(temp_min)

print(f"Max: {temp_max}°C à l'index {index_max}")
print(f"Min: {temp_min}°C à l'index {index_min}")
```

## Solution Exercice 7

### 7.1 : Tri simple

```python
nombres = [64, 34, 25, 12, 22, 11, 90]

croissant = sorted(nombres)
decroissant = sorted(nombres, reverse=True)

print(f"Croissant: {croissant}")
print(f"Décroissant: {decroissant}")
print(f"Originale inchangée: {nombres}")

# Tri en place
nombres.sort()
print(f"Triée en place: {nombres}")
```

### 7.2 : Tri de strings

```python
mots = ["banane", "pomme", "orange", "kiwi", "ananas"]

alphabetique = sorted(mots)
par_longueur = sorted(mots, key=len)

print(f"Alphabétique: {alphabetique}")
print(f"Par longueur: {par_longueur}")
```

### 7.3 : Tri personnalisé

```python
etudiants = [("Alice", 18), ("Bob", 20), ("Charlie", 17)]

tri_age = sorted(etudiants, key=lambda x: x[1])
tri_nom = sorted(etudiants, key=lambda x: x[0])

print(f"Par age: {tri_age}")
print(f"Par nom: {tri_nom}")
```

## Solution Exercice 8

### 8.1 : Gestion de panier

```python
panier = []
prix = [2.5, 1.8, 3.2, 4.5]

# Ajout de produits
panier.append("pomme")
panier.append("banane")
panier.extend(["orange", "kiwi"])

print(f"Panier: {panier}")

# Suppression
panier.remove("banane")
produit_supprime = panier.pop()

print(f"Après suppression: {panier}")
print(f"Produit supprimé: {produit_supprime}")

# Calcul total (simplifié)
total = sum(prix[:len(panier)])
print(f"Total estimé: {total}€")

# Vidage
panier.clear()
print(f"Panier vidé: {panier}")
```

### 8.2 : Système de notes

```python
notes = [15, 8, 12, 18, 6]

# Ajout
notes.append(14)
notes.insert(2, 16)

print(f"Notes: {notes}")

# Suppression pire note
pire_note = min(notes)
notes.remove(pire_note)

print(f"Sans pire note: {notes}")

# Calculs
moyenne = sum(notes) / len(notes)
bonnes_notes = [note for note in notes if note > moyenne]

print(f"Moyenne: {moyenne:.1f}")
print(f"Notes au-dessus moyenne: {bonnes_notes}")
```

### 8.3 : Mélange et tirage

```python
joueurs = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

# Simulation de mélange (sans random)
melange = joueurs[::-1] + joueurs[:2]
print(f"Joueurs mélangés: {melange}")

# Formation d'équipes
equipe1 = melange[:3]
equipe2 = melange[3:]

print(f"Équipe 1: {equipe1}")
print(f"Équipe 2: {equipe2}")

# Tirage "aléatoire" simplifié
tire = melange[2]
print(f"Joueur tiré: {tire}")
```
