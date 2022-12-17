

from pygame import Surface
from pygame.event import Event
import pygame

from fenetre import Fenetre
from vues.vue import Vue


class Entite:
	COLOR = 0, 0, 255

	def __init__(self, fenetre: Fenetre, vue: Vue, largeur: float, hauteur: float, x: float, y: float) -> None:
		self.largeur = largeur
		self.hauteur = hauteur
		self.x = x
		self.y = y

		self.rect = pygame.Rect(x, y, largeur, hauteur)
		self.fenetre = fenetre


	def update(self, events: list[Event]):
		pass

	def draw(self):
		fenetre = self.fenetre.getFenetre()
		fenetre.fill(Entite.COLOR, self.rect)


