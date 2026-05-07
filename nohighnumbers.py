from game import get_valid_moves, ALL_TILES

def play_nohigh(rolls):
    tiles = list(ALL_TILES)
    for roll in rolls:
        moves = get_valid_moves(tuple(tiles), roll)
        if not moves:
            break
        best = max(moves, key=lambda c: max(c))
        for t in best:
            tiles.remove(t)
    return sum(tiles)