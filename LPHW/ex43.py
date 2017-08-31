from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        pass


class Engine(object):
	
	the_bomb = False
	the_weapon = False
	
	def __init__(self, scene_map):
		self.scene_map = scene_map
		#pass
	
	def play(self):
		self.scene_map.opening_scene()
		x = self.scene_map.next_scene('CentralCorridor').enter()
		while x != 'Death':
			x = self.scene_map.next_scene(x).enter()
			raw_input('')
		if x == 'Death':
			self.scene_map.next_scene('Death').enter()

class Death(Scene):

	def enter(self):
		print "\nYou made it to Death."
		exit(0)

class CentralCorridor(Scene):

	def enter(self):
		print "\nYou are in the central corridor of the ship"
		print "There is a passage to the (L)eft or to the (R)ight"
		LorR = raw_input('Which will you choose (L or R)?\n')
		if LorR == 'L' or LorR == 'l':
			return 'LaserWeaponArmory'
		elif LorR == 'R' or LorR == 'r':
			return 'TheBridge'
		else:
			return 'Death'
        #pass

class LaserWeaponArmory(Scene):

	def enter(self):
		print "\nYou made it to the Laser weapon Armory."
		print "There is a keypad that is keeping the armory locked."
		print "Try to (O)pen it or go (B)ack?"
		OorB = raw_input('Which will you choose (O or B)?\n')
		if OorB == 'O' or OorB == 'o':
			guessesLeft = 5
			pin1 = randint(0,9)
			pin2 = randint(0,9)
			pin3 = randint(0,9)
			print "You must guess the 3 number pin on the keypad, pin by pin."
			print "Numbers are between 0-9."
			print "You have 5 guesses for each pin"
			print "After that, the Gothons find you and eat you!\n"
			try1 = self.guess_pin(guessesLeft, pin1, 'first')
			if try1 is True:
				try2 = self.guess_pin(guessesLeft, pin2, 'second')
				if try2 is True:
					try3 = self.guess_pin(guessesLeft, pin3, 'third')
					if try3 is True:
						print "You guessed the password!"
						print "The armory opened up and you grabbed the bomb!"
						print "You decide to take a gun too, because why not?"
						print "You head back to the Central Corridor."
						Engine.the_bomb = True
						Engine.the_weapon = True
						return 'CentralCorridor'
					else:
						return 'Death'
				else:
					return 'Death'
			else:
				return 'Death'
		elif OorB == 'B' or OorB == 'b':
			return 'CentralCorridor'
		else:
			return 'Death'

	def guess_pin(self, guesses, pin, pin_try):
		while guesses is not 0:
			guess1 = int(raw_input('Enter your guess for the %s Pin > ' % (pin_try)))
			print "\n"
			print pin
			if guess1 == pin:
				print "You got it right!\n"
				return True
			else:
				print "Wrong guess! you have %d more tries left!\n" % (guesses-1)
				guesses -= 1
		return False

class TheBridge(Scene):

    def enter(self):
		print "\nYou made it to the Bridge."
		if Engine.the_bomb is True:
			print "You decide to place the bomb here."
			print "As you place the bomb down and activate it.."
			print "You can hear Gothons in the Central Corridor!"
			print "You make a run for the escape pod dock!"
			return 'EscapePod'
		else:
			print "There is a passage. Go (S)traight or go (B)ack?"
			SorB = raw_input('Which will you choose (S or B)?\n')
			if SorB == 'S' or SorB == 's':
				return 'EscapePod'
			elif SorB == 'B' or SorB == 'b':
				return 'CentralCorridor'
			else:
				return 'Death'

class EscapePod(Scene):

    def enter(self):
		print "\nYou made it to the Escape Pod dock."
		print "The door to the escape pods is locked."
		print "Maybe if you had something to blow it up..."
		if Engine.the_weapon is True:
			print "The weapon!"
			print "You decide to use the weapon from the Laser Weapon Armory..."
			print "And it blows a huge hole in the door!"
			print "Hopefully it didn't damage the escape pods!"
			print "There are 3 escape Pods."
			LRM = raw_input('Which escape pod will you take? (L)eft, (R)ight, or (M)iddle?\n')
			if LRM == 'L' or LRM =='l':
				print "You get inside the pod and it's a bit cramped..." 
				raw_input('')
				print "From behind you, you hear a sound.."
				raw_input('')
				print "There's a Gothon inside the pod!"
				raw_input('')
				print "You woke it up and it took a nice bite off your face!!"
				return 'Death'
			elif LRM == 'M' or LRM == 'm':
				print "You get inside the pod and get comfortable."
				raw_input('')
				print "You're ready to go, but you notice a loose wire inside the pod.."
				print "You decide to ignore it as you're pressed for time."
				raw_input('')
				print "You press the \'Take-off\' button..."
				raw_input('')
				print "And the pod explodes! Should've payed attention in circuits class!"
				return 'Death'
			elif LRM == 'R' or LRM == 'r':
				print "You get inside the pod and get comfortable."
				print "Looking outside, you notice the Gothons breaking out of the Central Corridor!"
				print "You hit the \'Take Off\' button!"
				print "The Gothons are on the bridge as you watch them from your escape pod..."
				print "And then..."
				raw_input('')
				print "The bomb goes off!"
				print "Gothon body parts fly all over the place as you successfully escape!"
				print "Congratulations! You made it!"
				exit(0)
			else:
				return 'Death'
		else:
			print "You have no way of getting in, so you decide to go back to the bridge."
			return 'TheBridge'

class Map(object):
	
	scene_select = {
		'Death': Death(),
		'CentralCorridor': CentralCorridor(),
		'LaserWeaponArmory': LaserWeaponArmory(),
		'TheBridge': TheBridge(),
		'EscapePod': EscapePod(),
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
        #pass

	def next_scene(self, scene_name):
		next = Map.scene_select.get(scene_name)
		return next

	def opening_scene(self):
		print "Aliens have invaded a space ship and our hero has"
		print "to go through a maze of rooms defeating them so"
		print "they can escape into an escape pod to the planet below. "
		print "Are you ready to be a hero?\n"
		return self.next_scene(self.start_scene)
        #pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()