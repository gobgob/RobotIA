
from math import *

class Table:
	"""The table class !"""
	width=3000
	height=2000
	margin=200
	cakeRayon=550
	def isInTable(self,point):
		#on est sur la table en longueur
		if abs(point.y)<(self.width/2-self.margin):
			#on est sur la table en largeur
			if point.x>self.margin and point.x<(self.height-self.margin):
				#on est pas dans le cadeau
				if hypot(point.x,point.y)>(self.cakeRayon-self.margin):
					return True

		