import smbus
import time
from proxi2c_generated import *

class Proxy_i2c(GeneratedProxy_i2c):
	"""proxy i2c"""

	def __init__(self):
		self.address = 0x42
		try:
			self.bus = smbus.SMBus(1)
		except:
			self.bus=None
			print("I2c not supported");
	

	def checkChecksum(self,vals):
		checksum=0;
		for val in vals[:-1]:
			checksum^=val
		return(checksum==vals[-1])

	def readBlock(self,register,lenght):
		vals=None;
		while True:
			vals=self.bus.read_i2c_block_data(self.address,self.i2c_registers['REG_GETTICKS'],9)
			if self.checkChecksum(vals) :
				break;
		return vals;

# @flag SET_ODO_X	1
# @flag SET_ODO_Y	2
# @flag SET_ODO_ANGLE	4

# @method move
# @type setter
# @param uinteger 32 rel_dist
# @param bool 8 sign

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

## @method getUltrasounds
## @type getter
## @param integer 8 kp
## @param integer 32 dist

## @method getJumper
## @type getter
## @param bool 8 dist

# @method getStatus
# @type getter
# @param bool 8 bfr
# @param bool 8 bfl
# @param bool 8 bbr
# @param bool 8 bbl
# @param bool 8 cmdhack