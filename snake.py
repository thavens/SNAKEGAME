from grid import Grid, Location, Entity
import pygame


class Snake:
    orange = pygame.Color(255, 165, 0)
    green = pygame.Color(0, 255, 100)
    colors = (orange, green)

    def __init__(self, grid):
        self.body = []
        self.curr_direction = Grid.down
        self.grid = grid
        self.head_color = 0

        self.init_snake()



    def init_snake(self):
        for i in range(20):
            self.add_part(Location(i, 0))

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
        self.add_part(new_loc)
        self.remove_tail()

    def remove_tail(self):
        self.grid.remove_entity(self.body.pop())

    def add_part(self, loc):
        self.body.insert(0, loc)
        self.head_color = (self.head_color + 1) % len(self.colors)

        entity = Entity(loc, self.colors[self.head_color], "snake part")
        self.grid.add_entity(entity)

