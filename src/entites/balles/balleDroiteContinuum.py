from __future__ import annotations
from typing import TYPE_CHECKING

from spritesheet import Spritesheet

# typage
if TYPE_CHECKING:
	from fenetre import Fenetre
	from vues.vue import Vue

from entites.balles.balle import Balle
from math import cos, sin


class BalleDroiteContinuum(Balle):
	NOM = "balleDroiteContinuum"
	COLOR = 0, 0, 255  # Bleu

	def __init__(self, fenetre: Fenetre, vue: Vue, largeur: float, hauteur: float,
		x: float, y: float, groupe: int, vitesse: float, degats: float,
		direction: float, continuum: int) -> None:
		"""
			Constructeur de BalleDroiteContinuum
			Paramètres:
				- fenetre: Fenetre, la fenêtre dans laquelle on affiche la balle
				- vue: Vue: la vue dans laquelle on affiche la balle
				- largeur: la largeur de la balle
				- hauteur: la hauteur de la balle
				- x: la position de départ en x
				- y: la position de départ en y
				- groupe: int, le groupe auquel la balle appartient, permet de détecter
					les adversaires
				- vitesse: float, la vitesse de la balle, elle est constante
				- degats: float, dégats infligés à chaque balle
				- direction: se déplace en ligne droite selon l'angle direction, défini
					entre \vec x et \vec y
		"""
		SPRITESHEET = Spritesheet("/home/odasta/Documents/programmation/python/prepa-2/bulletHell/src/assets/LaserSprites/05.png")

		super().__init__(BalleDroiteContinuum.NOM, fenetre, vue, largeur, hauteur, x, y,
			groupe, degats, SPRITESHEET)

		self.direction = direction
		self.vy = sin(direction) * vitesse
		self.vx = cos(direction) * vitesse
		self.continuum = continuum

		self.rotImage(- direction)


	def update(self):
		"""
			Update BalleDroite
			La vitesse de ces balles est constante et va tout droite: il n'y a pas à
			modifier la vitesse
		"""

		super().update()

		# Si la balle sort de l'écran, on la retire

		h, k = self.fenetre.getDimensions()

		if self.y < -self.hauteur:
			if self.continuum <= 0:
				self.retire()

			self.y = k - self.hauteur
			self.continuum -= 1

		if self.y > k + self.hauteur:
			if self.continuum <= 0:
				self.retire()

			self.y = self.hauteur
			self.continuum -= 1

		if self.x > h + self.hauteur:
			if self.continuum <= 0:
				self.retire()

			self.x = self.hauteur
			self.continuum -= 1

		if self.x < -self.hauteur:
			if self.continuum <= 0:
				self.retire()

			self.x = h - self.hauteur
			self.continuum -= 1

