
from math import *
from class_cups import *
from utils import *

class Table:
	"""The table class !"""
	width=3000
	height=2000
	margin=200

	def __init__(self):
		self.cups = []
		self.cups.append(Cup(830,590))


  # popcornsList = [
  #   {
  #     x: 910,
  #     y: 830
  #   }, {
  #     x: 2090,
  #     y: 830
  #   }, {
  #     x: 1500,
  #     y: 1650
  #   }, {
  #     x: 250,
  #     y: 1750
  #   }, {
  #     x: 2750,
  #     y: 1750
  #   }
  # ];

	def isInTable(self,point):
		#on est sur la table en longueur
		if abs(point.y)<(self.width/2-self.margin):
			#on est sur la table en largeur
			if point.x>self.margin and point.x<(self.height-self.margin):
				return True

	