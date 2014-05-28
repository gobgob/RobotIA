#!/usr/bin/python3

from math import *
from class_robot import *
from class_table import *
from strategy_calibration import *
from strategy_depart import *
from strategy_homologation import *
from strategy_mammouth import *
from strategy_fresque import *
from time import sleep
import threading
from proxi_serial import *

table = Table();
proxy = Proxy_serial()
robot = Robot(table,proxy);

strategyHomologation=StrategyHomologation(robot)
strategyMammouth=StrategyMammouth(robot)
strategyFresque=StrategyFresque(robot)


def doStrategy( fun, *args ):
	try:
		fun( *args )
	except Obstacle as e:
		pass

def match():
	while True:
		try:
			doStrategy(strategyMammouth.run,0);
			doStrategy(strategyFresque.run);
			doStrategy(strategyMammouth.run,1);
			sleep(1)
			# strategyHomologation.run();
		except EndOfGame as e:
			print("Fin des 90 sec")

def funny():
	print("funny !")
	robot.launchNet()
	exit()


threadMatch = threading.Thread(None, match)
threadFunny = threading.Thread(None, funny)

robot.setTicks(0,0)
robot.setX(0)
robot.setY(0)
robot.setAngle(0)
robot.setX(415)
robot.setY(colorize_y(-1400))
robot.setAngle(colorize_angle((pi/180)*90))

while not robot.isJumperIn():
	pass

print("The Jumper is in.")
sleep(1)

while robot.isJumperIn():
	pass

print("The Jumper is out.")
sleep(1)


startTime=time.time()
threadMatch.start()
# match()

while time.time() < startTime+85:
	print ("remaining time :"+str((startTime+85)-time.time()))
	sleep(1)

robot.flag_endOfGame = True
print ("End of game thread master")

while time.time() < startTime+90:
	sleep(1)

threadFunny.start()

