#!/usr/bin/python3

# from class_highway import *<
from class_point import *
from class_robot import *
from class_table import *
from math import *
from math import *
from proxi_serial import *
from time import sleep
import random
import threading

table = Table();
proxy = Proxy_serial()
robot = Robot(table,proxy);

robot.distanceHard()
robot.rotationHard()
robot.distanceMedium()

robot.setTicks(0,0)
robot.setX(0)
robot.setY(0)
robot.setAngle(0)


# robot.setX(1000)
# robot.setY(1000)
# while True:
	# print(robot.checkObstacle())
# # while True :
# robot.openFrontGrip()
# sleep(1)
# robot.closeFrontGrip()
# sleep(1)

# robot.openBackGrip()
# sleep(1)
# robot.closeBackGrip()
# sleep(1)

# robot.openBallGrip()
# sleep(1)
# robot.closeBallGrip()


robot.setBras(0,0)
sleep(1)
robot.setBras(100,100)

# robot.goto(30, 0, end_angle = 0)
# robot.goto(0, 0, end_angle = 0)
# robot.moveBackwardUntilblockage()
# robot.emergencyStop()
 # robot.moveBackward(400)
# robot.rotateTo(pi)
# sleep(2)
# robot.rotateTo(0)
# sleep(5)
# robot.distanceSoft()
# robot.rotationSoft()
# # robot.setDistCoeffs(0,0)

# while True :
# 	print(robot.isJumperIn())
# 	robot.proxy.setServo(15,10)
# 	sleep(1)
# 	robot.proxy.setServo(15,100)
print(robot.getX())
print(robot.getY())
print(robot.getAngle())
# 	# print()
# 	sleep(1)

