import pygame as pg
import numpy as np
from tile import Tile, initialize_grid
from start_menu import start_menu
from game_state import Game_State
from inventory import Inventory

DARK = (137, 137, 137)
WHITE = (255, 255, 255)

# https://www.redblobgames.com/grids/hexagons/
# https://stackoverflow.com/questions/56984542/is-there-an-effiecient-way-of-making-a-function-to-drag-and-drop-multiple-pngs

# Inititalize the pygame
pg.init()

# Create the screen
WIDTH, HEIGHT = 884, 900  # TODO: Autosense window??
screen = pg.display.set_mode((WIDTH, HEIGHT))

# Background
background = pg.Surface(screen.get_size())
background.fill((0, 0, 0))

#Title and Icon
pg.display.set_caption("Hive")
# TODO: Icon not working on Ubuntu?? It works on windows though
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)

tiles = initialize_grid(HEIGHT - 200, WIDTH, radius=20)

game_state = Game_State()

inv_dark = Inventory(DARK)
inv_white = Inventory(WHITE)

clicked = False
moving_piece = None


def draw_drag(background, pos, piece=None):

    # blit in bug?selected_rect = pygame.Rect(BOARD_POS[0] + selected_piece[1] * TILESIZE, BOARD_POS[1] + selected_piece[2] * TILESIZE, TILESIZE, TILESIZE)
    pg.draw.line(background, pg.Color('red'), pos, piece.old_pos)


while game_state.running:
    while game_state.menu_loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_state.quit()
                break
            start_menu(screen, game_state, event)

    while game_state.main_loop:
        pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_state.quit()
                break
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_TAB:
                    old_tile = [x for x in tiles if x.piece is not None][0]
                    new_tile = tiles[np.random.randint(0, len(tiles))]
                    old_tile.move_piece(new_tile)
                if event.key == pg.K_ESCAPE:
                    game_state.quit()
                    break
            if event.type == pg.MOUSEBUTTONDOWN:
                clicked = True
            if event.type == pg.MOUSEBUTTONUP:
                clicked = False
                if moving_piece:
                    old_tile = next(
                        tile for tile in tiles if tile.piece == moving_piece)
                    new_tile = next(
                        (tile for tile in tiles if tile.under_mouse(pos)), None)
                    old_tile.move_piece(new_tile)
                moving_piece = None

        # only draw tiles once in a for loop
        background.fill((180, 180, 180))
        for tile in tiles:
            if clicked:
                tile.draw(background, pos, clicked)
                if tile.under_mouse(pos) and moving_piece is None:
                    moving_piece = tile.piece
            else:
                tile.draw(background, pos)
        inv_dark.draw_inventory(background, (0,160))
        inv_white.draw_inventory(background, (442, 160))
        if moving_piece:
            draw_drag(background, pos, moving_piece)
        pg.draw.circle(background, (1, 250, 1), (442, 380), 6)
        pg.draw.circle(background, (1, 250, 1), (0, 380), 6)
        screen.blit(background, (0, 0))
        pg.display.flip()
