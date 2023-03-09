
from __future__ import annotations
from typing import TYPE_CHECKING


# typage
if TYPE_CHECKING:
	from fenetre import Fenetre
	from vues.vue import Vue

from spritesheet import Spritesheet
from entites.entite import Entite
from math import pi
import pygame


class Balle(Entite):
	COLOR = 255, 0, 255  # violet

	def __init__(self, nom: str, fenetre: Fenetre, vue: Vue, largeur: float,
			hauteur: float, x: float, y: float, groupe: int,
			degats: float, spritesheet: Spritesheet | None = None) -> None:

		if spritesheet is not None:
			super().__init__(nom, fenetre, vue, largeur, hauteur, x, y, spritesheet)
		else:
			SPRITESHEET = Spritesheet("/home/odasta/Documents/programmation/python/prepa-2/bulletHell/src/assets/LaserSprites/01.png")
			super().__init__(nom, fenetre, vue, largeur, hauteur, x, y, SPRITESHEET)

		self.groupe = groupe
		self.degats = degats

		# coté en pixel d'un carré du sprite
		coteSprite = 121
		dimension = (self.largeur * 3, self.hauteur * 3)
		colorKey = None


		self.rectImage = pygame.Rect(0, 0, coteSprite, coteSprite)
		self.image = self.spritesheet.image_at(self.rectImage, colorKey)

		self.image = pygame.transform.scale(self.image, dimension)

	def collision(self):
		personnages = self.vue.getPersonnages()

		for personnage in personnages:
			if self.hitbox.colliderect(personnage.hitbox) and \
				personnage.getGroupe() != self.groupe:

				personnage.recoitDegats(self.degats)
				self.retire()


	def rotImage(self, angle):
		loc = self.image.get_rect().center  # rot_image is not defined
		self.image = pygame.transform.rotate(self.image, angle * 180 / pi)
		self.image.get_rect().center = loc


	def update(self) -> None:
		# Update entite -> update de la position
		super().update()

		# Teste les collisions
		self.collision()



	def draw(self) -> None:
		fenetre = self.fenetre.getFenetre()
		# On redéfini le rect pour qu'il ait la bonne origine
		if self.vue.getAfficheHitBox():
			self.rect = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
			fenetre.fill((255, 0, 0), self.rect)

		# self.rect = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
		# fenetre.fill((255, 0, 0), self.rect)

		coords = self.x - (self.largeur * 3) / 2, self.y - (self.hauteur * 3) / 2
		fenetre.blit(self.image, coords)



