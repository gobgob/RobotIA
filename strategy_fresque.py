from math import *
from class_robot import *
from strategy import *

class Fresque():
	x=0
	y=0
	isDead=False

	def __init__(self,x,y):
		self.x = x
		self.y = y

class StrategyFresque(Strategy):

	fresque=Fresque(140,-150)
	
	def run(self):
			print ("StrategyFresque")
			robot=self.robot
			table=self.table

			robot.distanceHard()
			robot.rotationHard()

			fresque=self.fresque

			if fresque.isDead :
				return True

			robot.activateUltrasounds()
			# self.takeTheHighway(fresque.x+300,fresque.y)
			robot.goto(fresque.x+300,fresque.y,(pi/180)*180,autocolor=True) 
			robot.deactivateUltrasounds()
			robot.goto(fresque.x+100,fresque.y,(pi/180)*0,autocolor=True) ##devant la fresque, regarde a l'opposé
			robot.rotateTo(0)
			sleep(0.5)
			# robot.distanceSoft()
			# robot.rotationSoft()
			robot.moveBackwardUntilblockage()	#et je recule pour me recaler au passage
			robot.setAngle(0)
			robot.setX(0+robot.height/2)
			robot.distanceHard()
			robot.rotationHard()
			
			robot.activateUltrasounds()
			sleep(0.5)
			robot.moveForward(50)
			sleep(0.5)
			robot.goto(fresque.x+100,fresque.y,autocolor=True) 
			robot.deactivateUltrasounds()

			fresque.isDead=True
			return True
