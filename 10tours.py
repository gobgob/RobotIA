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

robot.rotateTo(1*pi)
robot.rotateTo(0*pi)
# robot.rotate(1*2*pi,timeout=120)
sleep(5)
robot.distanceSoft()
robot.rotationSoft()

# robot.goto(400,0,pi/2)
# robot.goto(400,400,pi)
# robot.goto(0,400,3*pi/2)
# robot.goto(0,0,0)

print(robot.getAngle())
print(robot.getTicks())
