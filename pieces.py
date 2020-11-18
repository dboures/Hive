import numpy as np
import pygame as pg


class Queen:
    def __init__(self):
        self.image = pg.image.load('images/Queen.png')

    def draw(self, surface, hex_pos):
        x,y = hex_pos
        pos = (x - 16, y - 14)
        surface.blit(self.image, pos)
