import pygame
from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, grid, location, color, name):
        self.grid = grid
        self.loc = location
        self.color = color
        self.name = name

    def remove(self):
        self.grid.remove_entity(self.loc)

    @abstractmethod
    def draw(self, screen):
        pass


class BackgroundEntity(Entity):
    def __init__(self, grid, location, color):
        super().__init__(grid, location, color, "background")

    def draw(self, screen):
        y, x = self.loc.row * self.grid.block_size, self.loc.col * self.grid.block_size
        rect = pygame.Rect(x, y, self.grid.block_size, self.grid.block_size)
        pygame.draw.rect(screen, self.color, rect)





