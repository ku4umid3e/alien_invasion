import sys

import pygame

from bullet import Bullet


def chek_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Reacts to keystrokes."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and it to the bullets group.
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def chek_keyup_events(event, ship):
     if event.key == pygame.K_RIGHT:
         ship.moving_right = False
     elif event.key == pygame.K_LEFT:
         ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Handles keystrokes and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            chek_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            chek_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    """ Refreshes the screen images and displays the new screen. """
    # The screen is redrawn at each pass of the loop.
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Displays the last drawn screen.
    pygame.display.flip()
