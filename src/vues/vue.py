
# importations bizarre, permet d'importer les types sans avoir
# d'erreures d'importations circulaires
from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
	from entites.balles.balle import Balle
	from entites.entite import Entite
	from pygame.event import Event
	from entites.personnage import Personnage
	from entites.personnageJouable.personnageJouable import PersonnageJouable
	from jeu import Jeu


class Vue:
	ETAT_PAUSE = 1
	ETAT_NORMAL = 0

	def __init__(self, jeu: Jeu, etat: int, pausePossible: bool) -> None:
		self.jeu = jeu
		self.fenetre = jeu.fenetre

		self.etat = etat
		self.pausePossible = pausePossible

		self.balles: list[Balle] = []
		self.personnages: list[Personnage] = []

		self.joueurs: list[PersonnageJouable] = []

		self.entites: list[Entite] = []
		# self.entitesAAfficher: list[Entite] = []


	def getDT(self) -> float:
		return self.jeu.getDT()


	def getPersonnages(self):
		return self.personnages


	def ajouteEntites(self, entite: Entite):
		self.entites.append(entite)


	def ajouteBalle(self, balle: Balle):
		self.balles.append(balle)


	def getEntites(self):
		return self.entites


	def update(self, events: list[Event]):
		self.dt = self.jeu.dt

		# Update les entites
		for i in range(len(self.entites) - 1, - 1, - 1):
			entite = self.entites[i]
			entite.update()

			if entite.doitEtreRetirer():
				self.entites.pop(i)

		# Update les personnages
		for i in range(len(self.personnages) - 1, - 1, - 1):

			personnage = self.personnages[i]
			personnage.update(events)

			if personnage.doitEtreRetirer():
				self.personnages.pop(i)

		# Update les balles, de façon décroissante à cause
		# des pops
		for i in range(len(self.balles) - 1, - 1, - 1):
			balle = self.balles[i]
			balle.update()

			if balle.doitEtreRetirer():
				self.balles.pop(i)


	def draw(self):
		self.fenetre.draw()

		# affiche les entites
		for entite in self.entites:
			entite.draw()

		# Affiche les personnages
		for personnage in self.personnages:
			personnage.draw()

		# Affiche les balles
		for balle in self.balles:
			balle.draw()

		# Finalement, affiche les hitbox des joueurs au dessus des balles ...
		for joueur in self.joueurs:
			joueur.drawHitbox()

		# Affiche les hps de personnages
		for personnage in self.personnages:
			personnage.drawInterface()





