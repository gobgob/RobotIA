from serial import *
import time
from proxi_generated import *

# class Proxy_i2c(GeneratedProxy_i2c):
class Proxy_serial(GeneratedProxy):
	"""proxy i2c"""
	bus=None

	def __init__(self):
		# try:
		# self.bus = Serial('/dev/ttyS0', 115200,timeout=0.1)
		self.bus = Serial('/dev/ttyAMA0', 115200,timeout=0.1)
		# except:
		# 	self.bus=None
		# 	print("I2c not supported");
	

	# in case vals is empty, we cath errors...
	def checksum(self,vals):
		checksum=0;
		try:
			for val in vals:
				checksum^=(val)
			return checksum
		except:
			return 0

	def checkChecksum(self,vals):
		try:
			return (self.checksum(vals[:-1])==(vals[-1]))
		except:
			return False

	def readBlock(self,register,lenght):
		vals=None
		while True:
			self.writeBlock(register,[])
			vals=list(self.bus.read(lenght+1))
			if self.checkChecksum(vals) :
				break;
			print("retry")
			time.sleep(1)
		return vals

	def writeBlock(self,register,vals):
		lenght=len(vals)
		data=[0xFF,register,lenght] + vals
		checksum=self.checksum(data)
		data=data+[checksum]
		self.bus.write(bytes(data))

# @flag SET_ODO_X	1
# @flag SET_ODO_Y	2
# @flag SET_ODO_ANGLE	4

# @method move
# @type setter
# @param uinteger 32 rel_dist
# @param integer 8 sign

# @method rotate
# @type setter
# @param double 32 angle
# @param bool 8 isAbs

# @method goto
# @type setter
# @param integer 32 x
# @param integer 32 y
# @param integer 32 delta_max

# @method getPosition
# @type getter
# @param integer 32 x
# @param integer 32 y
# @param double 32 angle

# @method setOdo
# @type setter
# @param integer 32 x
# @param integer 32 y
# @param double 32 angle
# @param integer 8 flag

# @method setDistKpKd
# @type setter
# @param uinteger 32 kp
# @param uinteger 32 kd

# @method getDistKpKd
# @type getter
# @param uinteger 32 kp
# @param uinteger 32 kd

# @method setRotKpKd
# @type setter
# @param uinteger 32 kp
# @param uinteger 32 kd

# @method getRotKpKd
# @type getter
# @param uinteger 32 kp
# @param uinteger 32 kd

# @method getTicks
# @type getter
# @param integer 32 left
# @param integer 32 right

# @method setTicks
# @type setter
# @param integer 32 left
# @param integer 32 right

# @method getUltrasounds
# @type getter
# @param integer 32 dist

# @method getStatus
# @type getter
# @param bool 8 bfr
# @param bool 8 bfl
# @param bool 8 bbr
# @param bool 8 bbl
# @param bool 8 cmdhack

# @method setServo
# @type setter
# @param integer 8 pin
# @param integer 8 angle

# @method setTickRatio
# @type setter
# @param uinteger 32 new_ticks_per_meters
# @param uinteger 32 new_ticks_per_rads
