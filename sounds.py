import pygame

pygame.mixer.init()

eat_Sound = pygame.mixer.Sound("./Game Music/Eat Sound.wav")
die_Sound = pygame.mixer.Sound("./Game Music/Game Over.wav")
game_Music = pygame.mixer.Sound("./Game Music/Snake_Game.mp3")
hover = pygame.mixer.Sound("./Game Music/hover sound.wav")
click = pygame.mixer.Sound("./Game Music/click sound.wav")

class Sounds:
	def __init__(self):
		pass

	def game_music(self):
		pygame.mixer.music.load(game_Music)
		pygame.mixer.music.play(-1)
		
	def eat(self):
		pygame.mixer.music.load(eat_Sound)
		pygame.mixer.music.play(0)
	
	def die(self):
		pygame.mixer.music.load(die_Sound)
		pygame.mixer.music.play(0)

	def hover(self):
		pygame.mixer.music.load(hover)
		pygame.mixer.music.play(0)

	def click(self):
		pygame.mixer.music.load(click)
		pygame.mixer.music.play(0)

