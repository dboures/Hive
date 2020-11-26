import pygame as pg
import numpy as np
from pieces import Queen, Grasshopper, Spider, Beetle, Ant
from tile import Tile

BLACK = (71, 71, 71)
WHITE = (255, 255, 255)

# white is on the left


class Inventory:
    def __init__(self, background, pos, white=True):
        WIDTH, HEIGHT = background.get_size()
        left = pos[0]
        top = HEIGHT - pos[1]
        self.white = white

        inventory_width = WIDTH / 2
        inventory_height = 160

        inner_left = left + 5
        inner_top = top + 5
        inner_width = inventory_width - 10
        inner_height = inventory_height - 10

        self.back_panel = pg.Rect(
            left, top, inventory_width, inventory_height)
        self.inner_panel = pg.Rect(
            inner_left, inner_top, inner_width, inner_height)

        title_height = inner_height/8
        stock_height = inner_height * (7/8)  # the remaining inventory space
        stock_width = inner_width / 5

        self.tile_rects = []
        self.tiles = []
        if white:
            color = WHITE
        else:
            color = BLACK
        for i in range(0, 5):
            self.tile_rects.append(pg.Rect(inner_left + (i * stock_width) + 2, inner_top +
                                 title_height + 2, stock_width - 4, stock_height - 4))
            #if i == 0:
            self.tiles.append([Tile(
                (inner_left + (i * stock_width) + (stock_width / 2), inner_top + title_height + stock_height / 2)
                ,radius=20, piece=Queen(WHITE))])

        FONT = pg.font.SysFont("Times New Norman", 24)
        if self.white:
            self.font = FONT.render('White (Player 1) Inventory', True, (255, 255, 255))
        else:
            self.font = FONT.render('Black (Player 2) Inventory', True, (255, 255, 255))
        self.title_rect = self.font.get_rect(center=(
            inner_left + inner_width/2, inner_top + title_height/2))

        # if white:  # should always know where they need to be
        #     self.tiles = [[Tile(()), radius= 20, piece=Queen(WHITE)], [Beetle(WHITE), Beetle(WHITE)],
        #                   [Grasshopper(WHITE), Grasshopper(
        #                       WHITE), Grasshopper(WHITE)],
        #                   [Spider(WHITE), Spider(WHITE)],  [Ant(WHITE), Ant(WHITE), Ant(WHITE)]]
        # # else:
        # #     self.tiles = [[Queen(BLACK)], [Beetle(BLACK), Beetle(BLACK)],
        # #                   [Grasshopper(BLACK), Grasshopper(
        # #                       BLACK), Grasshopper(BLACK)],
        # #                   [Spider(BLACK), Spider(BLACK)],  [Ant(BLACK), Ant(BLACK), Ant(BLACK)]]

    def draw_inventory(self, background, pos, clicked=False, moving_piece=None):

        # still needs work
        pg.draw.rect(background, (1, 1, 1), self.back_panel)
        pg.draw.rect(background, (55, 55, 55), self.inner_panel)
        pg.draw.rect(background, (55, 55, 55), self.title_rect)
        for i in range(0,len(self.tile_rects)):
            pg.draw.rect(background, (137, 137, 137), self.tile_rects[i])
            for tile in self.tiles[i]: 
                # kind of feels like these tiles should be in the main tiles list
                # not sure how to get these things to talk to each other though
                if clicked:
                    tile.draw(background, tile.coords, clicked)
                    if tile.under_mouse(tile.coords) and moving_piece is None:
                        moving_piece = tile.piece
                else:
                    tile.draw(background, tile.coords)#messy

        background.blit(self.font, self.title_rect)
        pg.display.flip()
