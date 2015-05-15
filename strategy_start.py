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

			robot.goFast()
			robot.distanceHard()
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
			robot.goto(table.cups[0].x+10, table.cups[0].y+90, autocolor=True)
			# sleep(2)



			robot.closeFrontGrip()
			table.cups[0].isAvailable = False
			sleep(1)

			# robot.goFast()
			# robot.distanceHard()


			robot.goto(1040,605,0, autocolor=True)
			robot.deactivateUltrasounds()
			robot.rotateTo(-pi/3, autocolor=True)
			robot.rotateTo(-pi/2, autocolor=True)
			robot.rotateTo(-pi, autocolor=True)
			robot.distanceSoft()
			robot.moveBackward(300)
			# robot.distanceHard()
			robot.closeBackGrip()
			robot.moveBackward(250)
			sleep(1)
			sleep(20)

			robot.activateUltrasounds()
			robot.goto(1000, 800, pi/2, autocolor=True)
			robot.goto(1000, 1200, autocolor=True)
			robot.openFrontGrip()
			robot.deactivateUltrasounds()
			sleep(1)
			robot.moveBackward(200)
			robot.rotateTo(-pi/2, autocolor=True)
			robot.moveForward(80)
			sleep(1)

			robot.openBallGrip()
			sleep(1)
			robot.openBackGrip()
			
			sleep(1)
			robot.moveForward(140)
			robot.rotateTo(-pi/2, autocolor=True)


			print(robot.getX())
			print(robot.getY())
			print(robot.getAngle())
			self.done=1

			return True
