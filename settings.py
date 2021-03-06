class Settings:
    """class keeping all settings for game"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (56, 34, 141)

        self.ship_limit = 3

        #bullets stettings:
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 128, 0)
        self.bullets_allowed = 5

        self.fleet_drop_speed = 10

        self.alien_points = 30
        self.score_scale = 1.5

        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """dynamic settings for lvl updates"""

        self.bullet_speed = 1.5
        self.ship_speed = 1.5
        self.alien_speed = 1.0

        self.fleet_direction = 1 #  1 in right -1 in left

    def increase_speed(self):
        """speed up after lvl up"""

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)