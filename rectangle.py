class Rectangle:
    def __init__(self, screen, rect_obj):
        self.screen = screen
        self.rect = rect_obj

    def update_position(self):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        self.rect.update(20, 20, screen_width - 40, (screen_height - 40) / 2)


class NameRect(Rectangle):
    def __init__(self, screen, rect_obj, row, column, name_box):
        super().__init__(screen, rect_obj)
        self.row = row
        self.column = column
        self.name_box = name_box
        self.text = ""

    def update_position(self):
        new_box_height = self.name_box.height / 5
        new_box_width = self.name_box.width / 3

        self.rect.update(self.column * new_box_width + 20, self.row * new_box_height + 20, new_box_width,
                         new_box_height)

    def write_name(self, name):
        pass