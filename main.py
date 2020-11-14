import pygame as pg

#https://www.redblobgames.com/grids/hexagons/

#Inititalize the pygame
pg.init()

#Create the screen
screen_width, screen_height = 800, 600 # TODO: Autosense window??
screen = pg.display.set_mode((screen_width, screen_height))
# Background

background = pg.Surface(screen.get_size())
background.fill((250, 250, 250))

#Title and Icon
pg.display.set_caption("Hive")
#TODO: Icon not working on Ubuntu??
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)

#pg.draw.polygon()

def get_hex_points(coord_pair, side):
    x,y = coord_pair
    #top
    (x, y + side)
    #TL
    (x - side, y)
    #TR
    # bottom
    (x, y - side)
    #BL
    #BR
    print(y)

get_hex_points((5,2))

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
                pg.draw.polygon(background, (255,1,1), ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
                print(pos)

    screen.blit(background, (0, 0))
    pg.display.update()