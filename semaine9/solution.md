# Solutions des Exercices

## Solution 1.1

```python
# Sortie: [1, 4, 5]
# La fonction retourne les éléments de liste1 qui ne sont PAS dans liste2
```

## Solution 1.2

```python
def statistiques(temperatures):
    if not temperatures:  # Gestion liste vide
        return None

    max_temp = temperatures[0]  # Éviter shadowing de max()
    min_temp = temperatures[0]

    for temp in temperatures:
        if temp > max_temp:  # Manquait :
            max_temp = temp
        if temp < min_temp:  # Manquait :
            min_temp = temp

    moyenne = sum(temperatures) / len(temperatures)  # len() pas .len()

    return (moyenne, max_temp, min_temp)
```

## Solution 2.1

```python
a = 5
b = 3

print("=== CALCULATRICE ===")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"Moyenne: {(a + b) / 2}")
```

## Solution 2.2

```python
class CompteBancaire:
    nombre_comptes = 0

    def __init__(self, titulaire, solde_initial=0):
        self.titulaire = titulaire
        self.solde = solde_initial
        CompteBancaire.nombre_comptes += 1
        print(f"Création de Compte: {titulaire}, solde: {solde_initial}")

    def deposer(self, montant):
        self.solde += montant
        print(f"Dépôt: {montant}, nouveau solde: {self.solde}")

    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            print(f"Retrait: {montant}, nouveau solde: {self.solde}")
            return True
        else:
            print(f"Retrait impossible: {montant} demandé, solde: {self.solde}")
            return False

    @classmethod
    def get_nombre_comptes(cls):
        return cls.nombre_comptes

# Test
compte1 = CompteBancaire("Alice", 100)
compte1.deposer(50)
compte1.retirer(30)
compte1.retirer(200)

compte2 = CompteBancaire("Bob", 500)
print(f"Nombre de comptes créés: {CompteBancaire.get_nombre_comptes()}")
```

## Solution 3.1

```python
def filtre_complexe(nombres, conditions):
    resultat = []

    for nombre in nombres:
        valide = True

        for operateur, valeur in conditions:
            if operateur == ">":
                if not nombre > valeur:
                    valide = False
                    break
            elif operateur == "<":
                if not nombre < valeur:
                    valide = False
                    break
            elif operateur == ">=":
                if not nombre >= valeur:
                    valide = False
                    break
            elif operateur == "<=":
                if not nombre <= valeur:
                    valide = False
                    break
            elif operateur == "==":
                if not nombre == valeur:
                    valide = False
                    break
            elif operateur == "%":  # Pair
                if not nombre % 2 == 0:
                    valide = False
                    break

        if valide:
            resultat.append(nombre)

    return resultat

# Test
nombres = [5, 12, 15, 20, 25, 30, 35]
conditions = [(">", 10), ("<", 30), ("%", 2)]
print(filtre_complexe(nombres, conditions))  # [12, 20]
```

## Solution 3.2

```python
import random

class Personne:
    noms = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry"]
    professions = ["Dev", "Designer", "Manager", "Testeur", "Analyste", "Architecte"]
    villes = ["Montréal", "Calgary", "Toronto", "Québec", "Vancouver", "Halifax"]

    def __init__(self, nom, age, profession, ville):
        self.nom = nom
        self.age = age
        self.profession = profession
        self.ville = ville

    @classmethod
    def generer_personne(cls):
        nom = random.choice(cls.noms)
        age = random.randint(18, 65)
        profession = random.choice(cls.professions)
        ville = random.choice(cls.villes)
        return cls(nom, age, profession, ville)

    @classmethod
    def generer_groupe(cls, n):
        groupe = []
        profiles_uniques = set()

        while len(groupe) < n:
            personne = cls.generer_personne()
            profile = (personne.nom, personne.age, personne.profession, personne.ville)

            if profile not in profiles_uniques:
                profiles_uniques.add(profile)
                groupe.append(personne)

        return groupe

    def __str__(self):
        return f"{self.nom}, {self.age} ans, {self.profession} à {self.ville}"

# Test
groupe = Personne.generer_groupe(3)
for p in groupe:
    print(p)
```

## Solution 4.1

```python
class Etudiant:
    def __init__(self, nom):
        self.nom = nom
        self.notes = []

    def ajouter_note(self, note):
        if note is not None:  # Gestion absence
            self.notes.append(note)

    def moyenne(self, ignore_min=True):
        if not self.notes:
            return 0

        notes_triees = sorted(self.notes)

        if ignore_min and len(notes_triees) > 3:
            notes_triees = notes_triees[1:]  # Ignore la plus basse

        return round(sum(notes_triees) / len(notes_triees), 2)

    def __str__(self):
        return f"{self.nom}: {self.moyenne()}"

class Matiere:
    def __init__(self, nom, coefficient=1):
        self.nom = nom
        self.coefficient = coefficient
        self.etudiants = []

    def inscrire(self, etudiant):
        self.etudiants.append(etudiant)

    def note_finale(self, etudiant):
        note_base = etudiant.moyenne()
        if self.coefficient > 2:
            return round(note_base * 30 / 20, 2)  # Sur 30
        else:
            return round(note_base, 2)  # Sur 20

    def classement(self):
        classement_trie = sorted(
            self.etudiants,
            key=lambda e: self.note_finale(e),
            reverse=True
        )
        return classement_trie

    def afficher_classement(self):
        print(f"Classement {self.nom}:")
        for i, etudiant in enumerate(self.classement(), 1):
            note = self.note_finale(etudiant)
            print(f"{i}. {etudiant.nom}: {note}/{'30' if self.coefficient > 2 else '20'}")

# Test
maths = Matiere("Maths", coefficient=3)
info = Matiere("Info", coefficient=1)

alice = Etudiant("Alice")
alice.ajouter_note(15)
alice.ajouter_note(18)
alice.ajouter_note(12)
alice.ajouter_note(10)  # Sera ignorée (4 notes > 3)

bob = Etudiant("Bob")
bob.ajouter_note(8)
bob.ajouter_note(14)
bob.ajouter_note(16)

maths.inscrire(alice)
maths.inscrire(bob)
info.inscrire(alice)
info.inscrire(bob)

maths.afficher_classement()
```

## Solution 4.2

```python
class Forme:
    def __init__(self, couleur):
        self.couleur = couleur

    def aire(self):
        raise NotImplementedError("Méthode abstraite")

    def perimetre(self):
        raise NotImplementedError("Méthode abstraite")

    def __str__(self):
        return f"{self.__class__.__name__} {self.couleur}"

class Rectangle(Forme):
    def __init__(self, couleur, longueur, largeur):
        super().__init__(couleur)
        self._longueur = longueur
        self._largeur = largeur

    @property
    def longueur(self):
        return self._longueur

    @longueur.setter
    def longueur(self, valeur):
        if valeur > 0:
            self._longueur = valeur

    @property
    def largeur(self):
        return self._largeur

    @largeur.setter
    def largeur(self, valeur):
        if valeur > 0:
            self._largeur = valeur

    def aire(self):
        return self.longueur * self.largeur

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)

class Carre(Rectangle):
    def __init__(self, couleur, cote):
        super().__init__(couleur, cote, cote)

    @property
    def cote(self):
        return self.longueur

    @cote.setter
    def cote(self, valeur):
        if valeur > 0:
            self.longueur = valeur
            self.largeur = valeur

    # Surcharge des setters pour garder égalité
    @Rectangle.longueur.setter
    def longueur(self, valeur):
        if valeur > 0:
            self._longueur = valeur
            self._largeur = valeur

    @Rectangle.largeur.setter
    def largeur(self, valeur):
        if valeur > 0:
            self._largeur = valeur
            self._longueur = valeur

class Cercle(Forme):
    def __init__(self, couleur, rayon):
        super().__init__(couleur)
        self.rayon = rayon

    def aire(self):
        import math
        return math.pi * self.rayon ** 2

    def perimetre(self):
        import math
        return 2 * math.pi * self.rayon

# Test
carre = Carre("rouge", 5)
print(f"Aire: {carre.aire()}")  # 25
print(f"Périmètre: {carre.perimetre()}")  # 20

carre.largeur = 10
print(f"Longueur après modification largeur: {carre.longueur}")  # 10
print(f"Aire nouvelle: {carre.aire()}")  # 100

cercle = Cercle("bleu", 3)
print(f"Aire cercle: {cercle.aire():.2f}")
print(f"Périmètre cercle: {cercle.perimetre():.2f}")
```

## Solution 5.1

```python
import random

class Personnage:
    def __init__(self, nom, points_vie=100, force=10, defense=5):
        self.nom = nom
        self.points_vie = points_vie
        self.force = force
        self.defense = defense
        self.niveau = 1
        self.experience = 0

    def attaquer(self, adversaire):
        # Calcul des dégâts
        degats = self.force - (adversaire.defense / 2)
        degats = max(1, degats)  # Minimum 1 dégât

        adversaire.points_vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} pour {degats:.1f} dégâts")

        if not adversaire.est_vivant():
            self.gagner_experience(50)
            print(f"{adversaire.nom} est vaincu! {self.nom} gagne 50 XP")

    def est_vivant(self):
        return self.points_vie > 0

    def gagner_experience(self, xp):
        self.experience += xp
        if self.experience >= 100:
            self.niveau += 1
            self.experience -= 100
            self.points_vie += 10
            self.force += 5
            print(f"{self.nom} atteint le niveau {self.niveau}!")

    def __str__(self):
        return f"{self.nom} Niv.{self.niveau} (PV: {self.points_vie:.1f})"

class Guerrier(Personnage):
    def __init__(self, nom):
        super().__init__(nom, points_vie=120, force=12, defense=6)
        # Bonus/malus
        self.force = int(self.force * 1.2)  # +20%
        self.defense = int(self.defense * 0.9)  # -10%

class Mage(Personnage):
    def attaquer(self, adversaire):
        # Les mages ignorent 50% de la défense
        degats = self.force - (adversaire.defense * 0.5)
        degats = max(1, degats)

        adversaire.points_vie -= degats
        print(f"{self.nom} lance un sort sur {adversaire.nom} pour {degats:.1f} dégâts")

        if not adversaire.est_vivant():
            self.gagner_experience(50)

class Archer(Personnage):
    def __init__(self, nom):
        super().__init__(nom, points_vie=90, force=15, defense=3)

    def attaquer(self, adversaire):
        # 30% chance d'esquiver pour l'adversaire
        if random.random() < 0.3:
            print(f"{adversaire.nom} esquive l'attaque de {self.nom}!")
            return

        super().attaquer(adversaire)

class Combat:
    def __init__(self, personnage1, personnage2):
        self.p1 = personnage1
        self.p2 = personnage2
        self.tour = 0

    def demarrer(self):
        print(f"=== COMBAT: {self.p1.nom} vs {self.p2.nom} ===")

        # Qui commence ?
        attaquant = random.choice([self.p1, self.p2])
        defenseur = self.p2 if attaquant == self.p1 else self.p1

        while self.p1.est_vivant() and self.p2.est_vivant():
            self.tour += 1
            print(f"\n--- Tour {self.tour} ---")

            attaquant.attaquer(defenseur)

            # Échange des rôles
            attaquant, defenseur = defenseur, attaquant

        vainqueur = self.p1 if self.p1.est_vivant() else self.p2
        print(f"\n=== {vainqueur.nom} remporte le combat en {self.tour} tours! ===")
        return vainqueur

# Test
guerrier = Guerrier("Conan")
mage = Mage("Merlin")
archer = Archer("Legolas")

combat1 = Combat(guerrier, mage)
combat1.demarrer()

print(f"\nStatut après combat:")
print(guerrier)
print(mage)
```
