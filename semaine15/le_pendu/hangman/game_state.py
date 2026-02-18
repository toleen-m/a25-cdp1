# Responsabilité : représenter l’état du jeu Vous devez créer une classe GameState qui contient :

# secret_word (str)
# guess_word (str, avec _)
# life (int)
# Et au moins ces méthodes :

# is_won() → True/False
# is_lost() → True/False

class GameState:
    def __init__(self, secret_word, life) -> None:
        self.secret_word = secret_word
        self.life = life 
        self.guess_word = "_" * len(secret_word)
        self.used_letters = set()

    def is_won(self):
        return self.guess_word == self.secret_word
    
    def is_lose(self):
        return self.life <= 0