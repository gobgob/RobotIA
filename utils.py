
from math import *
import struct

def ClosestEquivalentAngle(old_angle,new_angle):
	if new_angle<=old_angle :
		while (not (old_angle-pi<=new_angle and new_angle<old_angle+pi)):
			new_angle+=2*pi
		return new_angle
	else:
		while (not (old_angle-pi<=new_angle and new_angle<old_angle+pi)):
			new_angle-=2*pi
		return new_angle;


def split_double_32(x):
	return split_integer_32(int(x*100000))

def make_double_32(vals,offset):
	return make_integer_32(vals,offset)/100000

def split_integer_32(x):
	return struct.pack('>i', int(x))[:4]

def split_uinteger_32(x):
	return struct.pack('>I', int(x))[:4]

def make_integer_32(vals,offset):
	return struct.unpack('>i', bytes(vals[offset:offset+4]))[0]

# def split_integer_16(x):
# 	splitted = []
# 	splitted.append(0xFF&(x>>8))
# 	splitted.append(0xFF&(x>>0))
# 	return splitted;

def split_integer_8(x):
	return struct.pack('>b', int(x))[:1]

def make_integer_8(vals,offset):
	return struct.unpack('>h', bytes(vals[offset:offset+1]))[0]

def make_bool_8(vals,offset):
	return struct.unpack('>?', bytes(vals[offset:offset+1]))[0]

def split_bool_8(x):
	return struct.pack('>?', int(x))[:1]