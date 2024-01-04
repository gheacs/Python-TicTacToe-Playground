# **Tic-Tac-Toe Game supported with AI player**
This is a simple Tic-Tac-Toe game implemented in Python. It allows you to play the game against an AI opponent or with another player.

## Files
### logic.py
This file contains the core logic and classes for the Tic-Tac-Toe game.

#### Player Class
The Player class defines a player in the game.
You can set the number of players using the set_player_type class method.
The __init__ method initializes a player with a specific symbol ('X' or 'O').
#### Board Class
The Board class represents the game board.
It has a method empty_board to create an empty board.
The print_board method is used to display the current state of the board.
#### Game Class
The Game class manages the game flow.
It takes an argument single_player, which is True for a single-player game and False for a two-player game.
The play method is the main game loop.
It includes methods for human and computer moves, checking for a winner, checking for a draw, and updating player statistics.
#### Other Functions
calculate_player_rank calculates the rank of a player based on their wins.
calculate_game_duration calculates the duration of a game.
generate_random_player_statistics generates random player statistics.
### cli.py
This file contains a simple command-line interface (CLI) for playing the game.

The player_input function gets the row and column input from the player.
The main function sets up and runs the game loop, allowing players to take turns.

## Usage
Run the cli.py file to start the game.
Follow the on-screen prompts to make your moves.
Enjoy the game and compete with the AI or another player!
