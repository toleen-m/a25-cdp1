# contenir la liste de mots (ou une chaîne de mots)
# fournir une fonction (ou méthode) pour choisir un mot aléatoire
# Attendu (minimum) : une fonction pick_secret_word().

import random

WORDS = "pointu raser ruisseau pastorale chiens cadre meteorite effacer naissance facteur".split()

def pick_secret_word():
    """
    choisir un mot aléatoire
    """
    return random.choice(WORDS)