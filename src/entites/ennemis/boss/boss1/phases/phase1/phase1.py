
# maths, cool
from math import pi, cos, sin
from random import randint, random
from entites.balles.balleCirculaire import BalleCirculaire
from entites.balles.balleDroite import BalleDroite

# classes
from entites.ennemis.boss.boss import Boss
from entites.ennemis.boss.phase import Phase
from entites.ennemis.ennemi import Ennemi



class Boss1Phase1(Phase):
	CADENCE_DE_TIR = 1

	PV = 2000

	def __init__(self, boss: Boss) -> None:
		super().__init__(boss, Boss1Phase1.PV)

		self.fenetre = self.boss.fenetre
		self.vue = self.boss.vue

		# Cadence de tir
		self.timerTir = 0  # 1 / Boss1Phase1.CADENCE_DE_TIR

		self.attaques = [
			self.attaque1
		]


	def attaque1(self):

		for i in range(13):
			balleLargeur, balleHauteur = (10, 10)

			centreX, centreY = self.boss.getPositionCentre()
			bossHauteur, _ = self.boss.getDimension()

			x0 = centreX
			y0 = centreY + bossHauteur / 2

			theta = - i * pi / 12

			tirVitesse = 50
			tirDegats = 1


			balle = BalleDroite(self.fenetre, self.vue, balleLargeur, balleHauteur,
				x0, y0, Ennemi.GROUPE, tirVitesse, tirDegats, theta)

			self.vue.ajouteBalle(balle)



	def attaque2(self):
		# theta_mvmt = random() * 2 * pi

		for i in range(13):
			balleLargeur, balleHauteur = (10, 10)

			centreX, centreY = self.boss.getPositionCentre()
			bossHauteur, _ = self.boss.getDimension()

			x0 = centreX
			y0 = centreY + bossHauteur / 2

			theta = - i * pi / 12

			tirVitesse = 50
			tirDegats = 1


			balle = BalleDroite(self.fenetre, self.vue, balleLargeur, balleHauteur,
				x0, y0, Ennemi.GROUPE, tirVitesse, tirDegats, theta)

			self.vue.ajouteBalle(balle)



	def deplacements(self):
		boss = self.boss

		boss.vx = 0
		boss.vy = 0
		"""
		# Si à gauche de l'écran: va à droite, ne peut pas sortir de l'écran
		if boss.x < 0:
			boss.x = 0
			boss.vx = boss.vitesse

		# Si à droite de l'écran: va à gauche, ne peut pas sortir de l'écran
		if boss.x > fenetre.largeur - boss.largeur:
			boss.x = fenetre.largeur - boss.largeur
			boss.vx = -boss.vitesse
		"""


	def tire(self) -> None:
		i = randint(0, len(self.attaques) - 1)
		attaque = self.attaques[i]

		attaque()
		"""
		# #  Balle Droite
		# pour un peu plus de lisibilité
		boss = self.boss

		# variables de la balle
		balleLargeur = 10
		balleHauteur = 10

		tir1X = boss.x + (boss.largeur / 2) - (balleLargeur / 2)
		# La balle apparait en dessous du boss
		tirY = boss.y + boss.hauteur + 2 * balleHauteur

		tirDirection = pi / 2  # part vers le bas

		tirVitesse = self.fenetre.getHauteur() / 2
		tirDegats = 1

		balle = BalleDroite(self.fenetre, self.vue, balleLargeur, balleHauteur,
			tir1X, tirY, Ennemi.GROUPE, tirVitesse, tirDegats,
			tirDirection)

		self.vue.ajouteBalle(balle)

		# # Balle circulaires
		for i in range(6):
			x0, y0 = boss.getPositionCentre()

			tirX0 = x0 - balleLargeur / 2
			tirY0 = y0 - balleHauteur / 2

			theta = i * (pi / 3) + self.dephasage
			v_r = self.fenetre.getHauteur() / 10
			v_theta = pi

			balle = BalleCirculaire(self.fenetre, self.vue, balleLargeur, balleHauteur,
				tirX0, tirY0, Ennemi.GROUPE, tirDegats,
				theta, v_r, v_theta)

			self.vue.ajouteBalle(balle)
		"""


	def update(self):
		# lisibilité
		boss = self.boss

		# Déplacements
		self.deplacements()

		# Tirs
		dt = self.vue.getDT()
		self.timerTir -= dt

		if self.timerTir <= 0:
			self.timerTir = 1 / Boss1Phase1.CADENCE_DE_TIR
			self.tire()

		# Change de phase
		if self.pv < 0:
			boss.changePhase()



