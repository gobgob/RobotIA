#!/usr/bin/python3

from class_robot import *
from class_table import *
from math import *
from math import *
from proxi_serial import *
from time import sleep
import threading

table = Table();
proxy = Proxy_serial()
robot = Robot(table,proxy);

robot.distanceHard()
robot.rotationHard()

robot.setTicks(0,0)
robot.setX(0)
robot.setY(0)
robot.setAngle(0)
robot.setTickRatio(27800,4350);

# robot.goto(300,0,pi/2)
# robot.goto(300,300,pi)
# robot.goto(0,300,-pi/2)
# robot.goto(0,0,0)

robot.goto(300,0,-pi/2)
robot.goto(300,-300,pi)
robot.goto(0,-300,pi/2)
robot.goto(0,0,0)

# robot.goto(30, 0, end_angle = 0)
# robot.goto(0, 0, end_angle = 0)
# robot.moveForward(400)
# robot.moveBackward(400)
# robot.rotate(3.14)
# robot.rotate(-3.14)
# # robot.setDistCoeffs(0,0)

# while True :
# 	print(robot.isJumperIn())
# 	robot.proxy.setServo(15,10)
# 	sleep(1)
# 	robot.proxy.setServo(15,100)
print(robot.getX())
print(robot.getY())
print(robot.getAngle())
sleep(5)
robot.distanceSoft()
robot.rotationSoft()
# 	# print()
# 	sleep(1)

