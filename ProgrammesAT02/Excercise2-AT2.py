while True:
    try:
        a = int(input("Inserer une valeur entière non nulle et positive: "))
        if a > 0:
            total_sum = sum(range(1, a + 1))
            print(f"Vous avez inséré {a}.")
            print(f"La somme de ton nombre de 1 à {a} est: {total_sum}")
            break
        else:
            print("La valeur doit être un nombre positif et non nul.")
    except ValueError:
        print("Veuillez entrer un entier valide.")
        
