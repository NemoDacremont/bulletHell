
from __future__ import annotations
from typing import TYPE_CHECKING

# typage
if TYPE_CHECKING:
	from fenetre import Fenetre
	from vues.vue import Vue
	# from pygame import Surface

from entites.entite import Entite
import pygame



class Balle(Entite):
	COLOR = 255, 0, 255  # violet

	def __init__(self, nom: str, fenetre: Fenetre, vue: Vue, largeur: float,
							hauteur: float, x: float, y: float, groupe: int,
							degats: float, couleur = (255, 0, 255)) -> None:
		super().__init__(nom, fenetre, vue, largeur, hauteur, x, y)

		self.groupe = groupe
		self.degats = degats
		self.color = couleur

	def collision(self):
		personnages = self.vue.getPersonnages()

		for personnage in personnages:
			if self.hitbox.colliderect(personnage.hitbox) and \
				personnage.getGroupe() != self.groupe:

				personnage.recoitDegats(self.degats)
				self.retire()

	def update(self) -> None:
		# Update entite -> update de la position
		super().update()

		# Teste les collisions
		self.collision()



	def draw(self) -> None:
		fenetre = self.fenetre.getFenetre()
		# On redéfini le rect pour qu'il ait la bonne origine
		self.rect = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
		fenetre.fill(self.color, self.rect)


