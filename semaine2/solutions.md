## Solutions Complètes

### **Exercices sur les Interpréteurs**

**Solution Exercice 1 :**

```python
# Dans l'interpréteur Python :
print("Bonjour le monde!")

# Différence :
# - Interpréteur : exécution immédiate ligne par ligne
# - Fichier .py : code sauvegardé et exécuté en entier
```

**Solution Exercice 2 :**

```python
# Dans l'interpréteur :
5 + 3          # → 8
10 - 2 * 3     # → 4 (priorité opérations)
(10 - 2) * 3   # → 24 (parenthèses changent la priorité)
```

### **Exercices sur les Messages et Commentaires**

**Solution Exercice 3 :**

```python
# Déclaration des variables
a = 5          # Premier nombre
b = 10         # Deuxième nombre

# Calcul de la somme
resultat = a + b

# Affichage du résultat
print("Le résultat de l'addition est :", resultat)
```

**Solution Exercice 4 :**

```python
"""
PRÉSENTATION PERSONNELLE
Programme : Affiche une présentation complète
Auteur : Débutant Python
"""

# Déclaration des informations personnelles
nom = "Alice"
age = 25
ville = "Paris"
profession = "Développeuse"

# Affichage de la présentation
print("=== PRÉSENTATION ===")
print("Nom :", nom)
print("Âge :", age, "ans")
print("Ville :", ville)
print("Profession :", profession)

# Message de fin
print("=== FIN DE LA PRÉSENTATION ===")
```

**Solution Exercice 5 :**

```python
# Programme d'interaction avec l'utilisateur

# Demander les informations
nom = input("Quel est votre nom ? ")
age = input("Quel est votre âge ? ")

# Afficher le message personnalisé
print("Bonjour", nom + "!", "Vous avez", age, "ans.")
print("Ravi de vous rencontrer !")
```

### **Exercices sur les Types**

**Solution Exercice 6 :**

```python
type(42)        # → <class 'int'> (entier)
type("Python")  # → <class 'str'> (chaîne de caractères)
type(3.14)      # → <class 'float'> (nombre décimal)
type(True)      # → <class 'bool'> (booléen)
type('123')     # → <class 'str'> (chaîne, pas un nombre)
```

**Solution Exercice 7 :**

```python
# Conversion en entier
nombre_texte = "100"
nombre_entier = int(nombre_texte)  # Convertit "100" en 100

# Conversion en texte
age = 25
age_texte = str(age)  # Convertit 25 en "25"

# Conversion en float
prix = "15.99"
prix_decimal = float(prix)  # Convertit "15.99" en 15.99

# Vérification
print(nombre_entier, type(nombre_entier))  # 100 <class 'int'>
print(age_texte, type(age_texte))          # 25 <class 'str'>
print(prix_decimal, type(prix_decimal))    # 15.99 <class 'float'>
```

**Solution Exercice 8 :**

```python
5 + 3.0                    # → 8.0 (int + float = float)
"Bonjour" + " " + "Monde"  # → "Bonjour Monde" (concaténation)
"10" + "5"                 # → "105" (concaténation de strings)
int("10") + int("5")       # → 15 (addition d'entiers)
```

### **Exercices Combinés**

**Solution Exercice 9 :**

```python
"""
CALCULATRICE SIMPLE
Programme : Effectue des opérations basiques
Auteur : [Ton nom]
Date : [Date]
"""

# Demander deux nombres à l'utilisateur
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

# Afficher les résultats des opérations
print("Addition :", nombre1 + nombre2)
print("Soustraction :", nombre1 - nombre2)
print("Multiplication :", nombre1 * nombre2)

# Gestion de la division par zéro
if nombre2 != 0:
    print("Division :", nombre1 / nombre2)
else:
    print("Division : Impossible de diviser par zéro")
```

**Solution Exercice 10 :**

```python
"""
PROFIL UTILISATEUR COMPLET
Programme : Crée et affiche un profil personnel détaillé
Auteur : Apprenant Python
Version : 1.0
"""

print("=== CRÉATION DE VOTRE PROFIL ===")

# SECTION 1 : COLLECTE DES INFORMATIONS
print("\nVeuillez répondre aux questions suivantes :")

# Informations personnelles
nom = input("Quel est votre nom complet ? ")
age = int(input("Quel est votre âge ? "))  # Conversion en entier
ville = input("Où habitez-vous ? ")
profession = input("Quelle est votre profession ? ")

# Informations supplémentaires
taille = float(input("Quelle est votre taille en mètres (ex: 1.75) ? "))
est_etudiant = input("Êtes-vous étudiant ? (oui/non) ").lower() == "oui"

# SECTION 2 : TRAITEMENT DES DONNÉES
# Calcul de l'année de naissance (approximative)
annee_naissance = 2024 - age

# SECTION 3 : AFFICHAGE DU PROFIL
print("\n" + "="*40)
print("VOTRE PROFIL COMPLET")
print("="*40)

print(f"Nom : {nom}")
print(f"Âge : {age} ans (né vers {annee_naissance})")
print(f"Ville : {ville}")
print(f"Profession : {profession}")
print(f"Taille : {taille} m")

# Affichage conditionnel
if est_etudiant:
    print("Statut : Étudiant")
else:
    print("Statut : Professionnel")

print("\nMerci d'avoir créé votre profil !")

# SECTION 4 : RÉSUMÉ TECHNIQUE (pour l'apprentissage)
print("\n" + "-"*20)
print("INFORMATIONS TECHNIQUES :")
print(f"Type de 'nom' : {type(nom)}")
print(f"Type de 'age' : {type(age)}")
print(f"Type de 'taille' : {type(taille)}")
print(f"Type de 'est_etudiant' : {type(est_etudiant)}")
```

## Conseils Supplémentaires

**Pour tester dans l'interpréteur :**

```python
# Tape directement ces commandes :
>>> x = 10
>>> type(x)
<class 'int'>

>>> message = "Hello"
>>> type(message)
<class 'str'>
```

**Erreurs courantes à éviter :**

```python
# MAUVAIS :
resultat = "5" + 3  # Erreur! On ne peut additionner string et int

# BON :
resultat = int("5") + 3  # → 8
# ou
resultat = "5" + str(3)  # → "53"
```

**Vérification des types :**

```python
# Pour vérifier un type :
nombre = 42
if type(nombre) == int:
    print("C'est un entier!")

# Méthode plus pythonique :
if isinstance(nombre, int):
    print("C'est un entier!")
```
