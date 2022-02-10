import pygame


class Entity:
    def __init__(self, location,  color, name):
        self.loc = location
        self.color = color
        self.name = name

class Location:

    def __init__(self,  row, col):
        self.row = row
        self.col = col

    @staticmethod
    def add(loc_a, loc_b):
        return Location(loc_a.row + loc_b.row, loc_a.col + loc_b.col)



class Grid:
    grey = pygame.Color(169, 169, 169)
    white = pygame.Color(190, 190, 190)

    grid_color = grey, white

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

        count = 0
        for r in range(self.num_rows):
            count += 1
            for c in range(self.num_cols):
                color = Grid.white if count % 2 == 0 else Grid.grey
                loc = Location(r, c)
                entity = Entity(loc, color, None)
                self.matrix[r][c] = entity

                count += 1


    def draw(self):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self.draw_entity(self.matrix[r][c])

    def draw_entity(self, entity):
        x, y = entity.loc.row * self.block_size, entity.loc.col * self.block_size
        rect = pygame.Rect(x, y, self.block_size, self.block_size)
        pygame.draw.rect(self.screen, entity.color, rect)

    def in_bounds(self, loc):
        return 0 <= loc.row < self.num_rows and 0 <= loc.col < self.num_cols

    def is_empty(self, loc):
        return self.get_entity(loc).name is None

    def get_entity(self, loc):
        return self.matrix[loc.row][loc.col]