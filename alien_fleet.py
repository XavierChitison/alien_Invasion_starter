import pygame
from typing import TYPE_CHECKING

from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    
   

class AlienFleet: 
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.aliens = pygame.sprite.Group()  # Group to hold all aliens in the fleet
        self.fleet_direction = self.settings.fleet_direction  # 1 for right, -1 for left
        self.fleet_drop_speed = self.settings.fleet_drop_speed  # Speed at which the fleet drops down

        self.create_fleet()  # Create the initial fleet of aliens

    def create_fleet(self):
        alien_width = self.settings.alien_width
        screen_width = self.screen.get_rect().width

        
        fleet_width = self.calculate_fleet_size(alien_width, screen_width)
        fleet_horizontal_spacing = fleet_width * alien_width
        x_offset = int((screen_width - fleet_horizontal_spacing) // 2)

        for col in range(fleet_width):
            current_x = alien_width * col + x_offset
            if col % 2 == 0:
                continue
            self.create_alien(current_x, 10)  # 10 is the y-coordinate for the top row of aliens


    def calculate_fleet_size(self, alien_width, screen_width):
        fleet_width = (screen_width//alien_width)

        if fleet_width % 2 == 0:
            fleet_width -= 1  
        else:
            fleet_width -= 2 
        return fleet_width


    def create_alien(self, current_x: int, current_y: int):
        new_alien = Alien(self.game, current_x, current_y)
        self.aliens.add(new_alien)


    def draw(self):
        alien: 'Alien'
        for alien in self.aliens:
            alien.draw_alien()
