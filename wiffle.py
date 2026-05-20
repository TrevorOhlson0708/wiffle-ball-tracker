import csv
import sys
from datetime import date

PLAYERS_FILE = "player.csv"
GAME_FILE = "game.csv"

def main():
    while True:
        print("Wiffle Ball Trackers")
        print("1. Add player")
        print("2. Record Game")
        print("3. View Stats")
        print("4. view Game History")
        print("5. quit")

        choice = input("\nChoose an option: ").strip()
        
        if choice == "1":
            add_player()
        elif choice == "2":
            record_game()
        elif choice == "3":
            view_stats()
        elif choice == "4":
            view_history()
        elif choice == "5":
            sys.exit("Smell ya")
        else:
            print("INVALID INPUT... try again :)")

def load_players():
    players = []
    with open("players.csv") as file:
        reader = csv.DirctReader(file)
        for row in reader:
            players.append(row)
        return players
    
def save_players(players):
    with open("players.csv", "w", newline="") as file:
        stats = ["Name", "ABs", "Hits", "HRs", "AVG", "OBP", "SLG", "OBPS",  "Walks", "Errors", "GP", "Wins", "Losses"]
        writer = csv.DictWriter(file, stats=stats)
        writer.writeheader()
        writer.writerows(players)

def add_player():
    players = load_players()
    name = input("Players name: ").strip().title()
    return

def get_player():

def load_games():

def save_games():

def record_game():

def view_stats():

def view_history():

if __name__ == "__main__":
    main()