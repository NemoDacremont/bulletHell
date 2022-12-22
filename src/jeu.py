
from fenetre import Fenetre
from vues.vue import Vue
from vues.vueBoss import VueBoss

import pygame


class Jeu():
	def __init__(self, fenetreLargeur: int, fenetreHauteur: int, fps: int):
		fondDecran = None
		self.fenetre = Fenetre(fenetreLargeur, fenetreHauteur, fps, fondDecran)

		# le jeu est en train de fonctionner
		self.tourne = True

		# clock, pour les fps
		self.clock: pygame.time.Clock = pygame.time.Clock()
		self.dt: float = -1  # valeur par défaut, sera mise à jour à la première update

		# Créé le joueur, pas sur de garder ce truc
		self.joueur = None

		# Créé les vues
		vue = VueBoss(self, Vue.ETAT_NORMAL, pausePossible=True)

		self.vues: list[Vue] = [vue]
		self.vueCourrante: int = 0

		pygame.display.init()
		pygame.font.init()
		print("default font:", pygame.font.get_default_font())
		# print("available fonts:", pygame.font.get_fonts())

		self.font = pygame.font.SysFont("sans", 16)





	def changeVue(self, indiceVue: int) -> bool:
		"""
			Change la vue courrante, renvoie True si réussi, False sinon
		"""

		if indiceVue < 0 or indiceVue > len(self.vues):
			return False

		self.vueCourrante = indiceVue
		return True

	def getDT(self) -> float:
		return self.dt


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
			# convertit en secondes
			self.dt = self.clock.tick(self.fenetre.fps) / 1000

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

			# AFfiche les fps (plus compliqué que prévu mdr
			fps = int(1 / self.getDT())
			WHITE = 255, 255, 255

			fenetreLargeur = self.fenetre.getLargeur()

			surface = self.font.render(f"fps: {fps}", True, WHITE)
			writeRect = pygame.Rect(fenetreLargeur - surface.get_width() - 10,
				10, surface.get_width(), surface.get_height())

			self.fenetre.getFenetre().blit(surface, writeRect)





			# on met à jour le visuel
			pygame.display.flip()
