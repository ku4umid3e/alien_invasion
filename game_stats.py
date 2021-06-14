

class GameStats():
    """Tracking statistics for the game Alien invasion."""
    
    def __init__(self, ai_settings):
        """Initializes statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Game "Alien Invasion" starts in active mode.
        self.game_active = False

    def reset_stats(self):
        """Initializes statistics that change during the game."""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
