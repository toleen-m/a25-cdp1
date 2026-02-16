# Responsabilités :

# créer la grille
# afficher la grille
# placer un symbole
# vérifier victoire
# vérifier égalité

class Board:
    EMPTY = " . "

    def __init__(self, size=3) -> None:
        self.size = size
        self.grid = [[self.EMPTY for _ in range(size)] for _ in range(size)]

    def draw(self):
        for row in self.grid:
            for cell in row:
                print(cell, end="")
            print()

    def is_empty(self, row, col):
        return self.grid[row][col] == self.EMPTY

    def place(self, row, col, symbol):
        """
        Place un symbole si la case est libre. Renvoie True si tout est ok et False si la case est occupée
        
        :param self: Description
        :param row: Description
        :param cell: Description
        :param symbol: Description
        """
        if not self.is_empty(row, col):
            return False  
        self.grid[row][col] = symbol
        return True
    
    def position_to_coords(self, position):
        """
        Convertir une position en colomne et ligne
        
        :param self: Description
        :param position: Description
        """
        pos = position - 1
        return pos // self.size, pos % self.size
    
    def is_winner(self):
        """
        Retourne True si gagnant et False sinon
        
        :param self: Description
        """

        # Lignes
        for i in range(self.size):
            if self.grid[i][0] != self.EMPTY and all(self.grid[i][j] == self.grid[i][0] for j in range(self.size)):
                return True
            
        # Colonnes
        for j in range(self.size):
            if self.grid[0][j] != self.EMPTY and all(self.grid[i][j] == self.grid[0][j] for i in range(self.size)):
                return True
            
        # Diagonale principale 
        if self.grid[0][0] != self.EMPTY and all(self.grid[i][i] == self.grid[0][0] for i in range(self.size)):
            return True

        # Diagonale secondaire
        if self.grid[0][self.size - 1] != self.EMPTY and all(self.grid[i][self.size - 1 - i] == self.grid[0][self.size - 1] for i in range(self.size)):
            return True
        
        return False
    
    def is_draw(self):
        """
        Retourne True si galité, False sinon
        
        :param self: Description
        """
        return all( cell != self.EMPTY for ligne in self.grid for cell in ligne)