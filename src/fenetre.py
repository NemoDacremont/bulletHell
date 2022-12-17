
import pygame
from pygame.event import Event

class Fenetre:
	DEFAULT_BACKGROUND_COLOR = 255, 0, 0 # red

	def __init__(self, largeur: int, hauteur: int, fps: int, fondDecran) -> None:
		# Dimensions
		self.largeur = largeur
		self.hauteur = hauteur

		self.fps = fps

		self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
		self.fondDecran = fondDecran

	def getFenetre(self):
		return self.fenetre

	def draw(self):
		if not self.fondDecran:
			self.fenetre.fill(Fenetre.DEFAULT_BACKGROUND_COLOR)

		else:
			self.fenetre.blit(self.fenetre, self.fondDecran)


