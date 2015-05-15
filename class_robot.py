import time
from time import sleep
from math import *
from utils import *
from class_exceptions import *
from class_point import *
from class_table import *
from color import *
import RPi.GPIO as GPIO

# from class_eyes import *


SERVO_FRONT_GRIP_PIN = 16
SERVO_FRONT_GRIP_CLOSE = 80
SERVO_FRONT_GRIP_OPEN = 0

SERVO_BACK_GRIP_PIN = 21
SERVO_BACK_GRIP_CLOSE = 180
SERVO_BACK_GRIP_OPEN = 70

SERVO_BALL_GRIP_PIN = 20
SERVO_BALL_GRIP_CLOSE = 40
SERVO_BALL_GRIP_OPEN = 0

SERVO_LEFT_ARM_PIN  = 14
SERVO_RIGHT_ARM_PIN = 15

SERVO_LEFT_ARM_HIGH = 40
SERVO_LEFT_ARM_LOW  = 90

SERVO_RIGHT_ARM_HIGH = 40
SERVO_RIGHT_ARM_LOW = 90

class Robot:
	"""The robot class !"""

	blockageFrontRight=False
	blockageFrontLeft=False
	blockageBackRight=False
	blockageBackLeft=False

	isObstacleDetectionOn=False

	flag_endOfGame = False

	width=180
	height=180

	table=None
	proxy = None

	x=0
	y=0
	angle=0

	KpLin=0
	KdLin=0

	# leftArm=None
	# rightArm=None


	gpio_jumper=9
	gpio_fan=7
	gpio_wheel=10

	def __init__(self,table,proxy):
		self.proxy = proxy
		self.table = table
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.gpio_jumper, GPIO.IN)
		self.setTickRatio(27800,4350);
		# eyes = Eyes()

	def openFrontGrip(self):
		print("openFrontGrip")
		self.proxy.setServo(SERVO_FRONT_GRIP_PIN, SERVO_FRONT_GRIP_OPEN)

	def closeFrontGrip(self):
		print("closeFrontGrip")
		self.proxy.setServo(SERVO_FRONT_GRIP_PIN, SERVO_FRONT_GRIP_CLOSE)

	def openBackGrip(self):
		print("openBackGrip")
		self.proxy.setServo(SERVO_BACK_GRIP_PIN, SERVO_BACK_GRIP_OPEN)

	def closeBackGrip(self):
		print("closeBackGrip")
		self.proxy.setServo(SERVO_BACK_GRIP_PIN, SERVO_BACK_GRIP_CLOSE)

	def openBallGrip(self):
		print("openBallGrip")
		self.proxy.setServo(SERVO_BALL_GRIP_PIN, SERVO_BALL_GRIP_OPEN)

	def closeBallGrip(self):
		print("closeBallGrip")
		self.proxy.setServo(SERVO_BALL_GRIP_PIN, SERVO_BALL_GRIP_CLOSE)

	def setBras(self, leftArm, rightArm):
		leftArm = SERVO_LEFT_ARM_HIGH  +(SERVO_LEFT_ARM_LOW  - SERVO_LEFT_ARM_HIGH)*leftArm/100
		rightArm =180-( SERVO_RIGHT_ARM_HIGH+(SERVO_RIGHT_ARM_LOW - SERVO_RIGHT_ARM_HIGH)*rightArm/100)
		self.proxy.setServo(SERVO_LEFT_ARM_PIN, leftArm)
		self.proxy.setServo(SERVO_RIGHT_ARM_PIN, rightArm)

#Mouvements#

	def moveForward(self,dist,noWait=False):
		print ("moveForward " +str(dist) + " noWait="+str(noWait))
		self.proxy.move(dist,+1)
		self.waitForEvent(noWait=noWait,exceptOnUltrasouds=True)

	def moveBackward(self,dist,noWait=False):
		print ("moveBackward " +str(dist))
		self.proxy.move(dist,-1)
		self.waitForEvent(noWait=noWait)

	def moveForwardUntilblockage(self,noWait=False):
		print ("moveForwardUntilblockage")
		while not (self.blockageFrontRight and self.blockageFrontLeft):
			self.proxy.move(1000,+1)
			self.waitForEvent(returnOnBlock=True,timeout=4,noWait=noWait)

	def moveBackwardUntilblockage(self,noWait=False):
		print ("moveBackwardUntilblockage")
		while not (self.blockageBackLeft and self.blockageBackRight):
			self.proxy.move(1000,-1)
			self.waitForEvent(returnOnBlock=True,timeout=4,noWait=noWait)
			self.proxy.move(0,1)

	def rotate(self,angle,autocolor=False,noWait=False,timeout=10):
		print ("rotate " +str(angle)+ "("+str((angle/pi)*180)+")"+" noWait="+str(noWait))
		if autocolor:
			self.proxy.rotate(colorize_angle(angle),False)
		else:
			self.proxy.rotate(angle,False)
		self.waitForEvent(returnOnBlock=False,timeout=timeout,noWait=noWait);

	def rotateTo(self,angle,autocolor=False,noWait=False):
		print ("rotateTo " +str(angle)+ "("+str((angle/pi)*180)+")"+" noWait="+str(noWait))
		if autocolor:
			self.proxy.rotate(colorize_angle(angle),True)
		else:
			self.proxy.rotate(angle,True)
		self.waitForEvent(returnOnBlock=True,timeout=5,noWait=noWait);


	def gotoEx(self,x,y,delta_max=10): #handle US
		print ("gotoex("+str(x)+","+str(y)+")")
		count=0
		while count<5 :
			try:
				self.proxy.goto(x,y,delta_max)
				if (self.waitForEvent(returnOnBlock=True,exceptOnUltrasouds=True, timeout=5)):
					break
				else:
					print ("jammed")
					count+=1
					self.unblock()
			except Obstacle as e:
				count+=1
				self.setBras(100,100)
				sleep(2)
				self.setBras(0,0)

		if (count>=5):
			raise Obstacle()

	def goto(self,x,y,end_angle=None,autocolor=False,rotateOnly=False):
		print ("goto("+str(x)+","+str(y)+")")

		if autocolor:
			y=colorize_y(y)

		self.getPosition()
		new_angle = atan2(y-self.y,x-self.x)
		new_angle = ClosestEquivalentAngle(self.angle,new_angle)
		diff_angle = new_angle-self.angle

		if fabs(diff_angle)>pi/3 or rotateOnly:
			sleep(0.5)
			self.rotateTo(new_angle)
			if rotateOnly:
				return

		self.gotoEx(x,y,15)
		
		if not end_angle is None:
			sleep(0.5)
			self.rotateTo(end_angle,autocolor=autocolor)

		return True

	def unblock(self):
		self.emergencyStop()
		pass
		# if (self.blockageFrontRight):
		# 	self.moveBackward(150,noWait=True)
		# 	sleep(0.5)
		# 	self.rotate(pi/8,noWait=True)
		# 	sleep(0.5)
		# 	self.moveForward(150,noWait=True)
		# 	sleep(0.5)

		# if (self.blockageFrontLeft):
		# 	self.moveBackward(100,noWait=True)
		# 	sleep(0.5)
		# 	self.rotate(-pi/8,noWait=True)
		# 	sleep(0.5)
		# 	self.moveForward(100,noWait=True)
		# 	sleep(0.5)

		# if (self.blockageBackLeft):
		# 	self.moveForward(100,noWait=True)
		# 	sleep(0.5)
		# 	self.rotate(pi/8,noWait=True)
		# 	sleep(0.5)
		# 	self.moveBackward(100,noWait=True)
		# 	sleep(0.5)

		# if (self.blockageBackRight):
		# 	self.moveForward(100,noWait=True)
		# 	sleep(0.5)
		# 	self.rotate(-pi/8,noWait=True)
		# 	sleep(0.5)
		# 	self.moveBackward(100,noWait=True)
		# 	sleep(0.5)


	def getPosition(self):
		res,x,y,a = self.proxy.getPosition()
		while True:
			if res==0:
				self.x=x
				self.y=y
				self.angle=a
				return True

	def setX(self,x,autocolor=False):
		print ("setX "+str(x))
		self.proxy.setOdo(x,0,0,1)
		self.moveForward(0)

	def getX(self):
		self.getPosition()
		return self.x

	def setY(self,y,autocolor=False):
		print ("setY "+str(y))
		if autocolor:
			y=colorize_y(y)			
		self.proxy.setOdo(0,y,0,2)
		self.moveForward(0)

	def getY(self):
		self.getPosition()
		return self.y

	def setAngle(self,angle,autocolor=False):
		print ("setAngle "+str(angle))
		if autocolor:
			y=colorize_angle(angle)	
		self.proxy.setOdo(0,0,angle,4)
		self.rotate(0,timeout=1)

	def getAngle(self):
		self.getPosition()
		return self.angle

	def getTicks(self):
		res=-1
		while res<0 :
			res,right,left = self.proxy.getTicks()
		return res,right,left

	def setTicks(self,right,left):
		self.proxy.setTicks(right,left)

	def emergencyStop(self):
		tmp = self.isObstacleDetectionOn
		self.isObstacleDetectionOn=False
		self.moveForward(0)
		self.rotate(0)
		self.isObstacleDetectionOn=tmp

	def setDistCoeffs(self,kp,kd):
		return self.proxy.setDistKpKd(kp,kd)

	def getDistCoeffs(self):
		res,kp,kd = avrSpi.avrGetDistKpKd()
		if res==0:
			self.KpLin=kp
			self.KdLin=kd
			return True
		else:
			return False

	def setRotCoeffs(self,kp,kd):
		return self.proxy.setRotKpKd(kp,kd)

	def getRotCoeffs(self):
		res,kp,kd = self.proxy.getRotKpKd()
		if res==0:
			self.KpRot=kp
			self.KdRot=kd
			return True
		else:
			return False

	def setTickRatio(self,new_ticks_per_meters,new_ticks_per_rads):
		return self.proxy.setTickRatio(new_ticks_per_meters,new_ticks_per_rads)

	def getUltrasounds(self):
		res,dist=self.proxy.getUltrasounds()
		return dist

	def activateUltrasounds(self):
		self.isObstacleDetectionOn=True

	def deactivateUltrasounds(self):
		self.isObstacleDetectionOn=False

	def isJumperIn(self):
		return not GPIO.input(self.gpio_jumper)

#evenement#

	def waitForEvent(self,returnOnBlock=False,timeout=0,noWait=False,exceptOnUltrasouds=False):
		
		if noWait :
			return True

		starttime=time.time()

		#timeout par default
		if timeout==0:
			timeout=10

		while True :
			res,bfr,bfl,bbr,bbl,cmdhack = self.proxy.getStatus()
			# print ("res "+str(res)+" ack " + str(cmdhack))
			# print ("bfr="+str(bfr)+" bfl="+str(bfl)+" bbr="+str(bbr)+" bbl="+str(bbl))
			self.checkEndOfGame()

			# self.getPosition()
			# print("x "+str(self.x))
			# print("y "+str(self.y))

			if self.isObstacleDetectionOn :
				if exceptOnUltrasouds and self.checkObstacle():
					self.emergencyStop()
					raise Obstacle()
					return True

			if(timeout>0 and starttime+timeout<time.time()):
				print ("!!! Timeout")
				return True

			if res==0:
				self.blockageFrontRight=bfr
				self.blockageFrontLeft=bfl
				self.blockageBackRight=bbr
				self.blockageBackLeft=bbl
				if returnOnBlock and (bfr or bfl or bbr or bbl):
					print("BLOCAGE\n")
					return False
				if cmdhack:
					return True
			time.sleep(0.02);

	def checkEndOfGame(self):
		if self.flag_endOfGame:
			self.flag_endOfGame=False
			raise EndOfGame()

	# def checkObstacle(self):
	# 	distmin=2
	# 	distblock=20

	# 	self.checkEndOfGame()
	# 	# return False
	# 	dist = self.getUltrasounds()
	# 	if dist>distmin and dist <distblock:
	# 		dist=0.0
	# 		for i in range(0,10):
	# 			dist=dist+self.getUltrasounds()/10.0
	# 			sleep(0.001)
	# 		print ("debug "+str(dist))
	# 		if dist>distmin and dist <distblock:
	# 			self.getPosition()
	# 			x=self.x+(dist+self.height/2)*cos(self.angle)
	# 			y=self.y+(dist+self.height/2)*sin(self.angle)
	# 			obstacle=Point(x,y)
	# 			if self.table.isInTable(obstacle) :
	# 				print ("Obstacle "+str(dist)+" "+str(x)+" "+str(y))
	# 				return True
	# 	return False

	def checkObstacle(self):
		distmin=0
		distblock=250

		self.checkEndOfGame()
		# return False
		dist = self.getUltrasounds()
		if dist>distmin and dist <distblock:
			dist=0.0
			for i in range(0,10):
				dist=dist+self.getUltrasounds()/10.0
				sleep(0.001)
			if dist>distmin and dist <distblock:
				self.getPosition()
				x=self.x+(dist+self.height/2)*cos(self.angle)
				y=self.y+(dist+self.height/2)*sin(self.angle)
				obstacle=Point(x,y)
				if self.table.isInTable(obstacle) :
					print ("Obstacle "+str(dist)+" "+str(x)+" "+str(y))
					return True
		return False

	def rotationSoft(self):
		self.setRotCoeffs(0,0)

	def rotationMedium(self):
		self.setRotCoeffs(100,0)

	def rotationHard(self):
		self.setRotCoeffs(300,20000)

	def rotationVeryHard(self):
		self.setRotCoeffs(100,0)

	def distanceSoft(self):
		self.setDistCoeffs(50,0)

	def distanceMedium(self):
		self.setDistCoeffs(40,30000)

	def distanceHard(self):
		self.setDistCoeffs(120,12000)

	def distanceVeryHard(self):
		self.setDistCoeffs(300,12000)


	def dumpSpeed(self):
		print(self.proxy.getMaxSpeeds())

	def goSlow(self):
		self.proxy.setMaxSpeeds(90000,50000)

	def goFast(self):
		self.proxy.setMaxSpeeds(90000,90000)
