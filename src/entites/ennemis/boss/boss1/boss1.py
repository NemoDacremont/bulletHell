# importations bizarre, permet d'importer les types sans avoir
# d'erreures d'importations circulaires
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from fenetre import Fenetre
	from vues.vue import Vue
	from pygame.event import Event

# classes ...
from entites.ennemis.boss.boss import Boss
from entites.ennemis.boss.boss1.phases.phase1 import Boss1Phase1


class Boss1(Boss):
	NOM = "unPremierBoss"

	LARGEUR = 60
	HAUTEUR = 60

	PV_MAX = 100

	VITESSE = 50

	def __init__(self, fenetre: Fenetre, vue: Vue, x: float, y: float) -> None:
		pv = -1  # Commence avec tout ses PVs
		super().__init__(Boss1.NOM, fenetre, vue, Boss1.LARGEUR, Boss1.HAUTEUR, x, y,
			Boss1.PV_MAX, pv, Boss1.VITESSE)

		# Définition des déplacements
		self.vx = self.vitesse
		self.vy = 0

		# Définition des phases
		self.phaseCourrante = 0
		self.phases = [Boss1Phase1(self)]


	def update(self, events: list[Event]):
		phase = self.phases[self.phaseCourrante]
		phase.update()

		super().update(events)
