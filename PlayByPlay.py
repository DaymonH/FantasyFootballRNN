TO_DROP = [
    "qb_epa", "xyac_epa", "xyac_mean_yardage", "xyac_median_yardage", "xyac_success", "xyac_fd", "xpass", "pass_oe",
    "tackle_for_loss_1_player_id", "tackle_for_loss_1_player_name", "tackle_for_loss_2_player_id", "tackle_for_loss_2_player_name",
    "qb_hit_1_player_id", "qb_hit_1_player_name", "qb_hit_2_player_id", "qb_hit_2_player_name", "forced_fumble_player_1_team",
    "forced_fumble_player_1_player_id", "forced_fumble_player_1_player_name", "forced_fumble_player_2_team", "forced_fumble_player_2_player_id",
    "forced_fumble_player_2_player_name", "solo_tackle_1_team", "solo_tackle_2_team", "solo_tackle_1_player_id", "solo_tackle_2_player_id",
    "solo_tackle_1_player_name", "solo_tackle_2_player_name", "assist_tackle_1_player_id", "assist_tackle_1_player_name", "assist_tackle_1_team",
    "assist_tackle_2_player_id", "assist_tackle_2_player_name", "assist_tackle_2_team", "assist_tackle_3_player_id", "assist_tackle_3_player_name",
    "assist_tackle_3_team", "assist_tackle_4_player_id", "assist_tackle_4_player_name", "assist_tackle_4_team", "tackle_with_assist",
    "tackle_with_assist_1_player_id", "tackle_with_assist_1_player_name", "tackle_with_assist_1_team", "tackle_with_assist_2_player_id",
    "tackle_with_assist_2_player_name", "tackle_with_assist_2_team", "pass_defense_1_player_id", "pass_defense_1_player_name",
    "pass_defense_2_player_id", "pass_defense_2_player_name", "fumbled_1_team", "fumbled_1_player_id", "fumbled_1_player_name",
    "fumbled_2_player_id", "fumbled_2_player_name", "fumbled_2_team", "fumble_recovery_1_team", "fumble_recovery_1_yards",
    "fumble_recovery_1_player_id", "fumble_recovery_1_player_name", "fumble_recovery_2_team", "fumble_recovery_2_yards",
    "fumble_recovery_2_player_id", "fumble_recovery_2_player_name", "sack_player_id", "sack_player_name", "half_sack_1_player_id",
    "half_sack_1_player_name", "half_sack_2_player_id", "half_sack_2_player_name", "lateral_receiver_player_id", "lateral_receiving_yards",
    "lateral_rusher_player_id", "lateral_rusher_player_name", "lateral_rushing_yards", "ep", "epa", "total_home_epa", "total_away_epa", 
    "total_home_rush_epa", "total_away_rush_epa", "total_home_pass_epa", "total_away_pass_epa", "air_epa", "yac_epa", 
    "comp_air_epa", "comp_yac_epa", "total_home_comp_air_epa", "total_away_comp_air_epa", 
    "total_home_comp_yac_epa", "total_away_comp_yac_epa", "total_home_raw_air_epa", 
    "total_away_raw_air_epa", "total_home_raw_yac_epa", "total_away_raw_yac_epa", "wp", 
    "def_wp", "home_wp", "away_wp", "wpa", "vegas_wpa", "vegas_home_wpa", "home_wp_post", 
    "away_wp_post", "vegas_wp", "vegas_home_wp", "total_home_rush_wpa", "total_away_rush_wpa", 
    "total_home_pass_wpa", "total_away_pass_wpa", "air_wpa", "yac_wpa", "comp_air_wpa", 
    "comp_yac_wpa", "total_home_comp_air_wpa", "total_away_comp_air_wpa", "total_home_comp_yac_wpa", 
    "total_away_comp_yac_wpa", "total_home_raw_air_wpa", "total_away_raw_air_wpa", 
    "total_home_raw_yac_wpa", "total_away_raw_yac_wpa"
]


import nfl_data_py as nfl

# pbp24 = nfl.import_pbp_data(years=[2024])
# pbp24.to_csv("newData/pbp/play_by_play_2024.csv", index=False)

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None) 

df = pd.read_csv("newData/pbp/play_by_play_2024.csv")
df = df.drop(TO_DROP, axis=1).reset_index(drop=True)

df = df[(df['play_type'] != 'no_play') & 
            (df['play_type'] != 'kickoff') & 
            (df['play_type'] != 'extra_point') &
             (df['season_type'] == 'REG')
             ].reset_index(drop=True)









# Get the top 15 receivers by total receiving yards
top_receivers = df.groupby(['receiver_player_id', 'receiver_player_name'])['receiving_yards'].sum()
top_receivers = top_receivers.sort_values(ascending=False).head(100)
# Filter the DataFrame to include only rows for the top 15 receivers
top_receivers_df = df[df['receiver_player_name'].isin(top_receivers.index.get_level_values('receiver_player_name'))]
# Group by receiver_player_name and calculate the total completed passes, total attempts, and total yards
completion_stats = top_receivers_df.groupby('receiver_player_name').agg(
    total_completions=('complete_pass', 'sum'),  # Sum of complete_pass (1 for completed passes)
    total_attempts=('complete_pass', 'count'),  # Count of all rows where receiver_player_name is present
    total_yards=('receiving_yards', 'sum')      # Sum of receiving yards
)
# Calculate the completion percentage
completion_stats['completion_percentage'] = (completion_stats['total_completions'] / completion_stats['total_attempts']) * 100
# Sort by total yards in descending order
completion_stats = completion_stats.sort_values(by='total_yards', ascending=False)
# Display the completion stats with total yards
print(completion_stats)

print(df.columns.tolist())

# pen_df = df[(df['penalty'] == 1.0)].reset_index(drop=True)
# pen_df = df[(df['penalty'] == 1.0) & (df['penalty_yards'] == 0.0)].reset_index(drop=True)
# pen_df = df[(df['play_type'] == 'no_play') & (df['penalty_yards'] == 0.0) & (df['yards_gained'] == 0.0)].reset_index(drop=True)
pen_df = df[(df['play_type'] == 'no_play')].reset_index(drop=True)
# pen_df = df[(df['penalty'] == 1.0) & (df['play_deleted'] == 1.0)].reset_index(drop=True)
pen_df = df[df['desc'].str.contains(r'.*Decline.*', case=False, regex=True)]

sf_rows = pen_df[(pen_df['posteam'] == 'SF') | (pen_df['defteam'] == 'SF')]

# play_type is the key
columns_to_check = [
    'posteam',
    'defteam',
    'extra_point_attempt',
    'field_goal_attempt',
    'yardline_100',
    'play_type',
    'down',
    'ydstogo',
    'first_down',
    'yards_gained',
    "penalty",
    "penalty_yards",
    "penalty_team",
    "penalty_player_id",
    "penalty_player_name",
    "penalty_type",
    "play_deleted",
    "replay_or_challenge_result",
    "aborted_play",
    "play",
    'desc'
]

pen_df.loc[pen_df.index[-3]]
sf_rows.loc[sf_rows.index[-3]][columns_to_check]
pen_df.loc[pen_df.index[-3]][columns_to_check]['desc']
pen_df.tail(5)[columns_to_check]
df.head(3)[columns_to_check]





Receptions Last 3 games / Last 18 games