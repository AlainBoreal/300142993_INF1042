def inverse(ch):
    return ch[::-1]

def palindrome(ch):
    return ch == inverse(ch)

if __name__ == "__main__":
    while True:
       
        user_input = input("Veuillez entrer une chaîne de caractères alphabétiques (ou tapez 'exit' pour quitter) : ")
        
        if user_input.lower() == 'exit':
            print("Sortie du programme.")
            break

        if not user_input.isalpha():
            print("Entrée invalide. Veuillez entrer uniquement des caractères alphabétiques.")
            continue
        
        reversed_word = inverse(user_input)
        print(f"Le mot à l'envers est : {reversed_word}")

        if palindrome(user_input):
            print(f'"{user_input}" est un palindrome.')
        else:
            print(f'"{user_input}" n\'est pas un palindrome.')
