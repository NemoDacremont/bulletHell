
class Vue:
	ETAT_PAUSE = 1
	ETAT_NORMAL = 0

	def __init__(self, jeu, etat: int, pausePossible: bool) -> None:
		self.jeu = jeu
		self.fenetre= jeu.fenetre

		self.etat = etat
		self.pausePossible = pausePossible

		self.entites = []
		self.entitesAAfficher = []


	def update(self, event):
		for entite in self.entites:
			entite.update(event)

	def draw(self):
		self.fenetre.draw()

		for entite in self.entitesAAfficher:
			entite.draw()


