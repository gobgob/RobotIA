from utils import *
	
class GeneratedProxy():
	
	i2c_registers = {
		"REG_MOVE":1,
		"REG_ROTATE":2,
		"REG_GOTO":3,
		"REG_GETPOSITION":4,
		"REG_SETODO":5,
		"REG_SETDISTKPKD":6,
		"REG_GETDISTKPKD":7,
		"REG_SETROTKPKD":8,
		"REG_GETROTKPKD":9,
		"REG_GETTICKS":10,
		"REG_SETTICKS":11,
		"REG_GETULTRASOUNDS":12,
		"REG_GETSTATUS":13,
		"REG_SETSERVO":14,
		"REG_RATATOUILLE":15,
		"REG_LAUNCHNET":16,
		"REG_SETTICKRATIO":17,
		"REG_SETBRAS":18,
	}
	
	def move(self,rel_dist,sign):
		vals=[]
		vals.extend(split_uinteger_32(rel_dist))
		vals.extend(split_integer_8(sign))
		self.writeBlock(self.i2c_registers['REG_MOVE'],vals)
	
	def rotate(self,angle,isAbs):
		vals=[]
		vals.extend(split_double_32(angle))
		vals.extend(split_bool_8(isAbs))
		self.writeBlock(self.i2c_registers['REG_ROTATE'],vals)
	
	def goto(self,x,y,delta_max):
		vals=[]
		vals.extend(split_integer_32(x))
		vals.extend(split_integer_32(y))
		vals.extend(split_integer_32(delta_max))
		self.writeBlock(self.i2c_registers['REG_GOTO'],vals)
	
	def getPosition(self,):
		vals=self.readBlock(self.i2c_registers['REG_GETPOSITION'],12)
		res=0
		x=make_integer_32(vals,0)
		y=make_integer_32(vals,4)
		angle=make_double_32(vals,8)
		return res,x,y,angle
	
	def setOdo(self,x,y,angle,flag):
		vals=[]
		vals.extend(split_integer_32(x))
		vals.extend(split_integer_32(y))
		vals.extend(split_double_32(angle))
		vals.extend(split_integer_8(flag))
		self.writeBlock(self.i2c_registers['REG_SETODO'],vals)
	
	def setDistKpKd(self,kp,kd):
		vals=[]
		vals.extend(split_uinteger_32(kp))
		vals.extend(split_uinteger_32(kd))
		self.writeBlock(self.i2c_registers['REG_SETDISTKPKD'],vals)
	
	def getDistKpKd(self,):
		vals=self.readBlock(self.i2c_registers['REG_GETDISTKPKD'],8)
		res=0
		kp=make_uinteger_32(vals,0)
		kd=make_uinteger_32(vals,4)
		return res,kp,kd
	
	def setRotKpKd(self,kp,kd):
		vals=[]
		vals.extend(split_uinteger_32(kp))
		vals.extend(split_uinteger_32(kd))
		self.writeBlock(self.i2c_registers['REG_SETROTKPKD'],vals)
	
	def getRotKpKd(self,):
		vals=self.readBlock(self.i2c_registers['REG_GETROTKPKD'],8)
		res=0
		kp=make_uinteger_32(vals,0)
		kd=make_uinteger_32(vals,4)
		return res,kp,kd
	
	def getTicks(self,):
		vals=self.readBlock(self.i2c_registers['REG_GETTICKS'],8)
		res=0
		left=make_integer_32(vals,0)
		right=make_integer_32(vals,4)
		return res,left,right
	
	def setTicks(self,left,right):
		vals=[]
		vals.extend(split_integer_32(left))
		vals.extend(split_integer_32(right))
		self.writeBlock(self.i2c_registers['REG_SETTICKS'],vals)
	
	def getUltrasounds(self,):
		vals=self.readBlock(self.i2c_registers['REG_GETULTRASOUNDS'],4)
		res=0
		dist=make_integer_32(vals,0)
		return res,dist
	
	def getStatus(self,):
		vals=self.readBlock(self.i2c_registers['REG_GETSTATUS'],5)
		res=0
		bfr=make_bool_8(vals,0)
		bfl=make_bool_8(vals,1)
		bbr=make_bool_8(vals,2)
		bbl=make_bool_8(vals,3)
		cmdhack=make_bool_8(vals,4)
		return res,bfr,bfl,bbr,bbl,cmdhack
	
	def setServo(self,number,angle):
		vals=[]
		vals.extend(split_uinteger_8(number))
		vals.extend(split_uinteger_8(angle))
		self.writeBlock(self.i2c_registers['REG_SETSERVO'],vals)
	
	def ratatouille(self,run,delay_ms):
		vals=[]
		vals.extend(split_bool_8(run))
		vals.extend(split_uinteger_32(delay_ms))
		self.writeBlock(self.i2c_registers['REG_RATATOUILLE'],vals)
	
	def launchNet(self,left,right,reset):
		vals=[]
		vals.extend(split_bool_8(left))
		vals.extend(split_bool_8(right))
		vals.extend(split_bool_8(reset))
		self.writeBlock(self.i2c_registers['REG_LAUNCHNET'],vals)
	
	def setTickRatio(self,new_ticks_per_meters,new_ticks_per_rads):
		vals=[]
		vals.extend(split_double_32(new_ticks_per_meters))
		vals.extend(split_double_32(new_ticks_per_rads))
		self.writeBlock(self.i2c_registers['REG_SETTICKRATIO'],vals)
	
	def setBras(self,left,right):
		vals=[]
		vals.extend(split_integer_8(left))
		vals.extend(split_integer_8(right))
		self.writeBlock(self.i2c_registers['REG_SETBRAS'],vals)
	
	