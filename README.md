# A Battleships Game
Portfolio Project 3 Python Essentials - Code Institute

# About

# How To Play

To play the game based on the provided code, follow these steps:

1. Run the Python script containing the game code in your preferred Python environment.

2. You'll be greeted with a welcome message, and the game will ask you to enter a username. Type in your username and press Enter.

3. The game initializes the boards and places battleships on both your board and the computer's board. However, you can't see the computer's board; it's hidden.

4. The main game loop runs for ten turns. In each turn:

   a. You'll see a message indicating the turn number (e.g., "This is turn 1/10").

   b. The game will ask you to make a guess by specifying a column and a row. You need to enter the coordinates as numbers between 1 and 5, not 0-based indices. For example, you can input "3" for the column and "2" for the row. The game validates your input to ensure it's within bounds and hasn't been guessed before.

   c. After you make your guess, the game displays your guesses on the `player_guesses` board. If your guess hits a computer battleship, it's marked with "#" (a hit), and if you miss, it's marked with "*" (a miss).

   d. The computer then takes its turn, and the result is displayed. The computer will guess a location on your `player` board, and you'll see if it hits or misses your ships.

5. Repeat steps 4 for ten turns. The game will keep track of hits on both boards.

6. After ten turns, the game will report the winner. The player with the most hits wins. If both sides have the same number of hits, it's considered a draw.

7. You'll see a message indicating the winner or a draw, and the game ends.

Enjoy playing the game, and try to outsmart the computer by finding its hidden battleships while protecting your own!



## Bugs/Updates after Testing

-Based on user feedback and testing, the code was modified to accept numbers in the range of 1 to 5 instead of starting at 0, which was initially confusing. Additionally, input breaks were introduced so that players could see the results of each turn without needing to scroll through the output. Several code commits were made to clarify the distinction between rows and columns. Furthermore, potential issues with the ship generating function being stuck in a loop if the code were edited for a smaller board with fewer than 4 locations were addressed.

## Validator Testing



# Deployment


# Credits

