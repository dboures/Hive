import socket
import os
from _thread import *
from networking import Client
from tile import Tile, Start_Tile, initialize_grid
from game_state import Game_State
from inventory_frame import Inventory_Frame
from move_checker import is_valid_move
import pickle
import sys
import pygame as pg
import move
from pieces import Queen


pg.font.init()

sys.setrecursionlimit(10**6)
WIDTH, HEIGHT = 880, 900
s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host =  "192.168.1.30"
port = 5555

try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))

print('Waiting for a connection .. ')
s.listen(2)

games = {}
idCount = 0

def threaded_client(conn, current_player, gameId):
    global idCount
    conn.send(pickle.dumps(current_player)) #not sure what should be sent here
    while True:
        try:
            data = pickle.loads(conn.recv(2048 * 200))
            # print(type(data))
            # print(data.old_coords)
            # print(data.new_coords)
            if not data:
                pass
            elif data == "get_state":
                print('get_state')
                reply = games[gameId]
                conn.sendall(pickle.dumps(reply))
                print('Sent reply')

            elif data == "get_turn_and_board":
                # print('get_board')
                reply = (games[gameId].turn ,games[gameId].board_tiles)
                conn.sendall(pickle.dumps(reply))
                # print('Sent reply')

            elif type(data) is Game_State:
                print('Received game state')
                games[gameId] = data
                reply = data
                conn.sendall(pickle.dumps(reply))
                print('Sent reply')

            elif type(data) is list: #assume its a board for now
                print('Received game board')

                for tile in data:
                    for piece in tile.pieces:
                        print(piece.old_pos)
                        print(type(piece))
                        print(tile.coords)
                #         if type(piece) is Queen and tile.coords == (440, 380):
                #             print('Queen in middle')

                games[gameId].board_tiles = data
                reply = data
                conn.sendall(pickle.dumps(reply))
                print('Sent reply')

            elif type(data) is move.Move: #assume its a board for now
                print('Received move')
                reply = False
                playerid = data.player
                games[gameId].add_moving_piece(data.piece)
                old_coords = data.old_coords
                new_coords = data.new_coords
                print(playerid, old_coords, new_coords)

                if games[gameId].player_can_move(playerid):
                    print(str(playerid) + ' can move')
                    old_tile = next(
                        (tile for tile in games[gameId].board_tiles if tile.coords == old_coords), None)
                    new_tile = next(
                        (tile for tile in games[gameId].board_tiles if tile.coords == new_coords), None)
                    print(old_tile, new_tile)
                    #send old_tile, new_tile
                    if is_valid_move(games[gameId], old_tile, new_tile):
                        print('move is valid')
                        old_tile.move_piece(new_tile)
                        games[gameId].next_turn()
                        reply = True
                        print('reply created')
                        # if player_has_no_moves(state):
                        #     print('player has no moves')
                        #     state.open_popup()
                conn.sendall(pickle.dumps(reply))
                print('Sent reply')
                games[gameId].remove_moving_piece() # clunky but hope it works
        except:
            break

    print("Lost Connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()

while True:
    conn, addr = s.accept()
    print('Connected to:' + addr[0] +':' + str(addr[1]))
    idCount += 1
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        print("Creating a new game...")
        new_game = Game_State(initialize_grid(HEIGHT - 200, WIDTH, radius=20))
        new_game.start_game() # going to handle waiting here eventually
        games[gameId] = new_game
        start_new_thread(threaded_client, (conn, 0, gameId)) 
    else:
        start_new_thread(threaded_client, (conn, 1, gameId))
        
    print('Thread Number: ' + str(idCount))


s.close()
