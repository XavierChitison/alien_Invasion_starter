import pygame
from bullet import Bullet
from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class ShipArsenal:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()  # Group to hold all bullets fired by the ship

    def update_arsenal(self):
        # Update the position of bullets in the arsenal
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom < 0:
                self.arsenal.remove(bullet)
                
    def draw(self):
        # Draw all bullets in the arsenal
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        if len(self.arsenal) < self.settings.bullets_allowed:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True # Bullet fired successfully
        return False # Bullet not fired, limit reached