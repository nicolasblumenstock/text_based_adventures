# import hero and goblin classes from their respective files
from hero import Hero
from goblin import Goblin

the_hero = Hero("Aragon")
the_goblin = Goblin()


while the_goblin.health > 0 and the_hero.is_alive():
	print "You have %d health and %d power." % (the_hero.health, the_hero.power)
	print "The goblin has %d health and %d power." % (the_goblin.health, the_goblin.power)
	print "What do you want to do?"
	print "1. fight goblin"
	print "2. do nothing"
	print "3. flee"
	print "> ",
	
	user_input = raw_input()

	if (user_input == "1"):
		the_goblin.health -= the_hero.power
		print "You have done %d damage to the goblin." % the_hero.power
		if the_goblin.health <= 0:
			print "You have defeated the goblin! ggez"		
	elif (user_input == "2"):
		pass
	elif (user_input == "3"):
		print "Goodbye, coward"
		break
	else:
		print "Invalid input %s" % user_input
	if the_goblin.health > 0:
		the_hero.health -= the_goblin.power
		print "Ho noes! You've taken %d from the goblin!" % the_goblin.power
		if the_hero.health <= 0:
			print "You've been killed by the goblin. gitgud"
	if the_hero.health > 0  and the_hero.health < 5:
		print "You have gone into a rage. Your power has increased!"
		the_hero.power += 5