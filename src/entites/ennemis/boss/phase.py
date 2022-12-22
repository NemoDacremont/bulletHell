
from entites.ennemis.boss.boss import Boss


class Phase:
	"""
		Simple classe décrivant le comportement d'un boss lors d'une de ses phases.

		Ne concerne pas l'affichage, juste update, ainsi les attaques ....
	"""

	def __init__(self, boss: Boss, PV: float) -> None:
		"""
			Constructeur Phase:
			Paramètres:
				- boss: Boss, le boss lié à la phase
				- PV: float, le nombre de PV dont dure la phase
		"""
		self.boss: Boss = boss
		self.pv = PV


	def recoitDegats(self, degats: float):
		"""
			Est appelé par le boss lorsqu'il recoit des dégats: permet de savoir quand
			changer de phase
		"""
		self.pv -= degats


	def update(self):
		pass
