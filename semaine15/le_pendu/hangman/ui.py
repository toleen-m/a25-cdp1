# Responsabilité : interface console Créer une classe ConsoleUI qui contient :

# ask_letter() → demande une lettre
# show_status(guess_word, life) → affiche l’état
# show_win() / show_lose(secret_word) → messages de fin
# Attendu : c’est ici qu’il y a input() et print().

class ConsoleUI: 

    def ask_letter(self):
        while True: 
            entree = input("Entrez une lettre > ")
            if len(entree) != 1 :
                print("Erreur : Entrez une seule lettre.")
                continue

            if not entree.isalpha():
                print("Erreur : Veuillez entrer une lettre (a-z).")
                continue 

            return entree
        
    def show_status(self, guess_word, life):
        print(f"{guess_word} | vie: {life}")

    def show_win(self):
        print("Gagné !")
    
    def show_lose(self, secret_word):
        print(f"Perdu !\nLe mot secret était {secret_word} !")

    def message(self, message):
        print(message)