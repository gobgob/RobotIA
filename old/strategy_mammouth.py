from math import *
from class_robot import *
from strategy import *
from color import *


class Mammouth():
	x=0
	y=0
	isDead=False

	def __init__(self,x,y):
		self.x = x
		self.y = y

class StrategyMammouth(Strategy):

	mammouths=[Mammouth(650,-800),Mammouth(650,-930)]
	


	def run(self,number):
			print ("StrategyMammouth "+str(number))
			robot=self.robot
			table=self.table


			robot.distanceHard()
			robot.rotationHard()

			mammouth=self.mammouths[number]

			if color=="RED" :
				pass
			else:
				mammouth.y=mammouth.y+150

			if mammouth.isDead :
				return True

			robot.activateUltrasounds()
			# self.takeTheHighway(mammouth.x,mammouth.y)
			robot.goto(mammouth.x,mammouth.y,(pi/180)*180,autocolor=True)
			robot.launchBall(10)					#je tire 3 balles
			robot.deactivateUltrasounds()

			# if number=1:
			# 	robot.rotateTo((pi/180)*210,autocolor=True)
			
			mammouth.isDead=True
			return True
