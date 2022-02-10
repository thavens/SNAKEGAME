import pygame


class Entity:
    def __init__(self, location, color, name):
        self.loc = location
        self.color = color
        self.name = name


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

        self.init_background()

    def init_background(self):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                loc = Location(r, c)
                self.add_entity(Entity(loc, self.get_background_color(loc), None))

    def add_snake(self, snake):
        count = 0
        for part_loc in snake.body:
            color = snake.colors[0] if count % 2 == 0 else snake.colors[1]
            if not self.in_bounds(part_loc):
                raise Exception("Snake body part out of bounds")
            self.add_entity(Entity(part_loc, color, "snake part"))
            count += 1

    def get_background_color(self, loc):
        # if row is even
        # col is even == colored
        # col is odd == blank
        # if row is odd
        # col is odd == colored
        # col is even = blank
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

    def draw(self):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self.draw_entity(self.matrix[r][c])

    def draw_entity(self, entity):
        y, x = entity.loc.row * self.block_size, entity.loc.col * self.block_size
        rect = pygame.Rect(x, y, self.block_size, self.block_size)
        pygame.draw.rect(self.screen, entity.color, rect)

    def in_bounds(self, loc):
        return 0 <= loc.row < self.num_rows and 0 <= loc.col < self.num_cols

    def is_empty(self, loc):
        return self.get_entity(loc).name is None

    def get_entity(self, loc):
        return self.matrix[loc.row][loc.col]

    def remove_entity(self, loc):
        self.matrix[loc.row][loc.col] = Entity(loc, self.get_background_color(loc), None)

    def add_entity(self, entity):
        self.matrix[entity.loc.row][entity.loc.col] = entity
