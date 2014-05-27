
from math import *

class Table:
	"""The table class !"""
	width=3000
	height=2000
	margin=200
	def isInTable(self,point):
		#on est sur la table en longueur
		if abs(point.y)<(self.width/2-self.margin):
			#on est sur la table en largeur
			if point.x>self.margin and point.x<(self.height-self.margin):
				return True

		