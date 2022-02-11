import sys
import pygame

class AlienInvasion:
    """Game initialization class"""
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("ALIEN INVASION!!!")

    def run_game(self): #main loop and game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip() #last modified window (view)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()