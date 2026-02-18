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

    while True: 
        nbr_vies = ui.ask_life_count()
        secret_word = pick_secret_word()
        state = GameState(secret_word, nbr_vies)
        game = HangmanGame(state)

        game.run(ui)

        if ui.ask_replay():
            ui.message("\nNouvelle partie !")
        else: 
            ui.message("\nAu revoir !")
            break

    

if __name__ == "__main__":
    main()