liste = [1, 2, 3]

def doubler_liste(une_liste):
    nouvelle_liste = []
    for item in une_liste:
       nouvelle_liste.append(item * 2)
    return nouvelle_liste

def tripler_liste(une_liste):
    nouvelle_liste = []
    for item in une_liste:
       nouvelle_liste.append(item * 3)
    return nouvelle_liste

def quadrupler_liste(une_liste):
    nouvelle_liste = []
    for item in une_liste:
       nouvelle_liste.append(item * 4)
    return nouvelle_liste

def multipler_liste(factor):
    def multiplier(une_liste):
        nouvelle_liste = []
        for item in une_liste:
            nouvelle_liste.append(item * factor)
        return nouvelle_liste
    return multiplier    
    
multipler_liste_par_2 = multipler_liste(2)
multipler_liste_par_5 = multipler_liste(5)
multipler_liste_par_4 = multipler_liste(4)
multipler_liste_par_10 = multipler_liste(10)

def multiplier_liste(une_liste, factor):
    nouvelle_liste = []
    for item in une_liste:
        nouvelle_liste.append(item * factor)
    return nouvelle_liste

print(multipler_liste_par_2(liste))
print(multipler_liste_par_5(liste))
print(multipler_liste_par_4(liste))
print(multipler_liste_par_10(liste))
print(liste)

# ----- La recusivité 
def sum(une_liste):
    total = 0
    for item in une_liste:
        total += item
    return total

print(sum(liste))

la_liste = [1, 5, 7, 15] 

def sum_recursif(une_liste):
    # if une_liste :
        return une_liste[0] + (sum_recursif(une_liste[1:]) if len(une_liste)>1 else 0) # voir cette ligne 
    # else:
    #     return 0

print(sum_recursif(la_liste)) # => 28
# 1 + sum_recursif([5, 7, 15]) => 1 + 27 
#       5 + sum_recursif([7, 15]) => 5 + 22
#           7 + sum_recursif([15])= => 7 + 15
#               15 + sum_recursif(None) => 15 + 0
#                       0
             
# valeur if condition else autre_valeur 
# if(condition)
#     fait valeur 
# else : 
#     fait autre valeur 