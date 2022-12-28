
from __future__ import annotations
from typing import TYPE_CHECKING

# typage
if TYPE_CHECKING:
	from fenetre import Fenetre
	from vues.vue import Vue

from entites.balles.balle import Balle
from math import cos, sin


class BalleDroite(Balle):
	NOM = "balleDroite"

	def __init__(self, fenetre: Fenetre, vue: Vue, largeur: float, hauteur: float,
		x: float, y: float, groupe: int, vitesse: float, degats: float,
		direction: float) -> None:
		"""
			Constructeur de BalleDroite
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

		super().__init__(BalleDroite.NOM, fenetre, vue, largeur, hauteur, x, y,
			groupe, degats)

		self.direction = direction
		self.vy = sin(direction) * vitesse
		self.vx = cos(direction) * vitesse


	def update(self):
		"""
			Update BalleDroite
			La vitesse de ces balles est constante et va tout droite: il n'y a pas à
			modifier la vitesse
		"""

		super().update()

		# Si la balle sort de l'écran, on la retire
		if self.y < -self.hauteur:
			self.retire()

