class Move:
    def __init__(self, player, piece, old_coords, new_coords):
        self.player = player
        self.piece = piece
        self.old_coords = old_coords
        self.new_coords = new_coords
