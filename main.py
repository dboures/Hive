import pygame as pg

#Inititalize the pygame
pg.init()

#Create the screen
screen = pg.display.set_mode((800,600))

#Title and Icon
pg.display.set_caption("Hive")
#TODO: Icon not working on Ubuntu??
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)

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
                print(pos)

    screen.fill((0,0,0))
    pg.display.update()