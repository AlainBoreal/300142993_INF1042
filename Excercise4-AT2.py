while True:
    x = input("Entrer seulement les lettres ou mots: ")
    if x.isalpha():
        while True:
            print(x)  
            x = input('Entrer "fin" pour finir le programme: ')
            if x.lower() == "fin":  
                print("Fin du programme.")
                break  
        break  
    else:
        print("S'il vous plaît entrer des caractères seulement.")
