class Move:
    def __init__(self, player, old_coords, new_coords):
        self.player = player
        self.old_coords = old_coords
        self.new_coords = new_coords
        print('made move')
        print(old_coords, new_coords)
