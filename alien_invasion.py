import sys
import pygame
from Settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_width, self.settings.screen_height))

        self.ship = Ship(self)

        self.running = True
        self.clock = pygame.time.Clock()


    def run_game(self):
        # Game Loop
        while self.running:
            self._check_events()
                    
            self._updated_screen()
            self.clock.tick(60) 

    def _updated_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit() # Limit the frame rate to 60 FPS


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()