import sys

import pygame

from bullet import Bullet
from alien import Alien


def chek_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Reacts to keystrokes."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
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


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """ Refreshes the screen images and displays the new screen. """
    # The screen is redrawn at each pass of the loop.
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Displays the last drawn screen.
    pygame.display.flip()


def update_bullets(bullets):
    """Updates bullet positions and destroys aold bullets. """
    # Updates bullet positions.
    bullets.update()
    # Removind bullets that go off the edge of screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """ Calculating the number of aliens in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2* alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """ Creates an alien and places it in a row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """ Created fleet aliens"""

    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
            alien.rect.height)

    # Created of the first row of alien.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Creating an alien and placing it in a row.
            create_alien(ai_settings, screen, aliens, alien_number, 
                    row_number)

def get_number_rows(ai_settings, ship_height, alien_height):
    """ Determines the number of rows that fit on the screen."""
    available_space_y = (ai_settings.screen_height - 
            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
