import smbus
import time

def split_integer_32(x):
	splitted = []
	splitted.append(0xFF&(x>>24))
	splitted.append(0xFF&(x>>16))
	splitted.append(0xFF&(x>>8))
	splitted.append(0xFF&(x>>0))
	return splitted;

def make_integer_32(vals,offset):
	value=0
	value+=vals[offset+0]<<24
	value+=vals[offset+1]<<16
	value+=vals[offset+2]<<8
	value+=vals[offset+3]<<0
	return value;


#move
#input integer 32 dist
#input bool forward

#rotate
#output integer 32 angle
#input bool isAbs

#goto
#input integer 32 x
#input integer 32 y
#input integer 32 delta_max

#getPosition
#output integer 32 x
#output integer 32 y
#output integer 32 angle

#setOdo
#input integer 32 x
#input integer 32 y
#input integer 32 angle
#input integer 8 flag

#setDistKpKd
#input integer 32 kp
#input integer 32 kd

#getLinKpKd
#output integer 32 kp
#output integer 32 kd

#setRotKpKd
#input integer 32 kp
#input integer 32 kd

#getRotKpKd
#output integer 32 kp
#output integer 32 kd

#getUltrasounds
#input integer 8 kp
#output integer 32 dist

#getJumper
#output bool dist

#getStatus
#output bool bfr
#output bool bfl
#output bool bbr
#output bool bbl
#output bool cmdhack

i2c_registers = {
	"REG_GOTO":1,
	"REG_GETPOSITION":2,
}


class Proxy_i2c:
	"""proxy i2c"""

	bus = smbus.SMBus(1)
	address = 0x42

	def goto(x,y,delta_max):
		vals=[]
		vals.extend(split_integer_32(x))
		vals.extend(split_integer_32(y))
		vals.extend(split_integer_32(delta_max))
		bus.write_block_data(address,i2c_registers['REG_GOTO'],vals)


	def getPosition():
		vals=bus.read_i2c_block_data(address,i2c_registers['REG_GETPOSITION'],12)
		res=0
		x=make_integer_32(vals,0)
		y=make_integer_32(vals,4)
		angle=make_integer_32(vals,8)
		return res,x,y,angle


# i2c_goto(7,9,10)
# print (i2c_getPosition())

# while True:
#     i2c_goto(7,9,10)
#     for i in range(0,255) :
#         print bus.read_byte_data(address, i)
#         # time.sleep(1)