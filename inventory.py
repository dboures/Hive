import pygame as pg
from pieces import Queen, Grasshopper, Spider, Beetle, Ant

class Inventory:
    def __init__(self, color):
        self.Queen = [Queen(color)]
        self.Beetles = [Beetle(color), Beetle(color)]
        self.Grasshoppers = [Grasshopper(color), Grasshopper(color), Grasshopper(color)]
        self.Spiders = [Spider(color), Spider(color)]
        self.Ants = [Ant(color), Ant(color), Ant(color)]



    def draw_inventory(self, background):
        WIDTH, HEIGHT = background.get_size()
        inventory_width = WIDTH / 4
        inventory_height = HEIGHT / 4
        print(WIDTH - inventory_width)

        rect = pg.Rect(WIDTH - inventory_width, HEIGHT - inventory_height, inventory_width, inventory_height)


        #still needs work
        pg.draw.rect(background, (1,1,1), rect)

        pg.display.flip()