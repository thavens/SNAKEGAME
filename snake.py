from grid import Grid, Location
import pygame

class Snake:
    orange = pygame.Color(255, 165, 0)
    green = pygame.Color(0, 255, 100)
    colors = (orange, green)
    def __init__(self):
        self.body = []
        self.init_snake()
        self.curr_direction = Grid.down

    def init_snake(self):
        for i in range(20):
            self.body.append(Location(i, 0))



    def move_up(self):
        self.move(Grid.up)

    def move_down(self):
        self.move(Grid.down)

    def move_right(self):
        self.move(Grid.right)

    def move_left(self):
        self.move(Grid.left)

    def move_forward(self):
        self.move(self.curr_direction)

    def move(self, direction):
        self.curr_direction = direction
        new_loc = Location.add(direction, self.body[0])
        self.body.insert(0, new_loc)
        self.remove_tail()

    def remove_tail(self):
        self.body.pop()
