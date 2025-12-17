# Exercice Progressif : Création d'une Classe Animal avec Héritage

## Étape 1 : Création de base de la classe Animal

### Code à Développer

```python
# 1. Créez une classe Animal avec:
#    - Attributs: nom, age
#    - Méthode __init__ pour initialiser
#    - Méthode manger() qui affiche "[nom] mange"
#    - Méthode dormir() qui affiche "[nom] dort"

class Animal:
    # À compléter
```

## Étape 2 : Ajout de méthodes spéciales

### Code à Développer

```python
# 2. Modifiez la classe Animal pour ajouter:
#    - Méthode __str__ qui retourne "Animal: [nom], âge: [age] ans"
#    - Méthode __eq__ qui compare deux animaux par nom et age
#    - Propriété get_age et set_age avec validation (age >= 0)

class Animal:
    # Modifier la classe précédente
```

## Étape 3 : Héritage simple - Classe Chien

### Code à Développer

```python
# 3. Créez une classe Chien qui hérite de Animal
#    - Ajoutez l'attribut race
#    - Surchargez __init__ pour inclure race
#    - Ajoutez méthode aboyer() qui affiche "[nom] aboie: Woof!"
#    - Surchargez __str__ pour inclure la race

class Chien(Animal):
    # À compléter
```

## Étape 4 : Héritage simple - Classe Chat

### Code à Développer

```python
# 4. Créez une classe Chat qui hérite de Animal
#    - Ajoutez l'attribut couleur
#    - Surchargez __init__ pour inclure couleur
#    - Ajoutez méthode miauler() qui affiche "[nom] miaule: Miaou!"
#    - Surchargez __str__ pour inclure la couleur

class Chat(Animal):
    # À compléter
```

## Étape 5 : Héritage multiple - AnimalDomestique

### Code à Développer

```python
# 5. Créez des classes pour l'héritage multiple:
#    - Classe Compagnon (attribut proprietaire, méthode jouer())
#    - Classe AnimalDomestique qui hérite de Animal et Compagnon

class Compagnon:
    # À compléter

class AnimalDomestique(Animal, Compagnon):
    # À compléter
```

## Étape 6 : Utilisation et tests

### Code à Développer

```python
# 6. Testez toutes vos classes:
#    - Créez des instances d'Animal, Chien, Chat, AnimalDomestique
#    - Testez les méthodes
#    - Testez les méthodes spéciales (__str__, __eq__)
#    - Testez l'héritage (méthodes parentes accessibles)

# Code de test à écrire
```
