
from __future__ import annotations
from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
	from pygame.event import Event
	from fenetre import Fenetre
	from vues.vue import Vue

from entites.personnageJouable.personnageJouable import PersonnageJouable
from entites.balles.balleDroite import BalleDroite
from entites.balles.balleHoming import BalleHoming
from math import pi


class Personnage1(PersonnageJouable):
	NOM = "personnage1"

	# Affichage
	LARGEUR = 50
	HAUTEUR = 50

	# caractéristiques
	PV_MAX = 10
	VITESSE = 500
	COEF_RALENTISSEMENT_FOCUS = 0.3

	CADENCE_DE_TIR = 10
	DEGATS = 1

	def __init__(self, fenetre: Fenetre, vue: Vue, x: float, y: float) -> None:
		# Constructeur PersonnageJouable
		super().__init__(Personnage1.NOM, fenetre, vue, Personnage1.LARGEUR,
										Personnage1.HAUTEUR, x, y, Personnage1.PV_MAX, PV=-1,
										vitesse=Personnage1.VITESSE,
										coefRalentissementFocus=Personnage1.COEF_RALENTISSEMENT_FOCUS)

		# Timer de tir
		self.timerTir = 1 / Personnage1.CADENCE_DE_TIR


	def tire(self, events: list[Event]):
		"""
			Attaque: tire 2 projectiles devant le personnage et une balle homing
		"""
		if self.toucheAttaque > 0:
			balleLargeur = 10
			balleHauteur = 10

			tir1X = self.x + (self.largeur / 4) - (balleLargeur / 2)
			tir2X = self.x + (3 * self.largeur / 4) - (balleLargeur / 2)
			tirY = self.y - 2 * balleHauteur

			tirDirection = -pi / 2  # part vers le haut

			tirVitesse = self.fenetre.getHauteur()
			tirDegats = Personnage1.DEGATS

			tir1 = BalleDroite(self.fenetre, self.vue, balleLargeur, balleHauteur,
											tir1X, tirY, PersonnageJouable.GROUPE, tirVitesse,
											tirDegats, tirDirection)
			tir2 = BalleDroite(self.fenetre, self.vue, balleLargeur, balleHauteur,
											tir2X, tirY, PersonnageJouable.GROUPE, tirVitesse,
											tirDegats, tirDirection)

			tir3 = BalleHoming(self.fenetre, self.vue, balleLargeur, balleHauteur,
											tir1X, tirY, PersonnageJouable.GROUPE, tirVitesse,
											tirDegats)


			self.vue.ajouteBalle(tir1)
			self.vue.ajouteBalle(tir2)
			self.vue.ajouteBalle(tir3)
			self.timerTir = 1 / Personnage1.CADENCE_DE_TIR


	def update(self, events: list[Event]):
		super().update(events)

		dt = self.vue.getDT()
		self.timerTir -= dt

		if self.timerTir <= 0:
			self.tire(events)



