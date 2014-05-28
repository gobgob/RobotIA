
from class_robot import *
from class_highway import *
from class_point import *

class Strategy:
	"""The Strategie class !"""

	robot=None
	table=None
	highway = Highway()

	def __init__(self,robot):
		self.robot=robot
		self.table=robot.table

	def takeTheHighway(self,x,y):
		print("taking the highway !")
		highway = self.highway
		robot=self.robot
		dest = Point(x,y)
		src = Point(robot.getX(),robot.getY())
		route1, route2 = highway.findRoute(src,dest)
		for pt in route1.points:
			print("Going to "+pt.name+" "+str(pt.x) + " "+str(pt.y))
			robot.goto(pt.x,pt.y,autocolor=True) 
