#!/usr/bin/python

import time
from class_robot import *
from class_table import *

table = Table()
gobywan = Robot(table)


def testPosition():
	gobywan.setX(123)
	gobywan.setY(-456)
	gobywan.setAngle(1.123)

	gobywan.getPosition()
	assert gobywan.getX()==123;
	assert gobywan.getY()==-456;
	assert gobywan.getAngle()==1.123;

def testCoeffSetGet():
	gobywan.setDistCoeffs(12345,999999)
	gobywan.getLinCoeffs()
	assert gobywan.KpLin==12345
	assert gobywan.KdLin==999999

	gobywan.setRotCoeffs(666,23232323)
	gobywan.getRotCoeffs()
	assert gobywan.KpRot==666
	assert gobywan.KdRot==23232323

def testServo():
	# gobywan.MoveServo(1,20)# bras  gauche
	# time.sleep(0.5)
	# gobywan.MoveServo(1,30)
	# time.sleep(0.5)


	gobywan.tongueOut()
	time.sleep(0.5)
	gobywan.tongueIn()
	time.sleep(0.5)


	# gobywan.MoveServo(3,20) #dent gauche
	# time.sleep(0.5)
	# gobywan.MoveServo(3,30)
	# time.sleep(0.5)


	# gobywan.MoveServo(4,20) #dent droite
	# time.sleep(0.5)
	# gobywan.MoveServo(4,30)
	# time.sleep(0.5)

	# gobywan.MoveServo(0,20)# bras  droit
	# time.sleep(0.5)
	# gobywan.MoveServo(0,30)
	# time.sleep(0.5)

def testJumper():
	while True:
		s=(gobywan.isJumperIn())
		print str(s)
		# time.sleep(0.1)

def testUS():
	while True:
		print gobywan.getUltrasounds()
		time.sleep(0.1)

def testObstacle():
	while True:
		print gobywan.checkObstacle()

def testBtn():
	while True:
		print gobywan.getButton(1)
		print gobywan.getButton(2)
		print " "

def testCheveux():
	print gobywan.hairUp()

import sys
from class_point import *

def testInTable():
	table=Table()
	for x in range(-10,25):
		for y in range (-20,20):
			p=Point(x*100,y*100)
			if table.isInTable(p):
				sys.stdout.write(' ')
			else:
				sys.stdout.write('o')
		print x

def testTick():
	while True:
		res,r,l=gobywan.getTicks()
		dist= (r+l)/2
		print "r "+str(r)
		print "l "+str(l)
		print "dist "+str(dist)


def testTick2():
	while True:
		gobywan.goto(4500,0)
		
def testCroc():
	while True:
		gobywan.crocOut()
		sleep(1)
		gobywan.crocIn()
		sleep(0.5)


def testgoto():
	gobywan.setX(0)
	gobywan.setY(0)
	gobywan.setAngle(0)

	gobywan.goto (1000,0)



# testPosition()
# testCoeffSetGet()
# testServo()
# testJumper()
# testTick()
# testInTable()
# testBtn()
# testCheveux()
testCroc()
# testgoto()
# testUS()
# testObstacle()

# import random
# from random import *

# def ran():
# 	return str(randrange(10,170)).zfill(3)

# while True:
# 	gobywan.eyes.rotate("R",ran())
# 	gobywan.eyes.rotate("L",ran())
# 	gobywan.eyes.police()
# 	sleep(0.3)