class User():
    ban = False

    def __init__(self, name, email, age) -> None:
        self.name = name
        self.email = email  
        self.age = age

    def bonjour(self, short:bool=False) -> bool: 
        if short:
            print("Bonjour !")
        else : 
            print(f"Bonjour, je suis {self.name}.")
        return short

    @classmethod
    def another_constructor(cls):
        return cls("Unknown", "unknown", 0)
    
    @staticmethod
    def is_ban(a_user):
        return a_user.age <= 16


t = User("Marie-Ève", "marie-eve@gmail.com", 27)
print(t.bonjour())

w = User.another_constructor()
print(w.bonjour())

print(User.is_ban(t))