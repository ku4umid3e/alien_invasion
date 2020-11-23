import sys

import pygame


def check_events(ship):
    """Handles keystrokes and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """ Refreshes the screen images and displays the new screen. """
    # The screen is redrawn at each pass of the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Displays the last drawn screen.
    pygame.display.flip()
