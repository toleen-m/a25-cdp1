EMPTY = " . "

def create_board():
    """
    Créer la grille 
    """
    return [
        [EMPTY, EMPTY, EMPTY ],
        [EMPTY, EMPTY, EMPTY ],
        [EMPTY, EMPTY, EMPTY ],
    ]

def position_to_coords(position):
    """
    convertir une position (1-9) en ligne et colonne
    
    :param position: Description
    """
    pos = position - 1
    row = pos // 3
    col = pos % 3
    return row, col

def is_empty(board, row, col):
    """
    vérifier si une case est vide
    
    :param board: Description
    :param row: Description
    :param col: Description
    """
    return board[row][col] == EMPTY

# placer un symbole
def place_symbol(board, row, col, symbol): 
    """
    Docstring for place_symbol
    
    :param board: Description
    :param row: Description
    :param col: Description
    :param symbol: Description
    """
    board[row][col] = symbol

