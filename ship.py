import pygame


class Ship:
    """Ship in game window"""

    def __init__(self, ai_game):  # ai_game reference to AlienInvasion

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()  # rect as rectangle

        self.rect.midbottom = self.screen_rect.midbottom  # in middle of bottom window

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        # ship view
        self.screen.blit(self.image, self.rect)
