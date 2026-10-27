from pathlib import Path


class Settings:

    def __init__(self):
        # Static settings stay the same as the player advances through levels.
        self.name: str = "Alien Invasion"
        self.screen_width: int = 1200
        self.screen_height: int = 800
        self.FPS: int = 60
        self.font_name = None
        self.hud_height = 88
        self.button_font_size = 40
        self.button_width = 240
        self.button_height = 60
        self.button_color = (25, 90, 140)
        self.button_text_color = (255, 255, 255)
        self.bg_file = Path(__file__).resolve().parent / 'Assets' / 'images' / 'Starbasesnow.png'

        self.ship_file = Path(__file__).resolve().parent / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_width: int = 100
        self.ship_height: int = 100
        self.ship_lives: int = 3

        self.bullet_file = Path(__file__).resolve().parent / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path(__file__).resolve().parent / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path(__file__).resolve().parent / 'Assets' / 'sound' / 'impactSound.mp3'
        self.bullet_width: int = 25
        self.bullet_height: int = 80
        self.bullet_amount: int = 5
        self.bullets_allowed: int = 5

        self.alien_file = Path(__file__).resolve().parent / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_width: int = 40
        self.alien_height: int = 40
        self.speedup_scale: float = 1.1  # Increase movement speeds by 10% per level.

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Set the starting movement values used to tune game difficulty."""
        self.ship_speed: float = 5.0
        self.bullet_speed: float = 7.0
        self.fleet_speed: float = 1.0
        self.fleet_direction: int = 1  # 1 represents right; -1 represents left
        self.fleet_drop_speed: int = 20  # Speed at which the fleet drops down when it hits an edge

    def increase_difficulty(self):
        """Increase movement speeds when the player clears a level."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.fleet_speed *= self.speedup_scale
