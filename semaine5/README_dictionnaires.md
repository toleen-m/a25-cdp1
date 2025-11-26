# Exercices sur les Dictionnaires en Python

## Exercice 1 : Déclaration et Création

### 1.1 : Déclaration basique (À compléter)

```python
# Créez un dictionnaire représentant une personne avec:
# - nom: "Dupont"
# - age: 25
# - ville: "Paris"
personne = ______

print(personne)
```

### 1.2 : Depuis une liste de tuples (À compléter)

```python
# Créez un dictionnaire à partir de cette liste de tuples
donnees = [("nom", "Alice"), ("age", 30), ("metier", "ingenieure")]
personne = ______

print(personne)
```

### 1.3 : Avec dict() (Erreurs à corriger)

```python
# Ce code devrait créer un dictionnaire mais contient des erreurs
etudiant = dict(
    nom = "Martin"
    prenom: "Pierre"
    notes = [15, 18, 12]
)

print(etudiant)
```

## Exercice 2 : Accès aux Éléments

### 2.1 : Accès simple (À compléter)

```python
livre = {
    "titre": "1984",
    "auteur": "George Orwell",
    "annee": 1949,
    "pages": 328
}

# Accédez au titre et à l'année
titre = ______
annee = ______

print(f"'{titre}' publié en {annee}")
```

### 2.2 : Accès sécurisé (Erreurs à corriger)

```python
# Ce code génère une erreur, corrigez-le
config = {"host": "localhost", "port": 8080}

print(f"Host: {config['host']}")
print(f"Database: {config['database']}")
print(f"Port: {config.get('port')}")
```

### 2.3 : Valeurs par défaut (À compléter)

```python
utilisateur = {"nom": "Alice", "age": 25}

# Utilisez get() avec valeur par défaut
ville = ______
profession = ______

print(f"Ville: {ville}")
print(f"Profession: {profession}")
```

## Exercice 3 : Modifications

### 3.1 : Ajout et modification (À compléter)

```python
inventaire = {"pommes": 10, "bananes": 5}

# Ajoutez "oranges" avec 8 unités
______
# Modifiez les bananes à 7 unités
______
# Ajoutez 3 aux pommes existantes
______

print(inventaire)
```

### 3.2 : update() (Erreurs à corriger)

```python
# Ce code ne fait pas ce qui est attendu, corrigez-le
base = {"a": 1, "b": 2}
nouveau = {"b": 3, "c": 4}

base = nouveau

print(base)  # Devrait être {"a": 1, "b": 3, "c": 4}
```

### 3.3 : setdefault() (À compléter)

```python
# Utilisez setdefault() pour initialiser des valeurs si absentes
stats = {"visites": 100}

# Si 'telechargements' n'existe pas, initialisez à 0
______
# Si 'visites' existe, ne changez pas
______

print(stats)
```

## Exercice 4 : Suppression

### 4.1 : Suppression basique (À compléter)

```python
donnees = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# Supprimez la clé 'c' avec del
______
# Supprimez 'd' avec pop() et récupérez la valeur
valeur_d = ______
# Supprimez et retournez un élément arbitraire
element = ______

print(f"Donnees: {donnees}")
print(f"Valeur de d: {valeur_d}")
print(f"Element supprimé: {element}")
```

### 4.2 : Nettoyage conditionnel (Erreurs à corriger)

```python
# Ce code devrait supprimer toutes les valeurs None mais contient des erreurs
produits = {
    "livre": 15,
    "stylo": None,
    "cahier": 8,
    "gomme": None,
    "regle": 12
}

for cle in produits:
    if produits[cle] == None:
        del cle

print(produits)
```

### 4.3 : pop() avec défaut (À compléter)

```python
config = {"theme": "sombre", "langue": "fr"}

# Supprimez 'theme' avec valeur par défaut "clair"
ancien_theme = ______
# Essayez de supprimer 'volume' avec défaut 50
volume = ______

print(f"Ancien theme: {ancien_theme}")
print(f"Volume: {volume}")
```

## Exercice 5 : Copies

### 5.1 : Copie superficielle (À compléter)

```python
original = {"a": 1, "b": [2, 3], "c": {"d": 4}}

# Créez une copie superficielle
copie = ______

# Modifiez la copie
copie["a"] = 10
copie["b"].append(4)

print(f"Original: {original}")
print(f"Copie: {copie}")
```

### 5.2 : Deepcopy (Erreurs à corriger)

```python
# Ce code ne crée pas une vraie copie indépendante, corrigez-le
import copy

niveau1 = {"donnees": [1, 2, 3], "config": {"resolu": False}}
niveau2 = niveau1.copy()

niveau2["donnees"].append(4)
niveau2["config"]["resolu"] = True

print(f"Niveau 1: {niveau1}")
print(f"Niveau 2: {niveau2}")
```

### 5.3 : Comparaison de copies (À compléter)

```python
d1 = {"a": 1, "b": 2}
d2 = ______  # Créez une copie de d1
d3 = d1

print(f"d1 == d2: {d1 == d2}")
print(f"d1 is d2: {d1 is d2}")
print(f"d1 is d3: {d1 is d3}")
```

## Exercice 6 : Parcours

### 6.1 : Parcours des clés (À compléter)

```python
employe = {"nom": "Alice", "age": 30, "poste": "Developpeur", "salaire": 50000}

# Parcourez et affichez toutes les clés
______

# Vérifiez si 'experience' est une clé
if ______:
    print("Experience trouvée")
else:
    print("Experience non trouvée")
```

### 6.2 : Parcours des valeurs (Erreurs à corriger)

```python
# Ce code devrait calculer la somme des valeurs mais contient des erreurs
notes = {"math": 15, "francais": 12, "histoire": 18, "sport": 16}

total = 0
for matiere in notes:
    total += matiere

print(f"Moyenne: {total / len(notes)}")
```

### 6.3 : Parcours des items (À compléter)

```python
inventaire = {"pommes": 10, "bananes": 5, "oranges": 8, "kiwis": 3}

# Affichez chaque produit avec sa quantité
______

# Trouvez le produit avec la plus grande quantité
max_produit = ______
max_quantite = ______

print(f"Produit le plus stocké: {max_produit} ({max_quantite} unités)")
```

## Exercice 7 : Méthodes Utiles

### 7.1 : keys(), values(), items() (À compléter)

```python
config = {"host": "localhost", "port": 8080, "debug": True}

# Obtenez la liste des clés
cles = ______
# Obtenez la liste des valeurs
valeurs = ______
# Obtenez la liste des items (clé, valeur)
items = ______

print(f"Clés: {cles}")
print(f"Valeurs: {valeurs}")
print(f"Items: {items}")
```

### 7.2 : fromkeys() (Erreurs à corriger)

```python
# Ce code devrait créer un dictionnaire avec des valeurs par défaut
cles = ["nom", "age", "ville"]
valeur_par_defaut = "inconnu"

resultat = dict.fromkeys(valeur_par_defaut, cles)

print(resultat)
```

### 7.3 : Comprehension de dictionnaire (À compléter)

```python
nombres = [1, 2, 3, 4, 5]

# Créez un dict {nombre: carre} avec compréhension
carres = ______

print(carres)
```
