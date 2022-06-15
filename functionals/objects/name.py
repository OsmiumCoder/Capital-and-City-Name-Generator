from pygame import Surface, Rect
from pygame.font import Font


class Name:
    """
    An object for handling name containers.

    Parameters
    ----------
    screen : Surface
        The screen for the name to be written on.
    row : int
        The row the name will be in.
    column : int
        The column the name will be in.
    name_box : Rect
        The text box the name will be in.
    font : Font
        The font style and size of the name.

    Attributes
    ----------
    row : int
        The row the name is in.
    column : int
        The column the name is in.
    name_box : Rect
        The text box the name is in.
    name : str
        The name written on the screen.
    font : Font
        The font style and size of the name.
    screen : Surface
        The screen for the name to be written on.

    Methods
    -------
    write_name()
        Write the name to the appropriate position.
    change_name(name)
        Change the name to a new name.

    """

    def __init__(self, screen, row, column, name_box, font):
        self.row = row
        self.column = column

        self.name_box = name_box

        self.name = ""
        self.font = font

        self.screen = screen

    def write_name(self):
        """
        Write the name to the appropriate position.

        Returns
        -------
        None

        """
        # calculate the distance between each name in both X and Y planes
        name_width_position = self.name_box.width / 3
        name_height_position = self.name_box.height / 5

        # render the text into a Surface
        text_surface = self.font.render(self.name, True, (0, 0, 0))

        # calculate the X and Y position for the text to be displayed
        text_x = 20 + self.column * name_width_position + name_width_position / 3 + name_width_position / 10
        text_y = 20 + self.row * name_height_position + name_height_position / 5 + name_height_position / 17

        # draw the text to the screen at its calculated position
        self.screen.blit(text_surface, (text_x, text_y))

    def change_name(self, name):
        """
        Change the name to a new name.

        Parameters
        ----------
        name : str
            The new name to be written.

        Returns
        -------
        None

        """
        self.name = name
