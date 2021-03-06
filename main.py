import sys

import pygame

from entities.edible import Apple
from entities.wall import Wall
from grid import Grid, Location
from entities.snake import Snake

W_SIZE = W_WIDTH, W_HEIGHT = 1280, 720
GAME_TITLE = "Snake Game by Palgorithms"

pygame.init()

# Create screen
screen = pygame.display.set_mode(W_SIZE)
pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.Clock()

# Create Grid
BLOCK_SIZE = 25
num_rows = W_HEIGHT // BLOCK_SIZE
num_cols = W_WIDTH // BLOCK_SIZE
grid = Grid(screen, num_rows, num_cols, BLOCK_SIZE)

# Create snake
snake = Snake(grid)

# Add apples
apples = []
for i in range(100):
    apple = Apple(grid, Location(*grid.random_cell()))
    grid.add_entity(apple)
    apples.append(apple)

#Add walls
    wall = []
for i in range(30):
    wall = Wall(grid, Location(*grid.random_cell()))
    grid.add_entity(wall)
    apples.append(wall)
    
def scoreBoard(score):
    font = pygame.font.Font('font/Pixeltype.ttf', 50)
    text = font.render('Score: ' + str(score), True, 'White')
    screen.blit(text, (10, 10))

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.curr_direction != Grid.right:
                snake.move_left()
            elif event.key == pygame.K_RIGHT and snake.curr_direction != Grid.left:
                snake.move_right()
            elif event.key == pygame.K_UP and snake.curr_direction != Grid.down:
                snake.move_up()
            elif event.key == pygame.K_DOWN and snake.curr_direction != Grid.up:
                snake.move_down()

    snake.move_forward()
    grid.draw()
    pygame.display.flip()
    scoreBoard(grid.score)
    pygame.display.update()

    clock.tick(15)
