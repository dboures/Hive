import socket
import pickle
#import move
from tile import Tile, Inventory_Tile
from pieces import Queen
import sys


sys.setrecursionlimit(10**6)
class Client:# need to know which player we are
    def __init__(self):
        #networking vars
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host_ip = "192.168.1.30"
        self.port = 5555
        self.player = self.connect()

    def connect(self): # want to assign player_id first time we connect
        try:
            self.socket.connect((self.host_ip, self.port))
            return pickle.loads(self.socket.recv(2048 * 200))
        except socket.error as e:
            print(str(e))

    def get_state(self):
        try:
            self.socket.send(pickle.dumps("get_state"))
            print("state requested")
            res = self.socket.recv(2048 * 200)
            print("socket received")
            state = pickle.loads(res)
            print("unpickled")
            print("state received")
            return state

        except socket.error as e:
            print(e)

    # def send_state(self, state):
    #     try:
    #         self.socket.send(pickle.dumps(state))
    #         print("move sending")
    #         state = pickle.loads(self.socket.recv(2048 * 200))
    #         print("move received")
    #         return state

    #     except socket.error as e:
    #         print(e)

    def get_turn_and_board(self):
        try:
            self.socket.send(pickle.dumps("get_turn_and_board"))
            # print("board requested")
            data = pickle.loads(self.socket.recv(2048 * 200))
            # print("board received")
            return data

        except socket.error as e:
            print(e)

    # def send_board(self, board):
    #     try:
    #         self.socket.send(pickle.dumps(board))
    #         print("board sent")
    #         board = pickle.loads(self.socket.recv(2048 * 200))
    #         print("board received")
    #         return board

    #     except socket.error as e:
    #         print(e)

    def send_move(self, proposed_move):
        try:
            self.socket.send(pickle.dumps(proposed_move))
            print("proposed_move sent")
            response = pickle.loads(self.socket.recv(2048 * 200))
            print(response) # acceptance bool
            return

        except socket.error as e:
            print(e)
