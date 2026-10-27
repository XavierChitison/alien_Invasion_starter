from enum import Enum, auto


class GameState(Enum):
    WAITING = auto()
    PLAYING = auto()
    GAME_OVER = auto()


class GameStats:
    # Track the current game's lives, score, level, and active status.

    def __init__(self, ship_limit):
        self.ship_limit = ship_limit
        self.reset_stats()
        self.state = GameState.WAITING

    @property
    def game_active(self):
        return self.state == GameState.PLAYING

    @property
    def waiting_to_start(self):
        return self.state == GameState.WAITING

    def reset_stats(self):
        self.lives_remaining = self.ship_limit
        self.score = 0
        self.level = 1
        self.state = GameState.PLAYING

    def add_score(self, points):
        if self.game_active:
            self.score += points

    def advance_level(self):
        if self.game_active:
            self.level += 1

    def lose_life(self):
        if not self.game_active:
            return
        if self.lives_remaining > 0:
            self.lives_remaining -= 1
        if self.lives_remaining == 0:
            self.state = GameState.GAME_OVER
