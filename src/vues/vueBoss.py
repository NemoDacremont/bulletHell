# importations bizarre, permet d'importer les types sans avoir
# d'erreures d'importations circulaires
from __future__ import annotations
from sys import path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from jeu import Jeu


import pygame
from vues.vue import Vue
from entites.personnage import Personnage
from entites.personnageJouable.personnage1 import Personnage1
from entites.ennemis.boss.boss1.boss1 import Boss1



class VueBoss(Vue):
	def __init__(self, jeu: Jeu, etat: int, pausePossible: bool) -> None:
		# Constructeur Vue
		super().__init__(jeu, etat, pausePossible)

		# Compteur pour connaître la phase actuelle
		self.phase = 0

		# Données cool
		fenetreLargeur, fenetreHauteur = jeu.fenetre.getDimensions()

		# Joueur
		joueurX = fenetreLargeur / 4
		joueurY = fenetreHauteur / 2

		joueur = Personnage1(self.fenetre, self, joueurX, joueurY)

		#  Création d'un ennemi
		ennemiX = fenetreLargeur / 2
		ennemiY = 50

		ennemi = Boss1(self.fenetre, self, ennemiX, ennemiY)

		# Création des listes
		self.personnages: list[Personnage] = [joueur, ennemi]
		self.joueurs = [joueur]

		# Gadget
		print("Personnages: ")
		for personnage in self.personnages:
			print(personnage.nom)

		# Sprites, tests
		self.image = pygame.image.load("/home/odasta/Documents/programmation/python/prepa-2/bulletHell/src/assets/Ship_Nebula-Sprite_Sheet.png")

	def draw(self):
		super().draw()

		self.fenetre.getFenetre().blit(self.image, (0, 0))




