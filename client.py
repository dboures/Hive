import pygame as pg
import numpy as np
from tile import Tile, Inventory_Tile, initialize_grid
from move_checker import is_valid_move, game_is_over, player_has_no_moves
from menus import start_menu, end_menu, no_move_popup
from game_state import Game_State
from networking import Client
#import move
from inventory_frame import Inventory_Frame
from turn_panel import Turn_Panel
import socket
import pickle
import sys
import move

pg.font.init()
sys.setrecursionlimit(10**6)


# p1 = Queen()
# x = Queen()
# p2 = x.get_pickleable_piece()

# s1 = State(0, [Tile((1,1), (0,0), 20, (1,1,1), piece=p1)], [], [])
# s2 = State(1, [Tile((1,1), (7,7), 20, (1,1,1), piece = p2)], [], [])

# a = Client()
# b = Client()

# print(a.connect_return)
# print(b.connect_return)

# # y = a.send(s1)
# # print(x)
# z = b.send(s2)
# print(z)

WIDTH, HEIGHT = 880, 900
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Client")
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)
background = pg.Surface(screen.get_size())
background.fill((0, 0, 0))

def main():
    client = Client()

    #gotta think about these tiles
    white_inventory = Inventory_Frame((0, 158), white=True)
    black_inventory = Inventory_Frame((440, 158), white=False)
    
    print('about to run')

    clicked= False
    while True:
        state = client.get_state()
        while state.main_loop: #state.main_loop:
            board_tiles = client.get_board()
            pos = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    state.quit()
                    break
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_TAB:
                        tile = next(
                            (tile for tile in board_tiles if tile.under_mouse(pos)), None)
                        q,r = tile.axial_coords
                        print(q,r)
                    if event.key == pg.K_ESCAPE:
                        state.quit()
                        break
                    # if event.key == pg.K_PAGEUP:
                    #     client.state.open_popup()
                if event.type == pg.MOUSEBUTTONDOWN:
                    clicked=True
                if event.type == pg.MOUSEBUTTONUP:
                    clicked=False


                    if state.moving_piece and state.is_player_turn():
                        old_tile = next(
                            tile for tile in board_tiles if  (tile.has_pieces() and tile.pieces[-1].old_pos == state.moving_piece.old_pos)) # differnet object bc one comes from the server
                        new_tile = next(
                            (tile for tile in board_tiles if tile.under_mouse(pos)), None)
                        #send old_tile, new_tile
                        if is_valid_move(state, old_tile, new_tile):
                            old_tile.move_piece(new_tile)
                            state.next_turn()
                            # if player_has_no_moves(state):
                            #     print('player has no moves')
                            #     state.open_popup()

                    state.remove_moving_piece()
                    client.send_board(board_tiles)
       
            # only draw tiles once in a for loop
            background.fill((180, 180, 180))
            white_inventory.draw(background, pos)
            black_inventory.draw(background, pos)
            for tile in board_tiles:
                if clicked:
                    tile.draw(background, pos, True)
                    if tile.under_mouse(pos) and state.moving_piece is None and tile.has_pieces():
                        state.add_moving_piece(tile.pieces[-1])
                else:
                    tile.draw(background, pos)
            if state.moving_piece:
                draw_drag(background, pos, state.moving_piece)
            state.turn_panel.draw(background, state.turn)
            # pg.draw.circle(background, (1, 250, 1), (440, 380), 6)
            # pg.draw.circle(background, (1, 250, 1), (0, 380), 6)
            screen.blit(background, (0, 0))
            pg.display.flip()

            # if game_is_over(state):
            #     state.end_game()

    # print('game over')
    # return state.play_new_game
    return 0


def draw_drag(background, pos, piece=None):
    pg.draw.line(background, pg.Color('red'), pos, piece.old_pos)


main()
