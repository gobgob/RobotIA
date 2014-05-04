
from math import *

def ClosestEquivalentAngle(old_angle,new_angle):
	if new_angle<=old_angle :
		while (not (old_angle-pi<=new_angle and new_angle<old_angle+pi)):
			new_angle+=2*pi
		return new_angle
	else:
		while (not (old_angle-pi<=new_angle and new_angle<old_angle+pi)):
			new_angle-=2*pi
		return new_angle;

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

def split_integer_16(x):
	splitted = []
	splitted.append(0xFF&(x>>16))
	splitted.append(0xFF&(x>>8))
	splitted.append(0xFF&(x>>0))
	return splitted;

def split_integer_8(x):
	splitted = []
	splitted.append(0xFF&(x>>16))
	splitted.append(0xFF&(x>>8))
	splitted.append(0xFF&(x>>0))
	return splitted;