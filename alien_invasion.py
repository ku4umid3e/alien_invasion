import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats


def run_game():
    """ Initializes the game and creates a screen object. """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height)
            )
    pygame.display.set_caption("Alien Invasion")
    
    #Creating an instance for storing the game
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)
    
    # Created group of a store bullets.
    bullets = Group()

    # Created group of store aliens
    aliens = Group()

    # Created fleet aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Starting the main game loop
    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        
        if stats.game_active:
        
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
