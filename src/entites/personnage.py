
import pygame
from pygame.event import Event
from entites.entite import Entite
from fenetre import Fenetre
from vues.vue import Vue

class Personnage(Entite):
	COLOR = 0, 255, 0
	V_EPS = 5 # on considère la vitesse nulle si <5

	def __init__(self, fenetre: Fenetre, vue: Vue, largeur: float, hauteur: float,
							x: float, y: float, groupe: int, vitesse: float = 100) -> None:
		super().__init__(fenetre, vue, largeur, hauteur, x, y)

		self.groupe = groupe

		# Vitesse
		self.vx, self.vy = 0, 0

		self.vitesse= vitesse

	def draw(self):
		self.rect = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
		self.fenetre.getFenetre().fill(Personnage.COLOR, self.rect)


