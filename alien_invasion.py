import sys
import pygame

class AlienInvasion:
    """Game initialization class"""
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("ALIEN INVASION!!!")

        self.bg_color = (0, 0, 255)

    def run_game(self): #main loop and game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color) #background color refresh
            pygame.display.flip() #last modified window (view)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()