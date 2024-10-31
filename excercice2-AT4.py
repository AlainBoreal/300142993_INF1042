import math

def surfCercle(R):
    return math.pi * R ** 2

while True:
    user_input = input("Entrez le rayon du cercle : ")
    try:
        rayon = float(user_input)
        break  
    except ValueError:
        print("Veuillez entrer un nombre valide.")

print("La surface du cercle est :", round(surfCercle(rayon), 3))
