import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien


def chek_keydown_events(event, ai_settings, screen, stats, ship, aliens, bullets):
    """ Reacts to keystrokes."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        start_game(ai_settings, screen, stats, ship, aliens, bullets)




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


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """Handles keystrokes and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            chek_keydown_events(event, ai_settings, screen, stats, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            chek_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    """ Refreshes the screen images and displays the new screen. """
    # The screen is redrawn at each pass of the loop.
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Play button is displayed if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Displays the last drawn screen.
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Updates bullet positions and destroys old bullets. """
    # Updates bullet positions.
    bullets.update()
    # Removind bullets that go off the edge of screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Checks to hit the alians
    # When hitting an alien remove the bullet and the alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        #
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

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

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """
    Checks if the fleet has reached the edge of the screen.
    Updates the position of all aliens in the fleet.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Colision check "alien-ship"
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    
    # Checking the aliens who have reached the bottom edge of the screen.
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
    """ Reacts when an alien reaches the edge of the screen. """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """ Drops the entire fleet and changes the direction of the fleet."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """ Handles the collision of the ship with the alien. """
    # Decrease ship_left.
    if stats.ship_left > 0:
        stats.ship_left -= 1

        # Clearing the lists of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Creating a new fleet and placing the ship in the center.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause.
        sleep(0.5)
    
    else:
        stats.game_active =  False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Checks if the aliens have made it to the bottom of the screen."""
    screen_rect  = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #The same happens as in a collision with a ship.
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def check_play_button(ai_settings, screen, stats, play_button, ship,
        aliens, bullets, mouse_x, mouse_y):
    """ Launches a new game when the play button is pressed. """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        start_game(ai_settings, screen, stats, ship, aliens, bullets)

def start_game(ai_settings, screen, stats, ship, aliens, bullets):

    if not stats.game_active:

        # The mouse pointer is hidden.
        pygame.mouse.set_visible(False)
        # Reset game statistics
        stats.reset_stats()
        stats.game_active = True
        
        # Clearing the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and place the ship in the center.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

