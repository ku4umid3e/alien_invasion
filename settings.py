class Settings:
    """Class for storing all settings of the game 'Alien Invasion'."""
    def __init__(self):
        """Initializes game settings."""
        # Screen options.
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        
        # Settings ship

#        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        
        # Bullet parametrs

#        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Aliens settings.

#        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        # Game accelerration rate.
        self.speedup_scale = 1.1
        
        # The rate of growth in the cost aof the aliel
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """ Initializes settings that change during the game. """
        
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5
        
        # fleet_direction = 1 indicates movement to the right and -1 to the left
        self.fleet_direction = 1
        
        # Scoring.
        self.alien_points = 50


    def increase_speed(self):
        # Increases the speed and cost of the aliens.
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
