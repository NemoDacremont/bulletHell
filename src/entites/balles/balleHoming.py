# importations bizarre, permet d'importer les types sans avoir
# d'erreures d'importations circulaires
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from fenetre import Fenetre
	from vues.vue import Vue
	from entites.personnage import Personnage

from entites.balles.balle import Balle

from math import sqrt, inf

class BalleHoming(Balle):
	NOM = "BalleHoming"

	def __init__(self, fenetre: Fenetre, vue: Vue, largeur: float, hauteur: float,
							x: float, y: float, groupe: int, vitesse: float, degats: float) -> None:
		super().__init__(BalleHoming.NOM, fenetre, vue, largeur, hauteur, x, y, groupe,
										vitesse, degats)


		self.cible: Personnage
		self.trouvePlusProche() # Permet d'initialiser la cible

		# On retire la balle si elle a parcouru une trop grande distance
		self.distanceParcouru = 0

	def trouvePlusProche(self):
		personnages = self.vue.getPersonnages()

		distMin = inf
		personnageMin = personnages[0]
		for personnage in personnages:
			if personnage.getGroupe() != self.groupe:
				personnageX, personnageY = personnage.getPosition()
				dist = sqrt( (self.x - personnageX)**2 + (self.y - personnageY)**2 )

				if dist < distMin:
					distMin = distMin
					personnageMin = personnage

		self.cible = personnageMin

	def update(self) -> None:
		if self.cible.doitEtreRetirer():
			self.trouvePlusProche() # Change de cible

		# Calcule les composantes de la vitesse:
		cibleX, cibleY = self.cible.getPosition()
		distCible = sqrt( (self.x - cibleX)**2 + (self.y - cibleY)**2 )

		self.vx = - ( (cibleX - self.x) / distCible ) * self.vitesse
		self.vy = - ( (cibleY - self.y) / distCible ) * self.vitesse


		super().update()





