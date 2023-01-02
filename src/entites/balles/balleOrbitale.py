from __future__ import annotations
from typing import TYPE_CHECKING

# typage
if TYPE_CHECKING:
	from fenetre import Fenetre
	from vues.vue import Vue
	from entites import Entite

from math import cos, sin, sqrt
from entites.balles.balle import Balle
from cmath import phase
import utils as u

class BalleOrbitale(Balle):
	
	NOM = "balleOrbitale"

	def __init__(self, fenetre: Fenetre, vue: Vue, largeur: float, hauteur: float
	   , groupe: int, direction : float, vr: float, vTheta : float, distance : float, degats: float,
		centre : Entite, timer : float) -> None:
		"""
			Constructeur de BalleOrbitale
			Paramètres:
				- fenetre: Fenetre, la fenêtre dans laquelle on affiche la balle
				- vue: Vue: la vue dans laquelle on affiche la balle
				- largeur: la largeur de la balle
				- hauteur: la hauteur de la balle
				- groupe: int, le groupe auquel la balle appartient, permet de détecter
					les adversaires
				- vr : vitesse radiale initiale
				- vTheta : vitesse angulaire (constante)
				- distance : distance cible à laquelle la balle va tourner autour du centre
				- degats : dégats de la balle
				- centre : entité autour de laquelle la balle va tourner
				- timer : temps durant lequel la balle va tourner. Une fois écoulé,
				elle se rétracte sur le centre.
		"""
		
		x, y = centre.x, centre.y
		super().__init__(BalleOrbitale.NOM, fenetre, vue, largeur, hauteur, x, y,
			groupe, degats)

		self.centre = centre
		self.timer = timer
		self.vrAbs = vr #Ne change jamais
		self.vr = vr
		self.vTheta = vTheta
		self.vx = vr * cos(direction) + centre.vx
		self.vy = vr * sin(direction) + centre.vy
		self.r = 0
		self.distance = distance
		self.theta = direction
		
	def calculeVitesse(self):
		
		x0, y0 = self.centre.x, self.centre.y
		
		# Recalcule r
		self.r = sqrt((self.x - x0)**2 + (self.y - y0)**2)

		# calcule theta
		dt = self.vue.getDT()
		self.theta += self.vTheta * dt

		# Histoire de rendre la formule buvable
		r, theta = self.r, self.theta
		vr, vTheta = self.vr, self.vTheta

		# Bon faut projeter :)
		self.vx = vr * cos(theta) + r * vTheta * sin(theta) + self.centre.vx
		self.vy = vr * sin(theta) - r * vTheta * cos(theta) + self.centre.vy
		
	def update(self):
		
		#Lisibilité
		dt = self.vue.getDT()
		x, y = self.x, self.y
		centre = self.centre
		
		self.calculeVitesse()
		super().update()
		
		r = abs(x - centre.x + 1j * (y - centre.y))
		self.timer -= dt
		
		#Il faut tourner autour du boss
		if self.timer > 0:
			self.vr = self.vrAbs * (1 - r / self.distance)
			print(self.vr)
 			
		#Si le temps est écoulé, on revient sur le boss
		else:
 			self.vr = - 1 * self.vrAbs
 			if r < self.vrAbs:
 				 self.retire()
			
		
		
		