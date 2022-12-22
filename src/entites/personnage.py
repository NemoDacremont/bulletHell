
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from pygame.event import Event
	from fenetre import Fenetre
	from vues.vue import Vue

import pygame
from entites.entite import Entite


class Personnage(Entite):
	COLOR = 0, 255, 0
	V_EPS = 5  # on considère la vitesse nulle si <5

	def __init__(self, nom: str, fenetre: Fenetre, vue: Vue, largeur: float, hauteur: float,
							x: float, y: float, PVMax: float, PV: float = -1, vitesse: float = 100) -> None:
		"""
			Constructeur Personnage
			Paramètres:
				- fenetre: Fenetre, la fenêtre du jeu
				- vue: Vue, La vue à laquelle il appartient
				- largeur: float, la largeur en pixels du perssonnage
				- hauteur: float, la hauteur en pixels du perssonnage
				- x: float, la position initiale en x du personnage
				- y: float, la position initiale en y du personnage
				- PVMax: float, les PVs max du personnage
				- PV: float, les PVs initiaux du personnage, si PV == -1, alors PV = PVMax
				- vitesse: float, le nombre de pixels parcourus en 1 sec
		"""
		super().__init__(nom, fenetre, vue, largeur, hauteur, x, y)

		# groupe par défaut: 0
		self.groupe = 0

		# PVs
		self.PVMax = PVMax

		self.PV = PV
		if PV == -1:
			self.PV = PVMax

		# Vitesse
		self.vx, self.vy = 0, 0

		self.vitesse = vitesse


	def getGroupe(self):
		return self.groupe


	def recoitDegats(self, degats: float):
		self.PV -= degats
		print(f"{self.nom} prend des dégats: il lui reste {self.PV} PVs")


	def update(self, events: list[Event]):
		"""
			On demande events, notament pour le personnage jouable
		"""
		# met à jour position
		super().update()


	def draw(self):
		self.rect = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
		self.fenetre.getFenetre().fill(Personnage.COLOR, self.rect)


