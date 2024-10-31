def nomMois(n):
    mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", 
            "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    return mois[n - 1]

while True:
    try:
        n = int(input("Entrez un numéro de mois (1-12) : "))
        
        if 1 <= n <= 12:
            print("Le mois correspondant est :", nomMois(n))
            
        else:
            print("Veuillez entrer un nombre entre 1 et 12.")
    
    except ValueError:
        print("Veuillez entrer un nombre valide.")
