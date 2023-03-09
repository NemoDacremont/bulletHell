# importations bizarre, permet d'importer les types sans avoir
# d'erreures d'importations circulaires
from __future__ import annotations
from typing import TYPE_CHECKING

from spritesheet import Spritesheet

if TYPE_CHECKING:
	from fenetre import Fenetre
	from vues.vue import Vue
	from entites.personnage import Personnage

from entites.balles.balle import Balle
from math import sqrt, inf, atan


class BalleHoming(Balle):
	NOM = "BalleHoming"

	def __init__(self, fenetre: Fenetre, vue: Vue, largeur: float, hauteur: float,
							x: float, y: float, groupe: int, vitesse: float, degats: float):

		SPRITESHEET = Spritesheet("/home/odasta/Documents/programmation/python/prepa-2/bulletHell/src/assets/LaserSprites/03.png")
		super().__init__(BalleHoming.NOM, fenetre, vue, largeur, hauteur, x, y,
			groupe, degats, SPRITESHEET)


		self.vitesse = vitesse
		self.cible: Personnage
		self.trouvePlusProche()  # Permet d'initialiser la cible

		# On retire la balle si elle a parcouru une trop grande distance
		self.distanceParcouru = 0

	def trouvePlusProche(self):
		personnages = self.vue.getPersonnages()
		# Si tous les personnages sont du même groupe, ne tire pas
		c = 0
		for personnage in personnages:
			if personnage.getGroupe() == self.groupe:
				c += 1

		if c == len(personnages):
			self.retire()

		# Cherche l'ennemi le plus proche
		distMin = inf
		personnageMin = personnages[0]
		for personnage in personnages:
			if personnage.getGroupe() != self.groupe:
				personnageCentreX, personnageCentreY = personnage.getPositionCentre()

				dist = sqrt((self.x - personnageCentreX)**2 + (self.y - personnageCentreY)**2)

				if dist < distMin:
					distMin = distMin
					personnageMin = personnage

		self.cible = personnageMin

	def update(self) -> None:
		if self.cible.doitEtreRetirer():
			self.trouvePlusProche()  # Change de cible

		# Calcule les composantes de la vitesse:
		cibleCentreX, cibleCentreY = self.cible.getPositionCentre()
		distCible = sqrt((self.x - cibleCentreX)**2 + (self.y - cibleCentreY)**2)

		self.vx = ((cibleCentreX - self.x) / distCible) * self.vitesse
		self.vy = ((cibleCentreY - self.y) / distCible) * self.vitesse


		super().update()





