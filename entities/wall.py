from abc import ABC

import pygame

from entities.entity import Entity


class ImmovableEntity(Entity, ABC):
    pass

class Wall(ImmovableEntity):
    wall_color = pygame.Color(0, 0, 0)

    def __init__(self, grid, location):
        super().__init__(grid, location, Wall.wall_color, "wall")

    def draw(self, screen):
        y, x = self.loc.row * self.grid.block_size, self.loc.col * self.grid.block_size
        rect = pygame.Rect(x, y, self.grid.block_size, self.grid.block_size)
        pygame.draw.rect(screen, self.color, rect)