from math import *
from class_robot import *
from class_table import *
from class_point import *
from strategy import *
from strategy_calibration import *
from time import sleep

class StrategyDepartCadeaux(Strategy):
	robot=None
	table=None
	liste_cadeau=[]
	
	def __init__(self,table,robot,liste_cadeau):
		self.table=table
		self.robot=robot
		self.liste_cadeau=liste_cadeau
		
	def run(self):
		robot=self.robot
		table=self.table
		print ("Strategy depart")

		robot.distanceHard()
		robot.rotationHard()

		robot.setAngle(colorize_angle(-pi/2))
		robot.setY(colorize_y(self.table.width/2 - self.robot.height/2))
		
		#pas besoin d'ultrasons en debut de match
		robot.deactivateUltrasounds()
		#je sort de la case
		if color=="RED" :
			robot.moveForward(470)
		else:
			robot.moveForward(460)


		robot.rotateTo(0)

		#je me raproche du bort de la table
		robot.moveForward(42)
		robot.tongueOut()
		robot.eyes.gift()

		#je recale et pousse le 1er cadeau
		robot.distanceVeryHard()
		robot.rotationSoft()
		robot.moveForwardUntilBlocage()
		robot.setAngle(0)
		robot.setX(table.height-robot.height/2)
		robot.tongueIn()

		robot.rotationHard()
		robot.distanceHard()

		robot.moveBackward(170)
		robot.rotateTo(-pi/2,autocolor=True)


		robot.moveForward(510)
		robot.primaryArm.up()
		sleep(0.4)
		robot.primaryArm.down()
		robot.moveBackward(100)
		robot.rotateTo(-pi)
		robot.crocOut()
		robot.moveForward(200)


		# try:
		# 	if not self.liste_cadeau[1].burned:
		# 		print "Burning cadeaux 1"
		# 		self.burn(1)
		# except Obstacle as e:
		# 	robot.emergencyStop()
		# 	sleep(3)
		# 	return

	def burn(self,i):
		robot=self.robot
		table=self.table
		robot.checkEndOfGame()
		cadeau = self.liste_cadeau[i]
		robot.activateUltrasounds()
		robot.goto(cadeau.x,cadeau.y,autocolor=True)
		robot.deactivateUltrasounds()
		robot.rotateTo(0)
		robot.tongueOut()
		robot.eyes.gift()
		robot.distanceVeryHard()
		robot.rotationSoft()
		robot.moveForwardUntilBlocage()
		robot.setAngle(0)
		robot.setX(table.height-robot.height/2)
		robot.tongueIn()
		cadeau.burned=True
		robot.rotationHard()
		robot.distanceHard()
		robot.moveBackward(200)