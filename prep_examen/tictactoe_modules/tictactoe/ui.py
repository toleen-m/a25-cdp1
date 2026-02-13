from Exceptions.nombreInvalideException import NombreInvalideException

def draw_board(board):
    """
    afficher la grille
    
    :param board: Description
    """
    for row in board:
        for cell in row:
            print(cell, end='')
        print()

def ask_position(player_name):
    """
    demander une position au joueur
    un message d'erreur si l'utilisateur entre une mauvaise valeur
    
    :param player_name: Description
    """
    while True: 
        try: 
            pos = int(input(f"\n{player_name} [1-9] ? > "))

            if pos < 1 or pos > 9 : 
                raise NombreInvalideException("Erreur: choisissez un nombre entre 1 et 9")
            
            return pos

        except ValueError:
            print("Erreur: entrez un nombre valide !") 
        except NombreInvalideException as nie:
            print(nie)

def show_message(message):
    """
    afficher un message
    
    :param message: Description
    """
    print(message)

