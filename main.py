"""Runs the program.

How the game works:

Each turn, a player repeatedly rolls a die until
the player decides to hold or until he rolls a 1.
If the player decides to hold he/she will add the total sum of all the
dice numbers he/she has rolled during that turn to his/her total points.
If the dice shows a 1 the player will not receive any points and his/her turn
will end letting the other player roll.
The one to get to 100 points or more first is the winner.
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
"""

import commands

if __name__ == "__main__":
    with open("Headline.txt", "r") as file:
        for line in file:
            print(line.strip("\n"))
    print(__doc__)
    commands.Commands().cmdloop()
