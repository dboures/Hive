import pygame as pg
import numpy as np
from tile import Tile, initialize_grid
from start_menu import start_menu
from game_state import Game_State
from inventory import Inventory

DARK = (137, 137, 137)
WHITE = (255, 255, 255)

# https://www.redblobgames.com/grids/hexagons/
#https://stackoverflow.com/questions/56984542/is-there-an-effiecient-way-of-making-a-function-to-drag-and-drop-multiple-pngs

# Inititalize the pygame
pg.init()

# Create the screen
WIDTH, HEIGHT = 900, 900  # TODO: Autosense window??
screen = pg.display.set_mode((WIDTH, HEIGHT))

# Background
background = pg.Surface(screen.get_size())
background.fill((0, 0, 0))

#Title and Icon
pg.display.set_caption("Hive")
# TODO: Icon not working on Ubuntu?? It works on windows though
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)

tiles = initialize_grid(HEIGHT, WIDTH, radius=20)

game_state = Game_State()

inv_dark = Inventory(DARK)
inv_white = Inventory(WHITE)

clicked = False
have_piece = False

while game_state.running:
    while game_state.menu_loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_state.quit()
                break
            start_menu(screen, game_state, event)

    while game_state.main_loop:
        pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_state.quit()
                break
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    game_state.toggle_inventory()
                if event.key == pg.K_TAB:
                    old_tile = [x for x in tiles if x.piece is not None][0]
                    new_tile = tiles[np.random.randint(0,len(tiles))]

                    old_tile.move_piece(new_tile)
                    # get first tile with piece
                    # move piece to random tile

                    #
            if event.type == pg.MOUSEBUTTONDOWN:
                clicked = True
            if event.type == pg.MOUSEBUTTONUP:
                clicked = False
                    
        #only draw tiles once in a for loop
        background.fill((180, 180, 180))
        for tile in tiles:
            tile.draw(background,pos,clicked)
        if game_state.inventory_open:
            inv_dark.draw_inventory(background)
        if have_piece:
            draw_drag(background, )
        pg.draw.circle(background, (1, 250, 1), (450, 450), 6)
        screen.blit(background, (0, 0))
        pg.display.flip()




def draw_drag(background, pos, piece = None):
    if piece:

        color, type = selected_piece[0]

        pos = pg.Vector2(pg.mouse.get_pos())
        screen.blit(s2, s2.get_rect(center=pos + (1, 1)))
        screen.blit(s1, s1.get_rect(center=pos))
        selected_rect = pygame.Rect(BOARD_POS[0] + selected_piece[1] * TILESIZE, BOARD_POS[1] + selected_piece[2] * TILESIZE, TILESIZE, TILESIZE)
        pg.draw.line(screen, pygame.Color('red'), selected_rect.center, pos)
        return (x, y)




# selected_piece = None
#     drop_pos = None
#     while True:
#         piece, x, y = get_square_under_mouse(board)
#         events = pygame.event.get()
#         for e in events:
#             if e.type == pygame.QUIT:
#                 return
#             if e.type == pygame.MOUSEBUTTONDOWN:
#                 if piece != None:
#                     selected_piece = piece, x, y
#             if e.type == pygame.MOUSEBUTTONUP:
#                 if drop_pos:
#                     piece, old_x, old_y = selected_piece
#                     board[old_y][old_x] = 0
#                     new_x, new_y = drop_pos
#                     board[new_y][new_x] = piece
#                 selected_piece = None
#                 drop_pos = None

#         screen.fill(pygame.Color('grey'))
#         screen.blit(board_surf, BOARD_POS)
#         draw_pieces(screen, board, font, selected_piece)
#         draw_selector(screen, piece, x, y)
#         drop_pos = draw_drag(screen, board, selected_piece, font)

#         pygame.display.flip()
#         clock.tick(60)