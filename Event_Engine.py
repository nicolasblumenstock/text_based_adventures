from random import randint
import time
import Monster
from Royksopp import Royksopp
from West import West
from Blahblahblah import Blahblahblah

class Event_Engine(object):
	def salutations(self,who):
		while who.greeted == False:
			print "````````````````````````````````````````-+yysooo+++/:::--...````````````````````````````````````````"
			print "`````````````````````````````````````./yhhys/--::://++ooosshd/``````````````````````````````````````"
			print "``````````````````````````````````.:shhysssss:.....------/ossd/`````````````````````````````````````"
			print "````````````````````````````````-shhsooooo+++/:-----..:+ossy/-d:````````````````````````````````````"
			print "``````````````````````````````.odhyo-.`````````-...-/osssssh-`:d:```````````````````````````````````"
			print "````````````````````````````.+dhysssyo/.`````...::+syysssssh```:d-``````````````````````````````````"
			print "```````````````````````````:hdysssssssyyo::::-:::+o//+oosssy````/d-`````````````````````````````````"
			print "`````````````````````````-ydysssssssssys-.........:+-.....-o`````+d.````````````````````````````````"
			print "````````````````````````+dyssssssssssyo.......-----:s:.....-/````-od.```````````````````````````````"
			print "`````````````````````-+sm:..--::/++oyy//+++ooosssyssh-.-....+```.-.sh..+o/-.````````````````````````"
			print "``````````````````./hdsos........../ysssssssssssssssy```.-..:/``-...hddoohhhy/``````````````````````"
			print "````````````````.+dho+++o-..::...-oysyyssssssssssssy+````.:-.o`-....+ooyhhys:oy`````````````````````"
			print "`````````````.oyyh/y+++++o+oooo++o+ssosyyyyshyysyyyh++/:/ooo+/::-...-y+++oys/`m-````````````````````"
			print "````````````.do..s+y++++++++++++++++++++ososoo++++oo+++++++++oyoo++o/s++++++syN/````````````````````"
			print "````````````hs`.syho+++++++++++++++++++++s.o.-+s++++++++++++++++++++++++++++++ohh/``````````````````"
			print "````````````+dsydy+++++++++++++++++++++++y/+-``-s++++++++++++++++++++++++++++++++hd/````````````````"
			print "````````````hdyo++++++++++++++++++++++++++y+s/.`o++++++++++++++++++++++++++oooo+++ohh-``````````````"
			print "```````````-No+++++++++++++++++++++++++++++hdhyyy++++++++++++++++++++++++++y/++o++++sm+`````````````"
			print "```````````+m++++++++++++++++++++++++++++++++oss+++++++++++++++++++++++++++s/+/h++++++hh.```````````"
			print "```````````od++++++++++++++ The Adventures of Brave Sir Knight +++++++++++++yddy+++++++ym:``````````"
			print "```````````:N+++++++++++++++++++++++++++++++++++++++++++++++++++oo++++s+++++++o+++++++++ym.`````````"
			print "``````````-omy+oo+++++++++++++++++++++++++++ooo++++oo++++oooo++++oso++oss++++++++++++++++No`````````"
			print "`````````:msossNNd++++++++++++++++++++++++++mNm++s++oss+++++oss++++os+++oyyyyyyyyyyyh++++ms`````````"
			print "`````````sd+++shyo++++++++++++++++++++++++++sysoso++++oso+++++so++++y+++oN/-.....--ym++++N+`````````"
			print "`````````:ms+++oso+++++++++++++++++++++++++++shys+++++++y++++oyo++sho+oydo```````.sdo+++hd``````````"
			print "``````````-yhso+omho+++++++++++++++++++++++shyMs+++oosydhssyhhhyyyshhhs/.```````:hh+++ohh.``````````"
			print "````````````-/syyo:syso+++++++++++++++++oyy+-`shyyysso:-/o+/-.---.``..````````.shs++ohh+.```````````"
			print "````````````````````-/syyssoo++++++oosyys:.`````.`````````````````````````````/myyyys/.`````````````"
			print "```````````````````````.-/+ossyyyyso+/-.```````````````````````````````````````-:-.`````````````````"
			time.sleep(2)
			print "Oh, hello there! Welcome to Magifantasilan, Brave Sir... wait."
			time.sleep(1)
			who.name = raw_input("What is your name, Brave Sir Knight? ")
			print "Ah, yes. Yes. Brave Sir %s" % who.name
			who.greeted = True


	def crossroads(self,who,where):
		print "You've come upon a strange crossroads. Each path leading you to a different land."
		time.sleep(1)
		print "North will take you to Royksopp."
		time.sleep(1)
		print "West to the West."
		time.sleep(1)
		print "And lastly, East to uh, Blahblahblah."
		time.sleep(1)
		decision = raw_input("Which way will you go? ")
		if (decision.upper() == "ROYKSOPP" or decision.upper() == "NORTH"):
			where.append(Royksopp())
		elif (decision.upper() == "WEST"):
			where.append(West())
		elif (decision.upper() == "BLAHBLAHBLAH" or decision.upper() == "EAST"):
			where.append(Blahblahblah())
		else:
			print "What?"
		print "So begins the tale of Brave Sir %s heading to %s" % (who.name, where[0].name)

	def battle(self,who,what,where):
		print "You turn towards the noise from behind."
		random_chance = randint(1,100)
		if (random_chance <= 95):
			number_of_enemies = randint(0, 6)
			print "Brave Sir %s finds %d monsters!" % (who.name, number_of_enemies)	
			for i in range(0, number_of_enemies):
				rand_num = randint(0,len(where[0].monster_types) - 1)
				if (where[0].monster_types[rand_num] == 'goblin'):
					what.append(Monster.Goblin())
				elif (where[0].monster_types[rand_num] == 'vampire'):
					what.append(Monster.Vampire())			
				elif (where[0].monster_types[rand_num] == 'rabbit'):
					what.append(Monster.Rabbit())
				elif (where[0].monster_types[rand_num] == 'zombie'):
					what.append(Monster.Zombie())
				elif (where[0].monster_types[rand_num] == 'bear'):
					what.append(Monster.Bear())
				elif (where[0].monster_types[rand_num] == 'wolf'):
					what.append(Monster.Wolf())								
				elif (where[0].monster_types[rand_num] == 'yeti'):
					what.append(Monster.Yeti())
				elif (where[0].monster_types[rand_num] == 'unicorn'):
					what.append(Monster.Unicorn())
				elif (where[0].monster_types[rand_num] == 'dragon'):
					what.append(Monster.Dragon())
		else:
			if (where[0].legendary[0] == 'ogre'):
				what.append(Monster.Ogre())
			elif (where[0].legendary[0] == 'jabberwocky'):
				what.append(Monster.Jabberwocky())
			else:
				what.append(Monster.Crystal_Lizard())

		for enemy in what:
			while enemy.is_alive() and who.is_alive():
				print "* * * * * * * * * * * * * * * * *"
				print "   %s wants to devour you!" % (enemy.name)
				print "* * * * * * * * * * * * * * * * *"
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