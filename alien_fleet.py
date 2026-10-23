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
        alien_height = self.settings.alien_height
        screen_width = self.screen.get_rect().width
        screen_height = self.screen.get_rect().height

        fleet_width, fleet_height = self.calculate_fleet_size(alien_width, screen_width, alien_height, screen_height)
        x_offset, y_offset = self.calcutate_offsets(alien_width, alien_height, screen_width, screen_height, fleet_width, fleet_height)

        
        self._create_rectangle_fleet(alien_width, alien_height, fleet_width, fleet_height, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_width, alien_height, fleet_width, fleet_height, x_offset, y_offset):
        for row in range(fleet_height):
            for col in range(fleet_width):
                current_x = alien_width * col + x_offset
                current_y = alien_height * row + y_offset
                # Skip every other column to create a staggered effect
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self.create_alien(current_x, current_y)

    def calcutate_offsets(self, alien_width, alien_height, screen_width, screen_height, fleet_width, fleet_height):
        half_screen = self.settings.screen_height // 2
        fleet_horizontal_spacing = fleet_width * alien_width
        fleet_vertical_spacing = fleet_height * alien_height
        x_offset = int((screen_width - fleet_horizontal_spacing) // 2)
        y_offset = int((screen_height - fleet_vertical_spacing) // 2)
        return x_offset,y_offset

    def calculate_offsets(self, alien_width, alien_height, screen_width, screen_height, fleet_width, fleet_height):
        half_screen = self.settings.screen_height // 2
        fleet_horizontal_spacing = fleet_width * alien_width
        fleet_vertical_spacing = fleet_height * alien_height
        x_offset = int((screen_width - fleet_horizontal_spacing) // 2)
        y_offset = int((screen_height - fleet_vertical_spacing) // 2)
        return x_offset,y_offset

    def new_method(self, alien_width, alien_height, screen_width, screen_height, fleet_width, fleet_height):
        half_screen = self.settings.screen_height // 2
        fleet_horizontal_spacing = fleet_width * alien_width
        fleet_vertical_spacing = fleet_height * alien_height
        x_offset = int((screen_width - fleet_horizontal_spacing) // 2)
        y_offset = int((screen_height - fleet_vertical_spacing) // 2)
        return x_offset,y_offset

    def calculate_offsets(self, alien_width, alien_height, screen_width, screen_height, fleet_width, fleet_height):
        half_screen = self.settings.screen_height // 2
        fleet_horizontal_spacing = fleet_width * alien_width
        fleet_vertical_spacing = fleet_height * alien_height
        x_offset = int((screen_width - fleet_horizontal_spacing) // 2)
        y_offset = int((screen_height - fleet_vertical_spacing) // 2)
        return x_offset,y_offset # 10 is the y-coordinate for the top row of aliens


    def calculate_fleet_size(self, alien_width, screen_width, alien_height, screen_height):
        fleet_width = (screen_width//alien_width)
        fleet_height = (screen_height // 2) // alien_height

        if fleet_width % 2 == 0:
            fleet_width -= 1  
        else:
            fleet_width -= 2 
        if fleet_height % 2 == 0:
            fleet_height -= 1
        else:
            fleet_height -= 2
        
        return fleet_width, fleet_height


    def create_alien(self, current_x: int, current_y: int):
        new_alien = Alien(self.game, current_x, current_y)
        self.aliens.add(new_alien)


    def draw(self):
        alien: 'Alien'
        for alien in self.aliens:
            alien.draw_alien()
