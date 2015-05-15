#!/usr/bin/python3

from class_robot import *
from class_table import *
from math import *
from proxi_serial import *
from strategy_start import *
from strategy_bis import *
from time import sleep
import threading

table = Table();
proxy = Proxy_serial()
robot = Robot(table,proxy);

strategyStart=StrategyStart(robot)
strategyBis=StrategyBis(robot)

def doStrategy( fun, *args ):
	try:
		fun( *args )
	except Obstacle as e:
		pass

def match():
	while True:
		try:
			doStrategy(strategyStart.run);
			doStrategy(strategyBis.run);
			robot.checkEndOfGame()
			sleep(1)
		except EndOfGame as e:
			# robot.goto(0,-630,autocolor=True,rotateOnly=True)
			print("Fin des 90 sec")
			return

def funny():
	robot.emergencyStop()
	print("funny !")
	exit()

threadMatch = threading.Thread(None, match)
threadFunny = threading.Thread(None, funny)


robot.distanceSoft()
robot.rotationSoft()


robot.setBras(100,100)
robot.openFrontGrip()
robot.openBackGrip()
robot.closeBallGrip()

print("Waiting for Jumper")

while not robot.isJumperIn():
	pass

robot.setBras(0,0)
print("The Jumper is in.")
sleep(1)





# robot appuyé contre tasseau posé sur bordure salle de cinéma
robot.setTicks(0,0)
robot.setY(colorize_y(1500-400-90))
#au milieu
robot.setX(1000)
#regarde vers l'autre coté de la table
robot.setAngle(colorize_angle((pi/180)*(-90)))

while robot.isJumperIn():
	pass
print("The Jumper is out.")

sleep(0.5)
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

