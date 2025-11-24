# Exercices sur les Listes en Python

## Exercice 1 : Index et Accès aux Éléments

### 1.1 : Accès par index

Soit la liste `nombres = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]`. Accédez aux éléments suivants :

- Premier élément
- Dernier élément
- 5ème élément
- Avant-dernier élément

### 1.2 : Slicing de liste

Avec la même liste, extrayez :

- Les 3 premiers éléments
- Les 3 derniers éléments
- Du 3ème au 7ème élément
- Un élément sur deux
- La liste inversée

### 1.3 : Modification par index

Modifiez la liste `fruits = ["pomme", "banane", "orange"]` pour :

- Remplacer "banane" par "kiwi"
- Changer le dernier fruit en "ananas"
- Ajouter "fraise" à la fin

## Exercice 2 : Décompactage (Unpacking)

### 2.1 : Décompactage basique

Décompactez la liste `coordonnees = [45.5, -73.5, 100]` dans trois variables : `latitude`, `longitude`, `altitude`.

### 2.2 : Décompactage partiel

Avec `donnees = ["Alice", 25, "Paris", "ingénieure", "python"]`, décompactez seulement le nom et l'âge.

### 2.3 : Échange de variables

Utilisez le décompactage pour échanger les valeurs de `a = 5` et `b = 10`.

## Exercice 3 : Opérations et Copies

### 3.1 : Concaténation et répétition

Soit `liste1 = [1, 2, 3]` et `liste2 = [4, 5, 6]` :

- Concaténez les deux listes
- Répétez `liste1` trois fois
- Ajoutez `liste2` à `liste1`

### 3.2 : Copies de listes

Avec `originale = [[1, 2], [3, 4]]`, créez :

- Une référence
- Une copie superficielle
- Observez les différences après modification

### 3.3 : Comparaison de listes

Comparez `[1, 2, 3]` avec `[3, 2, 1]` et avec `[1, 2, 3]` en utilisant `==` et `is`.

## Exercice 4 : Fonctions Natives et Ajout d'Éléments

### 4.1 : Fonctions de base

Pour `valeurs = [15, 2, 8, 20, 5]`, utilisez :

- `len()`, `max()`, `min()`, `sum()`
- `sorted()` sans modifier l'originale

### 4.2 : Ajout d'éléments

Avec `liste = ["a", "b"]`, ajoutez des éléments en utilisant :

- `append()`
- `insert()`
- `extend()`

### 4.3 : Conversion depuis string

Convertissez la string `"python"` en liste de caractères, puis `"1,2,3,4,5"` en liste d'entiers.

## Exercice 5 : Suppression d'Éléments

### 5.1 : Suppression par valeur et index

Avec `elements = ["a", "b", "c", "d", "e", "a"]` :

- Supprimez le premier "a"
- Supprimez l'élément à l'index 2
- Supprimez le dernier élément

### 5.2 : Nettoyage de liste

Soit `donnees = [1, None, "texte", 0, "", [], 42, False]`. Supprimez toutes les valeurs "fausses".

### 5.3 : Vidage et extraction

Avec `liste = [10, 20, 30, 40, 50]` :

- Extrayez et supprimez le dernier élément
- Extrayez et supprimez le premier élément
- Videz complètement la liste

## Exercice 6 : Recherche dans les Listes

### 6.1 : Recherche basique

Dans `nombres = [15, 8, 23, 42, 8, 15, 8]` :

- Trouvez le premier index de 8
- Comptez les occurrences de 15
- Vérifiez si 42 est dans la liste

### 6.2 : Recherche conditionnelle

Avec `ages = [25, 17, 30, 16, 22, 19]`, trouvez :

- Tous les ages >= 18
- L'index du premier majeur

### 6.3 : Recherche d'extremums

Pour `temperatures = [22, 18, 25, 20, 17, 23, 19]`, trouvez :

- La température maximale et son index
- La température minimale et son index

## Exercice 7 : Tri des Listes

### 7.1 : Tri simple

Triez `nombres = [64, 34, 25, 12, 22, 11, 90]` :

- Par ordre croissant
- Par ordre décroissant

### 7.2 : Tri de strings

Triez `mots = ["banane", "pomme", "orange", "kiwi", "ananas"]` :

- Par ordre alphabétique
- Par longueur de mot

### 7.3 : Tri personnalisé

Avec `etudiants = [("Alice", 18), ("Bob", 20), ("Charlie", 17)]`, triez :

- Par age croissant
- Par nom alphabétique

## Exercice 8 : Projets Complets

### 8.1 : Gestion de panier

Créez un système de panier d'achat avec :

- Ajout de produits
- Suppression de produits
- Calcul du total
- Vidage du panier

### 8.2 : Système de notes

Gérez une liste de notes avec :

- Ajout de notes
- Suppression de la pire note
- Calcul de la moyenne
- Liste des notes au-dessus de la moyenne

### 8.3 : Mélange et tirage

Créez un système pour :

- Mélanger une liste
- Tirer des éléments aléatoirement
- Former des équipes équilibrées
