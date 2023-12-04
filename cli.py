from logic import Game, Player, Board
import random
import csv
import time

def player_input():
    try:
        row = int(input("Enter the row number (0, 1, or 2): "))
        col = int(input("Enter the column number (0, 1, or 2): "))
        return row, col
    except ValueError:
        print('Invalid input. Please enter valid row and column numbers.')
        return player_input()

def main():
    game = Game(single_player=True)

    while game.check_winner() == '':
        if game.current_player == "X":
            row, col = player_input()
            game.play(player_move=(row, col))
        else:
            row, col = game.computer_move()
            game.play(computer_move=(row, col))

    game.board.print_board()
    if game.check_winner():
        print(f"Player {game.check_winner()} wins!")
    else:
        print("It's a draw!")  

if __name__ == "__main__":
    main()
