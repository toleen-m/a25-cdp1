from .board import Board

# Responsabilités :

# gérer le joueur courant
# gérer les tours
# gérer la boucle du jeu
# détecter la fin de partie

class Game:
    PLAYER_1 = "Joueur 1"
    PLAYER_2 = "Joueur 2"
    SYMBOL_1 = " X "
    SYMBOL_2 = " O "

    def __init__(self, ui, board=None) -> None:
        self.ui = ui
        self.board = board if board is not None else Board()
        self.current_player = self.PLAYER_1

    def switch_player(self):
        self.current_player = self.PLAYER_1 if self.current_player == self.PLAYER_2 else self.PLAYER_2

    def get_symbol(self):
        return self.SYMBOL_1 if self.current_player == self.PLAYER_1 else self.SYMBOL_2

    def play_turn(self):
        pos = self.ui.ask_position(self.board.size, self.current_player)
        row, col = self.board.position_to_coords(pos)
        symbol = self.get_symbol()

        if not self.board.place(row, col, symbol):
            self.ui.message("Case prise, recommencez : ")
            return False
        
        return True
    
    def run(self):
        self.board.draw()

        while True: 
            played = self.play_turn()
            if not played:
                continue

            self.board.draw()

            if self.board.is_winner():
                self.ui.message(f"{self.current_player} a gagné !")
                break

            if self.board.is_draw():
                self.ui.message("Égalité !")
                break

            self.switch_player()
