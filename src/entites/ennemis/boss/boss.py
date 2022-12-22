# importations bizarre, permet d'importer les types sans avoir
# d'erreures d'importations circulaires
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from fenetre import Fenetre
	from vues.vue import Vue
	from entites.ennemis.boss.phase import Phase

from entites.ennemis.ennemi import Ennemi
import pygame


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


	def recoitDegats(self, degats: float):
		super().recoitDegats(degats)

		phase = self.phases[self.phaseCourrante]
		phase.recoitDegats(degats)


	def drawInterface(self):
		RED = 255, 0, 0
		hauteur = 30
		largeur = 100 * (self.PV / self.PVMax)
		life = pygame.Rect(10, 10, largeur, hauteur)
		pygame.draw.rect(self.fenetre.getFenetre(), RED, life)


	def changePhase(self):
		if self.phaseCourrante < len(self.phases) - 1:
			self.phaseCourrante += 1

		if self.PV < 0:
			self.retire()
