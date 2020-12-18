import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class representing a single alien."""
    def __init__(self, ai_settings, screen):
        """Alien initialization, setting its initial position. """
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load image alien and the purpose of its attribute 'rect'.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Every new alien appears in the upper left cornerof the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.heigth

        # Keeping exact position of the alien
        self.x = float(self.rect.x)

    def blitme(self):
        """ Takes the alien in given position."""
        self.screen.blit(self.image, self.rect)
