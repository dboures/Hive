import pygame as pg

#Inititalize the pygame
pg.init()

#Title and Icon
pg.display.set_caption("Hive")
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)

#Create the screen
screen = pg.display.set_mode((800,600))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False