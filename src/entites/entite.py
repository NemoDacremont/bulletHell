

from pygame import Surface
from pygame.event import Event
import pygame

from fenetre import Fenetre
from vues.vue import Vue


class Entite:
	COLOR = 0, 0, 255

	def __init__(self, fenetre: Fenetre, vue: Vue, largeur: float, hauteur: float, x: float, y: float) -> None:

		# Forme
		self.largeur = largeur
		self.hauteur = hauteur

		# Position
		self.x = x
		self.y = y

		# Vitesse
		self.vx, self.vy = 0, 0

		# Sert à l'affichage
		self.rect = pygame.Rect(x, y, largeur, hauteur)
		self.fenetre = fenetre


	def update(self, events: list[Event]):
		"""
			Met à jour la position
		"""
		fps = self.fenetre.fps
		# Calculs position
		dx = self.vx / fps
		dy = self.vy / fps

		self.x += dx
		self.y += dy


	def draw(self):
		fenetre = self.fenetre.getFenetre()
		fenetre.fill(Entite.COLOR, self.rect)


