from .board import EMPTY

def is_winner(board):
    """
    vérifier si un joueur a gagné
    
    :param board: Description
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return True
        
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return True
        
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return True
    
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return True
    
    return False

def is_draw(board):
    """
    vérifier s'il y a une égalité
    
    :param board: Description
    """
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True