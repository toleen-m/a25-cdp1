# Corrigés — pip, PyPI, environnements virtuels (débutants)

## Exercice 1 — Vérifier Python et pip

### Commandes attendues

**Windows**

```bash
python --version
pip --version
where python
where pip
```

**macOS / Linux**

```bash
python3 --version
pip3 --version
which python3
which pip3
```

### Sorties attendues (exemples)

- `Python 3.x.x`
- `pip x.x.x from .../site-packages/pip (python 3.x)`
- Chemin vers l’exécutable Python et pip

---

## Exercice 2 — Installer un premier package (colorama)

### Commandes

```bash
pip install colorama
pip show colorama
pip list
```

### Sorties attendues (exemple)

- `Successfully installed colorama-0.4.6`
- `pip show colorama` affiche :
  - Name: colorama
  - Version: 0.4.6
  - Location: ...site-packages

---

## Exercice 3 — Utiliser `colorama` dans un script

### `test_colorama.py`

```python
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.RED + "Texte rouge")
print(Fore.GREEN + "Texte vert")
print(Fore.BLUE + "Texte bleu")
print(Style.RESET_ALL + "Retour normal")
```

### Exécution

```bash
python test_colorama.py
```

Résultat attendu : les textes s’affichent en couleurs (sur Windows, `init()` aide beaucoup).

---

## Exercice 4 — Installer et utiliser un package trouvé sur PyPI (`emoji`)

### Installation

```bash
pip install emoji
pip show emoji
```

### `test_emoji.py`

```python
import emoji

print(emoji.emojize("Python est amusant :snake:"))
print(emoji.emojize("Je code :laptop: :rocket:"))
```

### Exécution

```bash
python test_emoji.py
```

Résultat attendu : emojis affichés (si le terminal supporte les emojis).

---

## Exercice 5 — Comprendre le problème “global”

### “Réponse attendue”

Installer tout globalement peut causer :

- conflits de versions (un projet veut `requests==2.28`, un autre veut `2.32`)
- pollution de l’environnement (trop de packages inutiles)
- difficile de reproduire un projet sur une autre machine
- risque de casser un projet en mettant à jour un package “pour un autre projet”

---

## Exercice 6 — Créer un environnement virtuel

### Commandes

**Windows**

```bash
python -m venv env
```

**macOS / Linux**

```bash
python3 -m venv env
```

Attendu : un dossier `env/` apparaît.

---

## Exercice 7 — Activer / désactiver l’environnement

### Activation

**Windows (cmd)**

```bash
env\Scripts\activate
```

**Windows (PowerShell)**

```powershell
env\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source env/bin/activate
```

### Vérification

```bash
python --version
pip --version
```

Attendu : le prompt commence par `(env)`.

### Désactivation

```bash
deactivate
```

---

## Exercice 8 — Installer dans l’environnement

### Commandes

```bash
pip install colorama emoji
pip list
```

Attendu : dans `(env)`, la liste est “courte” et contient `colorama` et `emoji`.

---

## Exercice 9 — Vérifier l’isolation (preuve simple)

### Dans l’environnement `(env)`

```bash
pip show colorama
```

Puis :

```bash
deactivate
pip show colorama
```

Attendu :

- Dans `(env)` → `colorama` est trouvé
- Hors env → **soit** `Package(s) not found`, **soit** il est trouvé si installé globalement avant.

---

## Exercice 10 — Mini projet (couleur + emoji)

### Commandes (dans env)

```bash
pip install colorama emoji
```

### `main.py`

```python
from colorama import Fore, Style, init
import emoji

init(autoreset=True)

print(Fore.BLUE + emoji.emojize("Bonjour :smile:"))
print(Fore.MAGENTA + emoji.emojize("On code en Python :snake:"))
print(Style.RESET_ALL + "Fin du programme")
```

### Exécution

```bash
python main.py
```

---

## Exercice 11 — Générer `requirements.txt`

### Commande

```bash
pip freeze > requirements.txt
```

### Exemple de `requirements.txt`

```txt
colorama==0.4.6
emoji==2.10.1
```

Important : les versions peuvent différer selon la date d’installation.

---

## Exercice 12 — Reproduire l’environnement à partir de requirements

### Étapes attendues

1. Désactiver et supprimer `env/` (ou le renommer)
2. Recréer l’environnement :

```bash
python -m venv env
```

3. Activer :

```bash
env\Scripts\activate
```

4. Installer :

```bash
pip install -r requirements.txt
```

5. Vérifier :

```bash
pip list
python main.py
```

Attendu : le projet refonctionne sans réinstaller “à la main”.

---

## Bonus — `pyfiglet`

### Installation

```bash
pip install pyfiglet
```

### `test_pyfiglet.py`

```python
import pyfiglet

print(pyfiglet.figlet_format("Python"))
print(pyfiglet.figlet_format("Hello class!"))
```

---

# Corrigé “structure de projet” attendue (exemple)

```
mon_projet/
├── env/                # environnement virtuel (à ne pas versionner)
├── main.py
├── requirements.txt
├── test_colorama.py
├── test_emoji.py
└── test_pyfiglet.py
```

Bonus : faire créer aussi un `.gitignore` avec au minimum :

```txt
env/
__pycache__/
*.pyc
```
