class GameStats:
    # Track the current game's lives, score, level, and active status.

    def __init__(self, ship_limit):
        self.ship_limit = ship_limit
        self.reset_stats()

    def reset_stats(self):
        self.lives_remaining = self.ship_limit
        self.score = 0
        self.level = 1
        self.game_active = True

    def lose_life(self):
        if self.lives_remaining > 0:
            self.lives_remaining -= 1
        if self.lives_remaining == 0:
            self.game_active = False
