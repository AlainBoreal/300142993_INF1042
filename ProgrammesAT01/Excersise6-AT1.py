while True:
    a = int(input("Entrer le annee: "))
    if a >= 0:
        break
    print("Entrer une annee positive sil vout plait")
while True:
    m = int(input("Entrer le mois (1-12): "))
    if 1 <= m <= 12:
        break
    print("Le mois doit etre entre 1 et 12")

d = 0

ab = (a % 4 == 0)

if m in (1, 3, 5, 7, 8, 10, 12):
    d = 31
elif m in (4, 6, 9, 11):
    d = 30
elif m == 2:
    if ab:
        d = 29
    else:
        d = 28
    print("dans l'annee",a,"dans le,",m,"mois, le montant de jours du mois cerait:",d,)
            

    

