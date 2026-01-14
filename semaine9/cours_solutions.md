# Solutions des Exercices

## Solution Exercice 1

### 1.1 : Lancer de dés

```python
import random

# Lancement des dés
de1 = random.randint(1, 6)
de2 = random.randint(1, 6)

print(f"Dé 1: {de1}")
print(f"Dé 2: {de2}")
print(f"Somme: {de1 + de2}")

if de1 == de2:
    print("DOUBLE!")
```

### 1.2 : Tirage au sort

```python
import random

etudiants = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# 1. Mélanger la liste
random.shuffle(etudiants)
print(f"Ordre mélangé: {etudiants}")

# 2. Un gagnant au hasard
gagnant = random.choice(etudiants)
print(f"Gagnant: {gagnant}")

# 3. Deux gagnants différents
gagnants = random.sample(etudiants, 2)
print(f"Deux gagnants: {gagnants}")

# 4. Ordre de passage aléatoire
print("Ordre de passage:")
for i, etudiant in enumerate(etudiants, 1):
    print(f"{i}. {etudiant}")
```

## Solution Exercice 2

### 2.1 : Calculs géométriques

```python
import math

rayon = 5
cote_a = 3
cote_b = 4

# 1. Aire du cercle
aire_cercle = math.pi * rayon ** 2
print(f"Aire du cercle (r={rayon}): {aire_cercle:.2f}")

# 2. Périmètre du cercle
perimetre_cercle = 2 * math.pi * rayon
print(f"Périmètre du cercle: {perimetre_cercle:.2f}")

# 3. Hypoténuse
hypotenuse = math.sqrt(cote_a**2 + cote_b**2)
print(f"Hypoténuse ({cote_a}, {cote_b}): {hypotenuse:.2f}")

# 4. π arrondi
pi_arrondi = round(math.pi, 2)
print(f"π arrondi à 2 décimales: {pi_arrondi}")
```

### 2.2 : Conversions

```python
import math

# 1. Degrés → Radians
radians = math.radians(180)
print(f"180° en radians: {radians:.4f}")

# 2. Radians → Degrés
degrees = math.degrees(math.pi)
print(f"π radians en degrés: {degrees:.1f}")

# 3. sin(90°)
sin90 = math.sin(math.radians(90))
print(f"sin(90°): {sin90:.4f}")

# 4. cos(π)
cos_pi = math.cos(math.pi)
print(f"cos(π): {cos_pi:.4f}")
```

## Solution Exercice 3

### 3.1 : Sauvegarde de données

```python
import json

etudiant = {
    "nom": "Alice",
    "age": 20,
    "notes": [15, 18, 12],
    "present": True
}

# Écriture dans un fichier JSON
with open("etudiant.json", "w") as f:
    json.dump(etudiant, f, indent=2)
print("Fichier sauvegardé: etudiant.json")

# Lecture depuis le fichier
with open("etudiant.json", "r") as f:
    donnees_lues = json.load(f)

print("\nDonnées lues:")
print(f"Nom: {donnees_lues['nom']}")
print(f"Âge: {donnees_lues['age']}")
print(f"Notes: {donnees_lues['notes']}")
print(f"Moyenne: {sum(donnees_lues['notes'])/len(donnees_lues['notes']):.1f}")
```

### 3.2 : Journal d'événements

```python
import json
import datetime

def ajouter_evenement(type_event, message):
    """Ajoute un événement au journal"""
    # Lire les événements existants
    try:
        with open("journal.json", "r") as f:
            evenements = json.load(f)
    except FileNotFoundError:
        evenements = []

    # Ajouter le nouvel événement
    nouvel_event = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": type_event,
        "message": message
    }

    evenements.append(nouvel_event)

    # Sauvegarder
    with open("journal.json", "w") as f:
        json.dump(evenements, f, indent=2)

    return len(evenements)

def lire_journal():
    """Lit tout le journal"""
    try:
        with open("journal.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Test
print("=== JOURNAL D'ÉVÉNEMENTS ===")
ajouter_evenement("INFO", "Démarrage de l'application")
ajouter_evenement("ERREUR", "Fichier non trouvé")
ajouter_evenement("SUCCES", "Sauvegarde terminée")

# Lire et afficher
evenements = lire_journal()
print(f"\nNombre d'événements: {len(evenements)}")
for event in evenements[-3:]:  # 3 derniers
    print(f"{event['date']} [{event['type']}] {event['message']}")
```

## Solution Exercice 4

### 4.1 : Vérificateur de fichiers

```python
import os

fichier = "test.txt"

# 1. Vérifier si le fichier existe
if os.path.exists(fichier):
    print(f"Le fichier '{fichier}' existe.")

    # 2. Afficher la taille
    taille = os.path.getsize(fichier)
    print(f"Taille: {taille} octets")

    # Lire le contenu
    with open(fichier, "r") as f:
        print(f"Contenu: {f.read()}")
else:
    print(f"Le fichier '{fichier}' n'existe pas.")

    # 3. Créer le fichier
    with open(fichier, "w") as f:
        f.write("Ceci est un fichier test.\n")
        f.write("Créé par le programme Python.\n")
    print(f"Fichier '{fichier}' créé.")

# 4. Lister les fichiers du dossier courant
print("\nFichiers dans le dossier courant:")
for item in os.listdir("."):
    if os.path.isfile(item):
        print(f"  📄 {item}")
    elif os.path.isdir(item):
        print(f"  📁 {item}/")
```

### 4.2 : Gestionnaire de projets

```python
import os

def creer_projet(nom_projet):
    """Crée une structure de projet"""

    # 1. Créer le dossier du projet
    if not os.path.exists(nom_projet):
        os.mkdir(nom_projet)
        print(f"Dossier '{nom_projet}' créé.")
    else:
        print(f"Dossier '{nom_projet}' existe déjà.")
        return False

    # 2. Créer README.md
    chemin_readme = os.path.join(nom_projet, "README.md")
    with open(chemin_readme, "w") as f:
        f.write(f"# {nom_projet}\n\n")
        f.write("Description du projet.\n")
    print(f"Fichier '{chemin_readme}' créé.")

    # 3. Créer main.py
    chemin_main = os.path.join(nom_projet, "main.py")
    with open(chemin_main, "w") as f:
        f.write('print("Bonjour depuis le projet!")\n')
    print(f"Fichier '{chemin_main}' créé.")

    # 3. Vérifier la création
    if os.path.exists(nom_projet) and os.path.isdir(nom_projet):
        print(f"✅ Projet '{nom_projet}' créé avec succès!")
        return True
    else:
        print(f"❌ Erreur lors de la création du projet.")
        return False

def nettoyer_projet(nom_projet):
    """Supprime un projet (optionnel)"""
    if os.path.exists(nom_projet):
        # Supprimer les fichiers d'abord
        for item in os.listdir(nom_projet):
            chemin_item = os.path.join(nom_projet, item)
            if os.path.isfile(chemin_item):
                os.remove(chemin_item)
                print(f"Fichier supprimé: {chemin_item}")

        # Supprimer le dossier
        os.rmdir(nom_projet)
        print(f"Dossier '{nom_projet}' supprimé.")
        return True
    else:
        print(f"Projet '{nom_projet}' non trouvé.")
        return False

# Test
creer_projet("mon_projet")

# Vérification
print(f"\nContenu de 'mon_projet':")
for item in os.listdir("mon_projet"):
    print(f"  - {item}")

# Nettoyage (optionnel)
# nettoyer_projet("mon_projet")
```

## Solution Exercice 5

### 5.1 : Copies de listes

```python
import copy

originale = [[1, 2], [3, 4]]

print("=== DIFFÉRENTES COPIES ===")

# 1. Référence (même objet)
reference = originale
print(f"1. Référence: originale is référence = {originale is reference}")

# 2. Copie superficielle
copie_simple = copy.copy(originale)
print(f"2. Copie simple: originale is copie_simple = {originale is copie_simple}")

# 3. Copie profonde
copie_profonde = copy.deepcopy(originale)
print(f"3. Copie profonde: originale is copie_profonde = {originale is copie_profonde}")

# Modification pour montrer la différence
print("\n=== APRÈS MODIFICATION ===")
originale[0][0] = 100  # Modifie la sous-liste

print(f"Originale: {originale}")
print(f"Référence: {reference}")          # Modifiée aussi
print(f"Copie simple: {copie_simple}")    # Sous-liste modifiée!
print(f"Copie profonde: {copie_profonde}") # Inchangée
```

### 5.2 : Système de sauvegarde

```python
import copy

class SystemeSauvegarde:
    def __init__(self, donnees):
        self.donnees = donnees
        self.sauvegardes = []
        self.sauvegarder()  # Sauvegarde initiale

    def sauvegarder(self):
        """Crée une sauvegarde des données actuelles"""
        backup = copy.deepcopy(self.donnees)
        self.sauvegardes.append(backup)
        print(f"Sauvegarde #{len(self.sauvegardes)} créée.")

    def restaurer(self, index=-1):
        """Restaure une version précédente"""
        if 0 <= index < len(self.sauvegardes) or index < 0:
            self.donnees = copy.deepcopy(self.sauvegardes[index])
            print(f"Restauration version #{len(self.sauvegardes) + index + 1}")
            return True
        else:
            print("Index de sauvegarde invalide.")
            return False

    def comparer(self, index1, index2):
        """Compare deux versions"""
        if 0 <= index1 < len(self.sauvegardes) and 0 <= index2 < len(self.sauvegardes):
            v1 = self.sauvegardes[index1]
            v2 = self.sauvegardes[index2]

            print(f"\nComparaison v{index1+1} vs v{index2+1}:")

            # Comparaison simple
            if v1 == v2:
                print("  Identiques")
            else:
                print("  Différentes")

                # Détails des différences
                for key in v1:
                    if key in v2 and v1[key] != v2[key]:
                        print(f"  - '{key}': {v1[key]} → {v2[key]}")

            return True
        else:
            print("Indices invalides.")
            return False

    def afficher_historique(self):
        """Affiche l'historique des sauvegardes"""
        print(f"\n=== HISTORIQUE ({len(self.sauvegardes)} versions) ===")
        for i, save in enumerate(self.sauvegardes):
            print(f"v{i+1}: {save}")

# Test
donnees = {
    "utilisateurs": ["Alice", "Bob"],
    "config": {"theme": "sombre", "langue": "fr"}
}

systeme = SystemeSauvegarde(donnees)

# Modifications et sauvegardes
donnees["utilisateurs"].append("Charlie")
systeme.sauvegarder()

donnees["config"]["theme"] = "clair"
systeme.sauvegarder()

# Affichage
systeme.afficher_historique()

# Comparaison
systeme.comparer(0, 2)

# Restauration
systeme.restaurer(0)
print(f"\nDonnées après restauration: {systeme.donnees}")
```

## Solution Exercice 6

### 6.1 : Jeu de dés amélioré

```python
import random
import math
import json
import os

class JeuDeDes:
    def __init__(self):
        self.fichier_scores = "scores.json"
        self.charger_scores()

    def lancer_des(self, nombre=3):
        """Lance plusieurs dés"""
        resultats = [random.randint(1, 6) for _ in range(nombre)]
        return resultats

    def calculer_statistiques(self, resultats):
        """Calcule des statistiques sur les résultats"""
        stats = {
            "somme": sum(resultats),
            "moyenne": sum(resultats) / len(resultats),
            "ecart_type": math.sqrt(
                sum((x - (sum(resultats)/len(resultats)))**2 for x in resultats) / len(resultats)
            ),
            "maximum": max(resultats),
            "minimum": min(resultats)
        }
        return stats

    def sauvegarder_partie(self, joueur, resultats, stats):
        """Sauvegarde une partie dans le fichier JSON"""
        partie = {
            "joueur": joueur,
            "date": "2024-01-15",  # Simplifié
            "resultats": resultats,
            "stats": stats
        }

        # Charger les scores existants
        if os.path.exists(self.fichier_scores):
            with open(self.fichier_scores, "r") as f:
                scores = json.load(f)
        else:
            scores = []

        # Ajouter la nouvelle partie
        scores.append(partie)

        # Sauvegarder
        with open(self.fichier_scores, "w") as f:
            json.dump(scores, f, indent=2)

        print(f"Partie sauvegardée pour {joueur}")

    def charger_scores(self):
        """Charge les scores depuis le fichier"""
        if os.path.exists(self.fichier_scores):
            with open(self.fichier_scores, "r") as f:
                self.scores = json.load(f)
            print(f"{len(self.scores)} parties chargées.")
        else:
            self.scores = []
            print("Aucun fichier de scores trouvé.")

    def jouer(self, joueur):
        """Joue une partie complète"""
        print(f"\n=== TOUR DE {joueur} ===")

        # Lancer les dés
        resultats = self.lancer_des(3)
        print(f"Résultats: {resultats}")

        # Calculer les statistiques
        stats = self.calculer_statistiques(resultats)
        print(f"Somme: {stats['somme']}")
        print(f"Moyenne: {stats['moyenne']:.2f}")
        print(f"Max/Min: {stats['maximum']}/{stats['minimum']}")

        # Sauvegarder
        self.sauvegarder_partie(joueur, resultats, stats)

        return stats['somme']

# Test du jeu
jeu = JeuDeDes()

# Jouer quelques parties
jeu.jouer("Alice")
jeu.jouer("Bob")
jeu.jouer("Alice")

# Afficher l'historique
print(f"\n=== HISTORIQUE DES PARTIES ===")
for partie in jeu.scores:
    print(f"{partie['joueur']}: {partie['resultats']} (somme: {partie['stats']['somme']})")
```

### 6.2 : Système de configuration

```python
import json
import os
import random
import copy

class SystemeConfiguration:
    def __init__(self, fichier_config="config.json"):
        self.fichier_config = fichier_config
        self.config = self.charger_config()
        self.backup = None

    def charger_config(self):
        """Charge la configuration depuis le fichier"""
        if os.path.exists(self.fichier_config):
            try:
                with open(self.fichier_config, "r") as f:
                    config = json.load(f)
                print(f"Configuration chargée depuis {self.fichier_config}")
                return config
            except json.JSONDecodeError:
                print(f"Erreur de lecture de {self.fichier_config}")
                return self.config_par_defaut()
        else:
            print(f"Fichier {self.fichier_config} non trouvé. Création config par défaut.")
            return self.config_par_defaut()

    def config_par_defaut(self):
        """Retourne la configuration par défaut"""
        return {
            "application": {
                "nom": "MonApp",
                "version": "1.0",
                "debug": False
            },
            "utilisateurs": [],
            "parametres": {
                "theme": "sombre",
                "langue": "fr",
                "notifications": True
            }
        }

    def sauvegarder_config(self):
        """Sauvegarde la configuration actuelle"""
        # Créer un backup avant de sauvegarder
        self.backup = copy.deepcopy(self.config)

        with open(self.fichier_config, "w") as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)

        print(f"Configuration sauvegardée dans {self.fichier_config}")

    def creer_backup(self):
        """Crée un fichier de backup séparé"""
        if self.config:
            backup_file = f"config_backup_{random.randint(1000, 9999)}.json"
            with open(backup_file, "w") as f:
                json.dump(self.config, f, indent=2)
            print(f"Backup créé: {backup_file}")
            return backup_file
        return None

    def restaurer_backup(self, fichier_backup):
        """Restaure depuis un fichier backup"""
        if os.path.exists(fichier_backup):
            with open(fichier_backup, "r") as f:
                self.config = json.load(f)
            print(f"Configuration restaurée depuis {fichier_backup}")
            self.sauvegarder_config()
            return True
        else:
            print(f"Fichier backup {fichier_backup} non trouvé")
            return False

    def ajouter_utilisateur(self, nom):
        """Ajoute un utilisateur avec un ID aléatoire"""
        user_id = random.randint(10000, 99999)
        utilisateur = {
            "id": user_id,
            "nom": nom,
            "date_creation": "2024-01-15"
        }

        self.config["utilisateurs"].append(utilisateur)
        print(f"Utilisateur ajouté: {nom} (ID: {user_id})")
        self.sauvegarder_config()

        return user_id

    def modifier_parametre(self, cle, valeur):
        """Modifie un paramètre"""
        if cle in self.config["parametres"]:
            ancienne_valeur = self.config["parametres"][cle]
            self.config["parametres"][cle] = valeur
            print(f"Paramètre '{cle}' changé: {ancienne_valeur} → {valeur}")
            self.sauvegarder_config()
            return True
        else:
            print(f"Paramètre '{cle}' non trouvé")
            return False

    def afficher_config(self):
        """Affiche la configuration actuelle"""
        print("\n=== CONFIGURATION ACTUELLE ===")
        print(f"Application: {self.config['application']['nom']} v{self.config['application']['version']}")
        print(f"Utilisateurs: {len(self.config['utilisateurs'])}")
        print("Paramètres:")
        for cle, valeur in self.config['parametres'].items():
            print(f"  - {cle}: {valeur}")

# Test du système
systeme = SystemeConfiguration()

# Afficher la config initiale
systeme.afficher_config()

# Modifier des paramètres
systeme.modifier_parametre("theme", "clair")
systeme.modifier_parametre("langue", "en")

# Ajouter des utilisateurs
systeme.ajouter_utilisateur("Alice")
systeme.ajouter_utilisateur("Bob")

# Créer un backup
backup_file = systeme.creer_backup()

# Afficher la config modifiée
systeme.afficher_config()

# Restaurer depuis backup (optionnel)
# systeme.restaurer_backup(backup_file)
```
