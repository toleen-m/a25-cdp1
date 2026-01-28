## **Partie 1 : Compréhension de base des exceptions**

### **Exercice 1.1 : Gestion d'erreurs de division**

Écrivez un programme qui demande à l'utilisateur deux nombres et effectue leur division. Gérez les cas où :

1. L'utilisateur entre des valeurs non numériques
2. Le dénominateur est zéro
3. Tout se passe bien

Affichez un message approprié dans chaque cas.

### **Exercice 1.2 : Conversion sécurisée**

Créez une fonction `conversion_securisee` qui prend une chaîne de caractères et tente de la convertir en entier. Si la conversion échoue, la fonction doit retourner `None` au lieu de lever une exception.

Testez votre fonction avec :

- `"123"`
- `"12.5"`
- `"abc"`
- `"12a3"`

### **Exercice 1.3 : Accès sécurisé à une liste**

Écrivez une fonction `acces_liste` qui prend une liste et un index en paramètres. La fonction doit retourner l'élément à cet index si possible, sinon retourner la chaîne `"Index hors limites"`.

---

## **Partie 2 : Utilisation de try-except-else-finally**

### **Exercice 2.1 : Gestion complète de fichiers**

Écrivez un programme qui :

1. Demande à l'utilisateur un nom de fichier
2. Tente d'ouvrir et de lire le fichier
3. Si le fichier n'existe pas, affiche un message d'erreur
4. Si le fichier existe, compte le nombre de lignes
5. Finalement, affiche toujours "Opération terminée"

Utilisez les blocs `try`, `except`, `else` et `finally`.

### **Exercice 2.2 : Calculatrice robuste**

Créez une calculatrice qui gère les exceptions de manière exhaustive :

```python
def calculatrice():
    while True:
        try:
            a = float(input("Premier nombre: "))
            b = float(input("Deuxième nombre: "))
            operation = input("Opération (+, -, *, /): ")

            if operation == '+':
                resultat = a + b
            elif operation == '-':
                resultat = a - b
            elif operation == '*':
                resultat = a * b
            elif operation == '/':
                resultat = a / b
            else:
                print("Opération non valide")
                continue

        except ValueError:
            print("Erreur: Veuillez entrer des nombres valides")
            continue
        except ZeroDivisionError:
            print("Erreur: Division par zéro impossible")
            continue
        except Exception as e:
            print(f"Erreur inattendue: {e}")
            continue
        else:
            print(f"Résultat: {resultat}")
            break
        finally:
            print("--- Fin du calcul ---")
```

Modifiez cette calculatrice pour qu'elle continue de fonctionner après une erreur jusqu'à ce que l'utilisateur entre 'q' pour quitter.

### **Exercice 2.3 : Validation d'entrée utilisateur**

Écrivez une fonction `demander_age` qui :

- Demande l'âge de l'utilisateur
- Accepte uniquement les entiers entre 0 et 120
- Utilise des exceptions pour gérer les entrées invalides
- Redemande jusqu'à obtenir une valeur valide

---

## **Partie 3 : Création et levée d'exceptions personnalisées**

### **Exercice 3.1 : Classe CompteBancaire**

Créez une classe `CompteBancaire` avec :

- Un attribut `solde`
- Une méthode `retirer(montant)` qui lève une exception `SoldeInsuffisantError` si le montant > solde
- Une méthode `deposer(montant)` qui lève une exception `MontantNegatifError` si montant ≤ 0

Créez les exceptions personnalisées nécessaires.

### **Exercice 3.2 : Validation de mot de passe**

Écrivez une fonction `valider_mot_de_passe` qui lève des exceptions personnalisées si :

1. Le mot de passe a moins de 8 caractères (`MotDePasseTropCourtError`)
2. Le mot de passe ne contient pas de chiffre (`PasDeChiffreError`)
3. Le mot de passe ne contient pas de majuscule (`PasDeMajusculeError`)

Testez avec différents mots de passe.

### **Exercice 3.3 : Système d'inscription**

Créez un système d'inscription avec les règles suivantes :

- Nom d'utilisateur : 3-20 caractères, pas d'espaces
- Âge : 13-100 ans
- Email : doit contenir '@' et '.'

Lever des exceptions personnalisées pour chaque violation.

---

## **Partie 4 : Propagation et chaînage d'exceptions**

### **Exercice 4.1 : Fonctions imbriquées**

Créez trois fonctions imbriquées :

```python
def fonction_a():
    return fonction_b()

def fonction_b():
    return fonction_c()

def fonction_c():
    # Simule une erreur
    return 1 / 0
```

Appelez `fonction_a()` et observez la propagation de l'exception. Modifiez pour attraper l'exception dans `fonction_b()` et lever une nouvelle exception avec un message plus explicite.

### **Exercice 4.2 : Chaînage d'exceptions**

Écrivez un programme qui :

1. Tente d'ouvrir un fichier de configuration
2. Si le fichier n'existe pas, tente d'utiliser une configuration par défaut
3. Si la configuration par défaut échoue aussi, lever une exception qui montre les deux erreurs en chaîne

Utilisez `raise ... from ...` pour le chaînage.

### **Exercice 4.3 : Gestionnaire de contexte simple**

Créez un gestionnaire de contexte `FichierSecurise` qui :

- Ouvre un fichier en lecture
- Garantit sa fermeture même en cas d'erreur
- Relève les exceptions avec un message ajouté

Utilisez-le comme ceci :

```python
with FichierSecurise("fichier.txt") as f:
    contenu = f.read()
```

---

## **Partie 5 : Exercices de synthèse**

### **Exercice 5.1 : Gestionnaire de tâches**

Créez un gestionnaire de tâches qui lit un fichier JSON (simulez avec un dictionnaire Python). Gérez toutes les exceptions possibles :

- Fichier inexistant
- Format JSON invalide
- Champs manquants dans les tâches
- Types de données incorrects

### **Exercice 5.2 : Calculatrice scientifique étendue**

Étendez la calculatrice de l'exercice 2.2 pour gérer :

- Les racines carrées (erreur sur nombres négatifs)
- Les logarithmes (erreur sur nombres ≤ 0)
- Les puissances
- Créez une hiérarchie d'exceptions personnalisées

### **Exercice 5.3 : Système de réservation**

Simulez un système de réservation de billets avec :

- Un nombre limité de places
- Validation des données utilisateur
- Gestion des conflits (deux réservations simultanées)
- Sauvegarde/chargement depuis fichier

Utilisez des exceptions pour tous les cas d'erreur.

---

## **Partie 6 : Bonnes pratiques et cas avancés**

### **Exercice 6.1 : Exception ou valeur de retour ?**

Pour chaque scénario, décidez si une exception ou une valeur de retour spéciale est plus appropriée :

1. Recherche d'un élément dans une liste (élément non trouvé)
2. Conversion d'une chaîne en entier (chaîne invalide)
3. Ouverture d'un fichier (fichier inexistant)
4. Division de deux nombres (division par zéro)
5. Accès à une clé de dictionnaire (clé absente)

Implémentez les deux approches et discutez des avantages/inconvénients.

### **Exercice 6.2 : Nettoyage de ressources**

Écrivez un programme qui :

1. Ouvre deux fichiers
2. Copie le contenu du premier dans le second
3. Garantit que les deux fichiers sont fermés même en cas d'erreur
4. Supprime le fichier de sortie si la copie échoue

### **Exercice 6.3 : Journalisation des exceptions**

Créez un décorateur `journaliser_exceptions` qui :

- Enveloppe une fonction
- Capture toutes les exceptions
- Les journalise dans un fichier `erreurs.log` avec la date et les détails
- Relève l'exception originale

---

## **Corrections suggérées (extraits) :**

### **Pour l'exercice 1.1 :**

```python
def division_securisee():
    try:
        a = float(input("Entrez le numérateur: "))
        b = float(input("Entrez le dénominateur: "))
        resultat = a / b
    except ValueError:
        print("Erreur: Vous devez entrer des nombres")
    except ZeroDivisionError:
        print("Erreur: Division par zéro impossible")
    else:
        print(f"Le résultat est: {resultat}")
    finally:
        print("Fin de l'opération")
```

### **Pour l'exercice 3.1 :**

```python
class SoldeInsuffisantError(Exception):
    """Exception levée quand le solde est insuffisant"""
    pass

class MontantNegatifError(Exception):
    """Exception levée quand le montant est négatif"""
    pass

class CompteBancaire:
    def __init__(self, solde_initial=0):
        self.solde = solde_initial

    def deposer(self, montant):
        if montant <= 0:
            raise MontantNegatifError(f"Montant {montant} invalide")
        self.solde += montant

    def retirer(self, montant):
        if montant <= 0:
            raise MontantNegatifError(f"Montant {montant} invalide")
        if montant > self.solde:
            raise SoldeInsuffisantError(
                f"Solde insuffisant: {self.solde}, tentative: {montant}"
            )
        self.solde -= montant
        return montant
```

### **Pour l'exercice 6.3 :**

```python
import datetime

def journaliser_exceptions(fichier_log="erreurs.log"):
    def decorateur(fonction):
        def wrapper(*args, **kwargs):
            try:
                return fonction(*args, **kwargs)
            except Exception as e:
                with open(fichier_log, 'a', encoding='utf-8') as f:
                    maintenant = datetime.datetime.now()
                    message = f"[{maintenant}] {type(e).__name__}: {e}\n"
                    f.write(message)
                raise  # Relève l'exception originale
        return wrapper
    return decorateur

@journaliser_exceptions()
def fonction_dangereuse():
    return 1 / 0
```
