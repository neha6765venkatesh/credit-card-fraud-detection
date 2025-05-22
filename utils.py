import joblib
import pandas as pd

model = joblib.load('models/xgboost_model.pkl')
def preprocess_input(category, amt, gender, city_pop):
    gender_encoded = 1 if gender.lower() == "male" else 0
    # Use same encoding for category as during training (simplified for demo)
    category_mapping = {'gas_transport': 0, 'grocery_net': 1, 'grocery_pos': 2, 'shopping_pos': 3}
    category_encoded = category_mapping.get(category.lower(), 0)
    
    data = pd.DataFrame([[category_encoded, amt, gender_encoded, city_pop]],
                        columns=['category', 'amt', 'gender', 'city_pop'])
    return data

def predict(data):
    return model.predict(data)[0]