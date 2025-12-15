class User():
    # Passer des paramètres au constructeur
    def __init__(self, name, email, age) -> None:
        # attributs
        self.name = name
        self.email = email
        self.age = age
        
        
# x et y sont des instances de la classe User
x = User("Mathieu", "mathieu@gmail.com", 19)
y = User("Eva", "eva@gmail.com", 22)
print(x.name)
print(x.email)
print(x.age)
print(y.name)
print(y.email)
print(y.age)