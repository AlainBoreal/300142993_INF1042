class Voiture:
    def __init__(self, marque='Ford', couleur='rouge'):
        self.marque = marque
        self.couleur = couleur
        self.pilote = 'personne'
        self.vitesse = 0

    def choix_conducteur(self, nom):
        """Permet de désigner ou changer le nom du conducteur."""
        self.pilote = nom

    def accelerer(self, taux, duree):
        if self.pilote == 'personne':
            print("Impossible d'accélérer : aucun conducteur n'est désigné.")
            return

        variation = taux * duree
        self.vitesse += variation
        print(f"La vitesse a été modifiée de {variation:.2f} m/s.")

    def affiche_tout(self):
        """Affiche les propriétés actuelles de la voiture."""
        print(f"Marque : {self.marque}")
        print(f"Couleur : {self.couleur}")
        print(f"Pilote : {self.pilote}")
        print(f"Vitesse : {self.vitesse:.2f} m/s")

voiture1 = Voiture()
voiture1.affiche_tout()
voiture1.choix_conducteur("Alice")
voiture1.accelerer(1.3, 20)
voiture1.affiche_tout()

voiture2 = Voiture("Tesla", "bleu")
voiture2.affiche_tout()
voiture2.accelerer(2.0, 10)  
voiture2.choix_conducteur("Bob")
voiture2.accelerer(2.0, 10)
voiture2.affiche_tout()
