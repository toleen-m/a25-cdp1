# Responsabilité : démarrer le jeu main.py doit :

# créer l’UI
# créer le jeu (en choisissant un mot secret)
# lancer la boucle principale jusqu’à victoire ou défaite

from hangman.game_state import GameState
from hangman.game import HangmanGame
from hangman.ui import ConsoleUI
from hangman.words import pick_secret_word

def main():
    ui = ConsoleUI()
    secret_word = pick_secret_word()
    state = GameState(secret_word, 9)

    game = HangmanGame(state)

    ui.show_status(state.guess_word, state.life)

    while True: 
        letter = ui.ask_letter()
        already_used = game.play_turn(letter)

        if already_used : 
            ui.message("Lettre déjà utilisée !")

        ui.show_status(state.guess_word, state.life)
        if state.is_won():
            ui.show_win()
            break

        if state.is_lose():
            ui.show_lose(state.secret_word)
            break

if __name__ == "__main__":
    main()