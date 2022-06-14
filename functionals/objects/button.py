from pygame import Surface, Rect


class Button:
    """
    An object for handling the button to generate names.

    Parameters
    ----------
    image : Surface
        The image to be used as the button.
    screen : Surface
        The screen for the button to be drawn on.

    Attributes
    ----------
    image : Surface
        The image to be drawn on the screen as a button.
    width : int
        The width of the image.
    height : int
        The height of the image.
    screen : Surface
        The screen that the image button will be drawn on to.
    rect : Rect
        The Rect object of the image.

    Methods
    -------
    draw()
        Draw the button at its appropriate position.

    """

    def __init__(self, image, screen):
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.screen = screen

        self.rect = self.image.get_rect()

    def draw(self):
        """
        Draw the button at its appropriate position.

        Returns
        -------
        None

        """
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        button_position_x = screen_width / 2 - self.width / 2
        button_position_y = screen_height / 2 - self.height / 2 + screen_height / 4

        self.rect.topleft = (button_position_x, button_position_y)

        self.screen.blit(self.image, (self.rect.x, self.rect.y))
