import pandas as pd
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt

# Load your DataFrame
data = pd.read_csv('WK_1-5.csv')  # Replace 'your_data.csv' with the actual file path
data = data.dropna(subset=['WON'])

# Define the features and target variable
features = ['NAME', 'POS', 'TEAM', 'OPP', '@HOME', 'WEEK']
target = 'FPTS'


label_encoders = {}
categorical_columns = ['POS', 'TEAM', 'OPP', 'NAME', '@HOME']
for column in categorical_columns:
    label_encoders[column] = LabelEncoder()
    data[column] = label_encoders[column].fit_transform(data[column])



# Sort your data by week
data.sort_values(by='WEEK', inplace=True)
# Split the data by week
train_data = data[data['WEEK'] <= 4]  # Use the first four weeks for training
test_data = data[data['WEEK'] == 5]   # Use the fifth week for testing
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


# Create a new data point for prediction with the same features
new_data_point = {
    'NAME': label_encoders['NAME'].transform(['Trevor Lawrence'])[0],
    'POS': label_encoders['POS'].transform(['QB'])[0],
    'TEAM': label_encoders['TEAM'].transform(['Jax'])[0],
    'OPP': label_encoders['OPP'].transform(['Ind'])[0], 
    '@HOME': label_encoders['@HOME'].transform([True])[0], 
    'WEEK': 6
}
# Create a DataFrame with the new data point
new_data_df = pd.DataFrame([new_data_point])
# Use the model to make predictions
predicted_fpts = model.predict(new_data_df)
# Display the predicted fantasy points
print(f"Predicted Fantasy Points: {predicted_fpts[0]}")



# Get feature importances from the model
feature_importance = model.feature_importances_
feature_names = model.get_booster().feature_names
feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importance})
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
plt.figure(figsize=(10, 6))
plt.barh(feature_importance_df['Feature'], feature_importance_df['Importance'])
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Feature Importance')
plt.show()





