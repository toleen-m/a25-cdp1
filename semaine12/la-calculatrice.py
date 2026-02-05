# Correction de l'examen 3
def calcularice():
    """
    Fonction principale de la calculatrice
    """
    memories = {"M1": None, "M2": None, "M3": None, "M4": None, "M5": None}  # Dictionnaire pour stocker les valeurs
    current_memory = "M1"  # Mémoire active par défaut
    dernier_resultat = None


    # calcul avec plusieurs nombre 
    def operations_multiples():
        """Gère les calculs avec plus de 2 nombres"""
        nonlocal dernier_resultat
        # À implémenter - penser à demander l'utilisation d'une mémoire
        print("Opérations multiples")

        # Récupérer l'opération choisie par l'utilisateur
        while True: 
            operation = input("\nChoisissez l'opération (+, -, *, /) : ").strip()
            if operation in ['+', '-', '*', '/'] :
                break
            print("Erreur: Opération doit être +, -, *, /")
        
        # Nombre d'opérandes
        while True: 
            try:
                nb_nombres = int(input("Combien de nombre ? (minimum 2) : "))
                if nb_nombres >= 2:
                    break
                print("Erreur: Il faut au moins deux nombres")
            except ValueError : 
                print("Erreur : Entrez un nombre entier")

        nombres = []
        for i in range(nb_nombres) :
            resultat = demander_nombre(f"Entrez le nombre {i+1}")
            nombres.append(resultat)

        if operation == '/' and 0 in nombres[1:]:
            print("Erreur : Division par zéro imposiible")
            return None
        
        if operation == "+": 
            resultat = sum(nombres)
            operateur = " + "
        elif operation == "-":
            resultat = nombres[0]
            for n in nombres[1:0]:
                resultat -= n
            operateur = " - "
        elif operation == "*":
            resultat = 1
            for n in nombres:
                resultat *= n
            operateur = " * "
        elif operation == "/":
            resultat = nombres[0]
            for n in nombres[1:]:
                resultat /= n
            operateur = " / "

        # Affichage  
        expression = operateur.join(str(n) for n in nombres)
        print(f"\nRÉSULTAT : {expression} = {resultat}")

        dernier_resultat = resultat
        return resultat


    def utiliser_memoire():
        while True: 
            choix = input("\nQuelle mémoire utiliser ? (M1-M5 ou 'a' pour annuler) : ").upper()
            if choix == "A":
                print("Opération annulée !")
                return False
            if choix in memories: 
                if memories[choix] is not None:
                    print(f"Utilisation de {choix} = {memories[choix]}")
                    return memories[choix]
                else: 
                    print(f"La mémoire {choix} est vide !")
            else :
                print("Choix invalide. Entrez M1, M2, M3, M4, M5 ou 'a'")

    def gestion_memoire():
        """
        Docstring for gestion_memoire
        === GESTION DE LA MÉMOIRE (Active: M1) ===
        a. Stocker le dernier résultat
        b. Utiliser une mémoire dans un calcul
        c. Afficher toutes les mémoires
        d. Effacer une mémoire ou toutes les mémoires
        e. Retour au menu principal
        """

        nonlocal dernier_resultat, memories

        while True: 
            print(f"\n=== GESTION DE LA MÉMOIRE (Active: {current_memory}) ===")
            print("a. Stocker le dernier résultat")
            print("b. Utiliser une mémoire dans un calcul")
            print("c. Afficher toutes les mémoires")
            print("d. Effacer une mémoire ou toutes les mémoires")
            print("e. Retour au menu principal")

            choix = input("\nVotre choix (a-e) : ").lower()
            if choix == 'a': # stcokcer le resultat
                if dernier_resultat is None:
                    print("Aucun résultat à stocker")
                else: 
                    memories[current_memory] = dernier_resultat # type: ignore
                    print(f"Résultat {dernier_resultat} stocké dans {current_memory}")
            elif choix == 'b': # Utiliser une mémoire dans un calcul
                mem_val = utiliser_memoire()
                if mem_val == False : 
                    continue
                if mem_val is not None:
                    return mem_val
                else: 
                    print("Aucun mémoire sauvegardée")

            elif choix == 'c': # Afficher toutes les mémoires
                afficher_memoire()
                
            elif choix == 'd': # Effacer une mémoire
                mem = input("\nQuelle mémoire à effacer ? (M1-M5) ou TOUTES pour toutes : ").upper()
                if mem == "TOUTES" : 
                    for m in memories:
                        memories[m] = None
                    print("Toutes les mémoires effacées")
                elif mem in memories:
                    memories[mem] = None
                    print(f"Mémoire {mem} effacée")
                else:
                    print("Entrée invalide")
            elif choix == 'e': # Retour au menu principal
                break
            else : 
                print("Choix invalide. Entrez a, b, c, d ou e")

            

        

    def demander_nombre(message, allow_memory=True):
        """
        Docstring for demander_nombre
        demander l'utilisation de la mémoire
        """
        while True: 
            try:
                if allow_memory: 
                    use_mem = input("Voulez-vous utiliser une mémoire ? (o/n) ").lower()
                    if use_mem == 'o':
                        mem_val = utiliser_memoire()
                        if mem_val is not None:
                            return mem_val

                valeur = float(input(f"{message} : "))
                return valeur
            except ValueError:
                 print("Erreur : Entrez un nombre valide")

    def afficher_memoire():
        """
        Docstring for afficher_memoire
        Mémoires actuelles :
        M1: 15.50
        M2: vide
        M3: 8.25
        M4: vide
        M5: vide
        """
        print("\nMémoires actuelles :")
        for key, value in memories.items():
            if value is None: 
                print(f"{key}: vide")
            else:
                print(f"{key}: {value}")

    print("=== CALCULATRICE SIMPLE ===")

    while True:
        # Afficher le menu
        print("\nMenu principal :")
        print("1. Addition (+) [2 nombres]")
        print("2. Soustraction (-) [2 nombres]")
        print("3. Multiplication (*) [2 nombres]")
        print("4. Division (/) [2 nombres]")
        print("5. Opérations multiples (+, -, *, /)")
        print("6. Gestion de la mémoire")
        print("7. Quitter")

        try:
            choix = input("\nQuel est votre choix (1-7) : ")
            if choix == '7':
                print("\nMerci d'avoir utilisé la calculatrice. Au revoir !")
                break

            if choix in ['1', '2', '3', '4']:

                try :
                    # demander le premier nombre
                    num1 = demander_nombre("Entrez le premier nombre", False)
                    # demander le deuxième nombre
                    num2 = demander_nombre("Entrez le deuxième nombre", False)
                except ValueError:
                    raise ValueError("Veuillez entrer un nombre valide.")

                if choix == '1': # addition
                    resultat = num1 + num2
                    operateur = "+"
                elif choix == '2':  # soustraction
                    resultat = num1 - num2
                    operateur = "-"
                elif choix == '3':  # multiplication
                    resultat = num1 * num2
                    operateur = "*"
                elif choix == '4':  # division
                    if num2 == 0:
                        raise ZeroDivisionError("Division par zéro est impossible ! ")
                    resultat = num1 / num2
                    operateur = "/"

                # affichage du resultat
                print(f"Résultat : {num1} {operateur} {num2} = {resultat}")
                dernier_resultat = resultat

            elif choix == '5':
                operations_multiples()
                
            elif choix == '6':
                gestion_memoire()
                
            else : 
                print("Erreur: Choix invalide. Entrez un nombr de 1 à 7")

        except ValueError as ve :
            print(f"Erreur : {ve}")
        except ZeroDivisionError as zde:
            print(f"Erreur: {zde}")
        except Exception as e:
            print(f"Erreur inattendue : {e}")


calcularice()

# # Test 1 : Addition multiple
# 5 + 3 + 2 + 6 = 16

# # Test 2 : Soustraction multiple
# 20 - 5 - 3 - 2 = 10

# # Test 3 : Division avec mémoire
# # Stocker 100 dans M1
# # Faire : M1 ÷ 2 ÷ 5 = 10