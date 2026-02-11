## Exercice 1 — Module `calculs.py`

### `calculs.py`

```python
def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return None
    return a / b
```

### `main.py`

```python
import calculs

a = float(input("Entrez un premier nombre : "))
b = float(input("Entrez un deuxième nombre : "))

print("Addition :", calculs.addition(a, b))
print("Soustraction :", calculs.soustraction(a, b))
print("Multiplication :", calculs.multiplication(a, b))

resultat = calculs.division(a, b)
if resultat is None:
    print("Division : impossible (division par zéro)")
else:
    print("Division :", resultat)
```

---

## Exercice 2 — Import partiel et alias

### `geometrie.py`

```python
import math

def aire_carre(cote):
    return cote * cote

def aire_rectangle(longueur, largeur):
    return longueur * largeur

def aire_cercle(rayon):
    return math.pi * rayon * rayon
```

### `main.py`

```python
from geometrie import aire_cercle
from geometrie import aire_rectangle as rectangle

print("Aire cercle (r=2) :", aire_cercle(2))
print("Aire rectangle (4x3) :", rectangle(4, 3))
```

---

## Exercice 3 — Module avec classe (POO)

### `vehicule.py`

```python
class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def se_decrire(self):
        return f"{self.marque} {self.modele} ({self.annee})"

    def vieillir(self):
        self.annee -= 1
```

### `main.py`

```python
from vehicule import Vehicule

v1 = Vehicule("Toyota", "Corolla", 2020)
v2 = Vehicule("Renault", "Clio", 2018)

print(v1.se_decrire())
print(v2.se_decrire())

v1.vieillir()
print("Après vieillissement :", v1.se_decrire())
```

---

## Exercice 4 — Premier package `utilitaires`

### Structure

```
utilitaires/
├── __init__.py
├── texte.py
└── nombres.py
```

### `utilitaires/__init__.py`

```python
# Ce fichier peut être vide pour un début.
```

### `utilitaires/texte.py`

```python
def mettre_en_majuscule(texte):
    return texte.upper()

def compter_lettres(texte):
    return len(texte)
```

### `utilitaires/nombres.py`

```python
def est_pair(nombre):
    return nombre % 2 == 0

def est_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, nombre):
        if nombre % i == 0:
            return False
    return True
```

### `main.py`

```python
from utilitaires.texte import mettre_en_majuscule, compter_lettres
from utilitaires.nombres import est_pair, est_premier

print(mettre_en_majuscule("bonjour"))
print("Lettres :", compter_lettres("bonjour"))

print("10 est pair ?", est_pair(10))
print("7 est premier ?", est_premier(7))
```

---

## Exercice 5 — Package POO “bibliotheque”

### Structure

```
bibliotheque/
├── __init__.py
├── livre.py
└── gestion.py
```

### `bibliotheque/livre.py`

```python
class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def retourner(self):
        self.disponible = True
```

### `bibliotheque/gestion.py`

```python
from bibliotheque.livre import Livre

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, titre, auteur):
        self.livres.append(Livre(titre, auteur))

    def afficher_livres(self):
        for livre in self.livres:
            etat = "Disponible" if livre.disponible else "Emprunté"
            print(f"- {livre.titre} ({livre.auteur}) -> {etat}")
```

### `main.py`

```python
from bibliotheque.gestion import Bibliotheque

biblio = Bibliotheque()
biblio.ajouter_livre("1984", "George Orwell")
biblio.ajouter_livre("Le Petit Prince", "Antoine de Saint-Exupéry")

biblio.afficher_livres()

# Emprunt
livre0 = biblio.livres[0]
ok = livre0.emprunter()
print("Emprunt réussi ?" , ok)

biblio.afficher_livres()
```

---

## Exercice 6 — `__name__ == "__main__"`

### `test_module.py`

```python
def dire_bonjour():
    return "Bonjour !"

if __name__ == "__main__":
    print("Ce fichier est exécuté directement.")
    print(dire_bonjour())
```

### `main.py`

```python
import test_module

print("Dans main.py :", test_module.dire_bonjour())
```

---

## Exercice 7 — Challenge final (structure complète)

### `models/utilisateur.py`

```python
class Utilisateur:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email

    def __str__(self):
        return f"{self.nom} <{self.email}>"
```

### `utils/validations.py`

```python
def email_valide(email):
    return "@" in email and "." in email
```

### `services/gestion_utilisateurs.py`

```python
from models.utilisateur import Utilisateur
from utils.validations import email_valide

class GestionUtilisateurs:
    def __init__(self):
        self.utilisateurs = []

    def ajouter(self, nom, email):
        if not email_valide(email):
            return False
        self.utilisateurs.append(Utilisateur(nom, email))
        return True

    def afficher(self):
        for u in self.utilisateurs:
            print("-", u)
```

### `main.py`

```python
from services.gestion_utilisateurs import GestionUtilisateurs

gestion = GestionUtilisateurs()
gestion.ajouter("Alice", "alice@mail.com")
gestion.ajouter("Bob", "bobmail.com")  # email invalide

gestion.afficher()
```
