# importations bizarre, permet d'importer les types sans avoir
# d'erreures d'importations circulaires
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from spritesheet import Spritesheet


# from pygame import Surface
import pygame
from copy import copy
from fenetre import Fenetre
from vues.vue import Vue



class Entite:
	COLOR = 0, 0, 255

	def __init__(self, nom: str, fenetre: Fenetre, vue: Vue, largeur: float,
			hauteur: float, x: float, y: float, spritesheet: Spritesheet) -> None:

		self.nom = nom

		# Forme
		self.largeur = largeur
		self.hauteur = hauteur

		# Position
		self.x = x
		self.y = y

		# Vitesse
		self.vx, self.vy = 0, 0

		# pour les collisions
		self.hitbox = pygame.Rect(x, y, largeur, hauteur)

		# Sert à l'affichage
		self.rectAffichage = pygame.Rect(x, y, largeur, hauteur)
		self.fenetre = fenetre
		self.vue = vue

		# Permet à la vue de savoir s'il faut supprimer l'entite
		self.doitRetirer: bool = False

		self.spritesheet = copy(spritesheet)


	def getDimension(self):
		return self.largeur, self.hauteur

	def getPositionCentre(self):
		personnageCentreX = self.x + self.largeur / 2
		personnageCentreY = self.y + self.hauteur / 2

		return personnageCentreX, personnageCentreY


	def getPosition(self):
		return self.x, self.y


	def doitEtreRetirer(self) -> bool:
		return self.doitRetirer


	def retire(self) -> None:
		self.doitRetirer = True


	def update(self):
		"""
			Met à jour la position
		"""
		dt = self.vue.getDT()

		# Calculs position
		dx = self.vx * dt
		dy = self.vy * dt


		self.x += dx
		self.y += dy

		# Calcul de la hitbox
		self.hitbox = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)


	def draw(self):
		fenetre = self.fenetre.getFenetre()
		self.rectAffichage = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
		fenetre.fill(Entite.COLOR, self.rectAffichage)


