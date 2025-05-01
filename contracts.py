import nfl_data_py as nfl
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

team_to_name = {
    "ARI": "Cardinals",
    "ATL": "Falcons",
    "BAL": "Ravens",
    "BUF": "Bills",
    "CAR": "Panthers",
    "CHI": "Bears",
    "CIN": "Bengals",
    "CLE": "Browns",
    "DAL": "Cowboys",
    "DEN": "Broncos",
    "DET": "Lions",
    "GB":  "Packers",
    "HOU": "Texans",
    "IND": "Colts",
    "JAX": "Jaguars",
    "KC":  "Chiefs",
    "LAC": "Chargers",
    "LA":  "Rams",
    "LV":  "Raiders",
    "MIA": "Dolphins",
    "MIN": "Vikings",
    "NE":  "Patriots",
    "NO":  "Saints",
    "NYG": "Giants",
    "NYJ": "Jets",
    "PHI": "Eagles",
    "PIT": "Steelers",
    "SEA": "Seahawks",
    "SF":  "49ers",
    "TB":  "Buccaneers",
    "TEN": "Titans",
    "WAS": "Commanders"
}

team = 'KC'
name = team_to_name[team]
# positions = ['LT', 'LG', 'C', 'RG', 'RT', 'OL']
positions = ['FS']

# contracts = nfl.import_contracts()
# contracts.to_csv('newData/contracts/historical_contracts.csv', index=False)
contracts = pd.read_csv('newData/contracts/historical_contracts.csv')
contracts.value_counts("year_signed")
contracts['team'].unique()
contracts.value_counts("team")
contracts.head()
contracts.sort_values(by='draft_year', ascending=False).head()
contracts_latest = contracts.loc[contracts.groupby('gsis_id')['year_signed'].idxmax()]

con_filtered = contracts_latest[
    ((contracts_latest['team'] == name) | contracts_latest['team'].str.contains(fr'/{team}$', na=False)) &
    (contracts_latest['position'].isin(positions)) &
    (contracts_latest['is_active'] == True) 
].sort_values(by='inflated_apy', ascending=False)

con_filtered.head(50)


depth24 = pd.read_csv('newData/depthcharts/depth_charts_2024.csv')
depth24.value_counts("depth_position")
depth24.head()
depth24.value_counts("club_code")
dep_filt = depth24[
    (depth24['club_code'] == 'SF') & 
    (depth24['depth_position'].isin(['LT', 'LG', 'C', 'RG', 'RT', 'OL'])) & 
    (depth24['week'] == 2) &
    (depth24['season'] == 2024) &
    (depth24['depth_team'] == 1) 
]

contracts_sorted = contracts[['gsis_id', 'year_signed', 'apy', 'inflated_apy', 'apy_cap_pct']]\
    .sort_values(by=['year_signed'])  # right df: year_signed = right_on key

dep_sorted = dep_filt.sort_values(by=['season'])  # left df: season = left_on key

merged_df = pd.merge_asof(
    dep_sorted,
    contracts_sorted,
    by='gsis_id',
    left_on='season',
    right_on='year_signed',
    direction='backward'
)

merged_df.head(10)