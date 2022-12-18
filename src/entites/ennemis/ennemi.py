
import pygame
from entites.personnage import Personnage
from fenetre import Fenetre
from vues.vue import Vue


class Ennemi(Personnage):
	COLOR = 255, 0, 0 # rouge car méchant :)

	## Les ennemis appartiennent au groupe 1
	GROUPE = -1

	def __init__(self, nom: str, fenetre: Fenetre, vue: Vue, largeur: float, hauteur: float,
							x: float, y: float, PVMax: float, PV: float = -1, vitesse: float = 100) -> None:
		# Constructeur du personnage
		super().__init__(nom, fenetre, vue, largeur, hauteur, x, y, PVMax, PV, vitesse)

		# Toujours sympa d'avoir un nom :)
		self.nom = nom

		self.groupe = Ennemi.GROUPE


	def draw(self):
		self.rect = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
		self.fenetre.getFenetre().fill(Ennemi.COLOR, self.rect)

