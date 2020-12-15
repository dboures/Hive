import socket
import pickle
from tile import Tile, Inventory_Tile
from pieces import Queen



class Client:# need to know which player we are
    def __init__(self):
        #networking vars
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host_ip = "192.168.1.30"
        self.port = 5555
        self.state = self.connect()

        #pygame vars
        self.clicked = False
        self.moving_piece = None

    def connect(self):
        try:
            self.socket.connect((self.host_ip, self.port))
            return pickle.loads(self.socket.recv(2048))
        except socket.error as e:
            print(str(e))

    def send(self, data):
        try:
            # print('data')
            # print(data)
            self.socket.send(pickle.dumps(data))
            print('sent')
            return pickle.loads(self.socket.recv(2048)) 
            # returning the same thing that you sent seems to cause an issue with pickle
            # not really sure what the deal with that is but yeah
            # I guess the solution is to create a new state object any time it needs to be disseminated to the clients
            # sending a piece doesnt work as pieces have images that cannot be pickled
        except socket.error as e:
            print(e)

    def click(self):
        self.clicked = True
    
    def unclick(self):
        self.clicked = False

    def add_moving_piece(self, piece):
        self.moving_piece = piece

    def remove_moving_piece(self):
        self.moving_piece = None

    def get_tiles_with_pieces(self, include_inventory=False): # will remove with other move logic
        tiles = []
        for tile in self.state.board_tiles:
            if include_inventory:
                if tile.has_pieces():
                    tiles.append(tile)
            elif tile.has_pieces() and type(tile) is not Inventory_Tile:
                tiles.append(tile)
        return tiles

class State:
    def __init__(self, turn, board_tiles):
        self.turn = turn
        self.board_tiles = board_tiles


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
