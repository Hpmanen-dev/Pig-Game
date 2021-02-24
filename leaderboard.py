"""Save the highscore of all players."""

from tabulate import tabulate


def update_leaderboard(player1, player2, winner):
    """Update the txt file."""
    count = 0
    with open("log.txt", "a+") as file:
        file.seek(0)
        lines = file.readlines()
        if (f'Name: {player1.get_name()}\n') not in lines:
            file.write(f"Name: {player1.get_name()}")
            file.write("\nGames: 1\n")
            if player1 == winner:
                file.write("Wins: 1\n")
            else:
                file.write("Wins: 0\n")
        if (f'Name: {player2.get_name()}\n') not in lines:
            file.write(f"Name: {player2.get_name()}")
            file.write("\nGames: 1\n")
            if player2 == winner:
                file.write("Wins: 1")
            else:
                file.write("Wins: 0\n")
        for line in lines:
            if line.startswith("Name"):
                typen, name = line.split()
                if name == player1.get_name() or name == player2.get_name():
                    if name == player1.get_name():
                        currentplayer = player1
                    elif name == player2.get_name():
                        currentplayer = player2
                    typeg, game = lines[count+1].split()
                    game = int(game)
                    if currentplayer == winner:
                        typew, win = lines[count+2].split()
                        win = int(win)
                        lines[count+2] = (f"{typew} {win+1}\n")
                    with open("log.txt", 'w') as file1:
                        lines[count+1] = (f"{typeg} {game+1}\n")
                        for line1 in lines:
                            file1.write(line1)
            count += 1


def show_leaderboard():
    """Display the txt file."""
    table = []
    with open("log.txt", "r") as file:
        for line in file:
            typen, name = line.rstrip("/n").split(":")
            typeg, games = file.readline().rstrip("\n").split(":")
            typew, wins = file.readline().rstrip("\n").split(":")
            table.append([name, games, wins])
    table.sort(key=lambda x: x[2], reverse=True)
    print(tabulate(table, headers=[typen, typeg, typew]))
