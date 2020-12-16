import socket
from _thread import *
import sys
import pickle
from game_state import Game_State
from tile import initialize_grid
import pygame as pg

WIDTH, HEIGHT = 880, 900
server = "192.168.1.30"
port = 5555
pg.font.init()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for connection, Server Started")


def threaded_client(conn, state):
    conn.send(pickle.dumps(state))
    reply = ""
    while True:
        try:
            game_data = pickle.loads(conn.recv(2048 * 5))# larger size, longer to recive info, make it larger if there are issues


            if not game_data:
                print("Disconnected")
                break
            else:
                # if player == "WHITE":
                #     reply = ""#idk
                print("Received: ", reply)
                print("Sending :", reply)

                conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    state = Game_State(initialize_grid(HEIGHT - 200, WIDTH, radius=20))
    print(type(state))
    start_new_thread(threaded_client, (conn,state))

