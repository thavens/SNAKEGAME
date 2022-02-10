from Entity import SnakeEntity
from grid import Grid, Location, Entity
import pygame



class Snake:
    orange = pygame.Color(173, 72, 5)
    green = pygame.Color(3, 69, 26)
    colors = (orange, green)

    def __init__(self, grid):
        self.body = []
        self.curr_direction = Grid.down
        self.grid = grid
        self.head_color = 0

        self.init_snake()

    def init_snake(self):
        for i in range(30):
            self.add_part(Location(0, i))

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
        new_loc = Location.add(direction, self.body[0].loc)
        if not self.grid.in_bounds(new_loc):
            self.handle_out_of_bounds(new_loc)
        self.add_part(new_loc)
        self.remove_tail()

    def handle_out_of_bounds(self, loc):
        dir = self.grid.dir_out_bounds(loc)
        if dir == Grid.up:
            loc.row = self.grid.num_rows - 1
        elif dir == Grid.down:
            loc.row = 0
        elif dir == Grid.right:
            loc.col = 0
        elif dir == Grid.left:
            loc.col = self.grid.num_cols - 1

    def remove_tail(self):
        self.grid.remove_entity(self.body.pop().loc)

    def add_part(self, loc):
        self.update_head_color()
        color = self.colors[self.head_color]
        # color = helpers.random_color()
        body_part = SnakeEntity(self.grid, loc, color)
        self.body.insert(0, body_part )
        self.grid.add_entity(body_part)

    def update_head_color(self):
        self.head_color = (self.head_color + 1) % len(self.colors)