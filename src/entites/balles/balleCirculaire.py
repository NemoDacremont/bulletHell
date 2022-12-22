
from __future__ import annotations
from typing import TYPE_CHECKING

# typage
if TYPE_CHECKING:
	from fenetre import Fenetre
	from vues.vue import Vue

from entites.balles.balleDroite import Balle
from math import cos, sin, sqrt


class BalleCirculaire(Balle):
	NOM = "balleCirculaire"
	DISTANCE_PARCOURU_MAX = 10**4

	def __init__(self, fenetre: Fenetre, vue: Vue, largeur: float, hauteur: float,
							x: float, y: float, groupe: int, degats: float,
							theta: float, v_r: float, v_theta: float) -> None:
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
					entre \\vec x et \\vec y
		"""

		super().__init__(BalleCirculaire.NOM, fenetre, vue, largeur, hauteur, x, y,
			groupe, degats)

		self.theta = theta

		# On doit stocker le centre de rotation
		self.x0, self.y0 = x, y
		self.v_r = v_r
		self.v_theta = v_theta

		# On garde en mémoire la distance parcourue pour supprimer la balle si elle
		# est trop loin
		self.distanceParcourue = 0

		# la formule est infâme -> fonction :)
		self.calculeVitesse()



	def calculeVitesse(self):
		# Recalcule r
		self.r = sqrt((self.x - self.x0)**2 + (self.y - self.y0)**2)

		# calcule theta
		dt = self.vue.getDT()
		self.theta += self.v_theta * dt

		# Histoire de rendre la formule buvable
		r, theta = self.r, self.theta
		v_r, v_theta = self.v_r, self.v_theta

		# Bon faut projeter :)
		self.vx = v_r * cos(theta) + r * v_theta * sin(theta)
		self.vy = v_r * sin(theta) - r * v_theta * cos(theta)


	def update(self):
		"""
			Update BalleDroite
			La vitesse de ces balles est constante et va tout droite: il n'y a pas à
			modifier la vitesse
		"""

		self.calculeVitesse()
		super().update()

		dt = self.vue.getDT()
		dv = sqrt(self.vx**2 + self.vy**2) * dt
		self.distanceParcourue += dv

		# Si la  distance parcourue est trop grande: on la retire
		if self.distanceParcourue > BalleCirculaire.DISTANCE_PARCOURU_MAX:
			self.retire()



