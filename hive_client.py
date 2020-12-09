import pygame as pg
import numpy as np
from tile import Tile, initialize_grid
from move_checker import is_valid_move, game_is_over, player_has_no_moves
from menus import start_menu, end_menu, no_move_popup
from game_state import Game_State
from inventory_frame import Inventory_Frame
from turn_panel import Turn_Panel
from network import Network

#need a client somewhere

def Hive():
    print('new game')
    WHITE = (250, 250, 250)

    # https://www.redblobgames.com/grids/hexagons/
    # https://stackoverflow.com/questions/56984542/is-there-an-effiecient-way-of-making-a-function-to-drag-and-drop-multiple-pngs

    # Inititalize the pygame
    pg.init()

    # Create the screen
    WIDTH, HEIGHT = 880, 900  # TODO: Autosense window??
    screen = pg.display.set_mode((WIDTH, HEIGHT))

    # Background
    background = pg.Surface(screen.get_size())
    background.fill((0, 0, 0))

    #Title and Icon
    pg.display.set_caption("Hive")
    # TODO: Icon not working on Ubuntu?? It works on windows though
    icon = pg.image.load('icon.png')
    pg.display.set_icon(icon)

    #group these into an initialize function somewhow, so we can reinitialize when newgame is hit
    state = Game_State(initialize_grid(HEIGHT - 200, WIDTH, radius=20))

    #probably want to pass the state object back and forth between clients and the server
    #make it so that you can't do anything when it's not your turn (client is assigned to player)
    while state.running:
        while state.menu_loop:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    state.quit()
                    break
                start_menu(screen, state, event)

        while state.move_popup_loop:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    state.quit()
                    break
                no_move_popup(screen, background, state, event)

        while state.main_loop:
            pos = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    state.quit()
                    break
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_TAB:
                        tile = next(
                            (tile for tile in state.board_tiles if tile.under_mouse(pos)), None)
                        q,r = tile.axial_coords
                        print(q,r)
                        #print([at.pieces for at in tile.adjacent_tiles]) # -q-r third cube coord
                        #print('turn #: ' + str(state.turn))
                    if event.key == pg.K_ESCAPE:
                        state.quit()
                        break
                    if event.key == pg.K_PAGEUP:
                        state.open_popup()
                if event.type == pg.MOUSEBUTTONDOWN:
                    state.click()
                if event.type == pg.MOUSEBUTTONUP:
                    state.unclick()
                    if state.moving_piece and state.is_player_turn():
                        old_tile = next(
                            tile for tile in state.board_tiles if  (tile.has_pieces() and tile.pieces[-1] == state.moving_piece))
                        new_tile = next(
                            (tile for tile in state.board_tiles if tile.under_mouse(pos)), None)
                        if is_valid_move(state, old_tile, new_tile):
                            old_tile.move_piece(new_tile)
                            state.next_turn()
                            if player_has_no_moves(state):
                                print('player has no moves')
                                state.open_popup()

                    state.remove_moving_piece()

            # only draw tiles once in a for loop
            background.fill((180, 180, 180))
            state.white_inventory.draw(background, pos)
            state.black_inventory.draw(background, pos)
            for tile in state.board_tiles:
                if state.clicked:
                    tile.draw(background, pos, state.clicked)
                    if tile.under_mouse(pos) and state.moving_piece is None and tile.has_pieces():
                        state.moving_piece = tile.pieces[-1]
                else:
                    tile.draw(background, pos)
            if state.moving_piece:
                draw_drag(background, pos, state.moving_piece)
            state.turn_panel.draw(background, state)
            # pg.draw.circle(background, (1, 250, 1), (440, 380), 6)
            # pg.draw.circle(background, (1, 250, 1), (0, 380), 6)
            screen.blit(background, (0, 0))
            pg.display.flip()

            if game_is_over(state):
                state.end_game()

        while state.end_loop:
            end_menu(screen, state, event) # drawing takes precedence over the close window button
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    state.quit()
                    break
    print('game over')
    return state.play_new_game

def draw_drag(background, pos, piece=None):
    pg.draw.line(background, pg.Color('red'), pos, piece.old_pos)

def test(state, tile):
        # if len(piece_tiles) > 0:
        #     print('Hive Adjacent')
        #     return True
        print('Test')
        #return False


def main():
    run_game = True
    n = Network()
    while run_game:
         run_game = Hive()

if __name__ == "__main__":
    main()
