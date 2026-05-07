import random
from game import get_valid_moves, win_prob, expected_score, ALL_TILES
from nohighnumbers import play_nohigh

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def generate_rolls():
    rolls = []
    while True:
        roll = roll_dice()
        rolls.append(roll)
        if len(rolls) > 50:
            break
    return rolls

def play_game(rolls, strategy):
    tiles = list(ALL_TILES)
    for roll in rolls:
        moves = get_valid_moves(tuple(tiles), roll)
        if not moves:
            break
        if strategy == "maxwin":
            best = max(moves, key=lambda c: win_prob(tuple(t for t in tiles if t not in c)))
        else:
            best = min(moves, key=lambda c: expected_score(tuple(t for t in tiles if t not in c)))
        for t in best:
            tiles.remove(t)
    return sum(tiles)

def simulate(n=50000, seed=42):
    random.seed(seed)
    all_rolls = [generate_rolls() for _ in range(n)]

    maxwin_scores = [play_game(rolls, "maxwin") for rolls in all_rolls]
    minloss_scores = [play_game(rolls, "minloss") for rolls in all_rolls]
    nohigh_scores = [play_nohigh(rolls) for rolls in all_rolls]

    maxwin_wins = sum(1 for s in maxwin_scores if s == 0)
    minloss_wins = sum(1 for s in minloss_scores if s == 0)
    nohigh_wins = sum(1 for s in nohigh_scores if s == 0)
    maxwin_avg = sum(maxwin_scores) / n
    minloss_avg = sum(minloss_scores) / n
    nohigh_avg = sum(nohigh_scores) / n

    print(f"Results over {n} games (same rolls for all)\n")
    print(f"{'Metric':<25} {'MaxWin':<20} {'MinLoss':<20} {'NoHigh':<20}")
    print("-" * 85)
    print(f"{'Average score':<25} {maxwin_avg:<20.4f} {minloss_avg:<20.4f} {nohigh_avg:<20.4f}")
    print(f"{'Wins (score = 0)':<25} {maxwin_wins:<20} {minloss_wins:<20} {nohigh_wins:<20}")
    print(f"{'Win rate':<25} {maxwin_wins/n*100:<20.2f}% {minloss_wins/n*100:<20.2f}% {nohigh_wins/n*100:<20.2f}%")

if __name__ == "__main__":
    simulate(50000)