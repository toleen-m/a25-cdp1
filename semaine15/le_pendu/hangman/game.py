# Responsabilité : logique du jeu Vous devez créer une classe HangmanGame (ou Game) qui :

# possède un GameState
# gère un tour de jeu avec une méthode play_turn(letter)
# met à jour guess_word si lettre correcte
# enlève une vie si lettre incorrecte
# ne pénalise pas si la lettre a déjà été proposée (optionnel mais recommandé)
# Attendu : aucun input() ni print() dans ce fichier.

class HangmanGame:
    def __init__(self, game_state) -> None:
        self.game_state = game_state

    def play_turn(self, letter):
        letter = letter.lower()

        already_used = False

        if letter in self.game_state.used_letters :
            already_used = True
            return already_used
        
        self.game_state.used_letters.add(letter)

        if letter in self.game_state.secret_word:
            
            guess_list = list(self.game_state.guess_word)
            for index, current_letter in enumerate(self.game_state.secret_word):
                if current_letter == letter :
                    guess_list[index] = letter
            
            self.game_state.guess_word = "".join(guess_list)

        else : 
            self.game_state.life -=  1

        return already_used
        
        
