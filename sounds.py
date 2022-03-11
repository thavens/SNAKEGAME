import pygame

# eat_Sound = pygame.mixer.Sound("./Game Music/Eat Sound.wav")
# die_Sound = pygame.mixer.Sound("./Game Music/Game Over.wav")
# game_Music = pygame.mixer.Sound("./Game Music/Snake_Game.mp3")

# class Sounds:
#     happens = False
#     def __init__(self):
#         pygame.mixer.music.load(game_Music)
#         pygame.mixer.music.play(-1)

#     if happens:
#         pygame.mixer.music.load(eat_Sound)
#         pygame.mixer.music.play(0)

#     if happens:
#         pygame.mixer.music.load(die_Sound)
#         pygame.mixer.music.play(0)

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load('./Snake_Game.mp3')
    pygame.mixer.music.play(-1)
