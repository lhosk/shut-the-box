from itertools import combinations
from functools import lru_cache

def dice_probs():
    probs = {}
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            s = d1 + d2
            probs[s] = probs.get(s, 0) + 1/36
    return probs

DICE_PROBS = dice_probs()

def get_valid_moves(tiles, roll):
    moves = []
    for r in range(1, len(tiles) + 1):
        for combo in combinations(tiles, r):
            if sum(combo) == roll:
                moves.append(combo)
    return moves

@lru_cache(maxsize=None)
def win_prob(tiles):
    if not tiles:
        return 1.0
    total = 0.0
    for roll, prob in DICE_PROBS.items():
        moves = get_valid_moves(tiles, roll)
        if not moves:
            best = 0.0
        else:
            best = max(win_prob(tuple(t for t in tiles if t not in combo)) for combo in moves)
        total += prob * best
    return total

@lru_cache(maxsize=None)
def expected_score(tiles):
    if not tiles:
        return 0.0
    total = 0.0
    for roll, prob in DICE_PROBS.items():
        moves = get_valid_moves(tiles, roll)
        if not moves:
            best = sum(tiles)
        else:
            best = min(expected_score(tuple(t for t in tiles if t not in combo)) for combo in moves)
        total += prob * best
    return total

ALL_TILES = tuple(range(1, 10))