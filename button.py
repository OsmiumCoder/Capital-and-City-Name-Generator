class Button:
    def __init__(self, image, screen):
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.screen = screen

        self.rect = self.image.get_rect()

    def draw(self):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        button_position_x = screen_width / 2 - self.width / 2
        button_position_y = screen_height / 2 - self.height / 2 + screen_height / 4

        self.rect.topleft = (button_position_x, button_position_y)

        self.screen.blit(self.image, (self.rect.x, self.rect.y))
