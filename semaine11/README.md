## **Exercice 1 : Gestionnaire de Contacts (2-3 heures)**

**Objectif** : Créer un système de gestion de contacts avec gestion d'erreurs complète.

```python
"""
Gestionnaire de Contacts
- Ajouter un contact (nom, téléphone, email)
- Rechercher un contact
- Supprimer un contact
- Afficher tous les contacts
- Sauvegarder/charger depuis un fichier
"""

class ContactError(Exception):
    """Base exception pour les erreurs de contact"""
    pass

class ContactExisteDejaError(ContactError):
    pass

class ContactNonTrouveError(ContactError):
    pass

class FormatTelephoneError(ContactError):
    pass

class FormatEmailError(ContactError):
    pass

class GestionnaireContacts:
    def __init__(self):
        self.contacts = {}

    def valider_telephone(self, telephone):
        """Valide le format du téléphone (10 chiffres)"""
        if not telephone.isdigit():
            raise FormatTelephoneError("Le téléphone doit contenir uniquement des chiffres")
        if len(telephone) != 10:
            raise FormatTelephoneError("Le téléphone doit avoir 10 chiffres")
        return True

    def valider_email(self, email):
        """Valide le format de l'email"""
        if '@' not in email or '.' not in email:
            raise FormatEmailError("Email invalide: doit contenir '@' et '.'")
        if email.count('@') != 1:
            raise FormatEmailError("Email invalide: doit contenir exactement un '@'")
        return True

    def ajouter_contact(self, nom, telephone, email):
        """Ajoute un nouveau contact"""
        # À compléter

    def rechercher_contact(self, nom):
        """Recherche un contact par nom"""
        # À compléter

    def supprimer_contact(self, nom):
        """Supprime un contact"""
        # À compléter

    def afficher_contacts(self):
        """Affiche tous les contacts"""
        # À compléter

    def sauvegarder(self, nom_fichier="contacts.txt"):
        """Sauvegarde les contacts dans un fichier"""
        # À compléter

    def charger(self, nom_fichier="contacts.txt"):
        """Charge les contacts depuis un fichier"""
        # À compléter

def menu():
    """Menu principal"""
    gestionnaire = GestionnaireContacts()

    while True:
        print("\n=== GESTIONNAIRE DE CONTACTS ===")
        print("1. Ajouter un contact")
        print("2. Rechercher un contact")
        print("3. Supprimer un contact")
        print("4. Afficher tous les contacts")
        print("5. Sauvegarder les contacts")
        print("6. Charger les contacts")
        print("7. Quitter")

        choix = input("Votre choix (1-7): ")

        if choix == '1':
            # À compléter
            pass
        elif choix == '2':
            # À compléter
            pass
        # ... autres choix

if __name__ == "__main__":
    menu()
```

---

## **Exercice 2 : Calculatrice Scientifique avec Historique (1-2 heures)**

**Objectif** : Créer une calculatrice avec gestion d'erreurs et historique.

```python
"""
Calculatrice Scientifique avec:
- Opérations de base (+, -, *, /)
- Puissance, racine carrée
- Historique des calculs
- Gestion d'erreurs complète
"""

class CalculError(Exception):
    pass

class DivisionZeroError(CalculError):
    pass

class RacineNegativeError(CalculError):
    pass

class Calculatrice:
    def __init__(self):
        self.historique = []

    def addition(self, a, b):
        # À compléter

    def soustraction(self, a, b):
        # À compléter

    def multiplication(self, a, b):
        # À compléter

    def division(self, a, b):
        # À compléter (gérer division par zéro)

    def puissance(self, a, b):
        # À compléter

    def racine_carree(self, a):
        # À compléter (gérer nombres négatifs)

    def afficher_historique(self):
        # À compléter

    def effacer_historique(self):
        # À compléter

def interface_calculatrice():
    """Interface utilisateur de la calculatrice"""
    calc = Calculatrice()

    operations = {
        '1': ('Addition', calc.addition),
        '2': ('Soustraction', calc.soustraction),
        '3': ('Multiplication', calc.multiplication),
        '4': ('Division', calc.division),
        '5': ('Puissance', calc.puissance),
        '6': ('Racine carrée', calc.racine_carree)
    }

    while True:
        print("\n=== CALCULATRICE ===")
        for key, (nom, _) in operations.items():
            print(f"{key}. {nom}")
        print("7. Afficher l'historique")
        print("8. Effacer l'historique")
        print("9. Quitter")

        choix = input("Votre choix: ")

        if choix == '9':
            break
        elif choix == '7':
            calc.afficher_historique()
        elif choix == '8':
            calc.effacer_historique()
        elif choix in operations:
            try:
                # À compléter: demander les nombres et exécuter l'opération
                pass
            except (ValueError, DivisionZeroError, RacineNegativeError) as e:
                print(f"Erreur: {e}")
            except Exception as e:
                print(f"Erreur inattendue: {type(e).__name__}: {e}")

if __name__ == "__main__":
    interface_calculatrice()
```

---

## **Exercice 3 : Système de Réservation de Salles (2-3 heures)**

**Objectif** : Gérer les réservations de salles avec conflits et validations.

```python
"""
Système de Réservation de Salles
- Ajouter une salle
- Réserver une salle (date, heure, durée)
- Annuler une réservation
- Vérifier les disponibilités
- Gérer les conflits de réservation
"""

from datetime import datetime, timedelta

class ReservationError(Exception):
    pass

class SalleIndisponibleError(ReservationError):
    pass

class DateInvalideError(ReservationError):
    pass

class DureeInvalideError(ReservationError):
    pass

class Reservation:
    def __init__(self, salle, date_debut, duree_heures, utilisateur):
        # À compléter

    def chevauche(self, autre_reservation):
        """Vérifie si deux réservations se chevauchent"""
        # À compléter

class Salle:
    def __init__(self, nom, capacite):
        # À compléter

    def est_disponible(self, date_debut, duree_heures):
        """Vérifie si la salle est disponible"""
        # À compléter

    def ajouter_reservation(self, reservation):
        """Ajoute une réservation"""
        # À compléter

    def annuler_reservation(self, reservation_id):
        """Annule une réservation"""
        # À compléter

class SystemeReservation:
    def __init__(self):
        self.salles = {}
        self.reservations = []

    def ajouter_salle(self, nom, capacite):
        # À compléter

    def reserver_salle(self, nom_salle, date_str, heure_str, duree, utilisateur):
        # À compléter (gérer toutes les erreurs)

    def annuler_reservation(self, reservation_id):
        # À compléter

    def afficher_reservations_salle(self, nom_salle):
        # À compléter

    def afficher_reservations_date(self, date_str):
        # À compléter

def menu_reservation():
    """Menu du système de réservation"""
    systeme = SystemeReservation()

    # Ajouter quelques salles par défaut
    salles_par_defaut = [
        ("Salle A", 20),
        ("Salle B", 30),
        ("Salle C", 50),
        ("Salle de Réunion", 10)
    ]

    for nom, capacite in salles_par_defaut:
        systeme.ajouter_salle(nom, capacite)

    while True:
        print("\n=== SYSTÈME DE RÉSERVATION ===")
        print("1. Réserver une salle")
        print("2. Annuler une réservation")
        print("3. Afficher les réservations d'une salle")
        print("4. Afficher les réservations d'une date")
        print("5. Quitter")

        choix = input("Votre choix: ")

        if choix == '1':
            try:
                # À compléter: demander les infos et faire la réservation
                pass
            except (SalleIndisponibleError, DateInvalideError, DureeInvalideError) as e:
                print(f"Erreur de réservation: {e}")
            except Exception as e:
                print(f"Erreur inattendue: {type(e).__name__}: {e}")

        elif choix == '2':
            # À compléter
            pass

        elif choix == '3':
            # À compléter
            pass

        elif choix == '4':
            # À compléter
            pass

        elif choix == '5':
            print("Au revoir!")
            break

if __name__ == "__main__":
    menu_reservation()
```

---

## **Exercice 4 : Quiz Interactif avec Score (1-2 heures)**

**Objectif** : Créer un quiz avec gestion d'erreurs de saisie et calcul de score.

```python
"""
Quiz Interactif
- Charger les questions depuis un fichier
- Poser les questions dans un ordre aléatoire
- Calculer le score
- Gérer le temps (optionnel)
- Sauvegarder les résultats
"""

import random
import time

class QuizError(Exception):
    pass

class FormatQuestionError(QuizError):
    pass

class FichierQuizError(QuizError):
    pass

class Question:
    def __init__(self, texte, options, reponse_correcte):
        # À compléter

    def poser(self):
        """Pose la question et retourne True si réponse correcte"""
        # À compléter

    def verifier_reponse(self, reponse_utilisateur):
        """Vérifie si la réponse est correcte"""
        # À compléter

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.temps_total = 0

    def charger_questions(self, nom_fichier="questions.txt"):
        """Charge les questions depuis un fichier"""
        # À compléter

    def demarrer(self):
        """Démarre le quiz"""
        # À compléter

    def afficher_resultat(self):
        """Affiche le résultat final"""
        # À compléter

    def sauvegarder_resultat(self, nom_utilisateur):
        """Sauvegarde le résultat"""
        # À compléter

def creer_fichier_questions_exemple():
    """Crée un fichier exemple de questions"""
    questions = [
        "Quelle est la capitale de la France?|Paris|Londres|Berlin|Madrid|1",
        "Combien font 2 + 2?|3|4|5|6|2",
        "Quel langage de programmation utilise 'print'?|Java|C++|Python|JavaScript|3",
        "Quelle planète est appelée 'Planète Rouge'?|Venus|Mars|Jupiter|Saturne|2",
        "Qui a peint la Joconde?|Van Gogh|Picasso|Leonard de Vinci|Michel-Ange|3"
    ]

    try:
        with open("questions.txt", "w", encoding="utf-8") as f:
            for question in questions:
                f.write(question + "\n")
        print("Fichier de questions créé avec succès!")
    except Exception as e:
        print(f"Erreur lors de la création du fichier: {e}")

def menu_quiz():
    """Menu du quiz"""
    quiz = Quiz()

    print("=== QUIZ INTERACTIF ===")

    try:
        quiz.charger_questions()
    except FichierQuizError:
        print("Fichier de questions non trouvé. Création d'un fichier exemple...")
        creer_fichier_questions_exemple()
        try:
            quiz.charger_questions()
        except FichierQuizError as e:
            print(f"Impossible de charger les questions: {e}")
            return

    nom = input("Entrez votre nom: ")

    try:
        quiz.demarrer()
        quiz.afficher_resultat()
        quiz.sauvegarder_resultat(nom)
    except Exception as e:
        print(f"Erreur pendant le quiz: {type(e).__name__}: {e}")

if __name__ == "__main__":
    menu_quiz()
```

---

## **Exercice 5 : Convertisseur d'Unités (1 heure)**

**Objectif** : Créer un convertisseur robuste avec gestion d'erreurs.

```python
"""
Convertisseur d'Unités
- Température (Celsius, Fahrenheit, Kelvin)
- Distance (mètres, kilomètres, miles, pieds)
- Poids (grammes, kilogrammes, livres, onces)
- Monnaie (taux fixes ou fichier de configuration)
"""

class ConversionError(Exception):
    pass

class UniteInvalideError(ConversionError):
    pass

class ValeurInvalideError(ConversionError):
    pass

class Convertisseur:
    # Définitions des taux de conversion
    TAUX_MONNAIE = {
        'USD_EUR': 0.85,
        'EUR_USD': 1.18,
        'USD_GBP': 0.73,
        'GBP_USD': 1.37
    }

    def convertir_temperature(self, valeur, source, cible):
        """Convertit entre Celsius, Fahrenheit et Kelvin"""
        # À compléter

    def convertir_distance(self, valeur, source, cible):
        """Convertit entre mètres, km, miles, pieds"""
        # À compléter

    def convertir_poids(self, valeur, source, cible):
        """Convertit entre grammes, kg, livres, onces"""
        # À compléter

    def convertir_monnaie(self, valeur, source, cible):
        """Convertit entre devises"""
        # À compléter

    def valider_unite(self, unite, categorie):
        """Valide si l'unité existe dans la catégorie"""
        # À compléter

def menu_convertisseur():
    """Menu du convertisseur"""
    convertisseur = Convertisseur()

    categories = {
        '1': ('Température', ['Celsius', 'Fahrenheit', 'Kelvin']),
        '2': ('Distance', ['Mètres', 'Kilomètres', 'Miles', 'Pieds']),
        '3': ('Poids', ['Grammes', 'Kilogrammes', 'Livres', 'Onces']),
        '4': ('Monnaie', ['USD', 'EUR', 'GBP'])
    }

    while True:
        print("\n=== CONVERTISSEUR D'UNITÉS ===")
        for key, (nom, unites) in categories.items():
            print(f"{key}. {nom} ({', '.join(unites)})")
        print("5. Quitter")

        choix_categorie = input("Choisissez une catégorie (1-5): ")

        if choix_categorie == '5':
            break

        if choix_categorie not in categories:
            print("Choix invalide!")
            continue

        nom_categorie, unites = categories[choix_categorie]

        try:
            # À compléter: demander valeur, unité source, unité cible
            # et effectuer la conversion
            pass

        except UniteInvalideError as e:
            print(f"Erreur d'unité: {e}")
        except ValeurInvalideError as e:
            print(f"Erreur de valeur: {e}")
        except Exception as e:
            print(f"Erreur inattendue: {type(e).__name__}: {e}")

if __name__ == "__main__":
    menu_convertisseur()
```

---

## **Solutions partielles (pour guider les étudiants) :**

### **Pour l'Exercice 1 (extrait) :**

```python
def ajouter_contact(self, nom, telephone, email):
    """Ajoute un nouveau contact"""
    try:
        # Validation
        nom = nom.strip()
        if not nom:
            raise ValueError("Le nom ne peut pas être vide")

        self.valider_telephone(telephone)
        self.valider_email(email)

        # Vérifier si le contact existe déjà
        if nom in self.contacts:
            raise ContactExisteDejaError(f"Le contact '{nom}' existe déjà")

        # Ajouter le contact
        self.contacts[nom] = {
            'telephone': telephone,
            'email': email
        }
        print(f"Contact '{nom}' ajouté avec succès!")

    except (ValueError, FormatTelephoneError, FormatEmailError) as e:
        raise ContactError(f"Impossible d'ajouter le contact: {e}")
```

### **Pour l'Exercice 2 (extrait) :**

```python
def division(self, a, b):
    """Division avec gestion de division par zéro"""
    try:
        if b == 0:
            raise DivisionZeroError("Division par zéro impossible")

        resultat = a / b
        operation = f"{a} / {b} = {resultat}"
        self.historique.append(operation)
        return resultat

    except DivisionZeroError as e:
        # Ajouter à l'historique même en cas d'erreur
        self.historique.append(f"ERREUR: {a} / {b} -> {e}")
        raise
```

### **Pour l'Exercice 4 (extrait) :**

```python
def charger_questions(self, nom_fichier="questions.txt"):
    """Charge les questions depuis un fichier"""
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            lignes = f.readlines()

        if not lignes:
            raise FichierQuizError("Le fichier de questions est vide")

        for i, ligne in enumerate(lignes):
            try:
                parties = ligne.strip().split('|')
                if len(parties) != 6:
                    raise FormatQuestionError(
                        f"Format invalide à la ligne {i+1}: {ligne}"
                    )

                texte = parties[0]
                options = parties[1:5]
                reponse_correcte = int(parties[5]) - 1  # Convertir en index 0-based

                if not (0 <= reponse_correcte < 4):
                    raise FormatQuestionError(
                        f"Réponse invalide à la ligne {i+1}: doit être entre 1 et 4"
                    )

                question = Question(texte, options, reponse_correcte)
                self.questions.append(question)

            except (ValueError, IndexError) as e:
                raise FormatQuestionError(f"Erreur à la ligne {i+1}: {e}")

        print(f"{len(self.questions)} questions chargées avec succès!")

    except FileNotFoundError:
        raise FichierQuizError(f"Fichier '{nom_fichier}' non trouvé")
    except Exception as e:
        raise FichierQuizError(f"Erreur lors du chargement: {e}")
```
