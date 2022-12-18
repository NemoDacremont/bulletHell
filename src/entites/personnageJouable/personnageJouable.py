
from pygame.event import Event
import pygame

from entites.personnage import Personnage
from fenetre import Fenetre
from vues.vue import Vue


class PersonnageJouable(Personnage):
	TOUCHES_DEPLACEMENT_HAUT = ["z", "Z"]
	TOUCHES_DEPLACEMENT_BAS = ["s", "S"]
	TOUCHES_DEPLACEMENT_GAUCHE = ["q", "Q"]
	TOUCHES_DEPLACEMENT_DROITE = ["d", "D"]
	TOUCHES_FOCUS = ["o", "O"]

	GROUPE = 1

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
				- coefRalentissementFocus: float, correspond au ralentissement lors de l'action "focus"
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





	def deplacements(self, event: Event):
		## On met à jour les compteurs de touches pour les déplacements
		# Détecte l'appuie sur une touche
		if event.type == pygame.KEYDOWN:
			touche = event.__dict__["unicode"]

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



		# Détecte le relâchement d'une touche
		if event.type == pygame.KEYUP:
			touche = event.__dict__["unicode"]
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


		## on peut alors mettre à jour les vitesses
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
		self.rect = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
		self.fenetre.getFenetre().fill(Personnage.COLOR, self.rect)

