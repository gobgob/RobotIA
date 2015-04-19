from strategy import *
from math import *
from class_robot import *
from class_table import *
from color import *
from time import sleep


class StrategyCalibration(Strategy):
	robot=None
	table=None

	def __init__(self,table,robot):
		self.table=table
		robot=robot
		
	def Recalage(self):
		self.distanceMedium()
		self.rotationSoft()
		robot.setX(0)
		robot.setY(0)
		robot.setAngle(0)

		print ("Je recule")
		robot.moveBackwardUntilBlocage()
		robot.setY(colorize_y(self.table.width/2 - robot.height/2))
		robot.setAngle(colorize_angle(-pi/2))
		robot.moveForward(0)
		robot.rotate(0)
		print ("Y recale !")

		sleep(1)

		print ("J'avance")
		self.distanceHard()
		robot.moveForward(100);
		sleep(1)

		print ("Je tourne")
		self.rotationHard()
		robot.rotateTo(colorize_angle(-pi))
		self.rotationSoft()

		sleep(1)

		print ("Je recule")
		self.distanceMedium()
		robot.moveBackwardUntilBlocage()
		robot.setX(self.table.height - robot.height/2-100)
		robot.setAngle(colorize_angle(-pi))
		robot.moveForward(0);
		robot.rotate(0);

		print ("X recale !")	
		self.distanceHard()
		self.rotationHard()
		robot.moveForward(100);
		robot.rotateTo(colorize_angle(-pi/2))



	def calibrateRotation(self,count):
		print ("calibrateRotation")

		robot=self.robot

		robot.distanceSoft()
		robot.rotationSoft()
		robot.setX(0)
		robot.setY(0)
		robot.setAngle(0)


		print ("Je recule")
		robot.moveBackwardUntilBlocage()
		# robot.moveBackward(100)
		robot.setAngle(0)
		robot.rotate(0)
		robot.moveForward(0)
		robot.rotate(0)

		sleep(1)
		res,r,l=robot.getTicks()
		startDiff = r-l
		print ("res "+str(res))
		print ("r "+str(r))
		print ("l "+str(l))

		print ("J'avance")
		robot.distanceHard()
		robot.rotationHard()
		robot.moveForward(200);



		print ("Je tourne")
		robot.rotate(count*2*pi)
		sleep(1)

		print ("Je recule")
		robot.distanceMedium()
		robot.rotationSoft()
		robot.moveBackwardUntilBlocage()
		# robot.moveBackward(100)
		robot.moveForward(0)
		robot.rotate(0)
		sleep(1)

		res,r,l=robot.getTicks()
		endDiff = r-l
		print ("res "+str(res))
		print ("r "+str(r))
		print ("l "+str(l))

		print ("start "+str(startDiff))
		print ("end "+str(endDiff))

		print (str((endDiff-startDiff)/(count*2*pi)))
