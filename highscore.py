"""Save the highscore of all players."""

def updateHighscore(Player1, Player2):
    count = 0
    with open("log.txt", "a+") as file:
        file.seek(0)
        lines = file.readlines()
        if (f'Name: {Player1.get_name()}\n') not in lines:
            file.write(f"Name: {Player1.get_name()}")
            file.write("\nGames: 1\n")
        if (f'Name: {Player2.get_name()}\n') not in lines:
            file.write(f"Name: {Player2.get_name()}")
            file.write("\nGames: 1\n")
        for line in lines:
            if line.startswith("Name"):
                type, name = line.split()
                if name == Player1.get_name() or name == Player2.get_name():
                    type, game = lines[count+1].split()
                    game = int(game)
                    new = game + 1
                    with open("log.txt", 'w') as file1:
                        lines[count+1] = (f"{type} {new}\n")
                        for line in lines:
                            file1.write(line)
            count += 1


def showHighscore(self):
    with open("log.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line)

    
