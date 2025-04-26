# Mastermind
---
## Description
This is a python version of the classic logic game Mastermind. The aim of the game is to guess the colour combination of 5 hidden pegs. Here, the eight colours are represented by the digits 1-8, so the player must guess the correct combination of 5 of these digits. There is an easy mode and a hard mode.
## How to Use 
To play the game, the user must run the mastermind.py script. The player is asked if they would like to see instructions on how to play. These instructions are below.
### Mastermind Instructions
The aim of the game is to guess the correct colour combination of 5 pegs. Here, the 8 colours are represented by the 8 digits 1 through 8.
#### Gameplay
- To take a turn, the player must input a combination of 5 digits from 1 to 8 as their guess.
- The program will then compare this guess to the secret combination and return a set of up to five pegs, black or white. 
- If playing in easy mode, a black peg represents that the guessed digit in its position is correct, and in the right place, where a white peg represents that the guessed digit in its place is correct but in the wrong place.
- If playing in hard mode, the colour of the pegs has the same meaning, but the position of teh pegs does not, and the black pegs will always be shown first, followed by the white pegs.
- The player has 12 attempts to guess the combination.
