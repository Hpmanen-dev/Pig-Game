"""Save the highscore of all players."""

from tabulate import tabulate


def updateLeaderboard(Player1, Player2, Winner):
    """Update the txt file."""
    count = 0
    with open("log.txt", "a+") as file:
        file.seek(0)
        lines = file.readlines()
        if (f'Name: {Player1.get_name()}\n') not in lines:
            file.write(f"Name: {Player1.get_name()}")
            file.write("\nGames: 1\n")
            if(Player1 == Winner):
                file.write("Wins: 1\n")
            else:
                file.write("Wins: 0\n")
        if (f'Name: {Player2.get_name()}\n') not in lines:
            file.write(f"Name: {Player2.get_name()}")
            file.write("\nGames: 1\n")
            if(Player2 == Winner):
                file.write("Wins: 1")
            else:
                file.write("Wins: 0\n")
        for line in lines:
            if line.startswith("Name"):
                type, name = line.split()
                if name == Player1.get_name() or name == Player2.get_name():
                    if name == Player1.get_name():
                        currentPlayer = Player1
                    elif name == Player2.get_name():
                        currentPlayer = Player2
                    type, game = lines[count+1].split()
                    game = int(game)
                    new = game + 1
                    if currentPlayer == Winner:
                        typew, win = lines[count+2].split()
                        win = int(win)
                        lines[count+2] = (f"{typew} {win+1}\n")
                    with open("log.txt", 'w') as file1:
                        lines[count+1] = (f"{type} {new}\n")
                        for line in lines:
                            file1.write(line)
            count += 1


def showLeaderboard():
    """Display the txt file."""
    table = []
    with open("log.txt", "r") as file:
        for line in file:
            typen, name = line.rstrip("/n").split(":")
            typeg, games = file.readline().rstrip("\n").split(":")
            typew, wins = file.readline().rstrip("\n").split(":")
            table.append([name, games, wins])

    print(tabulate(table, headers=[typen, typeg, typew]))
