import pygame as pg
import numpy as np
from tile import Tile, Start_Tile, Inventory_Tile, initialize_grid
from start_menu import start_menu
from game_state import Game_State
from inventory_frame import Inventory_Frame

DARK = (137, 137, 137)
WHITE = (250, 250, 250)

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


state = Game_State(initialize_grid(HEIGHT - 200, WIDTH, radius=20))

inv_white = Inventory_Frame(background, (0, 158), state, white=True)
inv_dark = Inventory_Frame(background, (440, 158), state, white=False)


def draw_drag(background, pos, piece=None):  # move this somewhere??

    # blit in bug?selected_rect = pygame.Rect(BOARD_POS[0] + selected_piece[1] * TILESIZE, BOARD_POS[1] + selected_piece[2] * TILESIZE, TILESIZE, TILESIZE)
    pg.draw.line(background, pg.Color('red'), pos, piece.old_pos)


def is_valid_move(state, old_tile, new_tile): #still need to handle enforcing queen placement
    # first move
    if state.turn == 1:
        if (new_tile is not None 
                and new_tile.coords != old_tile.coords 
                and type(new_tile) is Start_Tile 
                and new_tile.piece is None):
            return True
    # second
    elif state.turn == 2:
        if (new_tile is not None 
            and new_tile.coords != old_tile.coords 
            and type(new_tile) is not Inventory_Tile
            and new_tile.piece is None 
            and new_tile.is_hive_adjacent(state)
            #and new move is valid for piece

            ):
            return True
    elif state.turn > 2:
        if (new_tile is not None 
            and new_tile.coords != old_tile.coords 
            and type(new_tile) is not Inventory_Tile 
            and new_tile.piece is None 
            and new_tile.is_hive_adjacent(state)
            and move_does_not_break_hive(state, old_tile)
            #and new move is valid for piece

            ):
            return True
    else:
        return False

def move_does_not_break_hive(state, old_tile):
    temp_piece = old_tile.piece
    old_tile.remove_piece()
    unvisited = state.get_tiles_with_pieces()
    print(unvisited)
    visited = [unvisited.pop()]
    for visited_tile in visited:
        for unvisited_tile in unvisited:
            if unvisited_tile in visited_tile.get_adjacent_tiles(state):
                visited.append(unvisited.pop(unvisited.index(unvisited_tile)))
    print(len(unvisited))
    if len(unvisited) > 0:
        old_tile.add_piece(temp_piece)
        print('One Hive Rule')
        print('unvisited tile:' + str(unvisited[0].axial_coords))
        return False
    else:
        old_tile.add_piece(temp_piece)
        return True

while state.running:
    while state.menu_loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                state.quit()
                break
            start_menu(screen, state, event)

    while state.main_loop:
        pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                state.quit()
                break
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_TAB:
                    tile = next(
                        (tile for tile in state.board_tiles if tile.under_mouse(pos)), None)
                    print(tile.axial_coords)
                    print('turn #: ' + str(state.turn))
                if event.key == pg.K_ESCAPE:
                    state.quit()
                    break
            if event.type == pg.MOUSEBUTTONDOWN:
                state.click()
            if event.type == pg.MOUSEBUTTONUP:
                state.unclick()
                if state.moving_piece and state.is_player_turn():
                    old_tile = next(
                        tile for tile in state.board_tiles if tile.piece == state.moving_piece)
                    new_tile = next(
                        (tile for tile in state.board_tiles if tile.under_mouse(pos)), None)
                    if is_valid_move(state, old_tile, new_tile):
                        old_tile.move_piece(new_tile)
                        state.next_turn()
                state.remove_moving_piece()

        # only draw tiles once in a for loop
        background.fill((180, 180, 180))
        inv_white.draw_inventory_frame(background, pos)
        inv_dark.draw_inventory_frame(background, pos)
        for tile in state.board_tiles:
            if state.clicked:
                tile.draw(background, pos, state.clicked)
                if tile.under_mouse(pos) and state.moving_piece is None:
                    state.moving_piece = tile.piece
            else:
                tile.draw(background, pos)
        if state.moving_piece:
            draw_drag(background, pos, state.moving_piece)
        pg.draw.circle(background, (1, 250, 1), (440, 380), 6)
        pg.draw.circle(background, (1, 250, 1), (0, 380), 6)
        screen.blit(background, (0, 0))
        pg.display.flip()
