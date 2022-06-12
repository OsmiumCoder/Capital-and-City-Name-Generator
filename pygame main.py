import pygame
from pygame.locals import *
from button import Button

# SCREEN
screen_height = 500
screen_width = 700

screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE)
pygame.display.set_caption("Capital and City Name Generator")

# FONT
pygame.font.init()
font_size = pygame.font.Font("NuosuSIL-Regular.ttf", 20)

# IMAGES
gen_img = pygame.image.load('Assets/generate-button.png').convert_alpha()
gen_img_height = gen_img.get_height()
gen_img_width = gen_img.get_width()

# BUTTON
button_position_x = screen_width / 2 - gen_img_width / 2
button_position_y = screen_height / 2 - gen_img_height / 2 + screen_height / 4
gen_button = Button(button_position_x, button_position_y, gen_img, screen)

# NAME BOX
name_box = pygame.Rect(20, 20, screen_width - 40, (screen_height - 40) / 2)
color = pygame.Color(255, 0, 0)

running = True

while running:

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, color, name_box, 2)

    gen_button.draw()

    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == WINDOWRESIZED:
            screen_width = screen.get_width()
            screen_height = screen.get_height()

            gen_button.update_position()

            name_box.update(20, 20, screen_width - 40, (screen_height - 40) / 2)

        elif event.type == MOUSEBUTTONDOWN:
            if gen_button.rect.collidepoint(pos):
                # generate names in box
                print(pos)

    pygame.display.update()

pygame.quit()
