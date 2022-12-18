
from __future__ import annotations
from typing import TYPE_CHECKING

# typage
if TYPE_CHECKING:
	from fenetre import Fenetre
	from vues.vue import Vue
	#from pygame import Surface

from entites.balles.balle import Balle

class BalleDroite(Balle):
	NOM = "balleDroite"

	def __init__(self, fenetre: Fenetre, vue: Vue, largeur: float, hauteur: float,
							x: float, y: float, groupe: int, vitesse: float, degats: float) -> None:
		super().__init__(BalleDroite.NOM, fenetre, vue, largeur, hauteur, x, y, groupe, vitesse, degats)

		self.vy = self.vitesse
		self.vx = 0


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

