import socket
import os
from _thread import *
from networking import Client
import move
from tile import Tile, Start_Tile
from game_state import Game_State
from inventory_frame import Inventory_Frame
import pickle
import sys
import pygame as pg


pg.font.init()


s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host =  "192.168.1.30"
port = 5555
current_player  = 0

try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))

print('Waiting for a connection .. ')
s.listen(2)

#init_state = State(0, init_tiles[0:4])
#init_state = State(0, init_tiles)
# print(sys.getsizeof(precursor))
# print(sys.getsizeof(init_state))
# print(sys.getsizeof(WIDTH))
# print(len(init_state.board_tiles))

# s3 = State(0, [Tile((400,400), (0,0), 20, (1,1,1)), Tile((400,640), (0,0), 20, (1,1,1)), Tile((400,170), (0,0), 20, (1,1,1)), Tile((400,325), (0,0), 20, (1,1,1)), Tile((400,80), (0,0), 20, (1,1,1)), Tile((400,400), (0,0), 20, (1,1,1)), Tile((50,400), (0,0), 20, (1,1,1))])
# print(type(s3))
# print(type(init_state))

# print(s3.turn)
# print(init_state.turn)

# print(sys.getsizeof(s3.board_tiles))
# print(sys.getsizeof(init_state.board_tiles))


# print(s3.board_tiles)
# print(init_state.board_tiles)


def threaded_client(conn):
    conn.send(pickle.dumps('start')) #init will eventually go here
    while True:
        try:
            data = pickle.loads(conn.recv(2048 * 2))
            # print(type(data))
            # print(data.old_coords)
            # print(data.new_coords)
            print('pickle load data')
            print(data.player)
            #reply = None
            print('reply done')
            if not data:
                print('disconnected')
                break
            else:
                print('else')
                reply = move.Move(data.player, data.old_coords, data.new_coords) # make new state so no pickle error, double check if i need to do that tho
                print('reply made')
                # if player == 0:
                #     reply = states[0]
                # else:
                #     reply = states[1]
                print('Received: ', data)
                print('Sending: ', reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

while True:
    client, addr = s.accept()
    print('Connected to:' + addr[0] +':' + str(addr[1]))
    start_new_thread(threaded_client, (client, ))
    current_player += 1
    print('Thread Number: ' + str(current_player))

s.close()
