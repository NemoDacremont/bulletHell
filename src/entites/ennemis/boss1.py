# importations bizarre, permet d'importer les types sans avoir
# d'erreures d'importations circulaires
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from fenetre import Fenetre
	from vues.vue import Vue
	from pygame.event import Event

from entites.ennemis.boss import Boss


class Boss1(Boss):
	NOM = "unPremierBoss"

	def __init__(self, fenetre: Fenetre, vue: Vue, largeur: float, hauteur: float,
							x: float, y: float, PVMax: float, PV: float = -1,
							vitesse: float = 50) -> None:
		super().__init__(Boss1.NOM, fenetre, vue, largeur, hauteur, x, y, PVMax, PV,
										vitesse)

		self.vx = vitesse
		self.vy = 0


	def update(self, events: list[Event]):

		# Si à gauche de l'écran: va à droite, ne peut pas sortir de l'écran
		if self.x < 0:
			self.x = 0
			self.vx = self.vitesse

		# Si à droite de l'écran: va à gauche, ne peut pas sortir de l'écran
		if self.x > self.fenetre.largeur - self.largeur:
			self.x = self.fenetre.largeur - self.largeur
			self.vx = -self.vitesse

		super().update(events)

