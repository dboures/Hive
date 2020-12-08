import numpy as np
import pygame as pg
from move_checker import axial_distance, move_is_not_blocked_or_jump, path_exists, spider_path_exists, is_straight_line

WHITE = (250, 250, 250)


class Piece:
    def __init__(self, color=WHITE):
        self.image = pg.image.load('images/{}.png'.format(type(self).__name__))
        self.old_pos = None
        self.color = color

    def update_pos(self, pos):
        self.old_pos = pos

    def move_is_valid(self, state, old_tile, new_tile):
        pass


class Queen(Piece):
    def __init__(self, color=WHITE):
        super().__init__(color)

    def draw(self, surface, hex_pos):
        x, y = hex_pos
        pos = (x - 16, y - 14)
        surface.blit(self.image, pos)

    def move_is_valid(self, state, old_tile, new_tile):
        dist = axial_distance(old_tile.axial_coords, new_tile.axial_coords)
        if dist == 1 and move_is_not_blocked_or_jump(state, old_tile, new_tile):
            return True
        else:
            print('Queen move criteria violated')
            return False



class Ant(Piece):
    def __init__(self, color=WHITE):
        super().__init__(color)

    def draw(self, surface, hex_pos):
        x, y = hex_pos
        pos = (x - 16, y - 17)
        surface.blit(self.image, pos)

    def move_is_valid(self, state, old_tile, new_tile):
        if path_exists(state, old_tile, new_tile):
            return True
        else:
            print('Ant move criteria violated')
            return False

class Spider(Piece):
    def __init__(self, color=WHITE):
        super().__init__(color)

    def draw(self, surface, hex_pos):
        x, y = hex_pos
        pos = (x - 16, y - 17)
        surface.blit(self.image, pos)

    def move_is_valid(self, state, old_tile, new_tile):
        if spider_path_exists(state, old_tile, new_tile) and move_is_not_blocked_or_jump(state, old_tile, new_tile):
            return True
        else:
            print('Spider move criteria violated')
            return False

class Beetle(Piece):
    def __init__(self, color=WHITE):
        super().__init__(color)

    def draw(self, surface, hex_pos):
        x, y = hex_pos
        pos = (x - 16, y - 16)
        surface.blit(self.image, pos)

    def move_is_valid(self, state, old_tile, new_tile):
        dist = axial_distance(old_tile.axial_coords, new_tile.axial_coords)
        if dist == 1 and (move_is_not_blocked_or_jump(state, old_tile, new_tile) or new_tile.has_pieces() or len(old_tile.pieces) > 1): 
            # cant slide into a blocked place but it can go up or down into one
            return True
        else:
            print('Beetle move criteria violated')
            return False


class Grasshopper(Piece):
    def __init__(self, color=WHITE):
        super().__init__(color)

    def draw(self, surface, hex_pos):
        x, y = hex_pos
        pos = (x - 12, y - 14)
        surface.blit(self.image, pos)
    
    def move_is_valid(self, state, old_tile, new_tile):
        #dist > 1, straight line, must hop over pieces
        dist = axial_distance(old_tile.axial_coords, new_tile.axial_coords)

        if dist > 1:
            visited = [old_tile]
            queue = [old_tile]
            while queue and new_tile not in visited:
                current_tile = queue.pop(0)
                for neighbor_tile in [x for x in current_tile.adjacent_tiles 
                                                if x.has_pieces()
                                                and is_straight_line(old_tile.axial_coords, x.axial_coords)]:
                    if neighbor_tile not in visited:
                        visited.append(neighbor_tile)
                        queue.append(neighbor_tile)
            # have to check last tile seperately bc it will never have a piece
            for penultimate_tile in [x for x in new_tile.adjacent_tiles if x.has_pieces()]: 
                if penultimate_tile in visited and is_straight_line(old_tile.axial_coords, new_tile.axial_coords):
                    return True
            else:
                print('no straight path with pieces')

        else:
            print('Grasshopper move criteria violated')
            return False
    