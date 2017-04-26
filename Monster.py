class Monster(object):
	def __init__(self,name):
		self.name = name
		# self.health = 10
		# self.power = 2
		# self.xp_value = 5

	def take_damage(self,damage):
		self.health -= damage

	def is_alive(self):
		return self.health > 0

class Vampire(Monster):
	def __init__(self):
		super(Vampire, self).__init__("Wampeer")
		self.health = 12
		self.power = 4
		# self.name = name
		self.xp_value = 10
		# self.gold = gold
		# self.weapon = weapon

class Goblin(Monster):
	def __init__(self,name = "Gob"):
		super(Goblin,self).__init__(name)
		self.health = 6
		self.power = 2
		self.name = name
		self.xp_value = 5
		# self.gold = gold
		# self.weapon = weapon

class Bear(Monster):
	def __init__(self):
		super(Bear,self).__init__("Berr")
		self.health = 15
		self.power = 4
		self.xp_value = 10

class Wolf(Monster):
	def __init__(self):
		super(Wolf,self).__init__("Woof")
		self.health = 7
		self.power = 3
		self.xp_value = 5

class Yeti(Monster):
	def __init__(self):
		super(Yeti,self).__init__("Snowball")
		self.health = 15
		self.power = 6
		self.xp_value = 12

class Crystal_Lizard(Monster):
	def __init__(self):
		super(Crystal_Lizard,self).__init__("Crystal Lizard")
		self.health = 100
		self.power = 0
		self.xp_value = 50

class Ogre(Monster):
	def __init__(self):
		super(Ogre,self).__init__("Ogress")
		self.health = 25
		self.power = 15
		self.xp_value = 20

class Zombie(Monster):
	def __init__(self):
		super(Zombie,self).__init__("Jim")
		self.health = 2
		self.power = 3
		self.xp_value = 1

class Rabbit(Monster):
	def __init__(self):
		super(Rabbit,self).__init__("Rabbit")
		self.health = 1
		self.power = 9000
		self.xp_value = 0

class Unicorn(Monster):
	def __init__(self):
		super(Unicorn,self).__init__("Billy the Unicorn")
		self.health = 10
		self.power = 8
		self.xp_value = 15

class Dragon(Monster):
	def __init__(self):
		super(Dragon,self).__init__("Kalmeet")
		self.health = 20
		self.power = 12
		self.xp_value = 15

class Jabberwocky(Monster):
	def __init__(self):
		super(Jabberwocky,self).__init__("Jabberwocky")
		self.health = 50
		self.power = 25
		self.xp_value = 50
		
