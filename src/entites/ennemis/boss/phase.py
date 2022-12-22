
from entites.ennemis.boss.boss import Boss


class Phase:
	"""
		Simple classe décrivant le comportement d'un boss lors d'une de ses phases.

		Ne concerne pas l'affichage, juste update, ainsi les attaques ....
	"""

	def __init__(self, boss: Boss) -> None:
		self.boss: Boss = boss

	def update(self):
		pass
