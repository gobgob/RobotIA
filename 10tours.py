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

#define DEFAULT_TICK_PER_METERS (4798.0)
#define DEFAULT_TICK_PER_RADS (515.678044375)

# robot.setTickRatio(25500,4356);
robot.setTickRatio(27793,3990);
robot.setTicks(0,0)
robot.setX(0)
robot.setY(0)
robot.setAngle(0)


robot.distanceHard()
robot.rotationHard()
robot.rotate(10*2*pi,timeout=120)
sleep(5)
robot.distanceSoft()
robot.rotationSoft()

# robot.goto(400,0,pi/2)
# robot.goto(400,400,pi)
# robot.goto(0,400,3*pi/2)
# robot.goto(0,0,0)

print(robot.getAngle())
print(robot.getTicks())
