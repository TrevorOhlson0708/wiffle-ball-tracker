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

# Stats Calculations

def calc_avg(hits, abs):
    return round(hits / abs_, 3) if abs_ > 0 else 0.0

def calc_obp(hits, walks, abs_):
    return ((hits + walks) / (abs_ + walks), 3) if (abs_ + walks) > 0 else 0.0

def calc_slug(hits, hrs, abs_):
    total_bases = (hits - hrs) + (hrs * 4)
    return round(total_bases / abs_, 3) if abs_ > 0 else 0.0

def calc_obps(obp, slg):
    return round(obp + slg, 3)

# Player Functions

def load_players():
    try:
        with open(PLAYERS_FILE) as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []
    
def save_players(players):
    with open(PLAYERS_FILE, "w", newline="") as file:
        stats = ["name", "ABs", "Hits", "HRs", "Walks", "Errors",]
        writer = csv.DictWriter(file, fieldnames=stats)
        writer.writeheader()
        writer.writerows(players)

def get_player(player, name):
    for player in players:
        if player["name"] == name:
            return player
    return None

def add_player():
    players = load_players()
    name = input("Players name: ").strip().title()
    
    if get_player(player, name):
        print(f"{name} already exists...")
        return

    players.append({"name": name, "ABs": 0, "Hits": 0, "HRs": 0, "Walks": 0, "Errors": 0})
    save_players(players)
    print(f"{name} was added!!")

# Game Functions

def load_games():
    try:
        with open(GAME_FILE) as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return[]

def save_games(game):
    games = load_games()
    games.append(game)
    with open(GAME_FILE, "w", newline="") as file:
        stats = ["date", "player", "ABs", "Hits", "HRs", "Walks", "Errors"]
        writer = csv.DictWriter(file, fieldnames=stats)
        writer.writeheader()
        writer.writerows(games)

def get_game_stats(player_name):
    print(f"\n Stats for {player_name}")
    try:
        abs_ = int(input("    ABS: "))
        hits = int(input("    Hits: "))
        hrs = int(input("    HRs: "))
        walks = int(input("    Walks: "))
        errors = int(input("    Errors: "))
    except ValueError:
        print("Stats must be a whole number...")
        return None

    return {"ABs": abs_, "Hits": hits, "HRs": hrs, "Walks": walks, "Errors": errors}

def record_game():
    players = load_players()

    if len(players) < 3:
        print("Need at least 3 players. Add more players")
        return

    print("\nPlayers:", ", ".join(p["name"] for p in players))
    print("Enter names of everyone who played")

    playing = []
    while True:
        name = input("  Player: ").strip().title()
        if not name:
            break
        player = get_player(players, name)
        if not player:
            print(f"    {name} not found")
        elif name in [p["name"] for p in playing]:
            print(f"{name} already added.")
        else:
            playing.append(player)

    if len(playing) < 2:
        print("Need at least 3 players for a game")
        return

    game_entries = []
    for player in playing:
        stats = get_game_stats(player["name"])
        if stats is None:
            return

        player["Abs"] = int(player["Abs"]) + stats["Abs"]
        player["Hits"] = int(player["Hits"]) + stats["Hits"]
        player["HRs"] = int(player["HRs"]) + stats["HRs"]
        player["Walks"] = int(player["Walks"]) + stats["Walks"]
        player["Errors"] = int(player["Errors"]) + stats["Errors"]

        game_entries.append({"date": date.today(), "player": player["name"], **stats})

    save_players(players)
    for entry in game_entries:
        save_games(entry)

    print("Game recorded!!")

# Display Functions

def view_stats():
    players = load_players()

    if not players:
        print("No players yet.")
        return

    row = []
    for p in players:
        abs_ = int(p["ABs"])
        hits = int(p["Hits"])
        hrs = int(p["HRs"])
        walks = int(p["Walks"])
        errors = int(p["Errors"])

        avg = calc_avg(hits, abs_)
        obp = calc_obp(hits, walks, abs_)
        slg = calc_slug(hits, hrs, abs_)
        obps = calc_obps(obp, slg)

        row.append((p["name"], abs_, hits, hrs, walks, errors, avg, obp, slg, obps))

    row.sort(key=lambda r: r[9], reverse=True)

    print(f"\n{'Name':<15} {'ABs':<5} {'Hits':<6} {'HRs':<5} {'Walks':<7} {'Errors':<8} {'AVG':<6} {'OBP':<6} {'SLG':<6} {'OBPS'}")
    print("-" * 75)
    for r in rows:
         print(f"{r[0]:<15} {r[1]:<5} {r[2]:<6} {r[3]:<5} {r[4]:<7} {r[5]:<8} {r[6]:<6.3f} {r[7]:<6.3f} {r[8]:<6.3f} {r[9]:.3f}")

def view_history():
    games = load_games()

    if not games:
        print("No games recorded yet :(")
        return

    print(f"\n{'Date':<12} {'Player':<15} {'ABs':<5} {'Hits':<6} {'HRs':<5} {'Walks':<7} {'Errors'}")
    print("-" * 55)
    for g in games:
        print(f"{g['date']:<12} {g['player']:<15} {g['ABs']:<5} {g['Hits']:<6} {g['HRs']:<5} {g['Walks']:<7} {g['Errors']}")

if __name__ == "__main__":
    main()