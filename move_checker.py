Queenimport numpy as np
from tile import Start_Tile, Inventory_Tile
from pieces import Queen

def is_valid_move(state, old_tile, new_tile): #still need to handle enforcing queen placement
    base_check = (new_tile is not None 
                and new_tile.coords != old_tile.coords
                and new_tile.piece is None)
    # first move
    if state.turn == 1:
        if base_check and type(new_tile) is Start_Tile:
            return True
    # second
    elif state.turn == 2:
        if (base_check 
            and new_tile.is_hive_adjacent(state)):
            return True
    elif state.turn >= 3 and state.turn <= 6:
        if (base_check
            and new_tile.is_hive_adjacent(state)
            and move_does_not_break_hive(state, old_tile)
            #and new move is valid for piece
            ):
            return True
    elif state.turn == 7 or state.turn == 8:
        if (base_check
            and new_tile.is_hive_adjacent(state)
            and move_does_not_break_hive(state, old_tile)
            #and new move is valid for piece
            and move_obeys_queen_by_4(state)
            ):
            return True
    else:
        if (base_check
            and new_tile.is_hive_adjacent(state)
            and move_does_not_break_hive(state, old_tile)
            and move_obeys_piece_movement(state, old_tile, new_tile)
            ):
            return True
        return False

def move_does_not_break_hive(state, old_tile):
    temp_piece = old_tile.piece
    old_tile.remove_piece()
    tile_list = state.get_tiles_with_pieces()
    #print(unvisited)
    visited = [] # List to keep track of visited nodes.
    queue = []     #Initialize a queue

    #BFS: https://www.quora.com/Is-BFS-faster-and-more-efficient-than-DFS
    visited.append(tile_list[0])
    queue.append(tile_list[0])

    while queue:
        current_tile = queue.pop(0) 
        #print(current_tile.axial_coords, type(current_tile.piece)) 

        for neighbor_tile in current_tile.get_adjacent_tiles(state, pieces=True):
            if neighbor_tile not in visited:
                visited.append(neighbor_tile)
                queue.append(neighbor_tile)
    
    if len(visited) != len(tile_list):
        old_tile.add_piece(temp_piece)
        print('One Hive Rule')
        return False
    else:
        old_tile.add_piece(temp_piece)
        return True

def move_obeys_queen_by_4(state):
    queens_on_board = [tile.piece for tile in state.get_tiles_with_pieces() if type(tile.piece) is Queen]
    #print(queens_on_board)
    # 2 queens
    if len(queens_on_board) == 2:
        return True
    elif len(queens_on_board) >= 0:
        if queens_on_board[0].color == (250, 250, 250) and state.turn == 7:
            return True
        elif queens_on_board[0].color == (137, 137, 137) and state.turn == 7 and type(state.moving_piece) is Queen:
            return True
        elif queens_on_board[0].color == (137, 137, 137) and state.turn == 8:
            return True
        elif queens_on_board[0].color == (250, 250, 250) and state.turn == 8 and type(state.moving_piece) is Queen:
            return True
        else:
            print('Queen by 4')
            return False

def move_obeys_piece_movement(state, old_tile, new_tile):
    if old_tile.axial_coords == (99,99):
        return True #placements are always ok

    elif type(state.moving_piece) is Queen:
        dist = axial_distance(old_tile.axial_coords, new_tile.axial_coords)
        if dist == 1:
            return True
        else:
            return False

def axial_distance(one,two):
    #straight moves give tile distance, but "down" two tiles gives 1.7s, not sure about that
    #feel like it would be most useful to have a tile distance counted from the outside type function
    q1,r1 = one
    q2,r2 = two
    return np.sqrt((q1-q2)*(q1-q2) + (r1-r2)*(r1-r2) + ((q1-q2)*(r1-r2)))
