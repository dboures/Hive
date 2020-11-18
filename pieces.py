import numpy as np
import pygame as pg


class Piece:
    def __init__(self):
        self.image = pg.image.load('images/{}.png'.format(type(self).__name__))
        self.pos = None
        
    def getName(self):
        raise NotImplementedError #you want to override this on the child classes


class Queen(Piece):
    def __init__(self):
        super().__init__()

    def draw(self, surface, hex_pos):
        x,y = hex_pos
        pos = (x - 16, y - 14)
        surface.blit(self.image, pos)

class Ant(Piece):
    def __init__(self):
        super().__init__()

    def draw(self, surface, hex_pos):
        x,y = hex_pos
        surface.blit(self.image, hex_pos)

class Spider(Piece):
    def __init__(self):
        super().__init__()

    def draw(self, surface, hex_pos):
        x,y = hex_pos
        pos = (x - 16, y - 17)
        surface.blit(self.image, pos)

class Beetle(Piece):
    def __init__(self):
        super().__init__()

    def draw(self, surface, hex_pos):
        x,y = hex_pos
        surface.blit(self.image, hex_pos)

class Grasshopper(Piece):
    def __init__(self):
        super().__init__()

    def draw(self, surface, hex_pos):
        x,y = hex_pos
        pos = (x - 12, y - 14)
        surface.blit(self.image, pos)
