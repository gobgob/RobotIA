#!/usr/bin/python

import time
from class_robot import *
from class_table import *
from proxi2c import *

table = Table()
proxy = Proxy_i2c()
robot = Robot(table,proxy);


def testPosition():
	# robot.setX(123)
	# robot.setY(-456)
	robot.setAngle(1.123)
	# proxy.setOdo(0,0,0,1)
	# proxy.setOdo(0,0,0,2)
	# proxy.setOdo(0,0,0,4)
	# print (proxy.getPosition())

	# robot.getPosition()
	# print(robot.getX())
	# assert robot.getX()==123;
	# print(robot.getY())
	# assert robot.getY()==-456;
	print(robot.getAngle())
	assert robot.getAngle()==1.123;


def test():
	print (proxy.getStatus())

test()
testPosition()
