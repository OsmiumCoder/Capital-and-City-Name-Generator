class Name:
    def __init__(self, screen, row, column, name_box, font):
        self.row = row
        self.column = column

        self.name_box = name_box

        self.text = ""
        self.font = font

        self.screen = screen

    def write_name(self):
        new_name_height = self.name_box.height / 5
        new_name_width = self.name_box.width / 3

        text_surface = self.font.render(self.text, True, (255, 0, 0))
        text_x = self.column * new_name_width + 20 + text_surface.get_width() / 2
        text_y = self.row * new_name_height + 20 + text_surface.get_height() / 2

        self.screen.blit(text_surface, (text_x, text_y))

    def change_name(self, name):
        self.text = name
