def maximum(numbers):
    return max(numbers)

while True:
    try:
        count = int(input("Combien de nombres voulez-vous entrer? "))
        if count <= 0:
            print("Veuillez entrer un nombre supérieur à zéro.")
        else:
            break
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

numbers = []

for i in range(count):
    while True:
        try:
            num = float(input(f"Entrez le nombre {i + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

max_value = maximum(numbers)
print("Le plus grand des nombres saisis est :", max_value)
