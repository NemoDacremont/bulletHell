
from pygame.event import Event
import pygame

from entites.personnage import Personnage
from fenetre import Fenetre
from vues.vue import Vue


class PersonnageJouable(Personnage):
	DEPLACEMENT_HAUT = ["z", "Z"]
	DEPLACEMENT_BAS = ["s", "S"]
	DEPLACEMENT_GAUCHE = ["q", "Q"]
	DEPLACEMENT_DROITE = ["d", "D"]

	def __init__(self, nom: str, fenetre: Fenetre, vue: Vue, largeur: float, hauteur: float,
							x: float, y: float, groupe: int, acceleration=10, vitesseMax=100,
							coefRalentissement=0.9) -> None:
		super().__init__(fenetre, vue, largeur, hauteur, x, y, groupe, acceleration, vitesseMax, coefRalentissement)

		self.nom = nom


	def deplacements(self, event: Event):
		if event.type == pygame.KEYDOWN:
			pass

	def update(self, event: Event):

		super().update(event)


