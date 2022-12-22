
# maths, cool
from math import pi
from entites.balles.balleDroite import BalleDroite

# classes
from entites.ennemis.boss.boss import Boss
from entites.ennemis.boss.phase import Phase
from entites.ennemis.ennemi import Ennemi



class Boss1Phase1(Phase):
	CADENCE_DE_TIR = 1

	def __init__(self, boss: Boss) -> None:
		super().__init__(boss)

		self.fenetre = self.boss.fenetre
		self.vue = self.boss.vue

		# Cadence de tir
		self.timerTir = 1 / Boss1Phase1.CADENCE_DE_TIR

	def deplacements(self):
		boss = self.boss
		fenetre = self.fenetre

		# Si à gauche de l'écran: va à droite, ne peut pas sortir de l'écran
		if boss.x < 0:
			boss.x = 0
			boss.vx = boss.vitesse

		# Si à droite de l'écran: va à gauche, ne peut pas sortir de l'écran
		if boss.x > fenetre.largeur - boss.largeur:
			boss.x = fenetre.largeur - boss.largeur
			boss.vx = -boss.vitesse


	def tire(self):
		# pour un peu plus de lisibilité
		boss = self.boss

		# variables de la balle
		balleLargeur = 10
		balleHauteur = 10

		tir1X = boss.x + (boss.largeur / 2) - (balleLargeur / 2)
		# La balle apparait en dessous du boss
		tirY = boss.y + boss.hauteur + 2 * balleHauteur

		tirDirection = pi / 2  # part vers le bas

		tirVitesse = 100
		tirDegats = 1

		balle = BalleDroite(self.fenetre, self.vue, balleLargeur, balleHauteur,
			tir1X, tirY, Ennemi.GROUPE, tirVitesse, tirDegats,
			tirDirection)

		self.vue.ajouteBalle(balle)

	def update(self):
		# Déplacements
		self.deplacements()

		# Tirs
		dt = 1 / self.fenetre.fps
		self.timerTir -= dt

		if self.timerTir <= 0:
			self.timerTir = 1 / Boss1Phase1.CADENCE_DE_TIR
			self.tire()



