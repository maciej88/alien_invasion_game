class GameStats:
    #ingame statistic
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_starts(self):
        self.ships_left = self.settings.ship_limit