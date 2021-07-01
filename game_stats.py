

class GameStats():
    """Tracking statistics for the game Alien invasion."""
    
    def __init__(self, ai_settings):
        """Initializes statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Game "Alien Invasion" starts in active mode.
        self.game_active = False

        # The record should not be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initializes statistics that change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
