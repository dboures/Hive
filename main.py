import pygame as pg
import numpy as np

#https://www.redblobgames.com/grids/hexagons/

#Inititalize the pygame
pg.init()

#Create the screen
screen_width, screen_height = 800, 800 # TODO: Autosense window??
screen = pg.display.set_mode((screen_width, screen_height))
# Background

background = pg.Surface(screen.get_size())
background.fill((250, 250, 250))

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
        self.inner = get_hex_points(coord_pair, radius * 0.8)

    def draw():
        pass
    #do I want a draw function? woud need to pass in a surface which seems undesirable



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
#Initialize grid -- have to make this stuff standardized/scalabe? probably use a tile size variable at the beginning
dist = 20
tiles = [Tile((10,860), 20)] #(0 + a/2, y - a)
for y in range (820, 0, -40):
    for x in range(0, 820, 40):
        if y % 80 != 0:
            tiles.append(Tile((x, y), 20))
        else: 
            tiles.append(Tile((x + 20, y), 20))






while running:
    for event in pg.event.get():        
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                # draw the whole grid each time, but only when someone clicks?
                for tile in tiles:
                    pg.draw.polygon(background, (255,1,1), tile.outer) # get_hex_points(pos, 20)
                    pg.draw.polygon(background, (250,250,250), tile.inner) # get_hex_points(pos, 16) 
                pos = pg.mouse.get_pos()
                #TODO: create hex and get position to print what hex we are in
                #Use axial coords
                pg.draw.circle(background, (250,1,1), (400,400), 3)
                print(pos)

    screen.blit(background, (0, 0))
    pg.display.update()