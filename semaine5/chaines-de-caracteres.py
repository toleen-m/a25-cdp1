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

nom = "Lilia"
age = 44

print("Bonjour, votre nom est " + nom + ".\nVotre âge est : " + str(age) + " ans!")

print(f"Bonjour, votre nom est  {nom} .\nVotre âge est : {age} ans!")

nom_livre = "Voyage au bout de la nuit"
auteur_livre = "Louis Férdinent Céline"
status_livre = "Emprunté"
un_livre = f"""
Le nom du livre : {nom_livre}
L'auteur du livre : {auteur_livre}
Le status : {status_livre}
"""

print(un_livre)