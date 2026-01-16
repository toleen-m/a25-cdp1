**Exercices de Révision - Programmation Orientée Objet en Python**

**Objectif** : Retravailler les concepts de base de la POO vus en classe à travers des problèmes concrets.

**Exercice 1 : Classe de base et constructeur**
Créez une classe `AppareilElectronique` destinée à représenter un appareil électronique personnel (comme un smartphone ou une tablette).

1.  Le constructeur `__init__` doit initialiser les attributs `nom` (chaîne de caractères), `systeme_exploitation` (chaîne de caractères) et `niveau_batterie` (entier, avec une valeur par défaut à 100).
2.  Écrivez une méthode `decrire()` qui retourne une chaîne de caractères formatée comme suit : "[nom] fonctionne sous [systeme_exploitation]."

**Exercice 2 : Méthodes d'instance et self**
Ajoutez des méthodes à la classe `AppareilElectronique` pour gérer son état.

1.  Écrivez une méthode `utiliser(self, duree)` qui réduit le `niveau_batterie` de l'appareil. Chaque minute d'utilisation (`duree` est un entier représentant des minutes) consomme 2% de batterie. La batterie ne peut pas descendre en dessous de 0.
2.  Écrivez une méthode `recharger(self, duree)` qui augmente le `niveau_batterie`. Chaque minute de recharge (`duree` est un entier) restaure 10% de batterie. La batterie ne peut pas dépasser 100.

**Exercice 3 : Héritage et polymorphisme**
Créez deux classes qui héritent de `AppareilElectronique`.

1.  Créez une classe `Smartphone`. Son constructeur doit appeler le constructeur de la classe parente et ajouter un attribut supplémentaire : `numero_telephone` (chaîne de caractères).
2.  **Surchargez** (redéfinissez) la méthode `decrire()` dans la classe `Smartphone` pour que le texte retourné soit : "Smartphone [nom] ([systeme_exploitation]) - Numéro : [numero_telephone]."
3.  Créez une classe `Tablette`. Son constructeur doit appeler le constructeur de la classe parente et ajouter un attribut supplémentaire : `taille_ecran` (nombre décimal, en pouces).
4.  **Surchargez** la méthode `decrire()` dans la classe `Tablette` pour que le texte retourné soit : "Tablette [nom] - Écran de [taille_ecran] pouces."

**Exercice 4 : Encapsulation et propriétés**

1.  Dans la classe `AppareilElectronique`, rendez l'attribut `niveau_batterie` "privé" en utilisant la convention `_niveau_batterie`.
2.  Créez une **propriété** (`@property`) appelée `niveau_batterie` pour permettre un accès en lecture sécurisé à cet attribut privé.
3.  Créez un **setter** (avec `@niveau_batterie.setter`) pour cet attribut. Ce setter doit valider que la nouvelle valeur assignée est bien un entier compris entre 0 et 100 inclus. Si ce n'est pas le cas, il doit lever une exception `ValueError` avec un message d'erreur explicite.

**Exercice 5 : Méthodes de classe**
Ajoutez un mécanisme pour suivre le nombre total d'appareils créés.

1.  Dans la classe `AppareilElectronique`, déclarez une **variable de classe** appelée `nombre_appareils` initialisée à 0.
2.  Modifiez le constructeur `__init__` pour qu'il **incrémente** cette variable de classe à chaque fois qu'un nouvel objet est créé.
3.  Écrivez une **méthode de classe** `obtenir_statistiques(cls)` qui affiche le message : "Nombre total d'appareils créés : [nombre_appareils]."

Absolument. Voici une série d'exercices complémentaires qui ciblent spécifiquement la maîtrise des **différents types de méthodes, d'attributs et de paramètres** au sein d'une classe.

---

**Exercices Complémentaires - Types de méthodes, attributs et paramètres**

Ces exercices viennent **renforcer la compréhension fine des mécanismes internes** des classes. Ils permettent de bien distinguer ce qui appartient à l'instance (`self`), à la classe entière (`cls`), ou à aucun des deux (`@staticmethod`), et d'expérimenter avec différentes façons de recevoir des paramètres.

**Exercice 6 : Attributs d'instance, de classe et constants**
Créez une classe `CapteurMeteo` simulant un capteur de température.

1.  Le constructeur `__init__` prend un paramètre `identifiant` (chaîne) et initialise un **attribut d'instance** `identifiant`. Il initialise aussi un **attribut d'instance** `_temperature` à `None`.
2.  Déclarez un **attribut de classe** `unite = "Celsius"` qui est commun à tous les capteurs.
3.  Déclarez une **constante de classe** `SEUIL_ALERTE = 40.0` (une température au-delà de laquelle on alerte).
4.  Créez une méthode `mesurer(self, nouvelle_temp)` qui met à jour l'attribut `_temperature` et affiche un message d'alerte si `nouvelle_temp` dépasse `SEUIL_ALERTE`.

**Exercice 7 : Méthodes d'instance, de classe et statiques**
Ajoutez les fonctionnalités suivantes à la classe `CapteurMeteo` :

1.  **Méthode d'instance** : `afficher(self)` qui retourne une chaîne formatée : `"Capteur [identifiant] : [temperature] °[unite]"`.
2.  **Méthode de classe** : `changer_unite(cls, nouvelle_unite)` qui modifie l'attribut de classe `unite` pour tous les capteurs. Validez que `nouvelle_unite` est soit `"Celsius"` soit `"Fahrenheit"`.
3.  **Méthode statique** : `convertir_en_fahrenheit(temperature_celsius)` qui prend une température en Celsius et retourne la conversion en Fahrenheit selon la formule `(temperature_celsius * 9/5) + 32`. Cette méthode n'a pas besoin de connaître l'état d'un capteur spécifique.

**Exercice 8 : Paramètres de méthodes (self, cls, paramètres normaux, paramètres par défaut, \*args)**
Créez une classe `StationMeteo` qui agrège plusieurs capteurs.

1.  Le constructeur prend un paramètre obligatoire `ville` et un paramètre optionnel `*capteurs` (un nombre variable d'instances de `CapteurMeteo`). Il les stocke dans une liste d'**attribut d'instance** `capteurs`.
2.  Créez une méthode `ajouter_capteurs(self, *nouveaux_capteurs)` qui permet d'ajouter un ou plusieurs capteurs supplémentaires à la station.
3.  Créez une méthode `resume(self, details=False)` :
    - Si `details` est `False` (valeur par défaut), elle affiche `"Station de [ville] : [nombre] capteur(s)."`
    - Si `details` est `True`, elle affiche en plus la sortie de `afficher()` pour chaque capteur.

**Exercice 9 : Utilisation de **dict** et introspection basique**
Dans la classe `StationMeteo`, ajoutez une méthode `inspecter(self, nom_attribut=None)`.

1.  Si aucun argument n'est passé (`nom_attribut` est `None`), la méthode affiche les clés et valeurs du dictionnaire `self.__dict__` qui représente les attributs d'instance.
2.  Si un `nom_attribut` (chaîne) est passé, la méthode vérifie si cet attribut existe pour cette instance (en utilisant `hasattr(self, nom_attribut)`) et affiche sa valeur si c'est le cas, ou un message d'erreur sinon.
