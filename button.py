import pygame


class Button:
    """A centered button with configurable appearance and text."""

    def __init__(self, game, msg):
        self.screen = game.screen
        self.settings = game.settings
        self.button_color = self.settings.button_color
        self.text_color = self.settings.button_text_color
        self.font = pygame.font.Font(
            self.settings.font_name, self.settings.button_font_size)
        self.rect = pygame.Rect(
            0, 0, self.settings.button_width, self.settings.button_height)
        self.rect.center = self.screen.get_rect().center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Render a label for this button."""
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect(center=self.rect.center)

    def draw_button(self):
        pygame.draw.rect(self.screen, self.button_color, self.rect)
        # Keep the label centered if the button is repositioned.
        self.msg_image_rect.center = self.rect.center
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def is_clicked(self, position):
        return self.rect.collidepoint(position)
