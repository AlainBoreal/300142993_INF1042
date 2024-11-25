x = int(input("Combien de nombres voulez-vous entrer ? "))

nombres = []

for i in range(x):
    nombre = int(input(f"Entrez le nombre {i+1}: "))
    nombres.append(nombre)

print(f"Liste initiale: {nombres}")

if x > 0:
    nombres = [nombres[-1]] + nombres[:-1]

print(f"Liste après permutation circulaire: {nombres}")
