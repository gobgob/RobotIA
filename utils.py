
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
