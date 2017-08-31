class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
								"I don't want to get sued",
								"So I'll stop right there."])

bulls_on_parade = Song(["They rally around tha family",
									"With pockets full of shells"])

youre_welcome = Song(["Hey, it's okay, it's okay, you're welcome",
									"For the tide, the sun, the sky"])

testify = Song(["Who controls the past now, controls the future",
						"Who controls the present now, controls the past"])
									
balls = "ballas ballas ballas ballas"

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

youre_welcome.sing_me_a_song()

testify.sing_me_a_song()

end_one = Song([balls])

end_one.sing_me_a_song()