while True:
    h = int(input("entrez le heure : "))
    if h < 24:
        break
    print("Entrer un nombre qui est sur le format 24h.")
    
while True:
    m = int(input("entrez le(s) minutes: "))
    if m < 60:
        break
    print("Entrer un nombre qui est moins que 60 pour les minutes")

m +=1

if m == 60:
    m = 0
    h += 1

if h == 24:
    h = 0

print("le temps dans le minute prochaine est: ",h,":",m)


