name = "Lilia"

class User():

    def __init__(self, name, email, age) -> None:
        self.name = name
        self.email = email 
        self.age = age

    def bonjour(self, short:bool=False) -> bool:
        if short : 
            print("Bonjour !")
        else : 
            print(f"Bonjour, je suis {self.name}.")
        return short

z = User("Clément", "clement@gmail.com", 15)
resultat = z.bonjour()
print(resultat)