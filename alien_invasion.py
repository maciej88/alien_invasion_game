import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Game initialization class"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("ALIEN INVASION!!!")

        self.ship = Ship(self)

    def run_game(self):  # main loop and game
        while True:
            self._check_events()

    def _check_events(self):
        #reactions on mouse and keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            self.screen.fill(self.settings.bg_color)  # background color refresh
            self.ship.blitme() #show ship

            pygame.display.flip()  # last modified window (view)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
