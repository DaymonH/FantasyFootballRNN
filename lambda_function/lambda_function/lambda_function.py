import json
import lightgbm as lgb
from sklearn.preprocessing import LabelEncoder

# Load the LightGBM model from a JSON file
def load_lightgbm_model(model_path):
    model = lgb.Booster(model_file=model_path)
    return model
# Load the label encoders from a JSON file
def load_label_encoders(label_encoders_path):
    with open(label_encoders_path, 'r') as label_encoders_file:
        label_encoders_dict = json.load(label_encoders_file)
    # Reconstruct the LabelEncoder objects
    label_encoders = {column: LabelEncoder() for column in label_encoders_dict}
    for column, label_encoder in label_encoders.items():
        label_encoder.classes_ = label_encoders_dict[column]
    return label_encoders

def lambda_handler(event, context):
    player = 'Jerome Ford'
    position = 'RB'
    team = 'Cle'
    Opp = 'Ind'
    at_home = False
    week = 7
    DnP = False
    
    # Example usage
    model_path = 'lambda_function/lightgbm_model.json'  # Specify the correct file path
    label_encoders_path = 'lambda_function/label_encoders1-5.json'  # Specify the correct file path

    # Load the LightGBM model
    loaded_model = load_lightgbm_model(model_path)
    # Load the label encoders
    loaded_label_encoders = load_label_encoders(label_encoders_path)
    
    new_data_point = {
        'NAME': label_encoders['NAME'].transform([player])[0],
        'POS': label_encoders['POS'].transform([position])[0],
        'TEAM': label_encoders['TEAM'].transform([team])[0],
        'OPP': label_encoders['OPP'].transform([Opp])[0], 
        '@HOME': label_encoders['@HOME'].transform([at_home])[0], 
        'WEEK': week,
        'DnP': label_encoders['DnP'].transform([DnP])[0]
    }

    predicted_fpts = model.predict([new_data_point])

    response = {
        "statusCode": 200,
        "body": f"Predicted points: {player} {predicted_fpts[0]:.2f}"
    }

    return response
