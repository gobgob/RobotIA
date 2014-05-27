from math import *
from class_robot import *
from strategy import *

class StrategyHomologation(Strategy):
		
	def run(self):
		try:
			print ("StrategyHomologation")
			robot=self.robot
			table=self.table

			robot.distanceHard()
			robot.rotationHard()

			robot.activateUltrasounds()

			robot.goto(490,-785,(pi/180)*180) 	#j'avance puis regarde le mammouths
			robot.launchBall(3)					#je tire 3 balles
			robot.rotateTo((pi/180)*90)
			robot.goto(490,-205,(pi/180)*180)	#j'avance vers les fresques et les regardes
			robot.goto(190,-190,(pi/180)*180)	#je me rapproche de la fresque
			robot.rotateTo((pi/180)*0)			#demi tour

			robot.distanceSoft()
			robot.rotationSoft()

			robot.moveBackwardUntilblockage()	#et je recule
			robot.setAngle(0)
			robot.setX(0+robot.height/2)
			

			robot.distanceHard()
			robot.rotationHard()
			robot.moveForward(100)
		except Obstacle as e:
			sleep(3)