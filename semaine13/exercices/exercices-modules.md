# Exercice 1 — Créer et utiliser un module simple

## Énoncé

Créez un module nommé `calculs.py` qui contient les fonctions suivantes :

- une fonction `addition(a, b)`
- une fonction `soustraction(a, b)`
- une fonction `multiplication(a, b)`
- une fonction `division(a, b)`

Ensuite, créez un fichier `main.py` qui :

- importe le module `calculs`
- demande à l'utilisateur deux nombres
- affiche le résultat des quatre opérations

## Structure attendue

```
projet/
│
├── calculs.py
└── main.py
```

---

# Exercice 2 — Import partiel et alias

## Énoncé

Créez un module `geometrie.py` contenant :

- `aire_carre(cote)`
- `aire_rectangle(longueur, largeur)`
- `aire_cercle(rayon)`

Ensuite, dans `main.py` :

- importez uniquement `aire_cercle`
- importez `aire_rectangle` avec un alias `rectangle`
- utilisez les fonctions

## Contraintes

```
from module import fonction
from module import fonction as alias
```

---

# Exercice 3 — Créer un module contenant une classe (POO)

## Énoncé

Créez un module `vehicule.py` contenant une classe `Vehicule` :

Attributs :

- marque
- modele
- annee

Méthodes :

- se_decrire()
- vieillir()

Ensuite, créez `main.py` qui :

- importe la classe
- crée plusieurs véhicules
- utilise leurs méthodes

---

# Exercice 4 — Créer son premier package

## Énoncé

Créez le package suivant :

```
utilitaires/
│
├── __init__.py
├── texte.py
└── nombres.py
```

### texte.py

Créer les fonctions :

- mettre_en_majuscule(texte)
- compter_lettres(texte)

### nombres.py

Créer les fonctions :

- est_pair(nombre)
- est_premier(nombre)

Ensuite, créez un fichier `main.py` qui utilise ces fonctions.

---

# Exercice 5 — Package orienté objet (mini projet)

## Énoncé

Créez le package :

```
bibliotheque/
│
├── __init__.py
├── livre.py
└── gestion.py
```

### livre.py

Créer la classe :

```
Livre
- titre
- auteur
- disponible
```

Méthodes :

```
emprunter()
retourner()
```

### gestion.py

Créer la classe :

```
Bibliotheque
```

Attribut :

```
liste de livres
```

Méthodes :

```
ajouter_livre()
afficher_livres()
```

### main.py

Créer une bibliothèque et tester les fonctionnalités.

---

# Exercice 6 — Comprendre **name** == "**main**"

## Énoncé

Créez un module `test_module.py` contenant :

- une fonction
- un print dans un bloc :

```
if __name__ == "__main__":
```

Puis importez ce module dans `main.py`.

---

# Exercice 7 — Challenge final (structure complète)

Créer :

```
mon_projet/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   └── utilisateur.py
│
├── services/
│   ├── __init__.py
│   └── gestion_utilisateurs.py
│
└── utils/
    ├── __init__.py
    └── validations.py
```

---

# Bonus - Exercice de débogage

```
import calcul
calcul.addition(5,3)
```

Corrigez ce code !
