from random import randint
import Monster
import time

class Battle_Engine(object):
	def fight(self,who,what,where):
		print "You turn towards the noise from behind."
		random_chance = randint(1,100)
		if (random_chance <= 95):
			number_of_enemies = randint(0, 6)
			print "Brave Sir %s finds %d monsters!" % (who.name, number_of_enemies)	
			for i in range(0, number_of_enemies):
				rand_num = randint(0,len(where.monster_types) - 1)
				if (where.monster_types[rand_num] == 'goblin'):
					what.append(Monster.Goblin())
				elif (where.monster_types[rand_num] == 'vampire'):
					what.append(Monster.Vampire())			
				elif (where.monster_types[rand_num] == 'rabbit'):
					what.append(Monster.Rabbit())
				elif (where.monster_types[rand_num] == 'zombie'):
					what.append(Monster.Zombie())
				elif (where.monster_types[rand_num] == 'bear'):
					what.append(Monster.Bear())
				elif (where.monster_types[rand_num] == 'wolf'):
					what.append(Monster.Wolf())								
				elif (where.monster_types[rand_num] == 'yeti'):
					what.append(Monster.Yeti())
				elif (where.monster_types[rand_num] == 'unicorn'):
					what.append(Monster.Unicorn())
				elif (where.monster_types[rand_num] == 'dragon'):
					what.append(Monster.Dragon())
		else:
			if (where.legendary[0] == 'ogre'):
				what.append(Monster.Ogre())
			elif (where.legendary[0] == 'jabberwocky'):
				what.append(Monster.Jabberwocky())
			else:
				what.append(Monster.Crystal_Lizard())

		for enemy in what:
			print "* * * * * * * * * * * * * * * * *"
			print "   %s wants to devour you!" % (enemy.name)
			print "* * * * * * * * * * * * * * * * *"

			while enemy.is_alive() and who.is_alive():
				print "You have %d health and %d power." % (who.health, who.power)
				print "The %s has %d health and %d power." % (enemy.name, enemy.health, enemy.power)
				time.sleep(1)
				print "What do you want to do?"
				print "1. fight %s" % enemy.name
				print "2. do nothing"
				print "3. Drink a Potion of Healing"
				print "4. flee"
				print "> ",

				user_input = raw_input()

				# if (user_input == "1" and who.turns > 0):
				if (user_input == "1"):
					enemy.take_damage(who.power)
					print "You have done %d damage to the %s." % (who.power, enemy.name)
					# who.turns -= 1

				# elif (user_input == "2" and who.turns > 0):
				elif (user_input == "2"):
					# who.turns -= 1
					pass

				elif (user_input == "4"):
					print "And there goes Brave Sir %s!" % who.name
					break

				# elif (user_input == "3" and who.turns > 0):
				elif (user_input == "3"):
					who.increase_health(20)
					# who.turns -= 1

				elif (user_input != "1" or user_input != "2" or user_input != "3" or user_input != "4"):
					print "Invalid input %s" % user_input

				if who.health <= 0:
					print "You've been killed by the %s. gitgud" % enemy.name

				if who.health > 0  and who.health <= 5 and enemy.is_alive():
					print "You have gone into a rage. Your power has increased!"
					who.power += 5
				# who.turns = 2
				
				if (enemy.health > 0):
					who.health -= enemy.power
					print "Ho noes! You've taken %d from the %s!" % (enemy.power, enemy.name)
					# who.turns = 1
					if who.health <= 0:
						print "You've been killed by the %s. gitgud" % enemy.name

				if enemy.health <= 0:
					print "You have defeated the %s! ggez" % enemy.name
					who.xp += enemy.xp_value
					print "You've gained %s experience points!" % enemy.xp_value
					who.check_level()
					# who.turns = 1					