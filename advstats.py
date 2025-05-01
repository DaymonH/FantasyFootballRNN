import pandas as pd

df = pd.read_csv(r'newData\advstats\advstats_week_def_2024.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df.sort_values(by='')