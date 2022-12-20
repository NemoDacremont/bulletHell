
from entites.ennemis.boss1 import Boss1
from entites.entite import Entite
from entites.personnage import Personnage
from entites.personnageJouable.personnage1 import Personnage1
from vues.vue import Vue


class VueBoss(Vue):
	def __init__(self, jeu, etat: int, pausePossible: bool) -> None:
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

		joueur = Personnage1(self.fenetre, self, 0, 0)

		#  Création d'un ennemi
		ennemiPVMax = 100
		ennemiX = 50
		ennemiY = 50
		ennemiLargeur = 40
		ennemiHauteur = 40
		ennemiVitesse = 20

		ennemi = Boss1(self.fenetre, self, ennemiLargeur, ennemiHauteur,
									ennemiX, ennemiY, ennemiPVMax, vitesse=ennemiVitesse)

		self.personnages: list[Personnage] = [joueur, ennemi]

		for personnage in self.personnages:
			print(personnage.nom)



