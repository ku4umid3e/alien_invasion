import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        """Initializes the ship and sets its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading a ship image and getting a rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Each new ship appears at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Saving the real coordinate of the ship center.
        self.center = float(self.rect.centerx)
        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update the ship's position, based on movement flags."""
        if self.moving_right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
        # Update the rect attribute based on self.center.
        self.rect.centerx = self.center 

    def blitme(self):
        """Draws the ship at the current position."""
        self.screen.blit(self.image, self.rect)
