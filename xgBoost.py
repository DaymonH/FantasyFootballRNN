import pandas as pd
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt

# Load your DataFrame
data = pd.read_csv('QB-RB-WR-TE.csv')  # Replace 'your_data.csv' with the actual file path
data = data.dropna(subset=['WON'])

# Define the features and target variable
features = ['NAME', 'POSITION', 'TEAM', 'OPP', 'AT_HOME', 'WEEK']
target = 'FPTS'


label_encoders = {}
categorical_columns = ['POSITION', 'TEAM', 'OPP', 'NAME', 'AT_HOME']
for column in categorical_columns:
    label_encoders[column] = LabelEncoder()
    data[column] = label_encoders[column].fit_transform(data[column])



# Sort your data by week
data.sort_values(by='WEEK', inplace=True)
# Split the data by week
train_data = data[data['WEEK'] <= 3]  # Use the first four weeks for training
test_data = data[data['WEEK'] == 4]   # Use the fifth week for testing
# Define the features and target variable
# Separate features and target variables for training and testing
X_train = train_data[features]
y_train = train_data[target]
X_test = test_data[features]
y_test = test_data[target]
# Create and train the XGBoost model
model = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
model.fit(X_train, y_train)
# Make predictions on the test set
y_pred = model.predict(X_test)
# Evaluate the model using RMSE (Root Mean Squared Error)
rmse = sqrt(mean_squared_error(y_test, y_pred))
print(f"Root Mean Squared Error: {rmse}")
