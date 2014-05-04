#!/usr/bin/python

from math import *
from class_robot import *
from class_table import *
from strategy_calibration import *
from strategy_depart import *
from time import sleep
import threading
from proxi2c import *

table = Table();
robot = Robot(table)
proxy = Proxy_i2c()

strategyCalibration=StrategyCalibration(table,robot)

def match():
	strategyDepartCadeaux.run();
	while True:
		try:
			robot.checkEndOfGame()
			strategyDiagVerres1.run()
			strategyGateau.run()
			strategyCadeau2.run()
			print("next strat")
			sleep(1)
		except EndOfGame as e:
			print("Fin des 90 sec")
			robot.rotateTo(0,noWait=True)
			sleep(1)
			robot.stop
			break

def funny():
	print("funny !")
	# robot.hairUp()


threadMatch = threading.Thread(None, match)
threadFunny = threading.Thread(None, funny)

robot.setX(0)
robot.setY(0)
robot.setAngle(0)

while not robot.isJumperIn():
	pass

sleep(1)

while robot.isJumperIn():
	pass

startTime=time.time()
threadMatch.start()


while time.time() < startTime+80:
	print ("remaining time :"+str((startTime+80)-time.time()))
	sleep(1)


while time.time() < startTime+88:
	print ("remaining time :"+str((startTime+88)-time.time()))
	sleep(1)

robot.flag_endOfGame = True
print ("End of game thread master")

while time.time() < startTime+90:
	sleep(1)
threadFunny.start()

