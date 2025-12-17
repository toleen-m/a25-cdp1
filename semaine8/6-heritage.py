class User():
    ban = False

    def __init__(self, nom, email, age) -> None:
        print("À partir du User __init__")
        if age < 16:
            self.ban = True
        self.nom = nom 
        self.email = email 
        self.age = age 

    def _say_hi(self):
        print("Bonjour")

    def bonjour(self, short: bool = False):
        if short:
            self._say_hi()
        else:
            print(f"Bonjour, je suis {self.nom} !")

class Hacker():
    def __init__(self, attack_type: str) -> None:
        self.attack_type = attack_type

    def attack(self, ip: str):
        print(f"{self.attack_type} launch on {ip}")

class Admin(Hacker, User): 

    def __init__(self, nom, email, age, origine, attack_type) -> None:
        # super().__init__(nom, email, age)
        User.__init__(self, nom, email, age)
        Hacker.__init__(self, attack_type)
        self.origine = origine 


    def delete_user(self, user: User): 
        print(f"Le user {user.email} a été supprimé ! ")

    def bonjour(self, short: bool = False):
        # return super().bonjour(short)
        print("Bonjour, je suis l'Admin.")
     

class Entreprise(User):
    pass 

admin = Admin("Jean", "jean@gmail.com", 25, "Hochelaga", "ddos")
user = User("Émile", "emile@gmail.com", 16)

# admin.bonjour()
# admin.delete_user(user)

# isinstance issubclass 
# print(isinstance(admin, Admin))
# print(isinstance(admin, User))
# print(isinstance(admin, object))

# a = 1 
# print(isinstance(a, object))

# print(issubclass(Admin, User))
# print(issubclass(Admin, object))
# print(issubclass(User, object))
# print(issubclass(User, Admin))

admin.attack("127.0.0.1")

