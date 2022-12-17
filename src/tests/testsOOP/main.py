
class Entity():
    def __init__(self, nom: str, x: int, y: int):
        self.nom = nom
        self.x = x
        self.y = y

    def getNom(self):
        return self.nom

class Tasse(Entity):
    EST_REMPLI = True
    NEST_PAS_REMPLI = False


    def __init__(self, proprietaire: str, estRempli: bool, x: int, y: int):
        self.proprietaire = proprietaire
        self.estRempli = estRempli

        # Fait appel au constructeur de Entity
        super(Tasse, self).__init__("Tasse", x, y)

    def vider(self):
        self.estRempli = Tasse.NEST_PAS_REMPLI

    def remplir(self):
        self.estRempli = Tasse.EST_REMPLI


    def boire(self):
        if self.estRempli:
            print(f"{self.proprietaire} boit dans sa tasse")
            self.vider()
        else:
            print(f"{self.proprietaire} est triste: sa tasse est vide")




unTruc = Entity("le truc", 3, 4)
maTasse = Tasse("Nemo", Tasse.EST_REMPLI, 0, 0)

print(unTruc.getNom())
print(maTasse.getNom())

maTasse.boire()
maTasse.boire()

maTasse.remplir()
maTasse.boire()

