from game import get_valid_moves, win_prob, ALL_TILES, DICE_PROBS

def analyze():
    print("STRATEGY: Maximize win probability (reach score of 0)")
    print(f"Overall win probability from start: {win_prob(ALL_TILES)*100:.4f}%\n")
    print("-" * 50)

    for roll in range(2, 13):
        moves = get_valid_moves(ALL_TILES, roll)
        if not moves:
            continue
        results = []
        for combo in moves:
            remaining = tuple(t for t in ALL_TILES if t not in combo)
            wp = win_prob(remaining)
            results.append((combo, wp))
        results.sort(key=lambda x: -x[1])

        print(f"\nRoll {roll} (prob={DICE_PROBS[roll]:.3f}):")
        for combo, wp in results:
            marker = " <- BEST" if combo == results[0][0] else ""
            print(f"  Flip {str(list(combo)):<20} -> {wp*100:.4f}% win prob{marker}")

if __name__ == "__main__":
    analyze()