import numpy as np
import pygame as pg


class Tile:
    def __init__(self, coord_pair, radius):
        self.coords = coord_pair
        self.side = radius
        self.hex = get_hex_points(coord_pair, radius)
        self.hex_border = get_hex_points(coord_pair, radius * 1.1) #maybe we don't need

    def draw_blank(self, surface):
        pg.draw.polygon(surface, (250, 250, 250), self.hex)

    def draw_clicked(self, surface):
        pg.draw.polygon(surface, (250, 1, 1), self.hex)

    def under_mouse(self, pos):
        if distance(self.coords, pos) < self.side - 1:
            return True
        else:
            return False

    def draw_selected(self, surface):
            pg.draw.polygon(surface, (250, 1, 1), self.hex_border)
            pg.draw.polygon(surface, (250, 250, 250), self.hex)




def distance(pair_one, pair_two):
    x1, y1 = pair_one
    x2, y2 = pair_two
    return np.sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)))


def get_hex_points(coord_pair, side):
    x, y = coord_pair

    return (  # has to be in a certain order i guess?
        (x, y + side),  # top
        (x - ((side * np.sqrt(3))/2), y + (side / 2)),  # top-left
        (x - ((side * np.sqrt(3))/2), y - (side / 2)),  # bottom-left
        (x, y - side),  # bottom
        (x + ((side * np.sqrt(3))/2), y - (side / 2)),  # bottom-right
        (x + ((side * np.sqrt(3))/2), y + (side / 2))  # top-right
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
