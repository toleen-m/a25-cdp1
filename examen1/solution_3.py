# EXERCICE 3 - SYSTÈME DE NOTES
# Complétez les parties manquantes

# 1. Données des étudiants et leurs notes
# Utilisez un dictionnaire où la clé est le nom et la valeur est une liste de notes
etudiants_notes = {
    "Alice": [15, 18, 12],
    "Bob": [8, 14, 16],
    "Charlie": [20, 19, 18],
    "David": [10, 11, 9]
}

# 2. Affichage des notes de chaque étudiant
print("=== NOTES DES ÉTUDIANTS ===")
for etudiant, notes in etudiants_notes.items():
    print(f"{etudiant}: {notes}")

# 3. Calcul des moyennes individuelles
print("\n=== MOYENNES INDIVIDUELLES ===")
moyennes = {}  # Dictionnaire pour stocker les moyennes

for etudiant, notes in etudiants_notes.items():
    moyenne = sum(notes) / len(notes)
    # moyennes.update({etudiant: moyenne})
    moyennes[etudiant] = moyenne
    print(f"{etudiant}: {moyenne:.1f}/20")

# 4. Trouver le meilleur étudiant
print("\n=== CLASSEMENT ===")
meilleur_etudiant = None
meilleure_moyenne = 0

meilleur_etudiant = max(moyennes, key=moyennes.get)
meilleure_moyenne = moyennes[meilleur_etudiant]

# for etudiant, moyenne in moyennes.items():
#     if moyenne > meilleure_moyenne:
#         meilleure_moyenne = moyenne
#         meilleur_etudiant = etudiant
    
print(f"Meilleur étudiant: {meilleur_etudiant} avec {meilleure_moyenne:.2f}/20")

# 5. Statistiques de la classe
print("\n=== STATISTIQUES CLASSE ===")
toutes_notes = []
for notes in etudiants_notes.values():
    toutes_notes.extend(notes)

moyenne_generale = sum(toutes_notes) / len(toutes_notes)  
meilleure_note = max(toutes_notes)   
pire_note = min(toutes_notes)

print(f"Moyenne générale: {moyenne_generale:.2f}/20")
print(f"Meilleure note: {meilleure_note}/20")
print(f"Pire note: {pire_note}/20")

# 6. Distribution des notes
print("\n=== DISTRIBUTION DES NOTES ===")
notes_tranches = {
    "16-20": 0,
    "14-15": 0,
    "12-13": 0,
    "10-11": 0,
    "0-9": 0
}

for note in toutes_notes:
    if note >= 16 :
        notes_tranches["16-20"] +=1
    elif note >= 14 : 
        notes_tranches["14-15"] +=1
    elif note >= 12:
        notes_tranches["12-13"] +=1
    elif note >=10 : 
        notes_tranches["10-11"] +=1
    else : 
        notes_tranches["0-9"] +=1

for tranche, count in notes_tranches.items():
    print(f"{tranche}: {count} notes")

# 7. Ajout d'un nouvel étudiant
print("\n=== AJOUT NOUVEL ÉTUDIANT ===")
nouvel_etudiant = "Eve"
nouvelles_notes = [17, 16, 15]

etudiants_notes[nouvel_etudiant] = nouvelles_notes

print(f"Après ajout de {nouvel_etudiant}:")
print(etudiants_notes)