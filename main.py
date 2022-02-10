import sys

import pygame
from grid import Grid
from snake import Snake

W_SIZE = W_WIDTH, W_HEIGHT = 1280, 720
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

print(num_rows, num_cols)
snake = Snake(grid)
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.move_left()
            elif event.key == pygame.K_RIGHT:
                snake.move_right()
            elif event.key == pygame.K_UP:
                snake.move_up()
            elif event.key == pygame.K_DOWN:
                snake.move_down()

        grid.draw()
        pygame.display.flip()