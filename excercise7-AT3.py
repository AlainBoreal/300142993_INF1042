N = int(input("Combien de nombres souhaitez-vous saisir ? "))

nombres = []

for i in range(N):
    nombre = float(input(f"Saisissez le nombre {i+1}: "))
    nombres.append(nombre)

nombres_sans_doublons = list(dict.fromkeys(nombres))

print("\nListe sans doublons :", nombres_sans_doublons)
