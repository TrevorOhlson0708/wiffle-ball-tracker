# Wiffle Ball Tracker

A command-line app for tracking wiffle ball player stats across multiple games. Built with Python using CSV files for data storage.

---

## How to Run

```
python wiffle.py
```

---

## Menu Options

```
1. Add player
2. Record Game
3. View Stats
4. View Game History
5. Quit
```

---

## Features

### 1. Add Player
Adds a new player to the roster. All stats start at zero.
- Minimum of 3 players required before recording a game.

### 2. Record Game
Enter the names of everyone who played (press Enter on a blank line when done).
You'll then be prompted to enter each player's stats for that game:
- **ABs** — At Bats
- **Hits**
- **HRs** — Home Runs
- **Walks**
- **Errors**

Stats are added to each player's running career totals and saved automatically.

### 3. View Stats
Displays a full stat table for every player, sorted by OBPS (best to worst).

| Stat | What it is | How it's calculated |
|------|-----------|-------------------|
| ABs | At Bats | Entered per game |
| Hits | Hits | Entered per game |
| HRs | Home Runs | Entered per game |
| Walks | Walks | Entered per game |
| Errors | Errors | Entered per game |
| AVG | Batting Average | Hits ÷ ABs |
| OBP | On Base Percentage | (Hits + Walks) ÷ (ABs + Walks) |
| SLG | Slugging Percentage | (Singles + HRs × 4) ÷ ABs |
| OBPS | On Base + Slugging | OBP + SLG |

> SLG assumes any hit that isn't a HR is a single (1 base).

### 4. View Game History
Shows a log of every game recorded, with the date and each player's raw stats for that game.

---

## Data Storage

Two CSV files are created automatically in the same folder as `wiffle.py`:

- **`player.csv`** — career stats for every player
- **`game.csv`** — a game-by-game log

---

## Requirements

- Python 3.x
- No external libraries needed (uses built-in `csv`, `sys`, `datetime`)
