import numpy as np
import pygame as pg
import statistics
from pieces import Queen, Grasshopper, Spider, Beetle, Ant

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)
DARK = (137, 137, 137)


class Tile:
    def __init__(self, coord_pair, axial_coords, radius, color, piece=None):
        self.coords = coord_pair
        self.axial_coords = axial_coords
        self.radius = radius
        self.hex = get_hex_points(coord_pair, radius)
        self.hex_select = get_hex_points(coord_pair, radius * 1.1)
        self.color = color
        self.piece = piece

        # selector = np.random.randint(1, 50)
        # if selector == 1:
        #     self.add_piece(Queen())
        # elif selector == 2:
        #     self.add_piece(Grasshopper())
        # elif selector == 3:
        #     self.add_piece(Spider())
        # elif selector == 4:
        #     self.add_piece(Beetle())
        # elif selector == 5:
        #     self.add_piece(Ant())

        # color = np.random.randint(1,3)
        # if color > 1:
        #     self.color = DARK

    def draw(self, surface, pos, clicked=False):  # pos to None as default?
        # if mouse, determine select or click then draw
        if self.under_mouse(pos):
            if clicked:
                pg.draw.polygon(surface, (250, 1, 1), self.hex)
                #print(self.axial_coords)
            else:
                pg.draw.polygon(surface, (250, 1, 1), self.hex_select)
                pg.draw.polygon(surface, self.color, self.hex)
        else:
            pg.draw.polygon(surface, self.color, self.hex)
        if self.piece:
            self.piece.draw(surface, self.coords)

    def under_mouse(self, pos):
        if distance(self.coords, pos) < self.radius - 1:
            return True
        else:
            return False

    def add_piece(self, piece):
        self.piece = piece
        self.piece.update_pos(self.coords)
        self.color = piece.color

    def remove_piece(self):
        self.piece = None
        self.color = WHITE

    def move_piece(self, new_tile):
        new_tile.add_piece(self.piece)
        self.remove_piece()
        

    def set_coords_inventory(self, coord_pair):
        self.coords = coord_pair

    def is_hive_adjacent(self, state):
        print(len(state.board_tiles))
        for tile in self.get_adjacent_tiles(self.axial_coords, state):
            if tile.piece is not None:
                return True
        return False

    def get_adjacent_tiles(self, axial_coords, state):
        q,r = axial_coords
        adjacent_tiles = []
        #print([(q, r - 1), (q + 1, r - 1), (q + 1, r), (q, r + 1), (q - 1, r + 1), (q - 1, r)])
        #print(self.axial_coords)
        for tile in state.board_tiles:
            if tile.axial_coords in [(q, r - 1), (q + 1, r - 1), (q + 1, r), (q, r + 1), (q - 1, r + 1), (q - 1, r)]:
                adjacent_tiles.append(tile)
        return adjacent_tiles



class Inventory_Tile(Tile):
    def __init__(self, coord_pair, axial_coords, radius, color, piece):
        super().__init__(coord_pair, axial_coords, radius, color, piece)

class Start_Tile(Tile):
    def __init__(self, coord_pair, axial_coords, radius, color, piece):
        super().__init__(coord_pair, axial_coords, radius, (1,1,250), piece)

def distance(pair_one, pair_two):
    x1, y1 = pair_one
    x2, y2 = pair_two
    return np.sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)))


def get_hex_points(coord_pair, radius):
    x, y = coord_pair

    return (  # has to be in counterclockwise order for drawing
        (x, y + radius),  # top
        (x - ((radius * np.sqrt(3))/2), y + (radius / 2)),  # top-left
        (x - ((radius * np.sqrt(3))/2), y - (radius / 2)),  # bottom-left
        (x, y - radius),  # bottom
        (x + ((radius * np.sqrt(3))/2), y - (radius / 2)),  # bottom-right
        (x + ((radius * np.sqrt(3))/2), y + (radius / 2))  # top-right
    )


def initialize_grid(height, width, radius): #as far as intuitiveness goes, this function is a mess
    hex_radius = radius  # move this somewhere?
    # How is this 6 determined?
    pixel_y = list(range(height + hex_radius, 0, -2 * (hex_radius) + 6))
    pixel_x = list(range(0, width + hex_radius, 2 * hex_radius))
    axial_r = list(range((len(pixel_y) // 2) - 1, -(1 * len(pixel_y) // 2) - 1, -1))
    odd_y = pixel_y[1::2]
    tiles = []
    for j in range(0, len(pixel_y)):
        for k in range(0,len(pixel_x)):
            if pixel_y[j] in odd_y:
                tiles.append(Tile((pixel_x[k] + hex_radius, pixel_y[j]), (((j + 1) // 2) + k - 16, axial_r[j]), hex_radius + 1, WHITE))
            else:
                if pixel_x[k] == 440 and pixel_y[j] == 380: #middle tile
                    tiles.append(Start_Tile((pixel_x[k], pixel_y[j]), (((j + 1) // 2) + k - 16, axial_r[j]), hex_radius + 1, WHITE, None))
                else:
                    tiles.append(Tile((pixel_x[k], pixel_y[j]), (((j + 1) // 2) + k - 16, axial_r[j]), hex_radius + 1, WHITE))
    return tiles
