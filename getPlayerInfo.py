import pandas as pd

df = pd.read_csv('WK_1-8.csv')

# Initialize an empty dictionary to store player information
player_info_dict = {}

# Iterate through the DataFrame and populate the dictionary
for index, row in df.iterrows():
    player_name = row['NAME']
    pos = row['POS']
    team = row['TEAM']
    week = row['WEEK']

    # Check if the player's information is already in the dictionary
    if player_name in player_info_dict:
        # If the player's information is from WEEK 8, skip the entry from WEEK 7
        if week == 8:
            continue

    # Create a list of information for the player
    player_info = [pos, team]

    # Add the player's information to the dictionary
    player_info_dict[player_name] = player_info

# Now, player_info_dict contains the information for each player based on WEEK = 8 with fallback to WEEK = 7
print(player_info_dict)

# Specify the file name where you want to save the information
file_name = 'player_info.txt'

# Open the file for writing
with open(file_name, 'w') as file:
    # Iterate through the dictionary and write player information to the file
    for player, info in player_info_dict.items():
        # Extract position and team from the info list
        pos, team = info
        # Write the player's name, position, and team to the file as a comma-separated line
        file.write(f'{player}, {pos}, {team}\n')

print(f"Player information has been saved to {file_name}")