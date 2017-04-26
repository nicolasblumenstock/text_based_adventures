# import hero and goblin classes from their respective files
from Event_Engine import Event_Engine
from hero import Hero
from goblin import Goblin
from vampire import Vampire
from Royksopp import Royksopp
from West import West
from Blahblahblah import Blahblahblah
from Region import Region

# **-------- Variables --------**
monsters = []
the_hero = Hero()
events = Event_Engine()
game_on = True
region = []

# ** ---- GAME START ---- **
while game_on:
	
	events.salutations(the_hero)

	if (the_hero.greeted == True):
		events.crossroads(the_hero,region)
		print region[0].name

	if (region[0].name != 'home'):
		events.battle(the_hero,monsters,region)

	keep_playing = raw_input("Would you like to keep going? ")

	if (keep_playing.upper() == "YES" and keep_playing.upper == "Y"):
		game_on = False
	else:
		game_on = False



# while the_hero.is_alive():
# 	if the_hero.greeted == False:		
# 		events.salutations(the_hero)
# 	else:
# 		random_battles.fight(the_hero,monsters)








