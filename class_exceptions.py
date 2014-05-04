class Blocage(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class Timeout(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class EndOfGame(Exception):
	pass

class Obstacle(Exception):
	pass