import numpy as np
import pygame as pg
from pieces import Queen, Grasshopper, Spider, Beetle, Ant

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK = (137, 137, 137)


class Tile:
    def __init__(self, coord_pair, radius, piece=None):
        self.coords = coord_pair
        self.radius = radius
        self.hex = get_hex_points(coord_pair, radius)
        self.hex_select = get_hex_points(coord_pair, radius * 1.1)
        self.color = WHITE
        self.piece = piece

        selector = np.random.randint(1, 50)
        if selector == 1:
            self.add_piece(Queen())
        elif selector == 2:
            self.add_piece(Grasshopper())
        elif selector == 3:
            self.add_piece(Spider())
        elif selector == 4:
            self.add_piece(Beetle())
        elif selector == 5:
            self.add_piece(Ant())

        # color = np.random.randint(1,3)
        # if color > 1:
        #     self.color = DARK

    def draw(self, surface, pos, clicked=False): # pos to None as default?
        # if mouse, determine select or click then draw
        if self.under_mouse(pos):
            if clicked:
                pg.draw.polygon(surface, (250, 1, 1), self.hex)
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
        if new_tile is not None and new_tile.coords != self.coords:
            new_tile.add_piece(self.piece)
            self.remove_piece()


def distance(pair_one, pair_two):
    x1, y1 = pair_one
    x2, y2 = pair_two
    return np.sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)))


def get_hex_points(coord_pair, radius):
    x, y = coord_pair

    return (  # has to be in a certain order i guess?
        (x, y + radius),  # top
        (x - ((radius * np.sqrt(3))/2), y + (radius / 2)),  # top-left
        (x - ((radius * np.sqrt(3))/2), y - (radius / 2)),  # bottom-left
        (x, y - radius),  # bottom
        (x + ((radius * np.sqrt(3))/2), y - (radius / 2)),  # bottom-right
        (x + ((radius * np.sqrt(3))/2), y + (radius / 2))  # top-right
    )


def initialize_grid(height, width, radius):
    hex_radius = radius  # move this somewhere?
    # How is this 6 determined?
    y_range = list(range(height + hex_radius, 0, -2 * (hex_radius) + 6))
    x_range = list(range(0, width + hex_radius, 2 * hex_radius))
    odd_y = y_range[1::2]
    tiles = []
    for y in y_range:
        for x in x_range:
            if y in odd_y:
                tiles.append(Tile((x + hex_radius, y), hex_radius + 1))
            else:
                tiles.append(Tile((x, y), hex_radius + 1))
    return tiles
