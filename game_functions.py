import sys

import pygame

def check_events():
    """Handles keystrokes and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_sreen(ai_settings, screen, ship):
    """Refreshes the screen images and displays the new screen."""
    #The screen is redrawn at each pass of the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Displays the last drawn screen.
    pygame.display.flip()
