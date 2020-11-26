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

        #probably going to want to enforce player turns in here somehow

    def start_game(self):
        self.menu_loop = False
        self.main_loop = True

    def quit(self):
        self.running = False
        self.menu_loop = False
        self.main_loop = False

    def add_moving_piece(self, piece):
        self.moving_piece = piece

    def remove_moving_piece(self):
        self.moving_piece = None

    def click(self):
        self.clicked = True
    
    def unclick(self):
        self.clicked = False

    def add_tiles(self, tiles):
        self.tiles = self.board_tiles.extend(tiles) 
