class User():
    ban = False 

    def __init__(self, name, email, age) -> None:
        self.name = name
        self.email = email 
        self.age = age 

    def _say_hi(self):
        print("Oh hi !")

    def bonjour(self, short:bool=False) : 
        if short : 
            self._say_hi()
        else : 
            print(f"Bonjour, je suis {self.name}.")

r = User("Neil", "neil@gmail.com", 16)
# print(r._say_hi())

# r._say_hi = "Je suis une chaine de caractères"
# print(r._say_hi)
r.bonjour(True)

print(dir(r))