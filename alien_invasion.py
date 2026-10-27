import sys
import pygame
from Settings import Settings
from ship import Ship
from arsenal import ShipArsenal
from alien_fleet import AlienFleet
from game_stats import GameStats
from button import Button
from hud import HUD


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(
            self.bg, (self.settings.screen_width, self.settings.screen_height))

        self.running = True
        self.stats = GameStats(self.settings.ship_lives)
        self.play_button = Button(self, "Play")
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        print("Laser sound path:", self.settings.laser_sound)
        print("File exists:", self.settings.laser_sound.exists())
        self.laser_sound = pygame.mixer.Sound(str(self.settings.laser_sound))
        self.laser_sound.set_volume(1)  # Set the volume to 100%
        self.impact_sound = pygame.mixer.Sound(str(self.settings.impact_sound))

        self.arsenal = ShipArsenal(self)
        self.aliens = AlienFleet(self)
        self.ship = Ship(self, self.arsenal)
        self.hud = HUD(self)

    def run_game(self):
        # Game Loop
        while self.running:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self.aliens.update_fleet()
                self.arsenal.update_arsenal()
                self._check_collisions()
            self._updated_screen()
            # Limit the frame rate to 60 FPS
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        if not self.stats.game_active:
            return
        bullet_hits = self.aliens.check_collisions(self.arsenal.arsenal)
        self.stats.add_score(len(bullet_hits) * 100)
        ship_hit = self.ship.check_collisions(self.aliens.aliens)
        if bullet_hits or ship_hit:
            self.impact_sound.play()

        if (ship_hit
                or any(alien.rect.bottom >= self.screen.get_rect().bottom
                       for alien in self.aliens.aliens)):
            self.stats.lose_life()
            if not self.stats.game_active:
                self.arsenal.arsenal.empty()
                self.ship.moving_left = False
                self.ship.moving_right = False
            else:
                self._reset_level()
            return

        if not self.aliens.aliens:
            self.stats.advance_level()
            self.settings.increase_difficulty()
            self.arsenal.arsenal.empty()
            self.aliens.create_fleet()

    def _reset_level(self):
        self.arsenal.arsenal.empty()
        self.aliens.create_fleet()
        self.ship._center_ship()
        self.ship.moving_left = False
        self.ship.moving_right = False

    def _updated_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        self.aliens.draw()
        self.arsenal.draw()
        self.hud.draw()
        if self.stats.waiting_to_start:
            self.play_button.draw_button()
        elif not self.stats.game_active:
            message = self.font.render(
                "Game Over - Press R to restart", True, (255, 255, 255), (0, 0, 0))
            self.screen.blit(message, message.get_rect(center=self.screen.get_rect().center))
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.stats.waiting_to_start and self.play_button.is_clicked(event.pos):
                    self._start_game()

    def _start_game(self):
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self._reset_level()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_keydown_events(self, event):
        if (not self.stats.game_active and not self.stats.waiting_to_start
                and event.key == pygame.K_r):
            self._start_game()
            return
        if not self.stats.game_active and event.key != pygame.K_q:
            return
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                # Play the laser sound
                self.laser_sound.play()
                # Fade out the sound over 500 milliseconds
                self.laser_sound.fadeout(500)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
