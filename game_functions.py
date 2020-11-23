import sys

import pygame


def chek_keydown_events(event, ship):
    """ Reacts to keystrokes."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def chek_keyup_events(event, ship):
     if event.key == pygame.K_RIGHT:
         ship.moving_right = False
     elif event.key == pygame.K_LEFT:
         ship.moving_left = False


def check_events(ship):
    """Handles keystrokes and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            chek_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            chek_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
    """ Refreshes the screen images and displays the new screen. """
    # The screen is redrawn at each pass of the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Displays the last drawn screen.
    pygame.display.flip()
