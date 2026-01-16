**Solutions des Exercices**

**Solution Exercice 1 & 2**

```python
class AppareilElectronique:
    nombre_appareils = 0  # Pour l'exercice 5

    def __init__(self, nom, systeme_exploitation, niveau_batterie=100):
        self.nom = nom
        self.systeme_exploitation = systeme_exploitation
        self._niveau_batterie = niveau_batterie  # Privé pour l'exercice 4
        AppareilElectronique.nombre_appareils += 1  # Pour l'exercice 5

    def decrire(self):
        return f"{self.nom} fonctionne sous {self.systeme_exploitation}."

    def utiliser(self, duree):
        consommation = duree * 2
        nouveau_niveau = self._niveau_batterie - consommation
        self._niveau_batterie = max(0, nouveau_niveau)

    def recharger(self, duree):
        recharge = duree * 10
        nouveau_niveau = self._niveau_batterie + recharge
        self._niveau_batterie = min(100, nouveau_niveau)
```

**Solution Exercice 3**

```python
class Smartphone(AppareilElectronique):
    def __init__(self, nom, systeme_exploitation, numero_telephone, niveau_batterie=100):
        super().__init__(nom, systeme_exploitation, niveau_batterie)
        self.numero_telephone = numero_telephone

    def decrire(self):
        return f"Smartphone {self.nom} ({self.systeme_exploitation}) - Numéro : {self.numero_telephone}."

class Tablette(AppareilElectronique):
    def __init__(self, nom, systeme_exploitation, taille_ecran, niveau_batterie=100):
        super().__init__(nom, systeme_exploitation, niveau_batterie)
        self.taille_ecran = taille_ecran

    def decrire(self):
        return f"Tablette {self.nom} - Écran de {self.taille_ecran} pouces."
```

**Solution Exercice 4**

```python
# Ajout à la classe AppareilElectronique
    @property
    def niveau_batterie(self):
        return self._niveau_batterie

    @niveau_batterie.setter
    def niveau_batterie(self, valeur):
        if not isinstance(valeur, int):
            raise ValueError("Le niveau de batterie doit être un entier.")
        if valeur < 0 or valeur > 100:
            raise ValueError("Le niveau de batterie doit être compris entre 0 et 100.")
        self._niveau_batterie = valeur
```

**Solution Exercice 5**

```python
# La variable de classe et son incrémentation sont déjà dans la solution Exercice 1 & 2.

# Ajout à la classe AppareilElectronique
    @classmethod
    def obtenir_statistiques(cls):
        print(f"Nombre total d'appareils créés : {cls.nombre_appareils}.")
```

**Exemple d'utilisation et tests**

```python
# Création d'instances
tel = Smartphone("Pixel", "Android", "0123456789")
tab = Tablette("iPad Air", "iPadOS", 10.9)

# Test des méthodes
print(tel.decrire())
print(tab.decrire())

tel.utiliser(30)
print(f"Batterie après utilisation: {tel.niveau_batterie}%")
tel.recharger(10)
print(f"Batterie après recharge: {tel.niveau_batterie}%")

# Test de la propriété/setter
try:
    tel.niveau_batterie = 105
except ValueError as e:
    print(f"Erreur: {e}")

# Test de la méthode de classe
AppareilElectronique.obtenir_statistiques()
```

---

**Solutions des Exercices Complémentaires**

**Solution Exercice 6 & 7**

```python
class CapteurMeteo:
    # Attribut de classe et constante
    unite = "Celsius"
    SEUIL_ALERTE = 40.0

    def __init__(self, identifiant):
        # Attributs d'instance
        self.identifiant = identifiant
        self._temperature = None

    def mesurer(self, nouvelle_temp):
        self._temperature = nouvelle_temp
        if nouvelle_temp > self.SEUIL_ALERTE:
            print(f"[ALERTE] Température {nouvelle_temp}°{self.unite} dépasse le seuil !")

    # Méthode d'instance
    def afficher(self):
        return f"Capteur {self.identifiant} : {self._temperature} °{self.unite}"

    # Méthode de classe
    @classmethod
    def changer_unite(cls, nouvelle_unite):
        if nouvelle_unite in ("Celsius", "Fahrenheit"):
            cls.unite = nouvelle_unite
            print(f"Unité changée pour tous les capteurs : {cls.unite}")
        else:
            print("Unité non reconnue.")

    # Méthode statique
    @staticmethod
    def convertir_en_fahrenheit(temperature_celsius):
        return (temperature_celsius * 9/5) + 32
```

**Solution Exercice 8**

```python
class StationMeteo:
    def __init__(self, ville, *capteurs):
        self.ville = ville
        self.capteurs = list(capteurs) # *capteurs est un tuple, on le convertit en liste

    def ajouter_capteurs(self, *nouveaux_capteurs):
        self.capteurs.extend(nouveaux_capteurs) # extend ajoute plusieurs éléments à une liste

    def resume(self, details=False):
        print(f"Station de {self.ville} : {len(self.capteurs)} capteur(s).")
        if details:
            for capteur in self.capteurs:
                print(f"  - {capteur.afficher()}")
```

**Solution Exercice 9**

```python
# Ajout à la classe StationMeteo
    def inspecter(self, nom_attribut=None):
        if nom_attribut is None:
            print("=== Inspection complète ===")
            for cle, valeur in self.__dict__.items():
                print(f"  {cle}: {valeur}")
        else:
            if hasattr(self, nom_attribut):
                print(f"Attribut '{nom_attribut}': {getattr(self, nom_attribut)}")
            else:
                print(f"Attribut '{nom_attribut}' non trouvé.")
```

**Exemple d'utilisation et tests des nouveaux exercices**

```python
# Création de capteurs
c1 = CapteurMeteo("SALON")
c2 = CapteurMeteo("JARDIN")

# Test attributs/classe/instance et méthodes
c1.mesurer(22.5)
print(c1.afficher()) # Capteur SALON : 22.5 °Celsius
c2.mesurer(42.0) # Déclenche l'alerte

# Test méthode de classe
CapteurMeteo.changer_unite("Fahrenheit")
print(c1.unite) # Fahrenheit (affecte c1 et c2)

# Test méthode statique
temp_f = CapteurMeteo.convertir_en_fahrenheit(25)
print(f"25°C = {temp_f}°F")

# Test StationMeteo avec *capteurs
station = StationMeteo("Paris", c1)
station.ajouter_capteurs(c2) # Utilisation de *args
station.resume()
station.resume(details=True)

# Test introspection
station.inspecter()
station.inspecter('ville')
station.inspecter('inexistant')
```
