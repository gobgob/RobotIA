#!/usr/bin/python3

from math import *
from class_robot import *
from class_table import *
from strategy_calibration import *
from strategy_depart import *
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
# while True:
# 	robot.rotate(pi/20,timeout=300)
# 	sleep(2);


# highway = Highway()

# pts1 = Point(490,1025)
# pts2 = Point(502,728)
# res1=highway.findRoute(pts1,pts2)
# res=res1.points
# print("dist= "+str(res1.dist))
# for pt in res:
# 	print(pt.name+" "+str(pt.x) + " "+str(pt.y))

#define DEFAULT_TICK_PER_METERS (4798.0)
#define DEFAULT_TICK_PER_RADS (515.678044375)


# robot.setTicks(0,0)
# robot.setX(0)
# robot.setY(0)
# robot.setAngle(0)

# robot.launchNet()
# # robot.activateUltrasounds()
# # robot.distanceSoft()
# # robot.rotationSoft()

# robot.rotationHard()
# robot.distanceHard()
# # robot.rotate(40*pi,timeout=300)
# # robot.moveForward(200)
# # sleep(2)
# robot.rotate(-2*pi)
# sleep(0.5)
# robot.moveForward(100)
# sleep(0.5)
# robot.rotate(-2*pi)
# sleep(0.5)
# robot.moveBackward(100)



# robot.moveBackward(200)
# robot.goto(1000,0)
# sleep(0.5)
# robot.goto(0,0)
# sleep(0.5)
# robot.rotate(2*3.14)
# sleep(0.5)
# robot.rotate(-2*3.14)

# robot.launchBall(10)


while True :
	# robot.setBras(random.randint(1,100),random.randint(1,100))
	t=time.time()
	robot.setBras(
		50+50*sin(2*3.14*t*0.7),
		50+50*cos(2*3.14*t*0.7))
	sleep(0.01)


# robot.moveBackwardUntilblockage()


# robot.emergencyStop()

# while True :
# 	print(robot.getUltrasounds())
# 	sleep(0.5)

# while not robot.isJumperIn():
# 	pass

# print("The Jumper is in.")
# sleep(1)

# while robot.isJumperIn():
# 	pass

# print("The Jumper is out.")
# sleep(1)

# robot.rotate(40*pi+2*pi+pi/4,timeout=30)
# robot.rotate(80*pi,timeout=120)

# robot.goto(400,0,pi/2)
# robot.goto(400,400,pi)
# robot.goto(0,400,3*pi/2)
# robot.goto(0,0,0)

# print(robot.getAngle())
# print(robot.getTicks())
