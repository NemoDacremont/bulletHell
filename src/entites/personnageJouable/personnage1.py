
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from pygame.event import Event
	from fenetre import Fenetre
	from vues.vue import Vue

# Hérite
from entites.personnageJouable.personnageJouable import PersonnageJouable

# update
from entites.balles.balleDroite import BalleDroite
from entites.balles.balleHoming import BalleHoming

# math
from math import pi

# Affichage
from spritesheet import Spritesheet
import pygame


class Personnage1(PersonnageJouable):
	NOM = "personnage1"

	# Affichage
	LARGEUR = 50
	HAUTEUR = 50

	# caractéristiques
	PV_MAX = 10
	VITESSE = 500
	COEF_RALENTISSEMENT_FOCUS = 0.3

	CADENCE_DE_TIR = 10
	DEGATS = 1

	def __init__(self, fenetre: Fenetre, vue: Vue, x: float, y: float) -> None:
		# Constructeur PersonnageJouable
		PV = -1
		SPRITESHEET = Spritesheet("/home/odasta/Documents/programmation/python/prepa-2/bulletHell/src/assets/Ship_Nebula-Sprite_Sheet.png")

		super().__init__(Personnage1.NOM, fenetre, vue, Personnage1.LARGEUR,
			Personnage1.HAUTEUR, x, y, Personnage1.PV_MAX, PV, Personnage1.VITESSE,
			Personnage1.COEF_RALENTISSEMENT_FOCUS, SPRITESHEET)

		# Timer de tir
		self.timerTir = 1 / Personnage1.CADENCE_DE_TIR

		# coté en pixel d'un carré du sprite
		coteSprite = 32
		dimension = (self.largeur, self.hauteur)
		colorKey = None

		self.tempsAnimation = 0.1

		# Animation de gauche
		self.etatAnimationGauche = 0
		self.timerAnimationGauche = self.tempsAnimation
		rectGauche = pygame.Rect(0, 2 * coteSprite, coteSprite, coteSprite)
		nbImageGauche = 3
		self.animationGauche = self.spritesheet.load_strip(rectGauche, nbImageGauche,
			colorKey)

		# Redimensionne
		for i in range(len(self.animationGauche)):
			self.animationGauche[i] = pygame.transform.scale(self.animationGauche[i],
				dimension)

		# Animation de droite
		self.etatAnimationDroite = 0
		self.timerAnimationDroite = self.tempsAnimation
		rectDroite = pygame.Rect(0, 1 * coteSprite, coteSprite, coteSprite)
		nbImageDroite = 3
		self.animationDroite = self.spritesheet.load_strip(rectDroite, nbImageDroite,
			colorKey)

		# Redimensionne
		for i in range(len(self.animationDroite)):
			self.animationDroite[i] = pygame.transform.scale(self.animationDroite[i],
				dimension)

		# Animation idle
		self.etatAnimationIdle = 0
		self.timerAnimationIdle = self.tempsAnimation
		rectIdle = pygame.Rect(0, 0, coteSprite, coteSprite)
		nbImageIdle = 4
		self.animationIdle = self.spritesheet.load_strip(rectIdle, nbImageIdle,
			colorKey)

		# Redimensionne
		for i in range(len(self.animationIdle)):
			self.animationIdle[i] = pygame.transform.scale(self.animationIdle[i],
				dimension)

		# Animation explosion
		self.etatAnimationExplosion = 0
		rectExplosion = pygame.Rect(0, 3 * coteSprite, coteSprite, coteSprite)
		nbImageExplosion = 9
		self.animationExplosion = self.spritesheet.load_strip(rectExplosion,
			nbImageExplosion, colorKey)

		# Redimensionne
		for i in range(len(self.animationExplosion)):
			self.animationExplosion[i] = pygame.transform.scale(self.animationExplosion[i],
				dimension)

	def updateAnimation(self):
		dt = self.vue.getDT()

		if self.touchesGauche > 0:
			self.timerAnimationGauche -= dt
			if self.timerAnimationGauche < 0:
				self.etatAnimationGauche = (self.etatAnimationGauche + 1) % len(self.animationGauche)
				self.timerAnimationGauche = self.tempsAnimation

		elif self.touchesDroite > 0:
			self.timerAnimationDroite -= dt
			if self.timerAnimationDroite < 0:
				self.etatAnimationDroite = (self.etatAnimationDroite + 1) % len(self.animationDroite)
				self.timerAnimationDroite = self.tempsAnimation

		else:
			self.timerAnimationIdle -= dt
			if self.timerAnimationIdle < 0:
				self.etatAnimationIdle = (self.etatAnimationIdle + 1) % len(self.animationIdle)
				self.timerAnimationIdle = self.tempsAnimation


	def tire(self):
		"""
			Attaque: tire 2 projectiles devant le personnage et une balle homing
		"""
		if self.toucheAttaque > 0:
			balleLargeur = 10
			balleHauteur = 10

			tir1X = self.x + (self.largeur / 4) - (balleLargeur / 2)
			tir2X = self.x + (3 * self.largeur / 4) - (balleLargeur / 2)
			tirY = self.y - 2 * balleHauteur

			tirDirection = pi / 2  # part vers le haut

			tirVitesse = self.fenetre.getHauteur()
			tirDegats = Personnage1.DEGATS

			tir1 = BalleDroite(self.fenetre, self.vue, balleLargeur, balleHauteur,
				tir1X, tirY, PersonnageJouable.GROUPE, tirVitesse,
				tirDegats, tirDirection)
			tir2 = BalleDroite(self.fenetre, self.vue, balleLargeur, balleHauteur,
				tir2X, tirY, PersonnageJouable.GROUPE, tirVitesse,
				tirDegats, tirDirection)

			tir3 = BalleHoming(self.fenetre, self.vue, balleLargeur, balleHauteur,
				tir1X, tirY, PersonnageJouable.GROUPE, tirVitesse,
				tirDegats)


			self.vue.ajouteBalle(tir1)
			self.vue.ajouteBalle(tir2)
			self.vue.ajouteBalle(tir3)
			self.timerTir = 1 / Personnage1.CADENCE_DE_TIR


	def update(self, events: list[Event]):
		super().update(events)
		self.updateAnimation()

		dt = self.vue.getDT()
		self.timerTir -= dt

		if self.timerTir <= 0:
			self.tire()

	def draw(self):
		# rect = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
		coords = self.x, self.y
		fenetre = self.fenetre.getFenetre()
		if self.touchesGauche > 0:
			imageGauche = self.animationGauche[self.etatAnimationGauche]
			fenetre.blit(imageGauche, coords)
		elif self.touchesDroite > 0:
			imageDroite = self.animationDroite[self.etatAnimationDroite]
			fenetre.blit(imageDroite, coords)
		else:
			imageIdle = self.animationIdle[self.etatAnimationIdle]
			fenetre.blit(imageIdle, coords)


