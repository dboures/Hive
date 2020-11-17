import numpy as np
import pygame as pg


class Queen:
    def __init__(self):
        self.image = pg.image.load('images/Queen.png')

    def draw(self, surface, hex_pos):
        #transform center of hex into icon position? Queen icon is top left centered
        surface.blit(self.image, pos)
