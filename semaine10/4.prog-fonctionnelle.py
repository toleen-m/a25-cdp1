liste = [x for x in range(10)]
print(liste)

li = [5, 8, 17, 96]
li3 = [y * 3 for y in li]

print(li3)

resultat = [
    [' . ', ' . ', ' . '],
    [' . ', ' . ', ' . '],
    [' . ', ' . ', ' . ']
]

resultat2 = [' . ' for i in range(3)]
print(resultat2)

resultat3 = [[' . ' for i in range(3)] for j in range(3)]

print(resultat3)

la_liste = [1, 25, 45, 74, 8, 102, 56]
le_result = [y for y in la_liste if y%2==0]

print(le_result)

# reproduire ette liste avec la compréhension des listes comme vu plus haut
exercice = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
la_solution = [[ i + j*3 for i in range(3)] for j in range(3)]
print(la_solution)

# Compréhension de dictionnaire 
dict1 = { "a": 1, "b": 2, "c": 3}
dict2 = {cle: valeur*2 for (cle, valeur) in dict1.items()}
print(dict2)

dict3 = {valeur: cle for (cle, valeur) in dict1.items()}

print(dict3)

print("----------------- TEST")
resultat_matrice = [m for m in range(3)], [n+3 for n in range(3)], [o+6 for o in range(3)]

print(resultat_matrice)