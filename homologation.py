#!/usr/bin/python3

from math import *
from class_robot import *
from class_table import *
from strategy_calibration import *
from strategy_depart import *
from strategy_homologation import *
from time import sleep
import threading
from proxi_serial import *

table = Table();
proxy = Proxy_serial()
robot = Robot(table,proxy);

StrategyHomologation=StrategyHomologation(robot)

def match():
	try:
		StrategyHomologation.run();
	except EndOfGame as e:
		print("Fin des 90 sec")

# def funny():
# 	print("funny !")
# 	# robot.hairUp()


# threadMatch = threading.Thread(None, match)
# threadFunny = threading.Thread(None, funny)

robot.setTicks(0,0)
robot.setX(0)
robot.setY(0)
robot.setAngle(0)

while not robot.isJumperIn():
	pass

# print("The Jumper is in.")
# sleep(1)

# while robot.isJumperIn():
# 	pass

# print("The Jumper is out.")
# sleep(1)


startTime=time.time()
# threadMatch.start()
match()

while time.time() < startTime+10:
	print ("remaining time :"+str((startTime+80)-time.time()))
	sleep(1)


while time.time() < startTime+10:
	print ("remaining time :"+str((startTime+88)-time.time()))
	sleep(1)

robot.flag_endOfGame = True
print ("End of game thread master")

while time.time() < startTime+15:
	sleep(1)
threadFunny.start()

