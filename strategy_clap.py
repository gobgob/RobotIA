from math import *
from class_robot import *
from strategy import *
from color import *

class StrategyClap(Strategy):
	done = 0
	def run(self):
			if self.done:
				return True

			print ("StrategyClap")
			robot=self.robot
			table=self.table

			robot.distanceHard()
			robot.rotationHard()

			print(robot.getX())
			print(robot.getY())
			print(robot.getAngle())

			robot.openFrontGrip()
			robot.openBackGrip()
			robot.activateUltrasounds()

			robot.goto(1000,800, 0, autocolor=True)
			robot.goto(1500,800, pi/2, autocolor=True)
			robot.goto(1500,1300,0, autocolor=True)
			robot.deactivateUltrasounds()
			robot.rotateTo(-pi/2, autocolor=True)
			robot.moveBackwardUntilblockage()
			robot.setAngle(-pi/2)
			robot.setY(table.width/2-robot.height/2)
			robot.activateUltrasounds()

			robot.goto(1500,1300,0, autocolor=True)
			robot.deactivateUltrasounds()
			robot.rotateTo(0, autocolor=True)
			robot.moveBackwardUntilblockage()
			robot.setX(1220+robot.width/2)
			robot.activateUltrasounds()

			robot.goto(1620,1255,0, autocolor=True)
			robot.closeFrontGrip()
			sleep(3)
			robot.goto(1495,885, autocolor=True)
			robot.goto(1070,995,pi, autocolor=True)
			robot.openFrontGrip()
			robot.moveBackward(200)


			robot.goto(1760,420, autocolor=True)
			robot.moveBackward(250)

			print(robot.getX())
			print(robot.getY())
			print(robot.getAngle())
			self.done=1

			return True
