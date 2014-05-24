from math import *
from class_robot import *
from strategy import *

class StrategyHomologation(Strategy):
		
	def run(self):
		print ("Strategy depart")
		robot=self.robot
		table=self.table

		# robot.distanceHard()
		# robot.rotationHard()

		# # robot.moveForward(195*4)
		# robot.goto(195*4,0)
		# robot.rotateTo(0)

		robot.rotationSoft()
		robot.distanceSoft()


		while True:
			print( robot.getTicks())
			print( robot.getX())
			print( robot.getAngle())
			time.sleep(0.01)

		print(robot.getX())
		print(robot.getY())
		print(robot.getAngle())

