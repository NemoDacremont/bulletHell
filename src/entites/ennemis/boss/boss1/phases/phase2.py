
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



class Boss1Phase2(Phase):
	
	CADENCE_DE_TIR = 10
	NB_BALLES = 36
	
	#Mouvement
	DUREE = 10
	VITESSE = 10

	PV = 2000

	def __init__(self, boss: Boss) -> None:
		super().__init__(boss, Boss1Phase2.PV)

		self.fenetre = self.boss.fenetre
		self.vue = self.boss.vue
		

		# Timer
		self.timerAttente = Boss1Phase2.DUREE
		self.timerTir = 1 / Boss1Phase2.CADENCE_DE_TIR
		
		self.etat = 0 #0 : rien faire ; 1 : fonce sur le joueur ; 2 : attaque
		self.xJ, self.yJ = boss.vue.getJoueurs()[0].getPositionCentre()


	def deplacements(self, xJ = None, yJ = None):
		
		#Un peu de lisibilité
		boss = self.boss
		x, y = boss.x, boss.y
		
		#Fonce sur le joueur
		if self.etat == 1:
			boss.vx = Boss1Phase2.VITESSE * (x - xJ) / sqrt((x - xJ) ** 2 + (y - yJ) ** 2)
			boss.vy = Boss1Phase2.VITESSE * (y - yJ) / sqrt((x - xJ) ** 2 + (y - yJ) ** 2)
		
		else:
			boss.vx = 0
			boss.vy = 0
		


	def tire(self):
		
		# pour un peu plus de lisibilité
		boss = self.boss
		n = Boss1Phase2.NB_BALLES
		
		# Balles droites de l'etat 1
		if self.etat == 1:
			
			# variables de la balle
			balleLargeur = 10
			balleHauteur = 10
			tirDirection = phase(boss.vx + 1j * boss.vy) + pi / 6 * random() - pi / 12

			tir1X = boss.x + (boss.largeur / 2) - (balleLargeur / 2)
			# La balle apparait en dessous du boss
			tirY = boss.y + boss.hauteur + 2 * balleHauteur

			tirVitesse = self.fenetre.getHauteur() / 2
			tirDegats = 1
			
			#On envoie deux balles perpendiculaires
			balle1 = BalleDroite(self.fenetre, self.vue, balleLargeur, balleHauteur,
							  tir1X, tirY, Ennemi.GROUPE, tirVitesse, tirDegats,
							  tirDirection)
			
			tirDirection += pi
			balle2 = BalleDroite(self.fenetre, self.vue, balleLargeur, balleHauteur,
							  tir1X, tirY, Ennemi.GROUPE, tirVitesse, tirDegats,
							  tirDirection)

			self.vue.ajouteBalle(balle1)
			self.vue.ajouteBalle(balle2)

		# Balles continuum pour l'état 2
		if self.etat == 2 :
			
			for i in range(n):
				# variables de la balle
				balleLargeur = 10
				balleHauteur = 10
				tirDirection = 2 * pi * i / n
	
				tir1X = boss.x + (boss.largeur / 2) - (balleLargeur / 2)
				# La balle apparait en dessous du boss
				tirY = boss.y + boss.hauteur + 2 * balleHauteur
	
				tirVitesse = self.fenetre.getHauteur() / 2
				tirDegats = 1	
				
				balle = BalleDroiteContinuum(self.fenetre, self.vue, balleLargeur, balleHauteur,
					  tir1X, tirY, Ennemi.GROUPE, tirVitesse, tirDegats,
					  tirDirection, 1)
				
				self.vue.ajouteBalle(balle)
			
			#On ne trigger qu'une fois, après on repasse en état 0
			self.etat = 0
				



	def update(self):
		# lisibilité
		dt = self.vue.getDT()
		boss = self.boss
		
		# Déplacements
		
		#Si on fait rien
		if self.etat == 0:
			self.timerAttente -= dt
		
		self.deplacements(self.xJ, self.yJ)
		
		# Chgt état
		if self.etat == 0 and self.timerAttente <= 0:
			self.etat = 1
			self.xJ, self.yJ = boss.vue.getJoueurs()[0].getPositionCentre
			self.timerAttente = Boss1Phase2.DUREE
		
		elif self.etat == 1 and abs(self.xJ - boss.x + 1j * (self.yJ - boss.y)) < Boss1Phase2.VITESSE:
			self.etat = 2
		

		# Tirs

		self.timerTir -= dt

		if self.timerTir <= 0:
			self.timerTir = 1 / Boss1Phase2.CADENCE_DE_TIR
			self.tire()

		# Change de phase
		if self.pv < 0:
			boss.changePhase()



