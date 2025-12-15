# premier exemple de portée
# a = 1 

# def une_fonction():
#     print(a)

# une_fonction()


# ------ Exemple 2

# def une_fonction_2():
#     b = 1

# une_fonction_2()
# print(b)

# ------ Exemple 3
# def une_fonction_3():

#     print(sum([1, 2]))

# une_fonction_3()

# ----- Exemple 4
# a = 1

# def fun_4():
#     def in_fun_4():
#         print(a)
#     in_fun_4()

# fun_4()

# --- Exemple 5 
# a = 1

# def fun_5():
#     a = 2

#     def in_fun5():
#         print(a)

#     in_fun5()

# fun_5()

# ---- Exemple 6 
# a = 1 

# def fun_6():
#     print(a)

# def fun_6_bis():
#     a = 2
#     fun_6()

# fun_6_bis()

# ----- Exemple 7
# def fun_7():
#     def in_fun_7():
#         b=2
#     in_fun_7()
#     print(b)

# fun_7()

# ------ Les fermetures (closures)

# def fonction_parent():
#     a = 2
#     def fonction_enfant():
#         print(a)
#     return fonction_enfant

# fonction = fonction_parent()
# fonction()

# def power_factor(power): 
#     def power_by(number):
#         return number ** power
#     return power_by

# power_by_2 = power_factor(2)

# print(power_by_2(4)) # 4 puissance 2

# power_by_4 = power_factor(4)
# print(power_by_4(3)) # 3 puissance 4

# --- Deuxième exemple de closures 

# def foo():
#     liste=[]
#     for item in range(3): # 0, 1, 2
#         def display():
#             print(item)
#         liste.append(display)
#     return liste

# a = foo()
# a[0]() # 2
# a[1]() # 2
# a[2]() # 2

# for patate in [1, 2, 3]:
#     pass
# print(patate)

# --- global nonlocal 
# a = 1
# def une_autre_fonction():
#     global a
#     a += 1

# une_autre_fonction()

# def un_conteur():
#     total = 0
#     def foo():
#         nonlocal total
#         print(total)
#         total += 1
#     return foo

# a = un_conteur()
# b = un_conteur()
# a()
# b()
# a()
# b()
# a()

# ---- Les annotations de fonctions
Boat = int | float

def additionner(a: int | float, b: int | float, c: Boat) -> int : 
    return a + b


additionner(1.1,2.1)

print()

# Les chaines de documentations
Nombre = int | float
def la_fonction_additionner(a: Nombre, b: Nombre) -> Nombre : 
    '''
    la description de la fonction / ce qu'elle fait, pourquoi elle seraut utilisée
    
    :param a: Description
    :type a: Nombre
    :param b: Description
    :type b: Nombre
    :return: Description
    :rtype: Nombre
    '''
    return a + b

la_fonction_additionner(1,2)