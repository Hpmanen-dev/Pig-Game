"""Save the highscore of all players."""

from tabulate import tabulate


def update_leaderboard(player1, player2, winner):
    """Update the leaderboard."""
    count = 0
    name1 = player1
    name2 = player2
    with open("log.txt", "r+") as file:
        file.seek(0)
        lines = file.readlines()
        if (f'Name: {name1}\n') not in lines:
            file.writelines(add_new_user(name1, winner))
        if (f'Name: {name2}\n') not in lines:
            file.writelines(add_new_user(name2, winner))
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


def add_new_user(name, winner):
    """Add new user to leaderboard."""
    with open('log.txt', 'a+') as file:
        file.seek(0)
        new_lines = []
        new_lines.append(f"Name: {name}")
        new_lines.append("\nGames: 1\n")
        if name == winner:
            new_lines.append("Wins: 1\n")
        else:
            new_lines.append("Wins: 0\n")
        file.close()
        return new_lines


def show_leaderboard():
    """Display the leaderboard."""
    table = []
    with open("log.txt", "r") as file:
        for line in file:
            name = line.rstrip("/n").split(":")[1]
            games = file.readline().rstrip("\n").split(":")[1]
            wins = file.readline().rstrip("\n").split(":")[1]
            table.append([name, games, wins])
    table.sort(key=lambda x: x[2], reverse=True)
    print(tabulate(table, headers=["Name", "Games", "Wins"]))
    return 'done'


def reset_leaderboard():
    """Reset the leaderboard."""
    file = open("log.txt", "r+")
    file.truncate(0)
    file.close()
    print("< LEADERBOARD RESET >")
