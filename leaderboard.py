"""Save the highscore of all players."""

from tabulate import tabulate


def update_leaderboard(player1, player2, winner):
    """Update the txt file."""
    count = 0
    name1 = player1.get_name()
    name2 = player2.get_name()
    winner = winner.get_name()
    with open("log.txt", "a+") as file:
        file.seek(0)
        lines = file.readlines()
        if (f'Name: {name1}\n') not in lines:
            add_new_user(name1, winner)
        if (f'Name: {name2}\n') not in lines:
            add_new_user(name2, winner)
        for line in lines:
            if line.startswith("Name"):
                name = line.split(":")[1].strip("\n").strip(" ")
                if name in (name1, name2):
                    currentplayer = name
                    games = lines[count+1].split()[1]
                    games = int(games)
                    if currentplayer == winner:
                        wins = lines[count+2].split()[1]
                        wins = int(wins)
                        lines[count+2] = (f"Wins: {wins+1}\n")
                    with open("log.txt", 'w') as file1:
                        lines[count+1] = (f"Games: {games+1}\n")
                        for line1 in lines:
                            file1.write(line1)
            count += 1
    return 'Updated'


def add_new_user(name, winner):
    """Add new user to leaderboard."""
    with open("log.txt", "a+") as file:
        file.write(f"Name: {name}")
        file.write("\nGames: 1\n")
        if name == winner:
            file.write("Wins: 1\n")
        else:
            file.write("Wins: 0\n")
    return 'done'


def show_leaderboard():
    """Display the txt file."""
    table = []
    with open("log.txt", "r") as file:
        for line in file:
            name = line.rstrip("/n").split(":")[1]
            games = file.readline().rstrip("\n").split(":")[1]
            wins = file.readline().rstrip("\n").split(":")[1]
            table.append([name, games, wins])
    table.sort(key=lambda x: x[2], reverse=True)
    print(tabulate(table, headers=["Name", "Games", "Wins"]))
