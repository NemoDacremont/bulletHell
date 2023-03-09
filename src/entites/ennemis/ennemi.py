# importations bizarre, permet d'importer les types sans avoir
# d'erreures d'importations circulaires
from __future__ import annotations
from typing import TYPE_CHECKING

from spritesheet import Spritesheet

if TYPE_CHECKING:
	from fenetre import Fenetre
	from vues.vue import Vue

from entites.personnage import Personnage
import pygame





class Ennemi(Personnage):
	COLOR = 255, 0, 0  # rouge car méchant :)

	# Les ennemis appartiennent au groupe 1
	GROUPE = -1

	def __init__(self, nom: str, fenetre: Fenetre, vue: Vue, largeur: float,
							hauteur: float, x: float, y: float, PVMax: float, PV: float = -1,
							vitesse: float = 100) -> None:

		# Constructeur du personnage
		spritesheet = Spritesheet("/home/odasta/Documents/programmation/python/prepa-2/bulletHell/src/assets/Ship_Nebula-Sprite_Sheet.png")
		super().__init__(nom, fenetre, vue, largeur, hauteur, x, y, PVMax, PV,
			vitesse, spritesheet)

		self.groupe = Ennemi.GROUPE


	def draw(self):
		self.rectAffichage = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
		self.fenetre.getFenetre().fill(Ennemi.COLOR, self.rectAffichage)


