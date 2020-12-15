import socket
import os
from _thread import *
from networking import State
from tile import Tile
import pickle
import sys

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

s1 = State(0, [Tile((1,1), (0,0), 20, (1,1,1))])
s2 = State(1, [Tile((1,1), (7,7), 20, (1,1,1))])
s3 = State(0, [Tile((1,1), (0,0), 20, (1,1,1))])

states = [s1,s2]

print(sys.getsizeof(s1))

def threaded_client(conn, player):
    conn.send(pickle.dumps(states[player]))
    while True:
        try:
            data = conn.recv(2048)
            reply = s3
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
    start_new_thread(threaded_client, (client,current_player % 2))
    current_player += 1
    print('Thread Number: ' + str(current_player))

s.close()
