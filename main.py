import pygame as pg
import numpy as np

#https://www.redblobgames.com/grids/hexagons/

#Inititalize the pygame
pg.init()

#Create the screen
WIDTH, HEIGHT = 900, 900 # TODO: Autosense window??
screen = pg.display.set_mode((WIDTH, HEIGHT))
# Background

background = pg.Surface(screen.get_size())
background.fill((250, 1, 1))

#Title and Icon
pg.display.set_caption("Hive")
#TODO: Icon not working on Ubuntu?? It works on windows though
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)


class Tile:
    def __init__(self, coord_pair, radius):
        self.coords = coord_pair
        self.side = radius
        self.outer = get_hex_points(coord_pair, radius)
        #self.inner = get_hex_points(coord_pair, radius * 0.8) #maybe we don't need

    def draw_blank(self, surface):
        pg.draw.polygon(surface, (250,250,250), tile.outer)

    def draw_clicked(self, surface):
        pg.draw.polygon(surface, (1,1,250), tile.outer)

    def was_clicked(self, pos):
        if distance(self.coords, pos) < self.side - 1:
            return True
        else:
            return False

def distance(pair_one, pair_two):
    x1,y1 = pair_one
    x2,y2 = pair_two
    return np.sqrt( ((x1- x2)* (x1 - x2)) + ((y1- y2)* (y1 - y2)) )


def get_hex_points(coord_pair, side):
    x,y = coord_pair

    return ( # has to be in a certain order i guess?
    (x, y + side), # top
    (x - ((side * np.sqrt(3))/2), y + (side / 2)), # top-left
    (x - ((side * np.sqrt(3))/2), y - (side / 2)), # bottom-left
    (x, y - side), # bottom
    (x + ((side * np.sqrt(3))/2), y - (side / 2)), # bottom-right
    (x + ((side * np.sqrt(3))/2), y + (side / 2)) # top-right
    )


running = True
#Initialize grid
hex_radius = 20 # move this somewhere?
y_range = list(range(HEIGHT + hex_radius, 0, -2 * (hex_radius) + 6)) #How is this 6 determined?
odd_y = y_range[1::2]
tiles = []
for y in y_range:
    for x in range(0, WIDTH + hex_radius, 2 * hex_radius): #consider putting this into a range as well?
        if y in odd_y:
            tiles.append(Tile((x + hex_radius, y), hex_radius + 1))
        else: 
            tiles.append(Tile((x, y), hex_radius + 1))



while running:
    for event in pg.event.get():        
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                click_pos = pg.mouse.get_pos()
                print(click_pos)
                # how do we draw the grid the first time
                for tile in tiles:
                    if tile.was_clicked(click_pos):
                        tile.draw_clicked(background)
                    else:
                        tile.draw_blank(background)

                
                    
                
                #TODO: create hex and get position to print what hex we are in
                #Use axial coords
                pg.draw.circle(background, (1,250,1), (450,450), 6)
                

    screen.blit(background, (0, 0))
    pg.display.update()