from math import *
from class_robot import *
from class_point import *
from class_circular import *

class Route():
	points=None
	dist=0

	def __init__(self):
		self.points=[]

class Highway():

	points=CircularList(
		[
		Point(415,-1000,"A"),
		Point(415,-750, "B"),
		Point(415,-500, "C"),
		Point(415,-250, "D"),
		Point(415,+000, "E"),
		Point(415,+250, "F"),
		Point(415,+500, "G"),
		Point(415,+750, "H"),
		# Point(500,+1000,"I"),

		Point(750, +1000,"J"),
		Point(1000,+1000,"K"),
		Point(1250,+1000,"L"),
		# Point(1500,+1000,"M"),

		Point(1500,+750, "N"),
		Point(1500,+500, "O"),
		Point(1500,+250, "P"),
		Point(1500,+000, "Q"),
		Point(1500,-250, "R"),
		Point(1500,-500, "S"),
		Point(1500,-750, "T"),
		# Point(1500,-1000,"U"),

		Point(1500,-1000,"V"),
		Point(1250,-1000,"W"),
		Point(1000,-1000,"X"),
		Point(750, -1000,"Y"),
		]
		)
	

	def findClosest(self,source):
		minDist=9999999
		for point in self.points:
			dist=self.dist(source,point)
			if (dist<minDist):
				minDist=dist
				res=point
		return res

	def dist(self,a,b):
		return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y))

	def findRoute(self,src,dest):
		start = self.findClosest(src)
		end = self.findClosest(dest)

		print("start at "+start.name)
		print("end at "+end.name)

		route1=Route()
		route2=Route()

		index = self.points.index(start)-1
		while self.points[index+1]!=end :
			route1.points.append(self.points[index+1])
			index+=1
		route1.points.append(self.points[index+1])

		index = self.points.index(start)+1
		while self.points[index-1]!=end :
			route2.points.append(self.points[index-1])
			index-=1
		route2.points.append(self.points[index-1])

		for i in range(0,len(route1.points)-1):
			route1.dist+=self.dist(route1.points[i],route1.points[i+1])

		for i in range(0,len(route2.points)-1):
			route2.dist+=self.dist(route2.points[i],route2.points[i+1])

		if route2.dist<route1.dist:
			return route2,route1
		else:
			return route1,route2
