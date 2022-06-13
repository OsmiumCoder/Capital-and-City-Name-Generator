from pygame import quit, Rect, Color, draw, mouse
from pygame import event as ev
from pygame.locals import *
from pygame.display import set_mode, set_caption, update
from pygame.font import init, Font
from pygame.image import load

from functionals.generator.generate_name import generate_name
from functionals.objects.button import Button
from functionals.objects.name import Name


def main():
    # SCREEN
    screen_height = 600
    screen_width = 1000
    screen = set_mode((screen_width, screen_height), RESIZABLE)
    set_caption("Capital and City Name Generator")

    # FONT
    init()
    font = Font("Assets/NuosuSIL-Regular.ttf", 15)

    # IMAGES
    gen_img = load('Assets/generate-button.png').convert_alpha()

    # BUTTON
    gen_button = Button(gen_img, screen)

    # NAME BOX
    name_box_container = Rect(20, 20, screen_width - 40, (screen_height - 40) / 2)

    # BOX COLOR
    color = Color(1, 50, 32)

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

        draw.rect(screen, color, name_box_container, 2)

        gen_button.draw()

        for name in names:
            name.write_name()

        pos = mouse.get_pos()

        for event in ev.get():
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

        update()

    quit()


if __name__ == "__main__":
    main()
