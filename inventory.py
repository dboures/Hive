import pygame as pg
import numpy as np
from pieces import Queen, Grasshopper, Spider, Beetle, Ant


class Inventory:
    def __init__(self, color):
        self.color = color
        self.Queen = [Queen(color)]
        self.Beetles = [Beetle(color), Beetle(color)]
        self.Grasshoppers = [Grasshopper(
            color), Grasshopper(color), Grasshopper(color)]
        self.Spiders = [Spider(color), Spider(color)]
        self.Ants = [Ant(color), Ant(color), Ant(color)]

    def draw_inventory(self, background, pos):
        WIDTH, HEIGHT = background.get_size()
        left = pos[0]
        top = HEIGHT - pos[1]

        #if self.color:
        #draw that side
        inventory_width = WIDTH / 2
        inventory_height = 160
        #print(WIDTH - inventory_width)

        inner_left = left + 5
        inner_top = top + 5
        inner_width = inventory_width - 10
        inner_height = inventory_height - 10

        back = pg.Rect(left, top, inventory_width, inventory_height)
        inner = pg.Rect(inner_left, inner_top, inner_width, inner_height)

        # still needs work
        pg.draw.rect(background, (1, 1, 1), back)
        pg.draw.rect(background, (55, 55, 55), inner)

        title_height = inner_height/8
        stock_height = inner_height * (7/8) #the remaining inventory space
        

        FONT = pg.font.SysFont("Times New Norman", 24)
        font = FONT.render('Player 1 Inventory', True, (255, 255, 255))
        title_rect = font.get_rect(center=(inner_left + inner_width/2, inner_top + title_height/2))
        rects = []
        for i in range(0,5):
            rects.append(pg.Rect(inner_left + (i * (inner_width/5)), inner_top + title_height, inner_width / 5, stock_height))

        pg.draw.rect(background, (55, 55, 55), title_rect)
        background.blit(font, title_rect)

        for rect in rects:
            pg.draw.rect(background, (np.random.randint(250), np.random.randint(250), np.random.randint(250)), rect)
            

        background.blit(font, title_rect)

        pg.display.flip()
