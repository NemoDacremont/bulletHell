
import pygame
from fenetre import Fenetre
from vues.vue import Vue
from vues.vueBoss import VueBoss

class Jeu():
	def __init__(self, fenetreLargeur, fenetreHauteur, fps):
		fondDecran = None
		self.fenetre = Fenetre(fenetreLargeur, fenetreHauteur, fps, fondDecran)

		# le jeu est en train de fonctionner
		self.tourne = True

		## Créé le joueur
		self.joueur = None

		## Créé les vues
		vue = VueBoss(self, Vue.ETAT_NORMAL, pausePossible=True)

		self.vues: list[Vue] = [vue]
		self.vueCourrante: int = 0





	def changeVue(self, indiceVue: int) -> bool:
		"""
			Change la vue courrante, renvoie True si réussi, False sinon
		"""

		if indiceVue < 0 or indiceVue > len(self.vues):
			return False

		self.vueCourrante = indiceVue
		return True

	def stopGame(self):
		"""
			Arrête le jeu
		"""
		self.tourne = False

	def joue(self):
		"""
			Boucle principale du jeu
		"""
		while self.tourne:
			# Racourci de notation
			vue = self.vues[self.vueCourrante]

			events = pygame.event.get()

			# Si on demande de fermer le jeu, on quitte
			for event in events:
				if event.type == pygame.QUIT:
					self.stopGame()

			# met à jour la vue
			vue.update(events)
			vue.draw()

			# on met à jour le visuel
			pygame.display.flip()

