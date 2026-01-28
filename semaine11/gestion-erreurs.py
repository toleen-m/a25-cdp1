from random import randint

nbr_secret = randint(0, 1000)
nbr_d_essai = 0

# class NumberTooBigError(Exception):
#     def __init__(self, message) -> None:
#         self.message = message

# class NumberTooSmallError(Exception): 
#     def __init__(self, message) -> None:
        # self.message = message 

class NumberIncorrect(Exception):
    def __init__(self, message, nbr) -> None:
        self.message = message
        self.nbr = nbr
    
    def __str__(self) -> str:
        return f"{self.nbr} : {self.message}"

def deal_input(nbr): 
    if nbr == nbr_secret:
        print("Bravo")
        return True
    elif nbr > nbr_secret:
        raise NumberIncorrect("Le nombre secret est plus petit.", nbr)
    else: 
        raise NumberIncorrect("Le nombre secret est plus grand.", nbr)

while True: 
    try :
        nbr = int(input("Veuillez entrer un nombre > "))
    except ValueError as err: 
        print("Veuillez rentrer un nombre.")         
    else : 
        try: 
           if deal_input(nbr) : 
               break
        except NumberIncorrect as err :
            print(err)
    finally : 
        nbr_d_essai += 1
        print(f"Essai numéro : {nbr_d_essai}")
    