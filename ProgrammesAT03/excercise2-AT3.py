
nombres = []

for i in range(10):
    nombre = float(input(f"Saisissez le nombre {i+1}: "))  
    nombres.append(nombre)
    
moyenne = sum(nombres) / len(nombres)

print("Liste des nombres saisis :", nombres)
print("Moyenne :", moyenne)
