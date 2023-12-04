import random
import csv

# Function to generate random game statistics
def generate_random_game_statistics():
    return {
        'TotalMoves': random.randint(10, 50)
    }

# Function to convert row and column to a 1-9 representation
def convert_to_1_9(row, col):
    return row * 3 + col + 1

# Generate random game data for 40 games
game_data = []

for _ in range(40):
    first_player = random.choice(['X', 'O'])
    winner = random.choice([first_player, 'Draw'])
    game_duration = round(random.uniform(10, 120), 2)
    game_stats = generate_random_game_statistics()
    
    # Generate random row and column for the first move
    row = random.randint(0, 2)
    col = random.randint(0, 2)

    # Convert row and column to a 1-9 representation
    first_move = convert_to_1_9(row, col)
    
    game_data.append([
        first_player,
        winner,
        'Bronze',
        game_duration,
        game_stats['TotalMoves'],
        first_move  # Include the first move in the data
    ])

# Write the game data to a CSV file
with open('random_game_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['First Player', 'Winner', 'Rank', 'Game Duration (s)', 'Total Moves', 'First Move (1-9)'])
    csv_writer.writerows(game_data)

print("Random game data with 'First Player', 'Winner', and 'First Move' statistics generated and saved to 'random_game_data.csv'.")
