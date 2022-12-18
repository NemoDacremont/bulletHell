
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
	FOCUS = ["o", "O"]

	def __init__(self, nom: str, fenetre: Fenetre, vue: Vue, largeur: float, hauteur: float,
							x: float, y: float, groupe: int, vitesse: float =100, coefRalentissementFocus=0.3) -> None:
		super().__init__(fenetre, vue, largeur, hauteur, x, y, groupe, vitesse)

		self.nom = nom

		# Compteurs pour utiliser
		self.toucheFocus = 0

		self.touchesHaut = 0
		self.touchesBas = 0
		self.touchesGauche = 0
		self.touchesDroite = 0

		self.coefRalentissementFocus = coefRalentissementFocus






	def deplacements(self, event: Event):
		## On met à jour les compteurs de touches pour les déplacements
		# si on appuie sur une touche
		if event.type == pygame.KEYDOWN:
			touche = event.__dict__["unicode"]

			if touche in PersonnageJouable.DEPLACEMENT_HAUT:
				self.touchesHaut += 1
			if touche in PersonnageJouable.DEPLACEMENT_BAS:
				self.touchesBas += 1
			if touche in PersonnageJouable.DEPLACEMENT_GAUCHE:
				self.touchesGauche += 1
			if touche in PersonnageJouable.DEPLACEMENT_DROITE:
				self.touchesDroite += 1

			if touche in PersonnageJouable.FOCUS:
				self.toucheFocus += 1



		# si on relache la touche
		if event.type == pygame.KEYUP:
			touche = event.__dict__["unicode"]
			if touche in PersonnageJouable.DEPLACEMENT_HAUT:
				self.touchesHaut -= 1
			if touche in PersonnageJouable.DEPLACEMENT_BAS:
				self.touchesBas -= 1
			if touche in PersonnageJouable.DEPLACEMENT_GAUCHE:
				self.touchesGauche -= 1
			if touche in PersonnageJouable.DEPLACEMENT_DROITE:
				self.touchesDroite -= 1

			if touche in PersonnageJouable.FOCUS:
				self.toucheFocus -= 1


		# on peut alors mettre à jour les vitesses
		coefRalentissement = 1
		if self.toucheFocus > 0:
			coefRalentissement = self.coefRalentissementFocus

		vitesse = self.vitesse * coefRalentissement

		if self.touchesHaut > 0:
			self.vy = -vitesse
		elif self.touchesBas > 0:
			self.vy = vitesse
		else:
			self.vy = 0

		if self.touchesGauche > 0:
			self.vx = -vitesse
		elif self.touchesDroite > 0:
			self.vx = vitesse
		else:
			self.vx = 0

	def update(self, events: list[Event]):
		# agis sur la vitesse
		for event in events:
			self.deplacements(event)

		# met à jour les déplacements etc
		super().update(events)


