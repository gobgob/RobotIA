from math import *
from class_robot import *
from strategy import *

class Filet():
	x=0
	y=0
	isDead=False

	def __init__(self,x,y):
		self.x = x
		self.y = y

class StrategyFilet(Strategy):

	mammouth=Filet(555,-385)

	def run(self):
			print ("StrategyFilet")
			robot=self.robot
			table=self.table

			mammouth=self.mammouth
			robot.distanceHard()
			robot.rotationHard()

			if color=="RED" :
				pass
			else:
				mammouth.y=mammouth.y+100

			if mammouth.isDead :
				return True

			robot.activateUltrasounds()
			robot.goto(0,-630,autocolor=True,rotateOnly=True)

			# robot.goto(mammouth.x,mammouth.y,(pi/180)*210,autocolor=True)
			robot.deactivateUltrasounds()

			mammouth.isDead=True
			return True
