from math import *
from class_robot import *
from strategy import *
from color import *

class StrategyStart(Strategy):
	done = 0
	def run(self):
			if self.done:
				return True

			print ("StrategyStart")
			robot=self.robot
			table=self.table

			robot.distanceHard()
			robot.rotationHard()

			# robot.activateUltrasounds()

			print(robot.getX())
			print(robot.getY())
			print(robot.getAngle())

			robot.openFrontGrip()
			robot.activateUltrasounds()

			#go take the 1st cup
			robot.goto(table.cups[0].x+60, table.cups[0].y+120, autocolor=True)
			# sleep(2)

			robot.closeFrontGrip()
			table.cups[0].isAvailable = False
			sleep(1)

			robot.goto(1140,645,0, autocolor=True)
			robot.deactivateUltrasounds()
			robot.rotateTo(-pi/3, autocolor=True)
			robot.rotateTo(-pi/2, autocolor=True)
			robot.rotateTo(-pi, autocolor=True)
			robot.distanceSoft()
			robot.moveBackward(200)
			robot.distanceHard()
			robot.closeBackGrip()
			sleep(1)


			robot.activateUltrasounds()
			robot.goto(1000, 800, pi/2, autocolor=True)
			robot.goto(1000, 1200, autocolor=True)
			robot.openFrontGrip()
			robot.deactivateUltrasounds()
			sleep(1)
			robot.moveBackward(200)
			robot.rotateTo(-pi/2, autocolor=True)
			sleep(1)

			robot.openBackGrip()
			robot.openBallGrip()
			sleep(1)
			robot.moveForward(80)
			robot.rotateTo(-pi/2, autocolor=True)


			print(robot.getX())
			print(robot.getY())
			print(robot.getAngle())
			self.done=1

			return True