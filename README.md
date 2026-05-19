# Wiffle Ball Tracker

A stat tracker for backyard wiffle ball games built with Python.

## Features
- Track hits, at bats, walks, and errors per player
- Automatically calculates batting average and on base percentage
- Saves stats between sessions so nothing gets lost
- Add and remove players anytime

## Stats Tracked
| Stat | Formula |
|------|---------|
| Batting Average (AVG) | Hits / At Bats |
| On Base Percentage (OBP) | (Hits + Walks) / At Bats |
| Errors | Tracked manually per player |

## How to Run
pip install -r requirements.txt
python main.py

## Built With
- Python
- CSV for data storage
