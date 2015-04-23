#!/usr/bin/python3

from math import *
from class_robot import *
from class_table import *
from strategy_calibration import *
# from strategy_depart import *
from strategy_homologation import *
from class_highway import *
from time import sleep
import threading
from proxi_serial import *
from math import *
from class_point import *


import random

table = Table();
proxy = Proxy_serial()
robot = Robot(table,proxy);

robot.distanceHard()
robot.rotationHard()

robot.setTicks(0,0)
robot.setX(0)
robot.setY(0)
robot.setAngle(0)

robot.setRotCoeffs(80,0)
robot.setDistCoeffs(70,0)

while True :
	robot.openFrontGrip()
	sleep(1)
	robot.closeFrontGrip()
	sleep(1)


# sleep(2)
# robot.moveForward(200)
# robot.moveBackward(200)
# robot.rotate(3.14)
# robot.rotate(-3.14)
# # robot.setDistCoeffs(0,0)

while True :
	print(robot.getX())
	print(robot.getY())
	print(robot.getAngle())
	print()
	sleep(0.5)

