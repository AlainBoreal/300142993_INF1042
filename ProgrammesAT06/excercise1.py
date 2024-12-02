class domino:
    def __init__(self, face_a=0, face_b=0):
        self.face_a = face_a
        self.face_b = face_b

    def affiche_points(self):
        print(f"face a : {self.face_a} face b : {self.face_b}")

    def valeur(self):
        return self.face_a + self.face_b

    def __repr__(self):
        return f"[{self.face_a}|{self.face_b}]"

d1 = domino(1, 4)
d2 = domino(5, 2)

d1.affiche_points()
d2.affiche_points()
print("total des points :", d1.valeur() + d2.valeur())

liste_dominos = []
for i in range(7):
    liste_dominos.append(domino(4, i))
print(liste_dominos)
