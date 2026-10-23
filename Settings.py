from pathlib import Path


class Settings:

    def __init__(self):
        self.name: str = "Alien Invasion"
        self.screen_width: int = 1200
        self.screen_height: int = 800
        self.FPS: int = 60
        self.bg_file = Path(__file__).resolve().parent / 'Assets' / 'images' / 'Starbasesnow.png'

        self.ship_file = Path(__file__).resolve().parent / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_width: int = 100
        self.ship_height: int = 100
        self.ship_speed: int = 5
        self.ship_lives: int = 3

        self.bullet_file = Path(__file__).resolve().parent / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path(__file__).resolve().parent / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path(__file__).resolve().parent / 'Assets' / 'sound' / 'impactSound.mp3'
        self.bullet_width: int = 25
        self.bullet_height: int = 80
        self.bullet_amount: int = 5
        self.bullet_speed: int = 7
        self.bullets_allowed: int = 5

        self.alien_file = Path(__file__).resolve().parent / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_width: int = 40
        self.alien_height: int = 40
        self.fleet_speed: int = 1
        self.fleet_direction: int = 1  # 1 represents right; -1 represents left
        self.fleet_drop_speed: int = 20  # Speed at which the fleet drops down when it hits an edge
