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
WIDTH, HEIGHT = 880, 900  # TODO: Autosense window??
screen = pg.display.set_mode((WIDTH, HEIGHT))

# Background
background = pg.Surface(screen.get_size())
background.fill((0, 0, 0))

#Title and Icon
pg.display.set_caption("Hive")
# TODO: Icon not working on Ubuntu?? It works on windows though
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)


inv_white = Inventory(background, (0,160), white=True)
inv_dark = Inventory(background, (440, 160), white=False)

gs = Game_State(initialize_grid(HEIGHT - 200, WIDTH, radius=20))


def draw_drag(background, pos, piece=None):

    # blit in bug?selected_rect = pygame.Rect(BOARD_POS[0] + selected_piece[1] * TILESIZE, BOARD_POS[1] + selected_piece[2] * TILESIZE, TILESIZE, TILESIZE)
    pg.draw.line(background, pg.Color('red'), pos, piece.old_pos)


while gs.running:
    while gs.menu_loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gs.quit()
                break
            start_menu(screen, gs, event)

    while gs.main_loop:
        pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gs.quit()
                break
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_TAB:
                    old_tile = [x for x in gs.board_tiles if x.piece is not None][0]
                    new_tile = gs.board_tiles[np.random.randint(0, len(gs.board_tiles))]
                    old_tile.move_piece(new_tile)
                    print('rules')
                if event.key == pg.K_ESCAPE:
                    gs.quit()
                    break
            if event.type == pg.MOUSEBUTTONDOWN:
                clicked = True
            if event.type == pg.MOUSEBUTTONUP:
                clicked = False
                if gs.moving_piece:
                    old_tile = next(
                        tile for tile in gs.board_tiles if tile.piece == gs.moving_piece)
                    new_tile = next(
                        (tile for tile in gs.board_tiles if tile.under_mouse(pos)), None)
                    old_tile.move_piece(new_tile)
                gs.moving_piece = None

        # only draw tiles once in a for loop
        background.fill((180, 180, 180))
        for tile in gs.board_tiles:
            if gs.clicked:
                tile.draw(background, pos, clicked)
                if tile.under_mouse(pos) and gs.moving_piece is None:
                    gs.moving_piece = tile.piece
            else:
                tile.draw(background, pos)
        inv_white.draw_inventory(background, pos, clicked, gs.moving_piece)# fix these, in game state now
        inv_dark.draw_inventory(background, pos, clicked, gs.moving_piece)
        if gs.moving_piece:
            draw_drag(background, pos, gs.moving_piece)
        pg.draw.circle(background, (1, 250, 1), (440, 380), 6)
        pg.draw.circle(background, (1, 250, 1), (0, 380), 6)
        screen.blit(background, (0, 0))
        pg.display.flip()
