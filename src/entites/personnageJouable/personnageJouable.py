# importations bizarre, permet d'importer les types sans avoir
# d'erreures d'importations circulaires
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from spritesheet import Spritesheet


from pygame.event import Event
import pygame

from entites.personnage import Personnage
from fenetre import Fenetre
from vues.vue import Vue


class PersonnageJouable(Personnage):
	TOUCHES_DEPLACEMENT_HAUT = [pygame.K_z, pygame.K_UP]
	TOUCHES_DEPLACEMENT_BAS = [pygame.K_s, pygame.K_DOWN]
	TOUCHES_DEPLACEMENT_GAUCHE = [pygame.K_q, pygame.K_LEFT]
	TOUCHES_DEPLACEMENT_DROITE = [pygame.K_d, pygame.K_RIGHT]

	TOUCHES_FOCUS = [pygame.K_k, pygame.K_LSHIFT]
	TOUCHE_ATTAQUE = [pygame.K_o, pygame.K_SPACE]

	GROUPE = 1

	HITBOX_COLOR = 255, 0, 255
	HITBOX_LARGEUR = 10
	HITBOX_HAUTEUR = 10

	DUREE_IFRAME = 0.5

	def __init__(self, nom: str, fenetre: Fenetre, vue: Vue, largeur: float,
		hauteur: float, x: float, y: float, PVMax: float, PV: float,
		vitesse: float, coefRalentissementFocus: float, spritesheet: Spritesheet) -> None:
		"""
			Constructeur Personnage
			Paramètres:
				- nom: str, le nom du personnage
				- fenetre: Fenetre, la fenêtre du jeu
				- vue: Vue, La vue à laquelle il appartient
				- largeur: float, la largeur en pixels du perssonnage
				- hauteur: float, la hauteur en pixels du perssonnage
				- x: float, la position initiale en x du personnage
				- y: float, la position initiale en y du personnage
				- PVMax: float, les PVs max du personnage
				- PV: float, les PVs initiaux du personnage, si PV == -1, alors PV = PVMax
				- vitesse: float, le nombre de pixels parcourus en 1 sec
				- coefRalentissementFocus: float, correspond au ralentissement lors de
					l'action "focus"
		"""
		super().__init__(nom, fenetre, vue, largeur, hauteur, x, y, PVMax, PV,
			vitesse, spritesheet)

		self.nom = nom

		# iframes
		self.dureeIframe = PersonnageJouable.DUREE_IFRAME
		self.timerIframe = 0

		# Compteurs pour utiliser
		self.toucheFocus = 0

		self.touchesHaut = 0
		self.touchesBas = 0
		self.touchesGauche = 0
		self.touchesDroite = 0

		self.toucheAttaque = 0

		self.coefRalentissementFocus = coefRalentissementFocus
		self.groupe = PersonnageJouable.GROUPE

		self.hitbox = pygame.Rect(x, y, PersonnageJouable.HITBOX_LARGEUR,
			PersonnageJouable.HITBOX_HAUTEUR)


	def recoitDegats(self, degats: float):
		# Ne prend des dégats que si il n'a pas d'iframe
		if self.timerIframe <= 0:
			super().recoitDegats(degats)
			self.timerIframe = self.dureeIframe

	def updateAppuiDeTouche(self, event: Event):
		# On met à jour les compteurs de touches pour les déplacements
		# Détecte l'appuie sur une touche
		if event.type == pygame.KEYDOWN:
			touche = event.__dict__["key"]

			if touche in PersonnageJouable.TOUCHES_DEPLACEMENT_HAUT:
				self.touchesHaut += 1
			if touche in PersonnageJouable.TOUCHES_DEPLACEMENT_BAS:
				self.touchesBas += 1
			if touche in PersonnageJouable.TOUCHES_DEPLACEMENT_GAUCHE:
				self.touchesGauche += 1
			if touche in PersonnageJouable.TOUCHES_DEPLACEMENT_DROITE:
				self.touchesDroite += 1

			if touche in PersonnageJouable.TOUCHES_FOCUS:
				self.toucheFocus += 1

			if touche in PersonnageJouable.TOUCHE_ATTAQUE:
				self.toucheAttaque += 1


	def updateRelachementTouche(self, event: Event):
		# Détecte le relâchement d'une touche
		if event.type == pygame.KEYUP:
			touche = event.__dict__["key"]
			if touche in PersonnageJouable.TOUCHES_DEPLACEMENT_HAUT:
				self.touchesHaut -= 1
			if touche in PersonnageJouable.TOUCHES_DEPLACEMENT_BAS:
				self.touchesBas -= 1
			if touche in PersonnageJouable.TOUCHES_DEPLACEMENT_GAUCHE:
				self.touchesGauche -= 1
			if touche in PersonnageJouable.TOUCHES_DEPLACEMENT_DROITE:
				self.touchesDroite -= 1

			if touche in PersonnageJouable.TOUCHES_FOCUS:
				self.toucheFocus -= 1

			if touche in PersonnageJouable.TOUCHE_ATTAQUE:
				self.toucheAttaque -= 1


	def updateHitbox(self):
		# On réécrit sur la hitbox
		centreX, centreY = self.getPositionCentre()
		hitboxX = centreX - PersonnageJouable.HITBOX_LARGEUR / 2
		hitboxY = centreY - PersonnageJouable.HITBOX_HAUTEUR / 2

		self.hitbox = pygame.Rect(hitboxX, hitboxY, PersonnageJouable.HITBOX_LARGEUR,
														PersonnageJouable.HITBOX_HAUTEUR)


	def deplacements(self, event: Event):
		# Mise à joue des compteurs
		self.updateAppuiDeTouche(event)
		self.updateRelachementTouche(event)

		# on peut alors mettre à jour les vitesses
		coefRalentissement = 1
		# Calcule en fonction du focus
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
		# Détecte les entrées de l'utilisateur, met à jour ainsi la vitesse
		for event in events:
			self.deplacements(event)

		# met à jour la position
		super().update(events)

		# On empêche le joueur de sortir de l'écran
		fenetreLargeur = self.fenetre.getLargeur()
		fenetreHauteur = self.fenetre.getHauteur()
		if self.x < 0:
			self.x = 0
		if self.x > fenetreLargeur - self.largeur:
			self.x = fenetreLargeur - self.largeur
		if self.y < 0:
			self.y = 0
		if self.y > fenetreHauteur - self.hauteur:
			self.y = fenetreHauteur - self.hauteur

		# Après la mise à jour de la position, la hitbox
		self.updateHitbox()

		# Update des timers
		dt = self.vue.getDT()
		self.timerIframe -= dt

		if self.timerIframe <= 0:  # On bloque le timer à 0 si il est à 0
			self.timerIframe = 0


	def drawHitbox(self):
		self.fenetre.getFenetre().fill(PersonnageJouable.HITBOX_COLOR, self.hitbox)


	def drawInterface(self):
		GREEN = 0, 255, 0
		fenetreLargeur, fenetreHauteur = self.fenetre.getDimensions()
		hauteur = 100 * (self.PV / self.PVMax)
		largeur = 30
		life = pygame.Rect(10, fenetreHauteur - 10 - hauteur, largeur, hauteur)
		pygame.draw.rect(self.fenetre.getFenetre(), GREEN, life)


	def draw(self):
		self.rectAffichage = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
		self.fenetre.getFenetre().fill(Personnage.COLOR, self.rectAffichage)



