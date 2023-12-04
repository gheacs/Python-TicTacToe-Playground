import random
import csv
import time

class Player:
    player_number = 1  # Default

    @classmethod
    def set_player_type(cls, number):
        Player.player_number = number
        if number == 1:
            print('Game is for a single player')
        elif number == 2:
            print('Game is for two players')
        else:
            print('Invalid number of players')

    def __init__(self, symbol):
        self.symbol = symbol

class Board:
    def __init__(self):
        self.board = self.empty_board()

    def empty_board(self):
        return [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]

    def print_board(self):
        for row in self.board:
            print(row)

class Game:
    def __init__(self, single_player):
        self.board = Board()
        self.single_player = single_player
        self.current_player = "X"
        self.player_statistics = {
            'X': {'wins': 0, 'losses': 0, 'rank': 'Bronze'},
            'O': {'wins': 0, 'losses': 0, 'rank': 'Bronze'},
        }
        self.start_time = None  # Record the start time when the game starts

    def play(self, player_move=None, computer_move=None):
        while True:
            self.board.print_board()
            if self.single_player and self.current_player == "O":
                self.computer_move()
            else:
                if player_move:
                    row, col = player_move
                else:
                    row, col = self.player_input()
                self.human_move(row, col)

            winner = self.check_winner()
            if winner != '':
                self.board.print_board()
                print(f"Player {winner} wins!")
                self.update_player_stats(winner)
                rank = calculate_player_rank(winner, self.player_statistics)
                print(f"Player {winner} rank: {rank}")
                break

            if not self.any_moves_left():
                self.board.print_board()
                print("It's a draw!")
                self.update_player_stats('Draw')
                break

            self.switch_player()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def any_moves_left(self):
        return any('' in row for row in self.board.board)

    def human_move(self, row, col):
        while self.board.board[row][col] != '':
            print("Spot already taken. Choose another spot.")
            row, col = self.player_input()
        self.board.board[row][col] = self.current_player

    def computer_move(self):
        empty_spots = [(r, c) for r in range(3) for c in range(3) if self.board.board[r][c] == '']
        row, col = random.choice(empty_spots)
        self.board.board[row][col] = "O"

    def is_valid_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3:
            return self.board.board[row][col] == ''
        return False

    def check_winner(self):
        # Check rows and columns
        for i in range(3):
            if self.board.board[i][0] != '' and self.board.board[i][0] == self.board.board[i][1] == self.board.board[i][2]:
                return self.board.board[i][0]
            if self.board.board[0][i] != '' and self.board.board[0][i] == self.board.board[1][i] == self.board.board[2][i]:
                return self.board.board[0][i]

        # Check diagonals
        if self.board.board[0][0] != '' and self.board.board[0][0] == self.board.board[1][1] == self.board.board[2][2]:
            return self.board.board[0][0]
        if self.board.board[0][2] != '' and self.board.board[0][2] == self.board.board[1][1] == self.board.board[2][0]:
            return self.board.board[0][2]

        return ''

    def is_draw_game(self):
        return all('' not in row for row in self.board.board)

    def player_input(self):
        try:
            row = int(input("Enter the row number (0, 1, or 2): "))
            col = int(input("Enter the column number (0, 1, or 2): "))
            return row, col
        except ValueError:
            print('Invalid input. Please enter valid row and column numbers.')
            return self.player_input()

    def update_player_stats(self, winner):
        if winner in ('X', 'O'):
            self.player_statistics[winner]['wins'] += 1
            other_player = 'X' if winner == 'O' else 'O'
            self.player_statistics[other_player]['losses'] += 1

def calculate_player_rank(winner, player_statistics):
    if winner in ('X', 'O'):
        wins = player_statistics[winner]['wins']
        if wins >= 5:
            return 'Gold'
        elif wins >= 3:
            return 'Silver'
        elif wins >= 1:
            return 'Bronze'
    return 'None'  # No rank for draws or incomplete games

def calculate_game_duration(start_time, end_time):
    return end_time - start_time

def generate_random_player_statistics():
    return {
        'X': {'wins': random.randint(0, 10), 'losses': random.randint(0, 10)},
        'O': {'wins': random.randint(0, 10), 'losses': random.randint(0, 10)}
    }

import random
import csv
import time

# ... (previous code remains the same) ...

def main():
    game = Game(single_player=True)
    game.start_time = time.time()  # Record the start time when the game starts

    while game.check_winner() == '':
        if game.current_player == "X":
            row, col = game.player_input()
            game.play(player_move=(row, col))
        else:
            row, col = game.computer_move()
            game.play(computer_move=(row, col))

    game.board.print_board()
    if game.check_winner():
        print(f"Player {game.check_winner()} wins!")
    else:
        print("It's a draw!")

    # Random player statistics
    random_player_statistics = generate_random_player_statistics()

    # Calculate player rank and game duration
    winner = game.check_winner()
    rank = calculate_player_rank(winner, game.player_statistics)
    length_of_game = calculate_game_duration(game.start_time, time.time())

    # Add game log with winner, rank, length_of_game, and random statistics
    with open('log.csv', 'a', newline='') as log_csv:
        csv_writer = csv.writer(log_csv)
        csv_writer.writerow([winner, rank, length_of_game])

if __name__ == "__main__":
    main()
