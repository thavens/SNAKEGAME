import pygame
import sys


#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)

class Button:
    def __init__(self, screen, font, size, color, x, y, width, height, text):
        self.screen = screen
        self.font = pygame.font.Font(font, size)
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        

    def draw_button(self, outline = None):
        if outline:
            pygame.draw.rect(self.screen, outline, (self.x - 2, self.y - 2, self.width/3 + 4, self.height/3 + 4), 0)

        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width/3, self.height/3), 0)

        if self.text != '':
            text = self.font.render(self.text, True, 'White')
            self.screen.blit(text, (self.x , self.y))


    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width/3:
            if pos[1] > self.y and pos[1] < self.y + self.height/3:
                return True

        return False

    

W_SIZE = W_WIDTH, W_HEIGHT = 1280, 720
GAME_TITLE = "Snake Game by Palgorithms"
#font_path = os.path.abspath("SNAKEGAME/Pixeltype.ttf")

pygame.init()

# Create screen
screen = pygame.display.set_mode(W_SIZE)
pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.Clock()

# Create Menu

start_button = Button(screen, 'font/Pixeltype.ttf', 50, BLACK, 575, 350, W_WIDTH / 2 - 200, W_HEIGHT / 2 - 100, "Start")
quit_button = Button(screen, 'font/Pixeltype.ttf', 50, BLACK, 575, 425, W_WIDTH / 2 - 200, W_HEIGHT / 2 - 100, "Quit")
menu_button = Button(screen, 'font/Pixeltype.ttf', 50, BLACK, 575, 350, W_WIDTH / 2 - 200, W_HEIGHT / 2 - 100, "Menu")
retry_button = Button(screen, 'font/Pixeltype.ttf', 50, BLACK, 575, 500, W_WIDTH / 2 - 200, W_HEIGHT / 2 - 100, "Retry")

# # Menu Stuff
# font = pygame.font.Font(font_path, 50)
# start_text = font.render('Start', True, 'White')
# quit_text = font.render('Quit', True, 'White')
# light_color = (170, 170, 170)
# width = screen.get_width()
# height = screen.get_height()


# text_surface = font.render('Palgorithm Winter 2022 Snake Game', False, 'White')

# snake_surface = pygame.image.load('SNAKEGAME/snake_palgorithm.png')
# snake_small = pygame.transform.scale(snake_surface, (300, 200))

def redrawMenuWindow():
    screen.fill((0, 0, 0))
    start_button.draw_button((0, 0, 0))
    quit_button.draw_button((0, 0, 0))

def redrawRetryMenu():
    menu_button.draw_button((0, 0, 0))
    quit_button.draw_button((0, 0, 0))
    retry_button.draw_button((0, 0, 0))

game_state = 'menu'
while True:
    if game_state == 'menu':
        redrawMenuWindow()


    pygame.display.update()
    mouse = pygame.mouse.get_pos()
    if game_state == "retry":
        redrawRetryMenu()
    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_state == "menu":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.isOver(mouse):
                        print("Game Started!")
                        game_state = "game"
                    if quit_button.isOver(mouse):
                        pygame.quit()
                        sys.exit()

            if game_state == "retry":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.isOver(mouse):
                        print("Game Started!")
                        game_state = "menu"
                    if quit_button.isOver(mouse):
                        pygame.quit()
                        sys.exit()

                    if retry_button.isOver(mouse):
                        game_state = "game"
                
            if game_state == "game":
                try:
                    import main.py
                except:
                    #game over screen code -- continue, back to menu, quit
                    game_state = "retry"
                    
            if event.type == pygame.MOUSEMOTION:
                    if start_button.isOver(mouse):
                        start_button.color = (105, 105, 105)
                    else:
                        start_button.color = GREEN
                    if quit_button.isOver(mouse):
                        quit_button.color = (105, 105, 105)
                    else:
                        quit_button.color = RED

                    if retry_button.isOver(mouse):
                        retry_button.color = (105, 105, 105)
                    else:
                        retry_button.color = BLUE
                    if menu_button.isOver(mouse):
                        menu_button.color = (105, 105, 105)
                    else:
                        menu_button.color = GREEN
    
    pygame.display.update()
    clock.tick(60)
