
from entites.ennemis.ennemi import Ennemi
from entites.entite import Entite
from entites.personnageJouable.personnageJouable import PersonnageJouable
from vues.vue import Vue

class VueBoss(Vue):
	def __init__(self, jeu, etat: int, pausePossible: bool) -> None:
		super().__init__(jeu, etat, pausePossible)

		## Création Personnage jouable
		# Valeurs pour le personnage
		joueurX = 0
		joueurY = 0
		joueurLargeur = 50
		joueurHauteur = 50

		# de façon à ce que la vitesse soit suffisante pour parcourir en 10 sec le plus petit
		# entre la largeur et la longueur
		vitesse = min(self.fenetre.getLargeur() / 10, self.fenetre.getHauteur() / 10)

		# Un gros coef
		coefRalentissementFocus = 0.2

		# Créé le personnage
		joueur = PersonnageJouable("moi", self.fenetre, self, joueurLargeur,
														joueurHauteur, joueurX, joueurY, -2, vitesse,
														coefRalentissementFocus)

		## Création d'un ennemi
		ennemiX = 0
		ennemiY = 0
		ennemiLargeur = 40
		ennemiHauteur = 40
		ennemiVitesse = 0

		ennemi = Ennemi(self.fenetre, self, "un gros méchant", ennemiLargeur, ennemiHauteur,
									ennemiX, ennemiY, 1, ennemiVitesse)

		self.entites = [joueur, ennemi]
		self.entitesAAfficher = [joueur, ennemi]



