
# maths, cool, random, cmath
from math import pi, sqrt
from entites.balles.balleDroite import BalleDroite
from entites.balles.balleDroiteContinuum import BalleDroiteContinuum
from random import random, choice
from cmath import phase

# classes
from entites.ennemis.boss.boss import Boss
from entites.ennemis.boss.phase import Phase
from entites.ennemis.ennemi import Ennemi

#paterns
from entites.ennemis.boss.boss1.phases.phase2.phase2Dash import Boss1Phase2Dash


class Boss1Phase2(Phase):

	PV = 2000
	INTERVALLE = 3

	def __init__(self, boss: Boss) -> None:
		super().__init__(boss, Boss1Phase2.PV)

		self.fenetre = self.boss.fenetre
		self.vue = self.boss.vue
		

		#Création des attaques
		attaque1 = Boss1Phase2Dash(boss)
		self.paterns = [attaque1]

		self.paternActif = choice(self.paterns)



	def update(self):
		# lisibilité
		dt = self.vue.getDT()
		boss = self.boss
				
		self.paternActif.update()
		self.paternActif = choice(self.paterns)
		
		
		# Change de phase
		if self.pv < 0:
			boss.changePhase()



