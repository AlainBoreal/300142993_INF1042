N = int(input("Combien de nombres souhaitez-vous saisir ? "))

nombres = []

for i in range(N):
    nombre = float(input(f"Saisissez le nombre {i+1}: "))
    nombres.append(nombre)

X = float(input("Saisissez le nombre à chercher dans la liste : "))

if X in nombres:
    occurrences = nombres.count(X)
    print(f"Le nombre {X} se trouve dans la liste et apparaît {occurrences} fois.")
else:
    print(f"Le nombre {X} ne se trouve pas dans la liste.")
