class Game_State:
    def __init__(self, tiles = [], white_inventory=None, black_inventory=None):
        #menu attributes
        self.running = True
        self.menu_loop = True
        self.main_loop = False
        #board attributes
        self.board_tiles = tiles
        self.white_inventory = white_inventory
        self.black_inventory = black_inventory
        #action attributes
        self.clicked = False
        self.moving_piece = None

    def start_game(self):
        self.menu_loop = False
        self.main_loop = True

    def quit(self):
        self.running = False
        self.menu_loop = False
        self.main_loop = False

