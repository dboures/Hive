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
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                pos = pg.mouse.get_pos()
                #TODO: create hex and get position to print what hex we are in
                #Use axial coords
                pg.draw.polygon(background, (255,1,1), get_hex_points(pos, 20))
                pg.draw.polygon(background, (250,250,250), get_hex_points(pos, 16))
                print(pos)

    screen.blit(background, (0, 0))
    pg.display.update()