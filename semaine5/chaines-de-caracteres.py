# une_str = "Je suis une chaine de caractères!"
# une_str2 = str("Je suis une chaine de caractères!")
# une_str3 = str([0, "Il fait beau", True, 1.2])

# print(une_str)
# print(une_str2)
# print(une_str3)

# # \n 
# # \t 8 caractères
# # \r 

# print("Je suis un merveilleux paragraphe \nEn voici la preuve")
# print("Voici le profil:\n\tNom: Lilia\n\tÂge: 44ans")
# print("Aujourd'hui il est fait beau\rAu fait pas du tout")

# un_paragraphe = "Je suis un paragraphe, " \
# "c'est quelque chose!"
# print(un_paragraphe)

# un_paragraphe2 = """Je suis un paragraphe, 
# C'est quelque chose!
# Mon contenu doir dépasser une seule ligne.
# Ceci est un test"""
# print(un_paragraphe2)

# nom = "Lilia"
# age = 44

# print("Bonjour, votre nom est " + nom + ".\nVotre âge est : " + str(age) + " ans!")

# print(f"Bonjour, votre nom est  {nom} .\nVotre âge est : {age} ans!")

# nom_livre = "Voyage au bout de la nuit"
# auteur_livre = "Louis Férdinent Céline"
# status_livre = "Emprunté"
# un_livre = f"""
# Le nom du livre : {nom_livre}
# L'auteur du livre : {auteur_livre}
# Le status : {status_livre}
# """

# print(un_livre)

# ----- Les indexes des chaines de caractères 
# a = "Les cours sont en ligne sut GitHub!"
# print(a[4])
# print(a[-1])
# print(a[-5])

# # a[x:y:1]
# # a[x:y:z]
# print(a[10:23:2])
# print(a[::3])

# print(a[-1::-1])

# ------ len() et les méthodes pour les chaines de caractères
# len
# capitalize 
# title
# upper 
# lower
# count
# find
# index
# endswith
# startswith

chaine = "On est lundi !"
# print(len(chaine))
# print(chaine.capitalize())
# print(chaine.title())
# print(chaine.upper())
# print(chaine.lower())

# print("Je suis malade".lower().title() == "je sUis malade".lower().title())

livre = "Les Misèrables"
# livre_recherche = input("Vous cherchez quel livre ?")
# print(livre.lower() == livre_recherche.lower())

# print(livre.count("e"))
# print(livre.count("e", 5))

# print(livre.lower().index("misèrable".lower()))

# print(livre.endswith("."))
# print(livre.startswith("[BD]"))

# ------ Autres méthodes pour les chaines de caractères
# split
# splitlines
# join
# replace 
# removeprefix
# removesuffix

chaine = "Je mange une pomme"
# result = chaine.split()
# print(result)
# print(chaine.split("suis"))
# print(chaine.split(" ", 1))

# un_paragraphe = """Je suis
# Un paragraphe
# sur plusieurs
# lignes"""

# print(un_paragraphe.splitlines(True))

print(chaine.join([',', ',']))

print(chaine.replace("e", 'E', 2))

test = "[DB] Je suis un test [DB]"
print(test.removeprefix("[DB]").removesuffix("[DB]"))