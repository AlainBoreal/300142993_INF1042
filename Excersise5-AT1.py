x = int(input("inserez une nombre: "))
y = int(input("inserez une nouveau nombre: "))

if x == 0 or y == 0:
    print("le produit sera neutre")
    
elif y > 0 and x > 0:
    print("le produit sera positif")
elif y < 0 and x < 0:
    print("le produit sera positif")
          
elif y > 0 and x < 0:
    print("le produit sera negatif")
elif y < 0 and x > 0:
    print("le produit sera negatif")
