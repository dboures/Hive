import pygame as pg
import numpy as np
from tile import Tile, initialize_grid
from start_menu import start_menu
from game_state import Game_State

# https://www.redblobgames.com/grids/hexagons/
#https://stackoverflow.com/questions/56984542/is-there-an-effiecient-way-of-making-a-function-to-drag-and-drop-multiple-pngs

# Inititalize the pygame
pg.init()

# Create the screen
WIDTH, HEIGHT = 900, 900  # TODO: Autosense window??
screen = pg.display.set_mode((WIDTH, HEIGHT))

# Background
background = pg.Surface(screen.get_size())
background.fill((137, 137, 137))

#Title and Icon
pg.display.set_caption("Hive")
# TODO: Icon not working on Ubuntu?? It works on windows though
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)

tiles = initialize_grid(HEIGHT, WIDTH, radius=20)

game_state = Game_State()

queen = pg.image.load('images/Queen.png')

while game_state.running:
    while game_state.menu_loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_state.quit()
                break
            start_menu(screen, game_state, event)

    while game_state.main_loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_state.quit()
                break
        pos = pg.mouse.get_pos()
        background.fill((137, 137, 137))
        for tile in tiles:
            tile.draw_blank(background)
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                for tile in tiles:
                    if tile.under_mouse(pos):
                        tile.draw_clicked(background)
        elif event.type == pg.MOUSEMOTION:
            for tile in tiles:
                    if tile.under_mouse(pos):
                        tile.draw_selected(background)
                        

        pg.draw.circle(background, (1, 250, 1), (450, 450), 6)
        background.blit(queen, (450, 450))
        screen.blit(background, (0, 0))
        pg.display.flip()
