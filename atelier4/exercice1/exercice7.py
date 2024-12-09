from module_test_numbers import is_number, is_positive_number

taille = input("Donner la taille de la liste : ")
while not is_positive_number(taille):
    taille = input(f"'{taille}' n'est pas une taille valide! Donner une valeur entière positive : ")
taille = int(taille)

numbers = []
for i in range(taille):
    a = input(f"Donner le nombre {i+1} : ")
    while not is_number(a):
        a = input(f"'{a}' n'est pas une bonne valeur! Donner une valeur numérique valide : ")
    numbers.append(float(a))

numbers = list(set(numbers))

print("La liste sans doublons est :", numbers)
