import pygame

from entities.entity import Entity


class Apple(Entity):
    red = pygame.Color(133, 0, 0)

    def __init__(self, grid, location):
        super().__init__(grid, location, self.red, "apple")

    def draw(self, screen):
        y, x = self.loc.row * self.grid.block_size, self.loc.col * self.grid.block_size
        center = x + self.grid.block_size / 2, y + self.grid.block_size / 2
        radius = self.grid.block_size / 2 * 0.8
        pygame.draw.circle(screen, self.color, center, radius)
