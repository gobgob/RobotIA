from math import *
from class_robot import *
from strategy import *

class Feu():
	x=0
	y=0
	isDead=False

	def __init__(self,x,y):
		self.x = x
		self.y = y

class StrategyFeu(Strategy):

	feu=Feu(1110,-1095)
	
	def run(self):
			print ("StrategyFeu")
			robot=self.robot
			table=self.table

			robot.distanceHard()
			robot.rotationHard()

			feu=self.feu

			if feu.isDead :
				return True

			robot.goto(feu.x,feu.y,autocolor=True) 

			feu.isDead=True
			return True
