import sys

import pygame
from grid import Grid
from snake import Snake

W_SIZE = W_HEIGHT, W_WIDTH = 1280, 720
GAME_TITLE = "Snake Game by Palgorithms"


pygame.init()

# Create screen
screen = pygame.display.set_mode(W_SIZE)
pygame.display.set_caption(GAME_TITLE)

# Create Grid
BLOCK_SIZE = 20
num_rows = W_HEIGHT // BLOCK_SIZE
num_cols = W_WIDTH // BLOCK_SIZE
grid = Grid(screen, num_rows, num_cols, BLOCK_SIZE)

snake = Snake()
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        grid.draw()
        pygame.display.flip()