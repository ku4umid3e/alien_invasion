class Settings:
    """Class for storing all settings of the game 'Alien Invasion'."""
    def __init__(self):
        """Initializes game settings."""
        # Screen options.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Settings ship
        self.ship_speed_factor = 1.5
        
        # Bullet parametrs
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Aliens settings.
        self.alien_speed_factor = 1
