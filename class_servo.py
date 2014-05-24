
class Servo():
	number=0
	angle=None
	proxy=None

	def __init__(self,number,proxy):
		self.proxy = proxy
		self.number = number
		self.proxy = proxy

	def move(self,angle):
		self.angle=angle
		self.proxy.moveservo