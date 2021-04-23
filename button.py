import pugame.font


class Button():

    def __init__(self, ai_settings, screen, msg):
        """ Initializes the attributes of the button. """
        self.screen = screen
        self.screen.rect =  screen.get_rect()

        # Assigning sizes and properties of a button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Building the rect object of the button and aligning it to the center of the screen.
        self.rect = pygame.Rect(0, 0, self.width, self,height)
        self.rect.center = self.screen_rect.centr

        # The button messege is created only once.
        self.prep_msg(msg)
