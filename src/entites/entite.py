

# from pygame import Surface
import pygame

from fenetre import Fenetre
from vues.vue import Vue


class Entite:
	COLOR = 0, 0, 255

	def __init__(self, nom: str, fenetre: Fenetre, vue: Vue, largeur: float,
							hauteur: float, x: float, y: float) -> None:

		self.nom = nom

		# Forme
		self.largeur = largeur
		self.hauteur = hauteur

		# Position
		self.x = x
		self.y = y

		# Vitesse
		self.vx, self.vy = 0, 0

		# pour les collisions
		self.hitbox = pygame.Rect(x, y, largeur, hauteur)

		# Sert à l'affichage
		self.rectAffichage = pygame.Rect(x, y, largeur, hauteur)
		self.fenetre = fenetre
		self.vue = vue

		# Permet à la vue de savoir s'il faut supprimer l'entite
		self.doitRetirer: bool = False

	def doitEtreRetirer(self) -> bool:
		return self.doitRetirer

	def retire(self) -> None:
		self.doitRetirer = True

	def update(self):
		"""
			Met à jour la position
		"""
		fps = self.fenetre.fps

		# Calculs position
		dx = self.vx / fps
		dy = self.vy / fps

		self.x += dx
		self.y += dy

		# Calcul de la hitbox
		self.hitbox = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)


	def draw(self):
		fenetre = self.fenetre.getFenetre()
		self.rectAffichage = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
		fenetre.fill(Entite.COLOR, self.rectAffichage)


