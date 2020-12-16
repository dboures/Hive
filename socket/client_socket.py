import pygame as pg
import numpy as np
from tile import Tile, Inventory_Tile, initialize_grid
from move_checker import is_valid_move, game_is_over, player_has_no_moves
from menus import start_menu, end_menu, no_move_popup
from game_state import Game_State
from networking import Client
import move
from inventory_frame import Inventory_Frame
from turn_panel import Turn_Panel
import socket
import pickle

pg.font.init()



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
    
    state = Game_State(initialize_grid(HEIGHT - 200, WIDTH, radius=20))

    state.start_game()
    print('about to run')

    while state.running:
        while state.main_loop: #state.main_loop:
            new_move = 'pass'
            #update inventories and turn panel for drawing
            pos = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    state.quit()
                    break
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_TAB:
                        tile = next(
                            (tile for tile in state.board_tiles if tile.under_mouse(pos)), None)
                        q,r = tile.axial_coords
                        print(q,r)
                    if event.key == pg.K_ESCAPE:
                        state.quit()
                        break
                    # if event.key == pg.K_PAGEUP:
                    #     client.state.open_popup()
                if event.type == pg.MOUSEBUTTONDOWN:
                    state.click()
                if event.type == pg.MOUSEBUTTONUP:
                    state.unclick()
                    

                    if state.moving_piece and state.is_player_turn():
                        old_tile = next(
                            tile for tile in state.board_tiles if  (tile.has_pieces() and tile.pieces[-1] == state.moving_piece))
                        new_tile = next(
                            (tile for tile in state.board_tiles if tile.under_mouse(pos)), None)
                        
                        # if is_valid_move(client, old_tile, new_tile):
                            # old_tile.move_piece(new_tile)
                            # client.next_turn()

                            # send client.state to server, for now server will just disseminate
                        new_move = move.Move(state.turn % 2, old_tile.coords, new_tile.coords)
                        


                            # if player_has_no_moves(client):
                            #     print('player has no moves')
                            #     client.open_popup()

            client.send_and_update(new_move, state)       
            # only draw tiles once in a for loop
            background.fill((180, 180, 180))
            state.white_inventory.draw(background, pos)
            state.black_inventory.draw(background, pos)
            for tile in state.board_tiles:
                if state.clicked:
                    tile.draw(background, pos, state.clicked)
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
