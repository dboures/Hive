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

        
        self.player_turn = 1 # 1 is white, 2 is black

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
    
    def next_turn(self):
        if self.player_turn == 1:
            self.player_turn = 2
        else:
            self.player_turn = 1

    def is_player_turn(self):
        if self.moving_piece.color == (250, 250, 250) and self.player_turn == 1:
            return True
        elif self.moving_piece.color == (71, 71, 71) and self.player_turn == 2:
            return True
        else:
            return False
