class Rectangle:
    def __init__(self, screen, rect_obj):
        self.screen = screen
        self.rect = rect_obj
        self.width = 1
        self.height = 1

    def update_position(self):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        button_position_x = screen_width / 2 - self.width / 2
        button_position_y = screen_height / 2 - self.height / 2 + screen_height / 4

        self.rect.topleft = (button_position_x, button_position_y)
