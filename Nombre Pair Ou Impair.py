n=int(input("Entrez un nombre:"))

if n>0 :
    if n%2==0:
        print("le nombre",n," est positif et pair ")
    else:
        print("le nombre",n," est positif et impair ")
elif n<0 :
    if n%2==0:
            print("le nombre",n," est negatif et pair ")
    else:   
            print("le nombre",n," est negatif et impair ")
    else:
    print("le nombre",n," est neutre et pair ")
