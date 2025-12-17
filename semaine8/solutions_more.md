# Solution Pas à Pas

## Étape 1 : Solution

```python
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def manger(self):
        print(f"{self.nom} mange")

    def dormir(self):
        print(f"{self.nom} dort")

# Test
animal1 = Animal("Rex", 3)
animal1.manger()  # Rex mange
animal1.dormir()  # Rex dort
```

## Étape 2 : Solution

```python
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self._age = age  # Privé pour la validation

    def manger(self):
        print(f"{self.nom} mange")

    def dormir(self):
        print(f"{self.nom} dort")

    def __str__(self):
        return f"Animal: {self.nom}, âge: {self.age} ans"

    def __eq__(self, autre):
        if not isinstance(autre, Animal):
            return False
        return self.nom == autre.nom and self.age == autre.age

    # Propriété pour l'âge avec validation
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, valeur):
        if valeur >= 0:
            self._age = valeur
        else:
            print("Âge doit être positif")

# Test
animal1 = Animal("Rex", 3)
animal2 = Animal("Rex", 3)
animal3 = Animal("Max", 5)

print(animal1)  # Animal: Rex, âge: 3 ans
print(animal1 == animal2)  # True
print(animal1 == animal3)  # False

animal1.age = 4
print(animal1)  # Animal: Rex, âge: 4 ans
animal1.age = -1  # Affiche: Âge doit être positif
```

## Étape 3 : Solution

```python
class Chien(Animal):
    def __init__(self, nom, age, race):
        super().__init__(nom, age)
        self.race = race

    def aboyer(self):
        print(f"{self.nom} aboie: Woof!")

    def __str__(self):
        # Appelle __str__ du parent et ajoute la race
        parent_str = super().__str__()
        return f"{parent_str}, race: {self.race}"

# Test
chien1 = Chien("Rex", 3, "Labrador")
chien1.manger()    # Hérité: Rex mange
chien1.aboyer()    # Spécifique: Rex aboie: Woof!
print(chien1)      # Animal: Rex, âge: 3 ans, race: Labrador
```

## Étape 4 : Solution

```python
class Chat(Animal):
    def __init__(self, nom, age, couleur):
        super().__init__(nom, age)
        self.couleur = couleur

    def miauler(self):
        print(f"{self.nom} miaule: Miaou!")

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str}, couleur: {self.couleur}"

# Test
chat1 = Chat("Misty", 2, "noir")
chat1.dormir()     # Hérité: Misty dort
chat1.miauler()    # Spécifique: Misty miaule: Miaou!
print(chat1)       # Animal: Misty, âge: 2 ans, couleur: noir
```

## Étape 5 : Solution

```python
class Compagnon:
    def __init__(self, proprietaire):
        self.proprietaire = proprietaire

    def jouer(self):
        print(f"Je joue avec {self.proprietaire}")

class AnimalDomestique(Animal, Compagnon):
    def __init__(self, nom, age, proprietaire):
        # Appel aux deux parents
        Animal.__init__(self, nom, age)
        Compagnon.__init__(self, proprietaire)

    def __str__(self):
        animal_str = Animal.__str__(self)
        return f"{animal_str}, propriétaire: {self.proprietaire}"

# Test
animal_dom = AnimalDomestique("Buddy", 4, "Alice")
animal_dom.manger()   # Hérité de Animal: Buddy mange
animal_dom.jouer()    # Hérité de Compagnon: Je joue avec Alice
print(animal_dom)     # Animal: Buddy, âge: 4 ans, propriétaire: Alice
```

## Étape 6 : Solution complète avec tests

```python
# Code complet avec toutes les classes et tests

class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self._age = age

    def manger(self):
        print(f"{self.nom} mange")

    def dormir(self):
        print(f"{self.nom} dort")

    def __str__(self):
        return f"Animal: {self.nom}, âge: {self.age} ans"

    def __eq__(self, autre):
        if not isinstance(autre, Animal):
            return False
        return self.nom == autre.nom and self.age == autre.age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, valeur):
        if valeur >= 0:
            self._age = valeur
        else:
            print("Âge doit être positif")

class Chien(Animal):
    def __init__(self, nom, age, race):
        super().__init__(nom, age)
        self.race = race

    def aboyer(self):
        print(f"{self.nom} aboie: Woof!")

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str}, race: {self.race}"

class Chat(Animal):
    def __init__(self, nom, age, couleur):
        super().__init__(nom, age)
        self.couleur = couleur

    def miauler(self):
        print(f"{self.nom} miaule: Miaou!")

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str}, couleur: {self.couleur}"

class Compagnon:
    def __init__(self, proprietaire):
        self.proprietaire = proprietaire

    def jouer(self):
        print(f"Je joue avec {self.proprietaire}")

class AnimalDomestique(Animal, Compagnon):
    def __init__(self, nom, age, proprietaire):
        Animal.__init__(self, nom, age)
        Compagnon.__init__(self, proprietaire)

    def __str__(self):
        animal_str = Animal.__str__(self)
        return f"{animal_str}, propriétaire: {self.proprietaire}"

# ===== TESTS COMPLETS =====

print("=== TEST CLASSE ANIMAL ===")
animal1 = Animal("Rex", 3)
animal2 = Animal("Rex", 3)
animal3 = Animal("Max", 5)

print(animal1)  # Animal: Rex, âge: 3 ans
print(f"animal1 == animal2: {animal1 == animal2}")  # True
print(f"animal1 == animal3: {animal1 == animal3}")  # False

animal1.manger()   # Rex mange
animal1.dormir()   # Rex dort

print("\n=== TEST CLASSE CHIEN ===")
chien1 = Chien("Rex", 3, "Labrador")
chien2 = Chien("Max", 2, "Berger")

print(chien1)      # Animal: Rex, âge: 3 ans, race: Labrador
chien1.manger()    # Rex mange (hérité)
chien1.aboyer()    # Rex aboie: Woof! (spécifique)
print(f"chien1 est un Animal: {isinstance(chien1, Animal)}")  # True

print("\n=== TEST CLASSE CHAT ===")
chat1 = Chat("Misty", 2, "noir")
print(chat1)       # Animal: Misty, âge: 2 ans, couleur: noir
chat1.dormir()     # Misty dort (hérité)
chat1.miauler()    # Misty miaule: Miaou! (spécifique)

print("\n=== TEST HERITAGE MULTIPLE ===")
animal_dom = AnimalDomestique("Buddy", 4, "Alice")
print(animal_dom)  # Animal: Buddy, âge: 4 ans, propriétaire: Alice
animal_dom.manger()   # Buddy mange (de Animal)
animal_dom.jouer()    # Je joue avec Alice (de Compagnon)
print(f"MRO: {AnimalDomestique.__mro__}")  # Ordre de résolution des méthodes

print("\n=== TEST POLYMORPHISME ===")
animaux = [animal1, chien1, chat1, animal_dom]

for animal in animaux:
    print(f"{animal.nom}: ", end="")
    animal.manger()  # Chaque animal mange à sa manière (tous utilisent la même méthode)

    # Vérification du type pour appeler les méthodes spécifiques
    if isinstance(animal, Chien):
        animal.aboyer()
    elif isinstance(animal, Chat):
        animal.miauler()
    elif isinstance(animal, AnimalDomestique):
        animal.jouer()

print("\n=== TEST SETTER AGE ===")
animal1.age = 5
print(f"Nouvel âge de {animal1.nom}: {animal1.age} ans")
animal1.age = -1  # Affiche: Âge doit être positif
print(f"Âge inchangé: {animal1.age} ans")
```

## Points Clés Appris :

1. **Classe de base** : Création avec `__init__`, méthodes simples
2. **Méthodes spéciales** : `__str__` pour l'affichage, `__eq__` pour la comparaison
3. **Propriétés** : Utilisation de `@property` pour la validation
4. **Héritage simple** : `class Chien(Animal)` avec `super()`
5. **Surcharge** : Redéfinition de `__str__` dans les classes enfants
6. **Héritage multiple** : `class AnimalDomestique(Animal, Compagnon)`
7. **Polymorphisme** : Traitement uniforme d'objets de types différents

Cet exercice couvre progressivement tous les aspects fondamentaux de la POO en Python.
