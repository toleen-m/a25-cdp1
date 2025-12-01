# EXERCICE 1 - SYSTÈME BIBLIOTHÈQUE
# Créez le système en utilisant uniquement des listes, dictionnaires et variables

# 1. Créez une liste de livres (chaque livre est un dictionnaire)
# Structure d'un livre: titre, auteur, année, statut ("disponible" ou "emprunté")

# {
#         "titre": ,
#         "auteur": ,
#         "année": ,
#         "statut":
#     } 

emprt = "emprunté"
dspnbl = "disponible"

livres = [
    {
        "titre": "1984",
        "auteur": "George Orwell",
        "année": 1949,
        "statut": dspnbl
    }, {
        "titre": "Python pour les nuls",
        "auteur": "John Doe",
        "année": 2020,
        "statut": dspnbl
    }, {
        "titre": "Le Seigneur des Anneaux",
        "auteur": "J.R.R. Tolkien",
        "année": 1954,
        "statut": emprt
    } , {
        "titre": "Harry Potter",
        "auteur": "J.K. Rowling",
        "année": 1997,
        "statut": dspnbl 
    }  , {
        "titre": "Dune",
        "auteur": "Frank Herbert",
        "année": 1965,
        "statut": emprt 
    } 
]

# 2. Affichez tous les livres disponibles
print("=== LIVRES DISPONIBLES ===")
for livre in livres: 
    if livre["statut"] == dspnbl: 
        print(f"- {livre['titre']} par {livre['auteur']} est {dspnbl}")

# 3. Empruntez un livre (changez son statut)
livre_a_emprunter = "1984"
print(f"\n=== EMPRUNT DE '{livre_a_emprunter}' ===")
for livre in livres: 
    if livre["titre"] == livre_a_emprunter :
        if livre["statut"] == dspnbl :
            livre["statut"] == emprt
            print(f" - {livre_a_emprunter} a été emprunté")
        else:
            print(f" - {livre_a_emprunter} non disponible")
        break

# 4. Retournez un livre
livre_a_retourner = "Le Seigneur des Anneaux"
print(f"\n=== RETOUR DE '{livre_a_retourner}' ===")
for livre in livres: 
    if livre["titre"] == livre_a_retourner:
        if livre["statut"] == emprt:
            livre["statut"] = dspnbl
            print(f" - {livre_a_retourner} a été retourné")
        else: 
            print(f" - {livre_a_retourner} est disponible")
        break

# 5. Calculez des statistiques
print("\n=== STATISTIQUES ===")
total_livres = len(livres)
livres_disponibles = 0
for livre in livres: 
    if livre["statut"] == dspnbl:
        livres_disponibles += 1

pourcentage_disponibles = (livres_disponibles / total_livres) * 100

print(f"Total livres: {total_livres}")
print(f"Livres disponibles: {livres_disponibles}")
print(f"Pourcentage disponibles: {pourcentage_disponibles:.1f}%")

# 6. Recherche par auteur
auteur_recherche = "George Orwell"
print(f"\n=== RECHERCHE PAR AUTEUR '{auteur_recherche}' ===")
for livre in livres : 
    if livre["auteur"] == auteur_recherche: 
        print(f"- {livre['titre']} ({livre['année']}) - {livre['statut']}")