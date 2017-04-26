class Hero(object):
	def __init__(self,name = "Robin"):
		self.name = name
		self.health = 10
		self.power = 5
		self.max_health = 10
		self.xp = 0
		self.level = 1
		# self.turns = 1
		self.greeted = False
		# self.weapon = 
		# self.armor = 
		# self.gold = 
		# self.item = 

	def cheer_hero(self):
		print "Fight hard, %s!" % self.name

	def is_alive(self):
		# if (self.health > 0):
		# 	return True
		# else:
		# 	return False
		return self.health > 0
	
	def attack(self,who_to_attack):
		who_to_attack.health -= self.power

	def increase_health(self,amount):
		self.health += amount
		if self.health > self.max_health:
			self.health = self.max_health

	def check_level(self):
		if self.xp > 3 and self.level < 2:
			self.level = 2
			self.level_up()


	def level_up(self):
		self.max_health += 10
		self.health = self.max_health
		self.power += 5
		print "Thou hast leveled up to Level %s, %s! Thy HP is now %s and thy power is %s" % (self.level, self.name, self.max_health, self.power)
