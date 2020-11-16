import pygame as pg
import numpy as np
from tile import Tile, initialize_grid
from start_menu import start_menu
from game_state import Game_State

# https://www.redblobgames.com/grids/hexagons/

# Inititalize the pygame
pg.init()

# Create the screen
WIDTH, HEIGHT = 900, 900  # TODO: Autosense window??
screen = pg.display.set_mode((WIDTH, HEIGHT))

# Background
background = pg.Surface(screen.get_size())
background.fill((250, 1, 1))

#Title and Icon
pg.display.set_caption("Hive")
# TODO: Icon not working on Ubuntu?? It works on windows though
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)

tiles = initialize_grid(HEIGHT, WIDTH, radius=20)

game_state = Game_State()

while game_state.running:
    while game_state.menu_loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_state.quit()
                break
            else:
                # how can this reach up to the global variable?
                start_menu(screen, game_state, event)

    while game_state.main_loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_state.quit()
                break
        else:
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    click_pos = pg.mouse.get_pos()
                    print(click_pos)
                    # how do we draw the grid the first time
                    for tile in tiles:
                        if tile.was_clicked(click_pos):
                            tile.draw_clicked(background)
                        else:
                            tile.draw_blank(background)

                    # TODO: create hex and get position to print what hex we are in
                    # Use axial coords
                    pg.draw.circle(background, (1, 250, 1), (450, 450), 6)
                    # pg.display.flip()

        screen.blit(background, (0, 0))
        pg.display.update()
