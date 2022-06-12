class Rectangle:
    def __init__(self, screen, rect_obj):
        self.screen = screen
        self.rect = rect_obj

    def update_position(self):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        self.rect.update(20, 20, screen_width - 40, (screen_height - 40) / 2)
