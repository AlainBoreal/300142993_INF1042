b = 0  
while True:
    try:
        a = int(input("Insérer une valeur entière positive et non nulle (ou '0' pour finir): "))
        if a == 0:  
            break
        if a > 0:
            if a > b:  
                b = a  
        else:
            print("La valeur doit être un nombre entier positif et non nul.")
    
    except ValueError:
        print("Veuillez entrer un entier valide.")
if b > 0: 
    print(f"Le plus grand nombre que vous avez entré est: {b}")
else:
    print("Aucun nombre valide n'a été entré.")
