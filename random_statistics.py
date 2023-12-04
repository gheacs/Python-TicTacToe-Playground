import random
import csv

# Function to generate random game statistics
def generate_random_game_statistics():
    return {
        'TotalMoves': random.randint(10, 50)
    }

# Generate random game data for 40 games
game_data = []

for _ in range(40):
    first_player = random.choice(['X', 'O'])
    winner = random.choice([first_player, 'Draw'])
    game_duration = round(random.uniform(10, 120), 2)
    game_stats = generate_random_game_statistics()
    
    game_data.append([
        first_player,
        winner,
        'Bronze',
        game_duration,
        game_stats['TotalMoves']
    ])

# Write the game data to a CSV file
with open('random_game_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['First Player', 'Winner', 'Rank', 'Game Duration (s)', 'Total Moves'])
    csv_writer.writerows(game_data)

print("Random game data with 'First Player' and 'Winner' statistics generated and saved to 'random_game_data.csv'.")
