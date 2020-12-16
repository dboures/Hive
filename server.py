import socket
import os
from _thread import *
from networking import Client
from tile import Tile, Start_Tile, initialize_grid
from game_state import Game_State
from inventory_frame import Inventory_Frame
import pickle
import sys
import pygame as pg


pg.font.init()

sys.setrecursionlimit(10**6)
WIDTH, HEIGHT = 880, 900
s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host =  "192.168.1.30"
port = 5555
current_player  = 0

init_state = Game_State(initialize_grid(HEIGHT - 200, WIDTH, radius=20))

init_state.start_game()

try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))

print('Waiting for a connection .. ')
s.listen(2)

def threaded_client(conn, state):
    conn.send(pickle.dumps('start')) #init will eventually go here
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
                reply = state
                conn.sendall(pickle.dumps(state))
                print("sent state")
            elif type(data) is Game_State:
                print('Received: ', data)
                state = data
                reply = state
                conn.sendall(pickle.dumps(state))
                print('Sending: ', reply)
        except:
            break

# """Using the below function, we broadcast the message to all  
# clients who's object is not the same as the one sending  
# the message """
# def broadcast_move(data):  
#     for conn in conn_list: 
#         try:
#             print('Broadcasting: ', data)  
#             conn.sendall(pickle.dumps(data))  
#         except:  
#             print('broadcast error')
#             # clients.close()  
#             # # if the link is broken, we remove the client  
#             # remove(clients) 


conn_list = []
while True:
    conn, addr = s.accept()
    conn_list.append(conn)
    print('Connected to:' + addr[0] +':' + str(addr[1]))
    start_new_thread(threaded_client, (conn,init_state ))
    current_player += 1
    print('Thread Number: ' + str(current_player))

s.close()





# clients = set()
# clients_lock = threading.Lock()

# def listener(client, address):
#     print "Accepted connection from: ", address
#     with clients_lock:
#         clients.add(client)
#     try:    
#         while True:
#             data = client.recv(1024)
#             if not data:
#                 break
#             else:
#                 print repr(data)
#                 with clients_lock:
#                     for c in clients:
#                         c.sendall(data)
#     finally:
#         with clients_lock:
#             clients.remove(client)
#             client.close()