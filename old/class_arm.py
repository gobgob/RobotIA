import time

class Arm():
	servNumber=0
	angleDown=0
	angleUp=0
	angleMedium=0
	servo=None

	def __init__(self,servo,angleDown,angleMedium,angleUp):
		self.servo=servo
		self.angleDown=angleDown
		self.angleMedium=angleMedium
		self.angleUp=angleUp

	def up(self):
		self.move(self.angleUp)

	def down(self):
		self.move(self.angleDown)

	def medium(self):
		self.move(self.angleMedium)
