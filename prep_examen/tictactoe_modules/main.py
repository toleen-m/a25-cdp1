# importer les modules
from tictactoe.board import create_board, position_to_coords, is_empty, place_symbol
from tictactoe.rules import is_winner, is_draw
from tictactoe.ui import show_message, draw_board, ask_position

PLAYER_1 = "Joueur 1"
PLAYER_2 = "Joueur 2"
SYMBOL_1 = " X "
SYMBOL_2 = " O "

def switch_player(current_player):
    """
    gérer le joueur courant
    
    :param current_player: Description
    """
    return PLAYER_1 if current_player == PLAYER_2 else PLAYER_2

def get_symbol(player):
    """
    Associer le bon symbol au player
    
    :param player: Description
    """
    return SYMBOL_1 if player == PLAYER_1 else SYMBOL_2

def main():
    """
    la boucle principale du je
    """
    board = create_board()
    current_player = PLAYER_1

    draw_board(board)
    while True: 
        pos = ask_position(current_player)
        row, col = position_to_coords(pos)

        if not is_empty(board, row, col):
            show_message("Case est déjà prise. Veuillez recommencer ! ")
            continue

        place_symbol(board, row, col, get_symbol(current_player))
        draw_board(board)

        if is_winner(board):
            show_message(f"\n{current_player} a gagné !")
            break
        if is_draw(board):
            show_message("\nÉgalité !")
            break

        current_player = switch_player(current_player)

if __name__ == "__main__":
    main()


 