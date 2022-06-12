import pygame
from pygame.locals import *
from button import Button
from rectangle import Rectangle
from name import Name

# SCREEN
screen_height = 500
screen_width = 700
screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE)
pygame.display.set_caption("Capital and City Name Generator")

# FONT
pygame.font.init()
font = pygame.font.Font("Assets/NuosuSIL-Regular.ttf", 20)

# IMAGES
gen_img = pygame.image.load('Assets/generate-button.png').convert_alpha()
gen_img_height = gen_img.get_height()
gen_img_width = gen_img.get_width()

# BUTTON
button_position_x = screen_width / 2 - gen_img_width / 2
button_position_y = screen_height / 2 - gen_img_height / 2 + screen_height / 4
gen_button = Button(button_position_x, button_position_y, gen_img, screen)

# NAME BOX
name_box_container = pygame.Rect(20, 20, screen_width - 40, (screen_height - 40) / 2)
name_box_obj = Rectangle(screen, name_box_container)

# BOX COLOR
color = pygame.Color(1, 50, 32)

# CREATE NAME DISPLAYS
names = []
rows = 5
columns = 3
for row in range(rows):
    for column in range(columns):
        new_name = Name(screen, row, column, name_box_container, font)
        names.append(new_name)

running = True

while running:

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, color, name_box_container, 2)

    gen_button.draw()

    for name in names:
        name.write_name()

    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == WINDOWRESIZED:
            gen_button.update_position()

            name_box_obj.update_position()

        elif event.type == MOUSEBUTTONDOWN:
            if gen_button.rect.collidepoint(pos):
                for name in names:
                    name.change_name("placeholder")

    pygame.display.update()

pygame.quit()
