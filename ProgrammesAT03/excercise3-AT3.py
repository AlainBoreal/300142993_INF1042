x = int(input("Combien de nombres souhaitez-vous saisir ? "))

nombres = []

for i in range(x):
    nombre = float(input(f"Saisissez le nombre {i+1}: "))
    nombres.append(nombre)

maximum = max(nombres)
minimum = min(nombres)

print("\nListe des nombres saisis :", nombres)
print("Maximum :", maximum)
print("Minimum :", minimum)
