import numpy as np
import pygame as pg

WHITE = (255, 255, 255)
DARK = (137, 137, 137)

class Piece:
    def __init__(self, color=WHITE):
        self.image = pg.image.load('images/{}.png'.format(type(self).__name__))
        self.pos = None
        self.color = color
        
    def getName(self):
        raise NotImplementedError #you want to override this on the child classes


class Queen(Piece): # no valide
    def __init__(self, color=WHITE):
        super().__init__(color)

    def draw(self, surface, hex_pos):
        x,y = hex_pos
        pos = (x - 16, y - 14)
        surface.blit(self.image, pos)

class Ant(Piece):
    def __init__(self, color=WHITE):
        super().__init__(color)

    def draw(self, surface, hex_pos):
        x,y = hex_pos
        pos = (x - 16, y - 17)
        surface.blit(self.image, pos)

class Spider(Piece):
    def __init__(self, color=WHITE):
        super().__init__(color)

    def draw(self, surface, hex_pos):
        x,y = hex_pos
        pos = (x - 16, y - 17)
        surface.blit(self.image, pos)

class Beetle(Piece):
    def __init__(self, color=WHITE):
        super().__init__(color)

    def draw(self, surface, hex_pos):
        x,y = hex_pos
        pos = (x - 16, y - 16)
        surface.blit(self.image, pos)

class Grasshopper(Piece):
    def __init__(self, color=WHITE):
        super().__init__(color)

    def draw(self, surface, hex_pos):
        x,y = hex_pos
        pos = (x - 12, y - 14)
        surface.blit(self.image, pos)
