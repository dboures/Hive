import pygame as pg
import numpy as np
from helper import Tile

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


#Initialize grid
hex_radius = 20 # move this somewhere?
y_range = list(range(HEIGHT + hex_radius, 0, -2 * (hex_radius) + 6)) #How is this 6 determined?
x_range = list(range(0, WIDTH + hex_radius, 2 * hex_radius))
odd_y = y_range[1::2]
tiles = []
for y in y_range:
    for x in x_range:
        if y in odd_y:
            tiles.append(Tile((x + hex_radius, y), hex_radius + 1))
        else: 
            tiles.append(Tile((x, y), hex_radius + 1))


#menu stuff here

running = True
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