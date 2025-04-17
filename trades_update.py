import pandas as pd
df = pd.read_csv("newData/player_stats_2024.csv")

df_filtered = df[df['player_id'] == '00-0023459']
df_filtered.head(20).sort_values(by='week', ascending=False)
df_filtered.columns


url = "https://www.spotrac.com/nfl/transactions/trade"  # Replace with your actual URL
tables = pd.read_html(url)

# If there are multiple tables, select the one you need
df = tables[0]  # Extracting the first table


print(len(tables))
print(df)

