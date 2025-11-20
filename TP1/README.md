# Travail Pratique : Système de Gestion de Bibliothèque Personnel

## Contexte

Vous devez créer un système simple de gestion de livres pour votre bibliothèque personnelle. Ce programme permettra de suivre vos livres, leurs statuts et d'effectuer diverses opérations de gestion.

## Objectifs du TP

### Partie 1 : Initialisation et Affichage (Boucles for, listes)

Créez un système qui :

- Stocke une liste de livres avec leurs titres, auteurs et statuts (disponible/emprunté)
- Affiche tous les livres avec leurs détails
- Affiche seulement les livres disponibles

```python
# Structure suggérée pour démarrer
livres = [
    {"titre": "Harry Potter", "auteur": "JK Rowling", "statut": "disponible"},
    {"titre": "1984", "auteur": "George Orwell", "statut": "emprunté"},
    # Ajoutez 3-4 livres supplémentaires...
]
```

### Partie 2 : Recherche et Filtrage (Boucles, conditions)

Implémentez les fonctionnalités de recherche :

- Recherche par titre (contient une chaîne)
- Recherche par auteur
- Affichage des livres empruntés
- Comptage des livres par statut

### Partie 3 : Gestion des Emprunts (Boucles while, break/continue)

Créez un système d'emprunt avec :

- Boucle principale de gestion
- Option pour emprunter un livre (change le statut)
- Option pour retourner un livre
- Vérification de la disponibilité avant emprunt
- Limite d'emprunts simultanés

### Partie 4 : Statistiques et Rapports (Range, enumerate)

Générez des rapports :

- Liste numérotée de tous les livres
- Top 3 des livres (simulation)
- Statistiques générales

## Défis Optionnels (Bonus)

### Défi 1 : Système de Notation

Ajoutez une note sur 5 à chaque livre et implémentez :

- Affichage des livres bien notés (≥4/5)
- Calcul de la note moyenne

### Défi 2 : Recherche Avancée

Recherche combinée par multiple critères (titre ET auteur, etc.)

### Défi 3 : Sauvegarde de Session

Simulez une sauvegarde en affichant un résumé formaté

## Contraintes Techniques

### Obligatoires :

- Utilisation de boucles `for` et `while`
- Utilisation de `break`, `continue`, `pass`
- Utilisation de `range()` et `enumerate()`
- Structures conditionnelles (`if`, `elif`, `else`)
- Opérateurs logiques

### Interdits :

- Fonctions personnalisées
- Classes
- Importation de modules externes

## Exemple de Sortie Attendue

```txt
=== MA BIBLIOTHÈQUE PERSONNELLE ===

1. Livres disponibles :
   1. Harry Potter - JK Rowling [DISPONIBLE]
   2. Le Seigneur des Anneaux - Tolkien [DISPONIBLE]

2. Recherche par auteur 'Rowling' :
   - Harry Potter

3. Statistiques :
   Total livres: 5
   Disponibles: 3
   Empruntés: 2

4. Livres bien notés (4+):
   - Harry Potter ★★★★☆
```

## Conseils de Démarrage

1. **Commencez simple** : Créez d'abord la liste de livres
2. **Testez chaque partie** : Vérifiez l'affichage avant d'ajouter la gestion
3. **Utilisez des variables claires** : `livre_disponible`, `recherche_trouvee`, etc.
4. **Gérez les erreurs** : Livre non trouvé, déjà emprunté, etc.
