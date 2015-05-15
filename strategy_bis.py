from math import *
from class_robot import *
from strategy import *
from color import *

class StrategyBis(Strategy):
	done = 0
	def run(self):
			if self.done:
				return True

			print ("StrategyBis")
			robot=self.robot
			table=self.table

			robot.goSlow()
			robot.distanceVeryHard()
			robot.rotationHard()

			# robot.activateUltrasounds()

			print(robot.getX())
			print(robot.getY())
			print(robot.getAngle())

			robot.openFrontGrip()
			robot.activateUltrasounds()

			#go take the 1st cup

			robot.distanceVeryHard()
			robot.goSlow()


			robot.goto(1650,510,(pi/180)*320, autocolor=True)

			#push spot in red zone
			robot.deactivateUltrasounds()
			robot.goto(1755,420,(pi/180)*320, autocolor=True)
			sleep(1)
			robot.moveBackward(150)


			robot.activateUltrasounds()
			robot.goto(1750,1020,(pi/180)*90, autocolor=True)
			robot.goto(1750,1150,(pi/180)*90, autocolor=True)
			robot.closeFrontGrip()
			sleep(2)


			robot.goto(1220,720,(pi/180)*120, autocolor=True)
			robot.goto(1095,845,(pi/180)*120, autocolor=True)
			robot.openFrontGrip()
			sleep(2)
			robot.moveBackward(150)
			robot.rotateTo(0)
		
			self.done=1

			return True
