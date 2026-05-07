from game import get_valid_moves, expected_score, ALL_TILES, DICE_PROBS

def analyze():
    print("STRATEGY: Minimize expected final score")
    print(f"Expected final score from start: {expected_score(ALL_TILES):.4f}\n")
    print("-" * 50)

    for roll in range(2, 13):
        moves = get_valid_moves(ALL_TILES, roll)
        if not moves:
            continue
        results = []
        for combo in moves:
            remaining = tuple(t for t in ALL_TILES if t not in combo)
            es = expected_score(remaining)
            results.append((combo, es))
        results.sort(key=lambda x: x[1])

        print(f"\nRoll {roll} (prob={DICE_PROBS[roll]:.3f}):")
        for combo, es in results:
            marker = " <- BEST" if combo == results[0][0] else ""
            print(f"  Flip {str(list(combo)):<20} -> expected score: {es:.4f}{marker}")

if __name__ == "__main__":
    analyze()