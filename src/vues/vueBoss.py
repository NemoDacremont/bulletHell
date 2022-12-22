# importations bizarre, permet d'importer les types sans avoir
# d'erreures d'importations circulaires
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from jeu import Jeu


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

		"""
		## Création Personnage jouable
		# Valeurs pour le personnage
		joueurPVMax = 3
		joueurX = 0
		joueurY = 0
		joueurLargeur = 50
		joueurHauteur = 50

		# de façon à ce que la vitesse soit suffisante pour parcourir en 10 sec le plus petit
		# entre la largeur et la longueur
		joueurVitesse = min(self.fenetre.getLargeur() / 10, self.fenetre.getHauteur() / 10)

		# Un gros coef
		coefRalentissementFocus = 0.2

		# Créé le personnage
		joueur = PersonnageJouable("moi", self.fenetre, self, joueurLargeur,
														joueurHauteur, joueurX, joueurY, joueurPVMax, vitesse=joueurVitesse,
														coefRalentissementFocus=coefRalentissementFocus)
		"""

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
		for personnage in self.personnages:
			print(personnage.nom)



