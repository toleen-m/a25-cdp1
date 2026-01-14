# Exercices de Révision (2h)

## Partie 1 : Problèmes Inversés (20 min)

### Exercice 1.1 : Devine le Code

```python
# Sans exécuter, devine la sortie de ce code mystère

def mystere(a, b):
    result = []
    for i in range(len(a)):
        if a[i] not in b:
            result.append(a[i])
    return result

liste1 = [1, 2, 3, 4, 2, 3, 5]
liste2 = [2, 3, 6]
print(mystere(liste1, liste2))
```

### Exercice 1.2 : Trouve l'Erreur

```python
# Ce code devrait calculer les statistiques mais contient 3 erreurs
def statistiques(temperatures):
    max = temperatures[0]
    min = temperatures[0]

    for temp in temperatures:
        if temp > max
            max = temp
        if temp < min
            min = temp

    moyenne = sum(temperatures) / temperatures.len()

    return (moyenne, max, min)

# Corrigez les 3 erreurs
```

## Partie 2 : Reconstruction (25 min)

### Exercice 2.1 : À Partir du Comportement

```python
# Écrivez le code qui produit exactement cette sortie:
"""
=== CALCULATRICE ===
5 + 3 = 8
5 - 3 = 2
5 * 3 = 15
5 / 3 = 1.666...
Moyenne: 6.5
"""

# Votre code doit utiliser:
# - Des variables
# - Des calculs
# - Un formatage de strings
```

### Exercice 2.2 : Puzzle de Classes

```python
# On vous donne seulement la sortie, recréez les classes
"""
Création de Compte: Alice, solde: 100
Dépôt: 50, nouveau solde: 150
Retrait: 30, nouveau solde: 120
Retrait impossible: 200 demandé, solde: 120
Nombre de comptes créés: 2
"""

# Écrivez la classe CompteBancaire qui produit cette sortie
```

## Partie 3 : Problèmes Hybrides (30 min)

### Exercice 3.1 : Filtre Personnalisé

```python
"""
Créez une fonction filtre_complexe qui:
1. Prend une liste de nombres ET une liste de conditions
2. Chaque condition est un tuple (opérateur, valeur)
   Ex: [(">", 10), ("<", 50), ("%", 2)] pour >10 ET <50 ET pair
3. Retourne les nombres qui satisfont TOUTES les conditions
4. Opérateurs supportés: >, <, >=, <=, ==, % (pair si %2==0)

Exemple:
nombres = [5, 12, 15, 20, 25, 30, 35]
conditions = [(">", 10), ("<", 30), ("%", 2)]
Résultat: [12, 20] (car >10 ET <30 ET pair)
"""
```

### Exercice 3.2 : Générateur de Profils

```python
"""
Créez un système qui génère des profils aléatoires:
1. Classe Personne: nom, age, profession, ville
2. Liste de noms prédéfinis: ["Alice", "Bob", "Charlie", "Diana"]
3. Liste de professions: ["Dev", "Designer", "Manager", "Testeur"]
4. Liste de villes: ["Montréal", "Toronto", "Vancouver", "Québec"]
5. Méthode generer_personne() qui crée une personne aléatoire
6. Méthode generer_groupe(n) qui crée n personnes uniques
7. Utilisez des sets pour éviter les doublons complets
"""
```

## Partie 4 : Défis Algorithmiques (45 min)

### Exercice 4.1 : Système de Notation Intelligent

```python
"""
Créez un système de notation qui:
1. Classe Etudiant: nom, liste_notes
2. Classe Matière: nom, coefficient, liste_etudiants
3. Règles spéciales:
   - Si un étudiant a plus de 3 notes, on ignore la plus basse
   - Chaque matière a un coefficient différent
   - La note finale est arrondie à 2 décimales
   - Si coefficient > 2, la note est sur 30 sinon sur 20
4. Méthode classement() qui trie les étudiants par note finale
5. Gestion des absences (note = None)

Exemple:
maths = Matière("Maths", coefficient=3)  # Note sur 30
info = Matière("Info", coefficient=1)    # Note sur 20
"""
```

### Exercice 4.2 : Héritage Circulaire

```python
"""
Créez un système de formes géométriques avec:
1. Classe Forme: couleur, méthode aire(), méthode perimetre()
2. Classe Rectangle (hérite de Forme): longueur, largeur
3. Classe Carre (hérite de Rectangle) - un carré EST-UN rectangle
4. Classe Cercle (hérite de Forme): rayon
5. Particularités:
   - Pour Carre, longueur = largeur automatiquement
   - Si on modifie largeur d'un Carre, longueur change aussi
   - Utilisez @property et @setter
   - Forme est abstraite (aire() et perimetre() doivent être implémentés)

Test:
carre = Carre("rouge", 5)
print(carre.aire())  # 25
carre.largeur = 10
print(carre.longueur)  # Doit aussi être 10
"""
```

## Partie 5 : Projet Synthèse (30 min)

### Exercice 5.1 : Jeu "Bataille des Classes"

```python
"""
Créez un jeu où différentes classes s'affrontent:

1. Classe Personnage (abstraite):
   - nom, points_vie, force, defense
   - méthode attaquer(adversaire)
   - méthode est_vivant()

2. Classes spécialisées:
   - Guerrier: +20% force, -10% defense
   - Mage: attaques magiques (ignore 50% defense)
   - Archer: 30% chance d'esquiver une attaque

3. Classe Combat:
   - personnage1, personnage2
   - méthode demarrer() -> tours jusqu'à la mort
   - affiche les dégâts chaque tour

4. Système de niveaux:
   - Chaque victoire donne de l'XP
   - À 100 XP, niveau +1, points_vie +10, force +5

Règles:
- Dégâts = force_attaquant - (defense_defenseur / 2)
- Minimum 1 dégât par attaque
- Combat aléatoire qui commence
"""
```
