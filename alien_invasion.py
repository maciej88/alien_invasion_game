import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
from bullet import Bullet
from button import Button
from scoreboard import Scoreboard


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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self._create_fleet()

        #play buttonn
        self.play_button = Button(self, "Play")

    def run_game(self):  # main loop and game
        while True:
            self._check_events()

            if self.stats.game_active:
                self._update_bullets()
                self._update_aliens()
                self.ship.update()
            self._update_screen()

    def _check_events(self):
        # reactions on mouse and keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # movements:
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

            self.screen.fill(self.settings.bg_color)  # background color refresh
            self.ship.blitme()  # show ship

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.midbottom_ship()

            self.settings.initialize_dynamic_settings()

            pygame.mouse.set_visible(False)

            #points reset
            self.sb.prep_score()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        avilable_space_y = (
                self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = avilable_space_y // (2 * alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens): #crash detection
            self._ship_hit()

        self._check_aliens_bottom()

    def _ship_hit(self):
        if self.stats.ships_left > 0:

            self.stats.ships_left -= 1

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.midbottom_ship()

            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
        
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():  # bullets out of border delete
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        self._update_screen()

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #points score
        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()  # last modified window (view)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
