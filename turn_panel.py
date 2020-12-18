import pygame as pg
import numpy as np
from pieces import Queen, Grasshopper, Spider, Beetle, Ant
from tile import Inventory_Tile

BLACK = (71, 71, 71)
WHITE = (250, 250, 250)

# white is on the left
class Turn_Panel: #Once we get a client, want to remind players what color they are
    def __init__(self):
        WIDTH, HEIGHT = 880, 900

        outline_width = WIDTH / 4
        outline_height = 40

        self.inner_left = 5
        self.inner_top = 5
        self.inner_width = outline_width - 10
        self.inner_height = outline_height - 10

        self.back_panel = pg.Rect(
            0, 0, outline_width, outline_height)
        self.inner_panel = pg.Rect(
            self.inner_left, self.inner_top, self.inner_width, self.inner_height)

    def draw(self, background, turn, player):
        FONT = pg.font.SysFont("Times New Norman", 32)
        if (turn - 1) % 2 == player: # turn starts at 1
            font = FONT.render(
                'Your Turn:', True, (255, 255, 255))
        else:
            font = FONT.render(
                'Opponent Turn:', True, (255, 255, 255))
        title_rect = font.get_rect(center=(
            self.inner_left + self.inner_width * (2/5), self.inner_top + self.inner_height/2))

        # still needs work
        pg.draw.rect(background, (1, 1, 1), self.back_panel)
        pg.draw.rect(background, (55, 55, 55), self.inner_panel)

        if turn % 2 == 1:
            pg.draw.circle(background, (250, 250, 250), (self.inner_left + self.inner_width * (7/8), self.inner_top + self.inner_height/2), 13)
        else:
            pg.draw.circle(background, (1, 1, 1), (self.inner_left + self.inner_width * (7/8), self.inner_top + self.inner_height/2), 13)
            #just like the inventory, we want to change some colors but whatever for now


        background.blit(font, title_rect)
        pg.display.flip()