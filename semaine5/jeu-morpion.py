# . . .
# . . .
# . . .
valeur_nulle = ' . '
valeur_1 = ' O '
valeur_2 = ' X '

# La map du morpion
la_map = [
    [valeur_nulle, valeur_nulle, valeur_nulle],
    [valeur_nulle, valeur_nulle, valeur_nulle],
    [valeur_nulle, valeur_nulle, valeur_nulle]
]

joueur_en_cours = "Joueur 1" 

# Fonction pour dessiner la map
def draw(): 
    for i in range(3):
        for j in range(3):
            print(la_map[i][j], end="")
        print()

# Fonction qui explore toutes les possibilité pour quil y ait un gagnant 
def check_win():
    # Vérifier si nous n'avons pas le même symbole sur les lignes
    for i in range(3):
        if la_map[i][0] == la_map[i][1] == la_map[i][2] != valeur_nulle :
            return True
        
    # Vérifier si nous n'avons pas le même symbole sur les colonnes 
    for j in range(3):
        if la_map[0][j] == la_map[1][j] == la_map[2][j] != valeur_nulle:
            return True
    
    # Vérifier les diagonales 
    if la_map[0][0] == la_map[1][1] == la_map[2][2] != valeur_nulle :
        return True
    if la_map[0][2] == la_map[1][1] == la_map[2][0] != valeur_nulle :
        return True

# Vérifier qu'il ne reste plus de point vide
def check_map(): 
    for i in range(3):
        for j in range(3):
            if la_map[i][j] == valeur_nulle:
                return False
    return True

# Premier dessin de la map
draw()

# Lancement du jeu
while True: 
    # Demander au joueur d'entrer son choix 
    # Vérifier la matrice 
    # Si un jour gagne ou la partie est égale on fait un break
    entree = int(input(f"{joueur_en_cours} [1-9] ? > "))

    ligne = (entree - 1) // 3 # 2
    colonne = (entree - 1) % 3 # 0

    if la_map[ligne][colonne] == valeur_nulle:
        la_map[ligne][colonne] = valeur_1 if joueur_en_cours == 'Joueur 1' else valeur_2

    draw()
    print(entree)

    # Vérifier s'il y a un gagnant
    if check_win():
        print(f"{joueur_en_cours} a gagné ! ")
        break

    # Vérifier si la partie est nulle
    if check_map():
        print("Match nul !")
        break
    
    # Si personne ne gagne, vérifier si la map n'est pas pleine
    # Si la map est pleine, c'est match nul

    joueur_en_cours = "Joueur 1" if joueur_en_cours == "Joueur 2" else "Joueur 2"


# Ajouter la logique qui permet à un joueur de recommancer si son entrée est déjà prise, ou est invalide (entree qui n'est pas entre le 1 et le 9)