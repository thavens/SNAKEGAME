import random
import pygame

from entities.entity import BackgroundEntity


class Location:

    def __init__(self, row, col):
        self.row = row
        self.col = col

    @staticmethod
    def add(loc_a, loc_b):
        return Location(loc_a.row + loc_b.row, loc_a.col + loc_b.col)


class Grid:
    grey = pygame.Color(169, 169, 169)
    white = pygame.Color(190, 190, 190)

    light_green = pygame.Color(140, 180, 69)
    dark_green = pygame.Color(144,203,69)

    grid_color = light_green, dark_green

    up = Location(-1, 0)
    down = Location(1, 0)
    right = Location(0, 1)
    left = Location(0, -1)

    def __init__(self, screen, num_rows, num_cols, block_size):
        self.screen = screen
        self.block_size = block_size

        self.num_rows = num_rows
        self.num_cols = num_cols

        self.init_matrix()
        self.draw()

    def init_matrix(self):
        self.matrix = []
        for r in range(self.num_rows):
            self.matrix.append([None] * self.num_cols)

        self.init_background()

    def init_background(self):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                loc = Location(r, c)
                self.add_entity(BackgroundEntity(self, loc, Grid.get_background_color(loc)))


    def draw(self):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self.matrix[r][c].draw(self.screen)

    def in_bounds(self, loc):
        return 0 <= loc.row < self.num_rows and 0 <= loc.col < self.num_cols

    def dir_out_bounds(self, loc):
        if loc.row < 0:
            return Grid.up
        elif loc.row >= self.num_rows:
            return Grid.down
        elif loc.col < 0:
            return Grid.left
        elif loc.col >= self.num_cols:
            return Grid.right

        raise Exception("location is inbounds")

    def is_empty(self, loc):
        return isinstance(self.get_entity(loc), BackgroundEntity)

    def get_entity(self, loc):
        return self.matrix[loc.row][loc.col]

    def add_entity(self, entity):
        self.matrix[entity.loc.row][entity.loc.col] = entity

    def remove_entity(self, loc):
        self.matrix[loc.row][loc.col] = None
        self.add_entity(BackgroundEntity(self, loc, self.get_background_color(loc)))

    def random_cell(self):
        return random.randrange(0, self.num_rows), random.randrange(0, self.num_cols)

    @staticmethod
    def get_background_color(loc):
        if loc.row % 2 == 0:
            if loc.col % 2 == 0:
                return Grid.grid_color[0]
            else:
                return Grid.grid_color[1]
        else:
            if loc.col % 2 == 1:
                return Grid.grid_color[0]
            else:
                return Grid.grid_color[1]
