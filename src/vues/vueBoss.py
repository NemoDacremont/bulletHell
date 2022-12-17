
from entites.entite import Entite
from vues.vue import Vue

class VueBoss(Vue):
	def __init__(self, jeu, etat: int, pausePossible: bool) -> None:
		super().__init__(jeu, etat, pausePossible)

		entite = Entite(self.fenetre, self, 50, 50, 0, 0)
		self.entites = [entite]
		self.entitesAAfficher = [entite]

