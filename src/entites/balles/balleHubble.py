
from __future__ import annotations
from typing import TYPE_CHECKING

# typage
if TYPE_CHECKING:
	from fenetre import Fenetre
	from vues.vue import Vue

from entites.balles.balle import Balle
from math import cos, sin

"""
Balle Hubble
------------

Une balle fondée sur la loi de Hubble qui dit que les galaxies ont une vitesse
d'éloignement proportionnelle à leur distance.

v = Hr
"""

class balleHubble(Balle):
	NOM = "balleHbble"

	def __init__(self, balle, ref, H) -> None:
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


		self.balle = balle
		self.H = H
		self.ref = ref


	def update(self):
		"""
			Update BalleDroite
			La vitesse de ces balles est constante et va tout droite: il n'y a pas à
			modifier la vitesse
		"""

		

		# Si la balle sort de l'écran, on la retire
		h, k = self.fenetre.getDimensions()
		
		if self.y < -self.hauteur:
			self.retire()
		
		if self.y > k + self.hauteur:
			if self.continuum <= 0:
				self.retire()

		if self.x > h + self.hauteur:
			self.retire()


		if self.x < -self.hauteur:
			self.retire()
