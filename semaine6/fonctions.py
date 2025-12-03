# -- définition des fonctions

def le_nom_de_la_fonction():
    print("Hello World !")

# le_nom_de_la_fonction()

# -- retourner des valeurs 

def le_nom_de_la_fonction_2():
    return "Hello World ! 2"
    print("!!!!!")

# a = le_nom_de_la_fonction()
# print('14', a)

b = le_nom_de_la_fonction_2()
# print('17', b)

def multiple_retours():
    return 'Salut', 'Comment ça va?', 1, True

c = multiple_retours()
# print(c)

# -- Les paramètres

def addition_entre_deux_nombres(a, b = 2): 
    return a + b

resultat = addition_entre_deux_nombres(8)
resultat2 = addition_entre_deux_nombres(8, 8)
# print(resultat)
# print(resultat2)

def greetings(nom, prenom):
    print(f"Bonjour {prenom} {nom}")

# greetings("Ould Hocine", "Lilia")
# greetings("Lilia", "Ould Hocine") # faux
# greetings(prenom="Lilia", nom="Ould Hocine")

# print("Salut", "Lilia", end="")
# print("test")

a = "Je suis a"  # immuable 
def my_func(b):
    b = 2
    print(b is a)

# my_func(a)
# print(a)

c = [1, 2]
def my_func_muable(b):
    b.append(3)
    print(c is b)

# my_func_muable(c)

d = [5, 6]
def my_func_muable_2(b):
    g = 9
    b = [7]
    print(b is d)

# my_func_muable_2(d)

# --- Psser un nombre indéfini d'arguments 
def somme_de_tout(*args, patate = "1", **kwargs):
    print(kwargs)
    print(patate)
    print(sum(args))

somme_de_tout(5, 47, 54, 98, name="Ould Hocine", prenom="Lilia")

# Scope 