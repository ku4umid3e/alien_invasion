import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for controlling bullets fired by a ship."""
    def __init__(self, ai_settings, screen, ship):
        """Creates a bullet object at the current position of the ship."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet at position (0,0) and assingthe correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # The bullet position is stored in real format.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
