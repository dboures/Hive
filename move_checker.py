import numpy as np
from tile import Start_Tile, Inventory_Tile
from pieces import Queen, Ant, Grasshopper, Beetle, Spider


def is_valid_move(state, old_tile, new_tile):
    base_move_check = (new_tile is not None
                       and new_tile.coords != old_tile.coords
                       and ((not new_tile.has_pieces()) or type(state.moving_piece) is Beetle))
    full_move_check = (base_move_check
                       and new_tile.is_hive_adjacent(state)
                       and move_does_not_break_hive(state, old_tile)
                       and move_obeys_piece_movement(state, old_tile, new_tile))
    # first move
    if state.turn == 1:
        if base_move_check and type(new_tile) is Start_Tile:
            return True
    # second
    elif state.turn == 2:
        if (base_move_check
                and new_tile.is_hive_adjacent(state)):
            return True
    elif state.turn <= 6 and state.turn >=3:
        if (full_move_check
                and queen_is_on_board(state, old_tile)):
            return True
    elif state.turn == 7 or state.turn == 8:
        if (full_move_check
                and move_obeys_queen_by_4(state)
            ):
            return True
    else:
        if (full_move_check):
            return True
    return False


def move_does_not_break_hive(state, old_tile):
    temp_piece = old_tile.pieces[-1]
    old_tile.remove_piece()
    tile_list = state.get_tiles_with_pieces()
    # print(unvisited)
    visited = []  # List to keep track of visited nodes.
    queue = []  # Initialize a queue

    # BFS: https://www.quora.com/Is-BFS-faster-and-more-efficient-than-DFS
    visited.append(tile_list[0])
    queue.append(tile_list[0])

    while queue:
        current_tile = queue.pop(0)
        #print(current_tile.axial_coords, type(current_tile.piece))

        for neighbor_tile in [x for x in current_tile.adjacent_tiles if x.has_pieces()]:
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

def queen_is_on_board(state, old_tile):
    if old_tile.axial_coords == (99,99): #placements are ok
        return True
    else:# allow move if queen is down for that color
        if state.turn % 2 == 1:
            color = (250, 250, 250)
        else:
            color = (71, 71, 71)
        for tile in state.get_tiles_with_pieces():
            for piece in tile.pieces:
                print(piece.color)
                if type(piece) is Queen and piece.color == color:
                    return True
    print('cant move till queen is placed')
    return False
def move_obeys_queen_by_4(state):
    queens_on_board = []
    for tile in state.get_tiles_with_pieces():
        for piece in tile.pieces:
            if type(piece) is Queen:
                queens_on_board.append(piece)
    #print(queens_on_board)
    # 2 queens
    if len(queens_on_board) == 2:
        return True
    elif len(queens_on_board) == 0:
        if state.turn == 7 and type(state.moving_piece) is Queen and state.moving_piece.color == (250, 250, 250):
            return True
        elif state.turn == 8 and type(state.moving_piece) is Queen and state.moving_piece.color == (71, 71, 71):
            return True
    elif len(queens_on_board) > 0:
        if queens_on_board[0].color == (250, 250, 250) and state.turn == 7:
            return True
        elif queens_on_board[0].color == (71, 71, 71) and state.turn == 7 and type(state.moving_piece) is Queen:
            return True
        elif queens_on_board[0].color == (71, 71, 71) and state.turn == 8:
            return True
        elif queens_on_board[0].color == (250, 250, 250) and state.turn == 8 and type(state.moving_piece) is Queen:
            return True
    
    print('Queen by 4')
    return False

def game_is_over(state):
    # obtain queen tiles
    # if white surronded and black surrounded -> draw
    # elif white surrounded -> black win
    #elif black surr -> white win
    # else:
    #     pass

    white_surrounded = False
    black_surrounded = False
    for tile in state.get_tiles_with_pieces():
        for piece in tile.pieces:
            if type(piece) is Queen:
                adjacent_tiles_with_pieces = [x for x in tile.adjacent_tiles if x.has_pieces()]
                if len(adjacent_tiles_with_pieces) == 6:
                    if piece.color == (250, 250, 250):
                        white_surrounded = True
                    elif piece.color == (71, 71, 71):
                        black_surrounded = True
                break
    if white_surrounded and black_surrounded:
        print('both surr')
        return True            
    elif white_surrounded:
        print('white surr')
        return True
    elif black_surrounded:
        print('black surrounded')
        return True
    else:
        return False

    

def move_obeys_piece_movement(state, old_tile, new_tile):
    if old_tile.axial_coords == (99, 99):
        new_tile_adjacents_with_pieces = [
            x for x in new_tile.adjacent_tiles if x.has_pieces()]
        for tile in new_tile_adjacents_with_pieces:
            # placed pieces cannot touch other player's pieces to start
            if tile.pieces[-1].color != state.moving_piece.color:
                print('piece placement violation')
                return False
        return True

    #Refactor into piece class methods eventually
    elif type(state.moving_piece) is Queen:
        return obeys_queen_movement(state, old_tile, new_tile)

    elif type(state.moving_piece) is Ant:
        return obeys_ant_movement(state, old_tile, new_tile) 

    elif type(state.moving_piece) is Grasshopper:
        return obeys_grasshopper_movement(state, old_tile, new_tile)

    elif type(state.moving_piece) is Beetle:
        return obeys_beetle_movement(state, old_tile, new_tile)

    elif type(state.moving_piece) is Spider:
        return obeys_spider_movement(state,old_tile,new_tile)
            
    else:
        return False 


def axial_distance(one, two):
    # straight moves give tile distance, but "down" two tiles gives 1.7s, not sure about that
    # feel like it would be most useful to have a tile distance counted from the outside type function
    q1, r1 = one
    q2, r2 = two
    return np.sqrt((q1-q2)*(q1-q2) + (r1-r2)*(r1-r2) + ((q1-q2)*(r1-r2)))


def move_is_not_blocked_or_jump(state, old_tile, new_tile):  # check for each pathfinding move
    dist = axial_distance(old_tile.axial_coords, new_tile.axial_coords)
    old_adjacents_with_pieces = [
        x for x in old_tile.adjacent_tiles if x.has_pieces()]
    new_adjacents_with_pieces = [
        x for x in new_tile.adjacent_tiles if x.has_pieces()]
    overlap_tiles = [
        x for x in new_adjacents_with_pieces if x in old_adjacents_with_pieces]

    if dist == 1 and len(overlap_tiles) == 0:# restrict jumps, incomplete
        print('cant jump gaps')
        return False
    elif dist == 1 and len(overlap_tiles) == 2:
        print('Move is physically blocked')
        return False
    else:
        return True

def path_exists(state, old_tile, new_tile):

    visited = [old_tile]  # List to keep track of visited nodes.
    queue = [old_tile]  # Initialize a queue

    while queue and new_tile not in visited:
        current_tile = queue.pop(0)
        for neighbor_tile in [x for x in current_tile.adjacent_tiles if x.is_hive_adjacent(state) and (not x.has_pieces())]:
            if neighbor_tile not in visited and move_is_not_blocked_or_jump(state, current_tile, neighbor_tile):
                visited.append(neighbor_tile)
                queue.append(neighbor_tile)
    vis = [x.axial_coords for x in visited]
    print(vis)
    if new_tile in visited:
        return True
    else:
        print('no path exists on hive edge')
        return False

#don't like how this repeats code at all
def spider_path_exists(state, old_tile, new_tile):
    temp_piece = old_tile.pieces[-1]
    old_tile.remove_piece()

    queue = [] #list of lists
    queue.append([old_tile])

    while queue:
        path = queue.pop(0)
        current_tile = path[-1]
        if current_tile == new_tile and (len(path) - 1 == 3):
                old_tile.add_piece(temp_piece)
                return True
        
        for neighbor_tile in [x for x in current_tile.adjacent_tiles if x.is_hive_adjacent(state) and (not x.has_pieces())]:
            if neighbor_tile not in path and move_is_not_blocked_or_jump(state, current_tile, neighbor_tile):
                print(neighbor_tile.axial_coords)
                new_path = list(path)
                new_path.append(neighbor_tile)
                queue.append(new_path)
        print('for cycle done')
                
    
    print('no path exists on hive edge')
    old_tile.add_piece(temp_piece)
    return False


def is_straight_line(old_coords, new_coords):
    q1, r1 = old_coords
    q2, r2 = new_coords

    return (q1 == q2) or (r1 == r2) or ((-q1 - r1) == (-q2 - r2))

def obeys_queen_movement(state, old_tile, new_tile):
    dist = axial_distance(old_tile.axial_coords, new_tile.axial_coords)
    if dist == 1 and move_is_not_blocked_or_jump(state, old_tile, new_tile):
        return True
    else:
        print('Queen move criteria violated')
        return False


def obeys_ant_movement(state, old_tile, new_tile):
    if path_exists(state, old_tile, new_tile):
        return True
    else:
        print('Ant move criteria violated')
        return False

def obeys_spider_movement(state, old_tile, new_tile):
    if spider_path_exists(state, old_tile, new_tile) and move_is_not_blocked_or_jump(state, old_tile, new_tile): #add 3 move restriction
        return True
    else:
        print('Spider move criteria violated')
        return False

def obeys_grasshopper_movement(state, old_tile, new_tile):
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

def obeys_beetle_movement(state, old_tile, new_tile):
    dist = axial_distance(old_tile.axial_coords, new_tile.axial_coords)
    if dist == 1 and (move_is_not_blocked_or_jump(state, old_tile, new_tile) or new_tile.has_pieces() or len(old_tile.pieces) > 1): 
        # cant slide into a blocked place but it can go up or down into one
        return True
    else:
        print('Beetle move criteria violated')
        return False
