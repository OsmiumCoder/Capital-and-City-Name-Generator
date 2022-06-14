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
        name_height_position = self.name_box.height / 5
        name_width_position = self.name_box.width / 3

        text_surface = self.font.render(self.name, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_x = self.column * name_width_position + text_rect.x + 20 + name_width_position / 3 + name_width_position / 13
        text_y = self.row * name_height_position + text_rect.y + 20 + name_height_position / 5

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
