
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from pygame.event import Event
	from fenetre import Fenetre
	from vues.vue import Vue

from entites.balles.balleCirculaire import BalleCirculaire
from entites.personnageJouable.personnageJouable import PersonnageJouable
from entites.balles.balleDroite import BalleDroite
from entites.balles.balleHoming import BalleHoming
from math import pi


class Personnage1(PersonnageJouable):
	NOM = "personnage1"
	LARGEUR = 50
	HAUTEUR = 50
	PV_MAX = 10
	VITESSE = 100
	COEF_RALENTISSEMENT_FOCUS = 0.3

	CADENCE_DE_TIR = 3
	DEGATS = 1

	def __init__(self, fenetre: Fenetre, vue: Vue, x: float, y: float) -> None:
		# Constructeur PersonnageJouable
		super().__init__(Personnage1.NOM, fenetre, vue, Personnage1.LARGEUR,
										Personnage1.HAUTEUR, x, y, Personnage1.PV_MAX, PV=-1,
										vitesse=Personnage1.VITESSE,
										coefRalentissementFocus=Personnage1.COEF_RALENTISSEMENT_FOCUS)

		self.timerTir = 1 / Personnage1.CADENCE_DE_TIR


	def tire(self):
		"""
			Attaque: tire 2 projectiles devant le personnage et une balle homing
		"""
		balleLargeur = 10
		balleHauteur = 10

		tir1X = self.x + (self.largeur / 4) - (balleLargeur / 2)
		tir2X = self.x + (3 * self.largeur / 4) - (balleLargeur / 2)
		tirY = self.y - 2 * balleHauteur

		tirDirection = -pi / 2  # part vers le haut

		tirVitesse = 200
		tirDegats = Personnage1.DEGATS

		tir1 = BalleDroite(self.fenetre, self.vue, balleLargeur, balleHauteur,
										tir1X, tirY, PersonnageJouable.GROUPE, tirVitesse,
										tirDegats, tirDirection)
		tir2 = BalleDroite(self.fenetre, self.vue, balleLargeur, balleHauteur,
										tir2X, tirY, PersonnageJouable.GROUPE, tirVitesse,
										tirDegats, tirDirection)

		tir3 = BalleHoming(self.fenetre, self.vue, balleLargeur, balleHauteur,
										tir1X, tirY, PersonnageJouable.GROUPE, tirVitesse / 2,
										tirDegats)


		for i in range(6):
			x0, y0 = self.getPositionCentre()

			tirX0 = x0 - balleLargeur / 2
			tirY0 = y0 - balleHauteur / 2

			theta = i * (pi / 3)
			v_r = 5
			v_theta = pi / 6

			balle = BalleCirculaire(self.fenetre, self.vue, balleLargeur, balleHauteur,
													tirX0, tirY0, PersonnageJouable.GROUPE, tirDegats,
													theta, v_r, v_theta)

			self.vue.ajouteBalle(balle)


		self.vue.ajouteBalle(tir1)
		self.vue.ajouteBalle(tir2)
		self.vue.ajouteBalle(tir3)


	def update(self, events: list[Event]):
		super().update(events)

		dt = 1 / self.fenetre.fps
		self.timerTir -= dt

		if self.timerTir <= 0:
			self.timerTir = 1 / Personnage1.CADENCE_DE_TIR
			self.tire()





