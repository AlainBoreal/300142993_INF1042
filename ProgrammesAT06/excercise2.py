class CompteBancaire:
    def __init__(self, nom='Dupont', solde=1000):
        self.nom = nom
        self.solde = solde

    def depot(self, somme):
        if somme > 0:
            self.solde += somme
            print(f"{somme} ajouté au compte.")
        else:
            print("Le montant du dépôt doit être positif.")

    def retrait(self, somme):
        if somme > 0:
            if somme <= self.solde:
                self.solde -= somme
                print(f"{somme} retiré du compte.")
            else:
                print("Fonds insuffisants.")
        else:
            print("Le montant du retrait doit être positif.")

    def affiche(self):
        print(f"Titulaire : {self.nom}, Solde : {self.solde} euros")

compte1 = CompteBancaire()
compte1.affiche()

compte1.depot(500)
compte1.affiche()

compte1.retrait(200)
compte1.affiche()

compte2 = CompteBancaire(nom="Martin", solde=2000)
compte2.affiche()
