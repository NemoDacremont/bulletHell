# Modules
from random import choice
from math import sqrt, exp, tanh


def norme1(vecteur: tuple) -> float:
	"""
	Paramètres
	---------
		vecteur : un vecteur dont les coordonnées sont stockées dans un tuple

	Renvoie la norme 1 du vecteur
	"""
	norme = 0

	for comp in vecteur:
		norme += abs(comp)
	return norme


def norme2(vecteur: tuple) -> float:
	"""
	Paramètres
	---------
		vecteur : un vecteur dont les coordonnées sont stockées dans un tuple
	Renvoie la norme 2 du vecteur

	"""

	norme = 0

	for comp in vecteur:
		norme += comp ** 2
	return sqrt(norme)


def normeInf(vecteur: tuple) -> float:
	"""
	Paramètres
	---------
		vecteur : un vecteur dont les coordonnées sont stockées dans un tuple

	Renvoie la norme infinie du vecteur

	"""
	absolu = [abs(comp) for comp in vecteur]
	return max(absolu)


def foncerSurLeJoueur(entite, vitesse: float, joueur=None) -> None:
	"""
	Paramètres
	----------
		entite : une entite (lol)
		vitesse : vitesse cible du déplacement
		joueur (optionnel) : le joueur à attaquer. Vide par défaut

	Procédure qui permet de modifier le vecteur vitesse de l'entite considérée,
	de sorte que celui-ci soit orienté de la balle vers le joueur, et de norme
	vitesse. Conçu pour les balles en particulier

	Si aucun joueur n'est spécifié, un joueur sera choisi aléatoirement (pour
	pouvoir gérer s'il y a plusieurs joueurs.

	Remarque : s'il n'y a qu'un joueur, ça ne sert à rien de le préciser.

	"""

	# Choix du joueur
	if joueur is None:
		joueur = choice(entite.vue.getJoueurs())

	# Lisibilité
	xBalle, yBalle = entite.x, entite.y
	xJoueur, yJoueur = joueur.getPositionCentre()

	# Calcul du vecteur, avec try au cas où la norme vaut 0
	try:
		vect = (xJoueur - xBalle, yJoueur - yBalle)
		vx = vitesse * vect[0] / norme2(vect)
		vy = vitesse * vect[1] / norme2(vect)
		entite.vx = vx
		entite.vy = vy

	except:
		return None


def pivoter(entite, theta: float) -> None:
	vit = entite.vX + 1j * entite.vY
	vit *= exp(1j * theta)
	entite.vX, entite.vY = vit.real, vit.imag


def vitesseHubble(entite, reference, H: float, distance: float) -> None:
	r = entite.x - reference.y + 1j * (entite.y - reference.y)
	vit = entite.vX + 1j * entite.vY
	vit *= 1 / 2 + 1 / 4 * tanh(H * (abs(r) - distance))
	entite.vX, entite.vY = vit.real, vit.imag
