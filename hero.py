class Hero(object):
	def __init__(self,name = "Link"):
		self.name = name
		self.health = 10
		self.power = 5

	def cheer_hero(self):
		print "Fight hard, %s!" % self.name

	def is_alive(self):
		if (self.health > 0):
			return True
		else:
			return False