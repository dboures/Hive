import numpy as np
import pygame as pg


class Tile:
    def __init__(self, coord_pair, radius):
        self.coords = coord_pair
        self.side = radius
        self.outer = get_hex_points(coord_pair, radius)
        #self.inner = get_hex_points(coord_pair, radius * 0.8) #maybe we don't need

    def draw_blank(self, surface):
        pg.draw.polygon(surface, (250,250,250), self.outer)

    def draw_clicked(self, surface):
        pg.draw.polygon(surface, (1,1,250), self.outer)

    def was_clicked(self, pos):
        if distance(self.coords, pos) < self.side - 1:
            return True
        else:
            return False

def distance(pair_one, pair_two):
    x1,y1 = pair_one
    x2,y2 = pair_two
    return np.sqrt( ((x1- x2)* (x1 - x2)) + ((y1- y2)* (y1 - y2)) )


def get_hex_points(coord_pair, side):
    x,y = coord_pair

    return ( # has to be in a certain order i guess?
    (x, y + side), # top
    (x - ((side * np.sqrt(3))/2), y + (side / 2)), # top-left
    (x - ((side * np.sqrt(3))/2), y - (side / 2)), # bottom-left
    (x, y - side), # bottom
    (x + ((side * np.sqrt(3))/2), y - (side / 2)), # bottom-right
    (x + ((side * np.sqrt(3))/2), y + (side / 2)) # top-right
    )

