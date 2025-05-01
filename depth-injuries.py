import nfl_data_py as nfl
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

depth24 = nfl.import_depth_charts(years=[2024])
depth24.to_csv('newData/depthcharts/depth_charts_2024.csv', index=False)
depth24.columns


injuries24 = nfl.import_injuries(years=[2024])
injuries24.to_csv('newData/injuries/injuries_2024.csv', index=False)


dep_filt = depth24[(depth24['club_code'] == 'SF') & (depth24['depth_position'] == 'WR') & (depth24['week'] == 10)]
dep_filt.sort_values(by=['week', 'depth_team'], ascending=True)


injuries24.head()

injuries24.value_counts("practice_status")
injuries24.value_counts("report_status")