class Name:
    def __init__(self, screen, row, column, name_box, font):
        self.row = row
        self.column = column

        self.name_box = name_box

        self.text = ""
        self.font = font

        self.screen = screen

    def write_name(self):
        name_height_position = self.name_box.height / 5
        name_width_position = self.name_box.width / 3

        text_surface = self.font.render(self.text, True, (255, 0, 0))
        text_x = self.column * name_width_position + 20 + text_surface.get_width()
        text_y = self.row * name_height_position + 20 + text_surface.get_height()

        self.screen.blit(text_surface, (text_x, text_y))

    def change_name(self, name):
        self.text = name
