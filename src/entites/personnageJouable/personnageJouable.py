
from pygame.event import Event
import pygame

from entites.personnage import Personnage
from fenetre import Fenetre
from vues.vue import Vue


class PersonnageJouable(Personnage):
	TOUCHES_DEPLACEMENT_HAUT = [pygame.K_z]
	TOUCHES_DEPLACEMENT_BAS = [pygame.K_s]
	TOUCHES_DEPLACEMENT_GAUCHE = [pygame.K_q]
	TOUCHES_DEPLACEMENT_DROITE = [pygame.K_d]
	TOUCHES_FOCUS = [pygame.K_o]

	GROUPE = 1

	HITBOX_COLOR = 255, 0, 255
	HITBOX_LARGEUR = 10
	HITBOX_HAUTEUR = 10

	def __init__(self, nom: str, fenetre: Fenetre, vue: Vue, largeur: float, hauteur: float,
							x: float, y: float, PVMax: float, PV: float = -1, vitesse: float = 100,
							coefRalentissementFocus: float = 0.3) -> None:
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
		super().__init__(nom, fenetre, vue, largeur, hauteur, x, y, PVMax, PV, vitesse)

		self.nom = nom

		# Compteurs pour utiliser
		self.toucheFocus = 0

		self.touchesHaut = 0
		self.touchesBas = 0
		self.touchesGauche = 0
		self.touchesDroite = 0

		self.coefRalentissementFocus = coefRalentissementFocus
		self.groupe = PersonnageJouable.GROUPE

		self.hitbox = pygame.Rect(x, y, PersonnageJouable.HITBOX_LARGEUR,
														PersonnageJouable.HITBOX_HAUTEUR)


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
		# Détecte les entrées de l'utilisateur
		for event in events:
			self.deplacements(event)

		# met à jour la position
		super().update(events)
		# On réécrit sur la hitbox
		centreX, centreY = self.getPositionCentre()
		hitboxX = centreX - PersonnageJouable.HITBOX_LARGEUR / 2
		hitboxY = centreY - PersonnageJouable.HITBOX_HAUTEUR / 2

		self.hitbox = pygame.Rect(hitboxX, hitboxY, PersonnageJouable.HITBOX_LARGEUR,
														PersonnageJouable.HITBOX_HAUTEUR)

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



	def draw(self):
		self.rectAffichage = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
		self.fenetre.getFenetre().fill(Personnage.COLOR, self.rectAffichage)

		self.fenetre.getFenetre().fill(PersonnageJouable.HITBOX_COLOR, self.hitbox)



