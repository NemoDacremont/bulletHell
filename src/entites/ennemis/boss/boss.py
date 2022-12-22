# importations bizarre, permet d'importer les types sans avoir
# d'erreures d'importations circulaires
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from fenetre import Fenetre
	from vues.vue import Vue
	from entites.ennemis.boss.phase import Phase

from entites.ennemis.ennemi import Ennemi



class Boss(Ennemi):
	def __init__(self, nom: str, fenetre: Fenetre, vue: Vue, largeur: float,
		hauteur: float, x: float, y: float, PVMax: float, PV: float = -1,
		vitesse: float = 100) -> None:

		super().__init__(nom, fenetre, vue, largeur, hauteur, x, y, PVMax, PV,
			vitesse)

		# Phases du boss
		self.phaseCourrante = 0
		self.phases: list[Phase] = []

		# composantes de la vitesse
		self.vx: float = 0
		self.vy: float = 0


