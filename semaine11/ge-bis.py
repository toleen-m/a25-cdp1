from random import randint

# nbr_secret = randint(0, 1000)

# while True: 
#     nbr = int(input("Devinez le numbre secret > "))
#     if nbr == nbr_secret: 
#         print("Trouvé !")
#         break
#     elif nbr > nbr_secret: 
#         print("Le nombre secret est plus petit")
#     else: 
#         print("Le nombre secret est plus grand")

# print(TypeError.mro())
# print(ValueError.mro())

# ------------------

# nbr_secret = randint(0, 1000)
# nbr_essais = 0

# while True: 
#     try : 
#         nbr = int(input("Devinez le numbre secret > "))
#     except ValueError : 
#         print("Oups, il y a eu une exception ! ")
#     else :
#         if nbr == nbr_secret: 
#             print("Trouvé !")
#             break
#         elif nbr > nbr_secret: 
#             print("Le nombre secret est plus petit")
#         else: 
#             print("Le nombre secret est plus grand")
#     finally: 
#         nbr_essais += 1
#         print(f"essai no : {nbr_essais}")

# -----------------------

# nbr_secret = randint(0, 1000)
# nbr_essais = 0

# def check_input(chaise): 
#     if chaise == nbr_secret:
#         print("Bravo")
#         return True
#     elif chaise > nbr_secret:
#         print("Le nombre secret est plus petit")
#     else:
#         print("Le nombre secret est plus grand")

# while True: 
#     try : 
#         nbr = int(input("Devinez le numbre secret > "))
#     except ValueError as patate : 
#         print(patate)
#     else :
#         if check_input(nbr):
#             break
#     finally: 
#         nbr_essais += 1
#         print(f"essai no : {nbr_essais}")


# -----------------------

nbr_secret = randint(0, 1000)
nbr_essais = 0

class IncorrectNumberError(Exception):
    def __init__(self, message, nbr) -> None:
        self.message = message
        self.nbr = nbr
    def __str__(self) -> str:
        return f"{self.nbr} : {self.message}"

def check_input(chaise): 
    if chaise == nbr_secret:
        print("Bravo")
        return True
    elif chaise > nbr_secret:
        raise IncorrectNumberError("Le nombre secret est plus petit", chaise)
    else:
        raise IncorrectNumberError("Le nombre secret est plus grand", chaise)

while True: 
    try : 
        nbr = int(input("Devinez le numbre secret > "))
    except ValueError as patate : 
        print(patate)
    else :
        try:
            if check_input(nbr):
                break
        except IncorrectNumberError as err:
            print(err)
    finally: 
        nbr_essais += 1
        print(f"essai no : {nbr_essais}")