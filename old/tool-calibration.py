#!/usr/bin/python

from math import *
from class_robot import *
from class_table import *
from strategy_calibration import *
from time import sleep
from proxi_serial import *

table = Table();
proxy = Proxy_serial()
robot = Robot(table,proxy)





def calibrateRotation(count,robot):
		print ("calibrateRotation")

		robot.distanceSoft()
		robot.rotationSoft()
		robot.setX(0)
		robot.setY(0)
		robot.setAngle(0)


		print ("Je recule")
		robot.moveBackwardUntilblockage()
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
		robot.rotate(count*2*pi,timeout=120)
		sleep(1)

		print ("Je recule")
		robot.distanceMedium()
		robot.rotationSoft()
		robot.moveBackwardUntilblockage()
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




calibrateRotation(5,robot)
