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
    """
    Main Script to be run.

    Returns
    -------
    None

    """
    # SCREEN
    screen_height = 600
    screen_width = 1000

    # displays a resizeable window of type Surface
    screen = set_mode((screen_width, screen_height), RESIZABLE)
    # sets the title of the displayed window
    set_caption("Capital and City Name Generator")

    # FONT
    init()  # initialize the font module to use its functions
    # create a Font object and initialize font type and default size
    font = Font("Assets/NuosuSIL-Regular.ttf", 15)

    # IMAGES
    # loads the generate button image as a Surface to be drawn
    gen_img = load('Assets/generate-button.png').convert_alpha()

    # BUTTON
    # create a Button object to draw the image to the screen Surface
    gen_button = Button(gen_img, screen)

    # NAME BOX
    # create a Rect to display the 15 generated names
    name_box_container = Rect(20, 20, screen_width - 40, (screen_height - 40) / 2)

    # BOX COLOR
    # initialize a pygame Color object to be the color of the name box
    # Dark Green
    color = Color(1, 50, 32)

    # CREATE NAME DISPLAYS
    names = []
    rows = 5
    columns = 3

    # create 15 Name objects each with a unique (row, column) pair
    for row in range(rows):
        for column in range(columns):
            new_name = Name(screen, row, column, name_box_container, font)
            names.append(new_name)

    running = True

    # so long as we haven't quit run the main game loop
    while running:

        screen.fill((255, 255, 255))  # maintain a white background every loop

        # draw the name box Rect to the screen Surface
        # border thickness of 2
        draw.rect(screen, color, name_box_container, 2)

        gen_button.draw()  # draw the button to the screen

        # maintain the display of the 15 names
        # if none have been generated they will remain blank
        for name in names:
            name.write_name()

        # get the position of the mouse as it moves around
        pos = mouse.get_pos()

        # loop through each event in the pygame event queue
        for event in ev.get():
            # if the user has clicked the X to close the window
            # end the main game loop and goto quit pygame
            if event.type == QUIT:
                running = False

            # if the user resizes the window
            # update the dimensions of the name box
            elif event.type == WINDOWRESIZED:
                screen_width = screen.get_width()
                screen_height = screen.get_height()

                name_box_container.update(20, 20, screen_width - 40, (screen_height - 40) / 2)

            # if the user clicks
            # check if the click is on the generate button
            elif event.type == MOUSEBUTTONDOWN:
                # if the user did click the button
                # assign each Name object a random name
                if gen_button.rect.collidepoint(pos):
                    for name in names:
                        name.change_name(generate_name())

        update()  # update graphics each loop

    quit()  # quits pygame


if __name__ == "__main__":
    main()
