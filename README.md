# Pig Dice Game

Application made by:
Kristian Åkerblom, Hampus Nilsson, Anton Thereström

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
restart                     Restarts the game
roll | r                    Roll the dice
hold | h                    Hold the points
exit                        Exit the game
cheat                       Gives you 100 points and you win the game immediately
intelligence (number)       Changes the intelligence of the computer (Only numbers between 1 - 3 will work.)
leaderboard                 Shows the leaderboard/highscore
resetlb                     Reset the leaderboard
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
Since this is a completely luck based game, being more safe does not always mean better but it made
more sense in this case since it wouldn't risk getting 1's.

## How to use
```
Download git at https://git-scm.com/downloads
Use command:
git clone https://github.com/Hpmanen-dev/Pig-Game
cd Pig-Game
'py -m pip install -r requirements.txt' or 'make install'
py main.py
```

## Install Make
To generate docs, uml and coverage from our code you will need to use 'Make' to get access to the make command on an windows computer,
you can install it with chocolatey, to get access to chocolatey follow these instructions: https://chocolatey.org/install

When you do have access to chocolatey you can run the command: 'choco install make'
Note that you need to run the terminal as administrator for it to work.

## How to make documentation
Use the command 'make doc' in the terminal to generate html documentation.

## Generate UML diagrams
First you need to make sure you have Graphviz installed.

Install Graphviz by chocolatey, to get access to chocolatey follow the instructions here: https://chocolatey.org/install

When you have access to chocolatey you can run the command: 'choco install graphviz'
Note that you need to run the terminal as administrator for it to work.

Use the command 'make uml' to regenerate the UML diagrams from our code. Again we suggest using Gitbash if this does not work in your usual terminal.

## How to run our tests
Just use the command 'make unittest' in the terminal to just run the tests and use 'make coverage' to get the coverage report of the tests. 
You can also do 'make test' to run a full test which will both do a coverage test and lint test on the code.

## If the commands does not work
If the commands does not work using your usual terminal we suggest using GitBash which you get from downloading git, if you do not already have it you can get it here: https://git-scm.com/downloads