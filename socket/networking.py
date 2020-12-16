import socket
import pickle
import move
from tile import Tile, Inventory_Tile
from pieces import Queen



class Client:# need to know which player we are
    def __init__(self):
        #networking vars
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host_ip = "192.168.1.30"
        self.port = 5555
        self.connect()

    def connect(self): # want to assign player_id first time we connect
        try:
            self.socket.connect((self.host_ip, self.port))
            return pickle.loads(self.socket.recv(2048 * 2))
        except socket.error as e:
            print(str(e))

    def send_and_update(self, data, state):
        try:
            self.socket.send(pickle.dumps(data))
            #print('sent')
            data = pickle.loads(self.socket.recv(2048 * 2)) # just send a pair of axial coords
            #self.turn = new_state.turn
            #print('received response')
            if type(data) == move.Move:
                print('moving')
                old_tile = state.get_tile_by_pos(data.old_coords)
                new_tile = state.get_tile_by_pos(data.new_coords)
                print(old_tile.pieces)
                old_tile.move_piece(new_tile)
                state.remove_moving_piece()
            else:
                #print('data was not a move')
                pass
        except socket.error as e:
            print(e)