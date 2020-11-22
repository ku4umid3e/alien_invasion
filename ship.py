import pygame


class Ship:

    def __init__(self, screen):
        """Initializes the ship and sets its starting position."""
        self.screen = screen

        # Loading a ship image and getting a rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Each new ship appears at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Movement flag
        self.moving_right = False

    def update(self):
        """ Update the ship's position, based on movement flags."""
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        """Draws the ship at the current position."""
        self.screen.blit(self.image, self.rect)
