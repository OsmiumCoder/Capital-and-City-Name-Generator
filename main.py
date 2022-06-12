from generate_name import generate_name
import pygame
from pygame.locals import *
from button import Button
from name import Name


def main():
    # SCREEN
    screen_height = 500
    screen_width = 700
    screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE)
    pygame.display.set_caption("Capital and City Name Generator")

    # FONT
    pygame.font.init()
    font = pygame.font.Font("Assets/NuosuSIL-Regular.ttf", 15)

    # IMAGES
    gen_img = pygame.image.load('Assets/generate-button.png').convert_alpha()

    # BUTTON
    gen_button = Button(gen_img, screen)

    # NAME BOX
    name_box_container = pygame.Rect(20, 20, screen_width - 40, (screen_height - 40) / 2)

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
                screen_width = screen.get_width()
                screen_height = screen.get_height()
                name_box_container.update(20, 20, screen_width - 40, (screen_height - 40) / 2)

            elif event.type == MOUSEBUTTONDOWN:
                if gen_button.rect.collidepoint(pos):
                    for name in names:
                        name.change_name(generate_name())

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
