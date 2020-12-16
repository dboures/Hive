import pygame as pg
import numpy as np
from pieces import Queen, Grasshopper, Spider, Beetle, Ant
from tile import Inventory_Tile

BLACK = (71, 71, 71)
WHITE = (250, 250, 250)

# white is on the left
class Inventory_Frame:
    def __init__(self, pos, white=True):
        WIDTH, HEIGHT = 880, 900
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

        title_height = inner_height/10
        stock_height = inner_height * (9/10)  # the remaining inventory space
        stock_width = inner_width / 5

        self.tile_rects = []
        self.tiles = [] # pieces move, tiles dont

        if white:
            self.color = WHITE
        else:
            self.color = BLACK
        for i in range(0, 5):
            self.tile_rects.append(pg.Rect(inner_left + (i * stock_width) + 2, inner_top +
                                           title_height + 2, stock_width - 4, stock_height - 4))

            if i == 0:
                tile_pos = (inner_left + (i * stock_width) + (stock_width / 2),
                            inner_top + title_height + stock_height / 2)
                self.tiles.append(Inventory_Tile(tile_pos, (99,99), 20, self.color,
                                  piece=Queen(self.color)))
            if i == 1:
                for j in range(1, 3):
                    tile_pos = (inner_left + (i * stock_width) + (
                        stock_width / 2), inner_top + title_height + (j * stock_height / 3))
                    self.tiles.append(Inventory_Tile(tile_pos, (99,99), 20, self.color,
                                      piece=Beetle(self.color)))
            if i == 2:
                for j in range(1, 3):
                    tile_pos = (inner_left + (i * stock_width) + (
                        stock_width / 2), inner_top + title_height + (j * stock_height / 3))
                    self.tiles.append(Inventory_Tile(tile_pos, (99,99), 20, self.color,
                                      piece=Spider(self.color)))
            if i == 3:
                for j in [25, 67, 109]:
                    tile_pos = (inner_left + (i * stock_width) + (
                        stock_width / 2), inner_top + title_height + (j * stock_height / 135))
                    self.tiles.append(Inventory_Tile(tile_pos, (99,99), 20, self.color,
                                      piece=Grasshopper(self.color)))
            if i == 4:
                for j in [25, 67, 109]:
                    tile_pos = (inner_left + (i * stock_width) + (
                        stock_width / 2), inner_top + title_height + (j * stock_height / 135))
                    self.tiles.append(
                        Inventory_Tile(tile_pos, (99,99), 20, self.color, piece=Ant(self.color)))
        for tile in self.tiles:
            for piece in tile.pieces:
                piece.update_pos(tile.coords)

        FONT = pg.font.SysFont("Times New Norman", 24)
        if self.white:
            self.font = FONT.render(
                'Player 1 Inventory', True, (255, 255, 255))
        else:
            self.font = FONT.render(
                'Player 2 Inventory', True, (255, 255, 255))
        self.title_rect = self.font.get_rect(center=(
            inner_left + inner_width/2, inner_top + title_height/2))

    def draw(self, background, pos):

        # still needs work
        pg.draw.rect(background, (1, 1, 1), self.back_panel)
        pg.draw.rect(background, (55, 55, 55), self.inner_panel)
        pg.draw.rect(background, (55, 55, 55), self.title_rect)
        for i in range(0, len(self.tile_rects)):
            pg.draw.rect(background, self.color, self.tile_rects[i])

        background.blit(self.font, self.title_rect)
        pg.display.flip()

