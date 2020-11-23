import pygame as pg
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

        
        title_rect = pg.Rect(inner_left, inner_top, inner_width, inner_height * (1/8))
        # rect1 = pg.Rect(button_pos, (3/9) * HEIGHT, button_width, button_height)
        # rect2 = pg.Rect(button_pos, (4/9) * HEIGHT, button_width, button_height)
        # rect3 = pg.Rect(button_pos, (5/9) * HEIGHT, button_width, button_height)
        # rect4 = pg.Rect(button_pos, (5/9) * HEIGHT, button_width, button_height)
        # rect5 = pg.Rect(button_pos, (5/9) * HEIGHT, button_width, button_height)

        FONT = pg.font.SysFont("Times New Norman", 25)
        font = FONT.render('Player 1 Inventory', True, (255, 255, 255))
        title_rect = font.get_rect(center=(inner_left + inner_width/2, inner_top + inner_height/9))
        pg.draw.rect(background, (55, 55, 55), title_rect)
        background.blit(font, title_rect)

        # font = pg.font.SysFont("Times New Norman", 25)
        # text = font.render("You win!", True, (255, 255, 255))
        # text_rect = text.get_rect(center=(inner_left + inner_width/2, inner_top - inner_height/2))
        # pg.draw.rect(background, (55, 55, 55), text_rect)
        # background.blit(text, text_rect)


        pg.display.flip()
