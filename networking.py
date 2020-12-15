import socket
import pickle
from tile import Tile

class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host_ip = "192.168.1.30"
        self.port = 5555
        self.connect_return = self.connect()

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
        except socket.error as e:
            print(e)
# no connection close in tims code?

class State:
    def __init__(self, player, board):
        self.player = player
        self.board = board

s1 = State(0, [Tile((1,1), (0,0), 20, (1,1,1))])
s2 = State(1, [Tile((1,1), (7,7), 20, (1,1,1))])

a = Client()
b = Client()

print(a.connect_return)
print(b.connect_return)

x = a.send(s1)
print(x)
#b.send(s2)
