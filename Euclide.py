a = int(input("entrer a : "))
while(a < 0):
    a = int(input("Donnez une valeur positive"))
b = int(input("etnrer B : "))
while(b < 0):
    b = int(input("Donnez une valeur positive"))

if(a < b):
    c = a
    a = b
    b = c
print(a , b)

m = a
n = b
if(a == 0):
    print("PGCD(",a," ",b,") = ", b)
if(b == 0):
    print("PGCD(",a," ",b,") = ", a)

while(b>0):
    c = a%b
    a = b
    b = c
print("PGCD(",a," ",b,") = ", a)
