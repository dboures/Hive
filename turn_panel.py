import pygame as pg
import numpy as np
from pieces import Queen, Grasshopper, Spider, Beetle, Ant
from tile import Inventory_Tile

BLACK = (71, 71, 71)
WHITE = (250, 250, 250)

# white is on the left
class Turn_Panel:
    def __init__(self, background, state):
        WIDTH, HEIGHT = background.get_size()

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

    def draw_turn_panel(self, background, state):
        FONT = pg.font.SysFont("Times New Norman", 32)
        if state.turn % 2 == 1:
            font = FONT.render(
                'Player 1 Turn:', True, (255, 255, 255))
        else:
            font = FONT.render(
                'Player 2 Turn:', True, (255, 255, 255))
        title_rect = font.get_rect(center=(
            self.inner_left + self.inner_width * (2/5), self.inner_top + self.inner_height/2))

        # still needs work
        pg.draw.rect(background, (1, 1, 1), self.back_panel)
        pg.draw.rect(background, (55, 55, 55), self.inner_panel)

        if state.turn % 2 == 1:#don't like that we check twice
            pg.draw.circle(background, (250, 250, 250), (self.inner_left + self.inner_width * (7/8), self.inner_top + self.inner_height/2), 13)
        else:
            pg.draw.circle(background, (1, 1, 1), (self.inner_left + self.inner_width * (7/8), self.inner_top + self.inner_height/2), 13)
            #just like the inventory, we want to change some colors but whatever for now


        background.blit(font, title_rect)
        pg.display.flip()