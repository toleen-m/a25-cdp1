# Exercices sur les Classes en Python

## Exercice 1 : Introduction aux Classes

### 1.1 : Code à Développer

Créez une classe `Personne` très simple avec seulement une méthode `se_presenter()` qui affiche "Je suis une personne".

### 1.2 : Code à Finaliser

```python
# Complétez cette classe
class ______:
    def dire_bonjour(self):
        print("Bonjour !")

# Créez une instance et appelez la méthode
personne = ______
personne.______
```

### 1.3 : Code à Corriger

```python
# Ce code contient des erreurs de syntaxe de classe
class Animal
    def faire_du_bruit()
        print("Bruit d'animal")

mon_animal = Animal()
mon_animal.faire_du_bruit
```

## Exercice 2 : La méthode **init**()

### 2.1 : Code à Développer

Créez une classe `Livre` avec `__init__()` qui initialise `titre` et `auteur`. Créez deux livres différents.

### 2.2 : Code à Finaliser

```python
class Etudiant:
    def ______(self, nom, age):
        self.nom = ______
        self.age = ______

# Créez un étudiant
etudiant1 = Etudiant("Alice", 20)
print(f"Nom: {______}")
```

### 2.3 : Code à Corriger

```python
class Voiture:
    def init(self, marque, modele):
        marque = marque
        modele = modele

voiture = Voiture("Toyota", "Corolla")
print(voiture.marque)
```

## Exercice 3 : Méthodes d'Instance

### 3.1 : Code à Développer

Créez une classe `CompteBancaire` avec :

- `__init__()` qui initialise `titulaire` et `solde` (par défaut 0)
- `deposer(montant)` qui ajoute au solde
- `retirer(montant)` qui retire si possible
- `afficher_solde()` qui affiche le solde

### 3.2 : Code à Finaliser

```python
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calculer_perimetre(self):
        return ______

    def calculer_surface(self):
        return ______

# Test
rect = Rectangle(5, 3)
print(f"Périmètre: {rect.calculer_perimetre()}")
print(f"Surface: {rect.calculer_surface()}")
```

### 3.3 : Code à Corriger

```python
class Calculatrice:
    def __init__(self):
        self.resultat = 0

    def addition(self, a, b):
        resultat = a + b

    def soustraction(a, b):
        self.resultat = a - b

calc = Calculatrice()
calc.addition(5, 3)
print(calc.resultat)
```

## Exercice 4 : Variables et Méthodes de Classe

### 4.1 : Code à Développer

Créez une classe `Employe` avec :

- Variable de classe `nombre_employes` qui compte les employés
- `__init__()` qui incrémente le compteur
- Méthode de classe `afficher_nombre()` qui affiche le total

### 4.2 : Code à Finaliser

```python
class Produit:
    # Variable de classe pour le taux de TVA
    taux_tva = ______

    def __init__(self, nom, prix_ht):
        self.nom = nom
        self.prix_ht = prix_ht

    @classmethod
    def changer_tva(cls, nouveau_taux):
        ______

    def prix_ttc(self):
        return ______

# Test
Produit.changer_tva(0.2)
p = Produit("Livre", 20)
print(f"Prix TTC: {p.prix_ttc()}")
```

### 4.3 : Code à Corriger

```python
class Mathematic:
    pi = 3.14159

    def __init__(self):
        self.pi = 22/7

    @staticmethod
    def carre(x):
        self.result = x * x
        return self.result

math = Mathematic()
print(math.pi)
print(math.carre(5))
```

## Exercice 5 : Méthodes Statiques

### 5.1 : Code à Développer

Créez une classe `Utilitaire` avec des méthodes statiques :

- `est_pair(nombre)` retourne True si pair
- `celsius_vers_fahrenheit(celsius)` fait la conversion
- `est_email_valide(email)` vérifie basiquement un email

### 5.2 : Code à Finaliser

```python
class Validateur:
    @staticmethod
    def ______(nombre):
        return nombre > 0

    @staticmethod
    def ______(texte):
        return len(texte) >= 3

# Utilisation sans instance
if Validateur.______(10):
    print("Nombre valide")
```

### 5.3 : Code à Corriger

```python
class Formateur:
    @staticmethod
    def majuscule(texte):
        return texte.upper()

    @classmethod
    def minuscule(cls, texte):
        return texte.lower()

# Problème ici
resultat = Formateur.majuscule("test")
print(resultat)
resultat2 = Formateur.minuscule("TEST")
print(resultat2)
```

## Exercice 6 : Propriétés Publiques et Privées

### 6.1 : Code à Développer

Créez une classe `CompteSecre` avec :

- Attribut privé `__code_secret`
- Méthode publique `verifier_code(code)` pour vérifier
- Méthode pour changer le code (avec vérification)

### 6.2 : Code à Finaliser

```python
class Temperature:
    def __init__(self, celsius):
        self.______ = celsius  # Privé

    def get_celsius(self):
        return ______

    def set_celsius(self, valeur):
        if valeur < -273.15:
            print("Température impossible")
        else:
            ______

temp = Temperature(25)
print(temp.______)  # Devrait utiliser getter
```

### 6.3 : Code à Corriger

```python
class Compte:
    def __init__(self, solde):
        self.__solde = solde

    def afficher_solde(self):
        print(f"Solde: {solde}")

    def __verifier_solde(self):
        return self.__solde > 0

compte = Compte(100)
print(compte.__solde)
compte.__verifier_solde()
```

## Exercice 7 : Projets Complets

### 7.1 : Système d'Inventaire (à Développer)

Créez une classe `Produit` et une classe `Inventaire` :

- `Produit` : nom, prix, quantité
- `Inventaire` : liste de produits, méthodes pour ajouter, supprimer, chercher, calculer valeur totale

### 7.2 : Gestion de Cours (à Finaliser)

```python
class Etudiant:
    def __init__(self, nom):
        self.nom = nom
        self.notes = []

    def ajouter_note(self, note):
        ______

    def moyenne(self):
        ______

class Cours:
    def __init__(self, nom):
        self.nom = nom
        self.etudiants = []

    def inscrire(self, etudiant):
        ______

    def meilleur_etudiant(self):
        ______

# Test
cours = Cours("Python")
alice = Etudiant("Alice")
cours.inscrire(alice)
```

### 7.3 : Jeu de Cartes (à Corriger)

```python
class Carte:
    def __init__(self, valeur, couleur):
        valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{valeur} de {couleur}"

class Jeu:
    def __init__(self):
        self.cartes = []
        couleurs = ["Coeur", "Carreau", "Pique", "Trèfle"]
        for couleur in couleurs:
            for i in range(1, 14):
                self.cartes.append(Carte(i, couleur))

    def melanger(self):
        # Simulation simple
        import random
        random.shuffle(self.cartes)

jeu = Jeu()
print(jeu.cartes[0])
```
