import copy
a = {
    'name': 'Lilia',
    'age': 15,
    9: 'Coucou',
    True: 'la clé est un booléen', 
    1: "La clé est un entier",
    'age': 25
}

# Clé (uniques) => Valeur 
une_liste = [1, 2 ]
# 0 => 1
# 1 => 2

# print(a)

# print(a[True])
# print(a['age'])

un_dict = {
    'nom': 'Beyoncé', 
    'prenom': 'Batman',
    'age': 35,
    0: 0,
    True: 'Ceci est un true', 
    'adress': {
        'rue': "Rue du Départ",
        'ville': "Paris",
        'code_postale': '75014'
    },
    'notes': [85, 92, 99, 74],
    'date_naissance': "26/11/1975"
}

un_etudiant = dict(name="Jean", age="33")

# print(un_etudiant)

# --- Opérateurs in et les méthodes get, copy, et clear 

# for item in un_dict:
#     print(item)

# for valeur in un_dict.values(): 
#     print(valeur)

# for cle in un_dict.keys():
#     print(cle)

# for item in un_dict.items():
#     print(item)

# for cle, valeur in un_dict.items():
#     print(cle, valeur)


# if 'date_naissance' in un_dict:
#     print(un_dict['date_naissance'])
# else: 
#     print("Non existant")

# print()
# if un_dict.get('date_naissance'): 
#     print(un_dict.get('date_naissance'))
# else: 
#     print('Non existant')

# print(un_dict.get('date_naissance', "0/0/0000"))

# if un_dict.get('date_naissance', "0/0/0000"): 
#     print(un_dict.get('date_naissance', "0/0/0000"))
# else: 
#     print('Non existant')

un_dict2 = un_dict # shallow copy 
# un_dict2['prenom'] = "Julien"

# print(un_dict['prenom'])
# print(un_dict2['prenom'])

un_dict2 = un_dict.copy()
un_dict2['prenom'] = "Julien"

# print(un_dict['prenom'])
# print(un_dict2['prenom'])

un_dict2['adress']['ville'] = 'Montréal'
# print('89', un_dict['adress']['ville'])
# print('90', un_dict2['adress']['ville'])

un_dict2 = copy.deepcopy(un_dict)

un_dict2['adress']['ville'] = 'Québec'
# print('95', un_dict['adress']['ville'])
# print('96', un_dict2['adress']['ville'])

# ----- Supprimer les élèments d'un dictionnaire 
# result = un_dict.pop(True)

# print(result)
# print(un_dict)

cle, valeur = un_dict.popitem()
# print(cle, valeur)
# print(un_dict)

# --- La méthode update

# un_dict.update({'age': [0, 1]})
# print(un_dict)

# un_dict['age'] = 35
# print(un_dict)

# un_dict.update({'status': 'inscrit'})
# print(un_dict)

un_dict.setdefault('presence', False)
un_dict.update({'presence': True})
print(un_dict)

nouvelle_note = 65
if 'notes' in un_dict: 
    un_dict['notes'].append(nouvelle_note)
else:
    un_dict['notes'] = [nouvelle_note]

un_dict.setdefault('notes', [])
un_dict['notes'].append(nouvelle_note)

