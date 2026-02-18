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
    
    def run(self, ui):
        ui.show_status(self.game_state.guess_word, self.game_state.life)

        while True: 
            letter = ui.ask_letter()
            already_used = self.play_turn(letter)

            if already_used : 
                ui.message("Lettre déjà utilisée !")

            ui.show_status(self.game_state.guess_word, self.game_state.life)
            if self.game_state.is_won():
                ui.show_win()
                break

            if self.game_state.is_lose():
                ui.show_lose(self.game_state.secret_word)
                break
        
        
