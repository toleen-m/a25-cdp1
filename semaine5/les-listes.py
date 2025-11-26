import copy

# a = [1, 2, "Hello", 1.2, [1, 2], True]
# b = list("Hello")
# c = list(range(0, 10, 2))

# print(a)
# print(b)
# print(c)

# --- L'index sur les listes 
# for i, val in enumerate(a): 
#     print(i, val)

# a[2] = "Lilia"
# print(a, a[2])
# print(a[::-1])

# -- Décompactage 
# x = ['q', 'w', 'e', 'r', 't', 'y']
# a = x[0]
# b = x[1]
# c = x[2]

# a, b, *d, e, f = x


# print(a, b, d, e, f)

# a, b, c = "Bleu", "Rouge", "Vert"

# print(a,b,c)

# ---- Les opérations sur les listes et les copies
x = ['1', '2', 'Coucou']
y = [True, 25, [1, 102]]
z = x + y

# print(z)

d = x
# x     &x      &ox     PyObject X
# d     &d      &ox     pyObject X
# print(d is x)
# d[2] = "Changement"
# print(x)

# ----- 
# e = x[:]
# print(x)
# e[2] = "Un autre changement"
# print(x)
# print(e)

x = ['1', "Un", 1, True, ['Une', 'superbe', 'liste']]
e = x.copy() # équivalent de :
e[2] = "Changement"
e[-1][1] = "Done"

# print(x)
# print(e)

# : shallow copie 
# le deepcopy 
y = ['1', "Un", 1, True, ['Une', 'superbe', 'liste']]
f = copy.deepcopy(y)
f[2] = "Changement"
f[-1][1] = "Done"

# print(y)
# print(f)

# ----- Les fonctions natives et ajouter des élèments aux listes

liste = [1, 2, 3, 4, 5]
# print(len(liste))
# print(sum(liste))
# print(max(liste))
# print(min(liste))

result = liste.append(6)
# print(liste)
# print(result)
liste.insert(0, "Start")
# print(liste)

# print(liste + [7, 8, 9])
# print(liste)
liste.extend([7, 8, 9])
# print(liste)

# ---- Supprimer des élèments des listes
n = ['une', 'liste', 2, True, 0.2, "liste"]
n.remove("liste")
# print(n)
n.pop()
# print(n)

m = n.pop(0)
# print(n)
# print(m)

n.clear()
# print(n)

# ---- Recherche dans une liste 
a = [1, 2, 3, 'a', 'b', [1, 2]]
b = a.index('a', 2, 5)
print(b)

if 'a' in a[2:5]:
    b = a.index('a', 2, 5)
    print('Dans la condition du if', b)

print([1, 2] in a)

# ------- Trier les listes 
a = [1, 11, 8, 57, 34, 3, 166]
b = ['Mission accomplie', 'Bon déjeuner', "j'ai faim"]
# a.sort()
# b.sort()

a.sort(reverse=True)
b.sort(reverse=True)
print(a)
print(b)


une_liste = ['Une ','fabuleuse ', 'soirée!']
print("".join(une_liste))

a = [1, 11, 8, 57, 34, 3, 166]
# print(sorted(a)) shallow copy
a.reverse()
print(a)

# reverse 
# sorted 