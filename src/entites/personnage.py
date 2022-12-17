
import pygame
from entites.entite import Entite
from fenetre import Fenetre
from vues.vue import Vue

class Personnage(Entite):
	COLOR = 0, 255, 0
	V_EPS = 5 # on considère la vitesse nulle si <5

	def __init__(self, fenetre: Fenetre, vue: Vue, largeur: float, hauteur: float,
							x: float, y: float, groupe: int, acceleration = 10, vitesseMax = 100,
							coefRalentissement = 0.9) -> None:
		super().__init__(fenetre, vue, largeur, hauteur, x, y)

		self.groupe = groupe

		# Vitesse et accélération
		self.vx, self.vy = 0, 0

		self.acceleration = acceleration
		self.vitesseMax = vitesseMax

		self.coefRalentissement = coefRalentissement


	def update(self, event):
		# Calculs Vitesse
		self.vx *= self.coefRalentissement
		self.vy *= self.coefRalentissement

		if self.vx < Personnage.V_EPS:
			self.vx = 0
		if self.vy < Personnage.V_EPS:
			self.vy = 0

		if self.vx < self.vitesseMax:
			self.vx = self.vitesseMax
		if self.vy < self.vitesseMax:
			self.vy = self.vitesseMax


		# Calculs position
		self.x += self.vx
		self.y += self.vy

	def draw(self):
		self.fenetre.getFenetre().fill(Personnage.COLOR, self.rect)


