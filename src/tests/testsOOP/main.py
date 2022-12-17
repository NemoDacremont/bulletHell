
class Entity():
    def __init__(self, nom: str, x: int, y: int):
        self.nom = nom
        self.x = x
        self.y = y

    def getNom(self):
        return self.nom

class Tasse(Entity):
    def __init__(self, x: int, y: int):

        # Fait appel au constructeur de Entity
        super(Tasse, self).__init__("Tasse", x, y)

unTruc = Entity("le truc", 3, 4)
maTasse = Tasse(0, 0)

print(unTruc.getNom())
print(maTasse.getNom())


