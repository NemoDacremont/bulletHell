
from entites.ennemis.boss.boss import Boss
from entites.ennemis.boss.phase import Phase
from entites.ennemis.ennemi import Ennemi


class Boss1Phase1Attaque1(Phase):
	PV = 2000  # Evite des bug

	CADENCE_DE_TIR = 10
	NB_BALLES = 36

	DUREE = 3
	VITESSE = 1000

	def __init__(self, boss: Boss) -> None:
		super().__init__(boss, 10000)

		self.fenetre = self.boss.fenetre
		self.vue = self.boss.vue


		# Timer
		self.timerAttente = Boss1Phase1Attaque1.DUREE
		self.timerTir = 1 / Boss1Phase1Attaque1.CADENCE_DE_TIR

		self.etat = 0  # 0 : rien faire ; 1 : fonce sur le joueur ; 2 : attaque 
		self.xJ, self.yJ = None, None


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

