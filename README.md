# Pig Dice Game

## How the game works
Each turn, a player repeatedly rolls a die until the player decides to hold or rolls a 1.
If the player decides to hold he/she will add the total sum of all the dice he/she has rolled during that turn to his/her total points.
If the dice shows a 1 the player will not receive any points and his/her turn will end letting the other player roll.
The one to get to 100 points or more first is the winner.

## Commands
```
help | ?                    Show all the commands
rules                       Show all the rules of the game
start                       Start the game
singleplayer | s            Play against the computer
multiplayer | m             Play against a friend
restart                     Restarts the game
roll | r                    Roll the dice
hold | h                    Hold the points
exit                        Exit the game
cheat                       Gives you 100 points
```

## Computer Logic
The Computer is built in a way which it rolls a random number 
and if that number is the same as its intelligence number it will choose to hold
if it is not the same as its intelligence number it will roll.
We have also made sure that it must roll atleast once every turn just like a human would.
It also calculates if the dice score + its own score is equals to 100 or more,
this means it will decide to hold if the dice score + its own score is equals to 100 or more.
The computer will also be more likely to hold for every roll it makes.

The intelligence setting will change the greedyness of the computer,
there are 3 intelligence settings: 1, 2 or 3.
In our case higher intelligence means to play more safe so it will decide to hold more often.
Since this is a completely luck based game more safe does not always mean better but it made
more sense in this case since it wouldn't risk getting 1's.

## How to use
```
git clone https://github.com/Hpmanen-dev/Pig-Game
cd Pig-Game
py -m pip install -r requirements.txt
py main.py
```