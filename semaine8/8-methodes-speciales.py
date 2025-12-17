from typing import Any


class User():
    ban = False
    notes = []

    def __init__(self, nom, email, age, notes) -> None:
        print("À partir du User __init__")
        if age < 16:
            self.ban = True
        self.nom = nom 
        self.email = email 
        self.age = age 
        self.notes = notes

    def _say_hi(self):
        print("Bonjour")

    def bonjour(self, short: bool = False):
        if short:
            self._say_hi()
        else:
            print(f"Bonjour, je suis {self.nom} !")
    def __str__(self) -> str:
        return f"Nom: {self.nom}, Email: {self.email}, Âge: {self.age}"
    
    def __eq__(self, value) -> bool:
        return self.nom == value.nom and self.email == value.email and self.age == value.age
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(f"{self.nom} est executé(e) !")

    def __getitem__(self, cle): 
        print(f"La réponse est {self.notes[cle]}")
    

un_user = User("Fabiola", "fabiola@gmail.com", 22, {"anglais": 82, "math" : 75, "python": 98})
# un_user3 = User("Fabiola", "fabiola@gmail.com", 22)
# un_user2 = User("Fatima", "fatima@gmail.com", 23)
# print(dir(un_user))
# print(un_user.__dir__())

# num = 45
# print(45 + 12)
# print(num.__add__(12))

# print(un_user.__str__())
# print(un_user2.__str__())

# print(un_user == un_user3)

# un_user()

un_user["python"]