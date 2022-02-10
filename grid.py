import pygame
class Grid:

    grey = pygame.Color(169,169,169)
    white = pygame.Color(255,255,255)

    def __init__(self, screen):
        self.screen = screen
        self.block_size = 15

        self.num_rows = screen.get_size()[0] // self.block_size
        self.num_cols = screen.get_size()[1] // self.block_size

    def draw(self):
        count = 0
        for r in range(self.num_rows):
            count += 1
            for c in range(self.num_cols):
                x, y = r * self.block_size, c * self.block_size
                color = Grid.white if count % 2 == 0 else Grid.grey
                rect = pygame.Rect(x, y, self.block_size, self.block_size)
                pygame.draw.rect(self.screen, color, rect)

                count += 1



