
import pygame
from entites.personnage import Personnage
from fenetre import Fenetre
from vues.vue import Vue


class Ennemi(Personnage):
	COLOR = 255, 0, 0

	def __init__(self, fenetre: Fenetre, vue: Vue, nom: str, largeur: float, hauteur: float,
							x: float, y: float, groupe: int, vitesse: float = 100) -> None:
		# Constructeur du personnage
		super().__init__(fenetre, vue, largeur, hauteur, x, y, groupe, vitesse)

		# Toujours sympa d'avoir un nom :)
		self.nom = nom


	def draw(self):
		self.rect = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
		self.fenetre.getFenetre().fill(Ennemi.COLOR, self.rect)


