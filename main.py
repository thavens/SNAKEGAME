import pygame
from grid import Grid

W_SIZE = W_HEIGHT, W_WIDTH = 1280, 720
GAME_TITLE = "Snake Game by Palgorithms"


pygame.init()

screen = pygame.display.set_mode(W_SIZE)
pygame.display.set_caption(GAME_TITLE)

grid = Grid(screen)
grid.draw()
pygame.display.flip()

while True:
    for event in pygame.event.get():
        print(event)
