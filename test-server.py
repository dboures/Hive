import socket
import os
from _thread import *
from networking import Client, State
from tile import Tile, initialize_grid
from game_state import Game_State
import pickle
import sys
import pygame as pg

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

pg.font.init()
WIDTH, HEIGHT = 880, 900
precursor = Game_State(initialize_grid(HEIGHT - 200, WIDTH, radius=20))
init_state = State(precursor.turn, precursor.board_tiles)
print(sys.getsizeof(init_state))
print(len(init_state.board_tiles))

s3 = State(0, [Tile((1,1), (0,0), 20, (1,1,1))])

def threaded_client(conn):
    conn.send(pickle.dumps(s3)) #init will eventually go here
    print(len(init_state.board_tiles))
    while True:
        try:
            data = conn.recv(2048)
            #reply = State(data.turn, data.board_tiles) # make new state so no pickle error
            reply = s3 # make new state so no pickle error
            if not data:
                print('disconnected')
                break
            else:
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
    start_new_thread(threaded_client, (client,))
    current_player += 1
    print('Thread Number: ' + str(current_player))

s.close()
