# Shut the Box

Code for the paper *Optimal Strategy in Shut the Box* by Lucas Hoskin.

## Files

**game.py**
The core engine. Defines the game state, valid moves, and computes the exact win probability and expected score for every reachable board using backwards induction.

**maxwins.py**
Runs the MaxWin analysis on the full opening board. For every roll from 2 to 12, prints all valid tile combinations ranked by win probability.

**minloss.py**
Same as above but ranked by expected final score instead of win probability.

**nohighnumbers.py**
The NoHigh baseline strategy. No lookahead, just always picks whichever valid combination contains the highest individual tile.

**simulate.py**
Runs 1,000,000 games with identical dice rolls across all three strategies and compares average score, total wins, and win rate.

## Usage

Run any of the following from the same directory:

```
python maxwins.py
python minloss.py
python simulate.py
```

## Results

### Optimal First Move

| Roll | Flip | Same Roll Again |
|------|------|-----------------|
| 2 | {2} | -- |
| 3 | {3} | {1, 2} |
| 4 | {4} | {1, 3} |
| 5 | {5} | {2, 3} |
| 6 | {6} | {2, 4} |
| 7 | {7} | {2, 5} |
| 8 | {8} | {3, 5} |
| 9 | {9} | {1, 8} |
| 10 | {1, 9} | {2, 8} |
| 11 | {2, 9} | {3, 8} |
| 12 | {3, 9} | {5, 7} |

### Simulation over 1,000,000 games

| Metric | MaxWin | MinLoss | NoHigh |
|--------|--------|---------|--------|
| Average score | 11.20 | 11.16 | 11.37 |
| Wins | 71,239 | 70,685 | 69,419 |
| Win rate | 7.12% | 7.07% | 6.94% |