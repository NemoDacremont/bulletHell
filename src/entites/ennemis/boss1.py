# importations bizarre, permet d'importer les types sans avoir
# d'erreures d'importations circulaires
from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
	from fenetre import Fenetre
	from vues.vue import Vue
	from pygame.event import Event

from entites.ennemis.ennemi import Ennemi
from entites.ennemis.boss import Boss
from entites.balles.balleDroite import BalleDroite
from math import pi


class Boss1(Boss):
	NOM = "unPremierBoss"
	CADENCE_DE_TIR = 1

	def __init__(self, fenetre: Fenetre, vue: Vue, largeur: float, hauteur: float,
							x: float, y: float, PVMax: float, PV: float = -1,
							vitesse: float = 50) -> None:
		super().__init__(Boss1.NOM, fenetre, vue, largeur, hauteur, x, y, PVMax, PV,
										vitesse)

		self.vx = vitesse
		self.vy = 0
		self.timerTir = 1 / Boss1.CADENCE_DE_TIR

	def tire(self):
		balleLargeur = 10
		balleHauteur = 10

		tir1X = self.x + (self.largeur / 2) - (balleLargeur / 2)
		tirY = self.y - 2 * balleHauteur

		tirDirection = pi / 2  # part vers le bas

		tirVitesse = 100
		tirDegats = 1

		balle = BalleDroite(self.fenetre, self.vue, balleLargeur, balleHauteur,
											tir1X, tirY, Ennemi.GROUPE, tirVitesse, tirDegats,
											tirDirection)
		self.vue.ajouteBalle(balle)

	def update(self, events: list[Event]):

		# Si à gauche de l'écran: va à droite, ne peut pas sortir de l'écran
		if self.x < 0:
			self.x = 0
			self.vx = self.vitesse

		# Si à droite de l'écran: va à gauche, ne peut pas sortir de l'écran
		if self.x > self.fenetre.largeur - self.largeur:
			self.x = self.fenetre.largeur - self.largeur
			self.vx = -self.vitesse

		# Tirs
		dt = 1 / self.fenetre.fps
		self.timerTir -= dt

		if self.timerTir <= 0:
			self.timerTir = 1 / Boss1.CADENCE_DE_TIR
			self.tire()

		super().update(events)

