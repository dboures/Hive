from tile import Inventory_Tile

class Game_State:
    def __init__(self, tiles = [], white_inventory=None, black_inventory=None):
        #menu attributes
        self.running = True
        self.menu_loop = True
        self.main_loop = False
        self.end_loop = False
        #board attributes
        self.board_tiles = tiles
        self.white_inventory = white_inventory
        self.black_inventory = black_inventory
        #action attributes
        self.clicked = False
        self.moving_piece = None

        self.turn = 1

    def start_game(self):
        self.menu_loop = False
        self.main_loop = True

    def end_game(self):
        self.main_loop = False
        self.end_loop = True

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
        self.turn += 1

    def is_player_turn(self):
        if self.moving_piece.color == (250, 250, 250) and self.turn % 2 == 1:
            return True
        elif self.moving_piece.color == (71, 71, 71) and self.turn % 2 == 0:
            return True
        else:
            return False
    
    def get_tiles_with_pieces(self):
        tiles = []
        for tile in self.board_tiles:
            if tile.has_pieces() and type(tile) is not Inventory_Tile:
                tiles.append(tile)
        return tiles

    def game_is_over(self):
        # obtain queen tiles
        # if white surronded and black surrounded -> draw
        # elif white surrounded -> black win
        #elif black surr -> white win
        # else:
        #     pass

        queen_tiles = []
        for tile in self.get_tiles_with_pieces():
            for piece in tile.pieces:
                if type(piece) is Queen:
                    queen_tiles.append(tile)
                    break


    def update_adjacent_tiles(self):
        for tile in self.board_tiles:
            tile.set_adjacent_tiles(self.board_tiles)
