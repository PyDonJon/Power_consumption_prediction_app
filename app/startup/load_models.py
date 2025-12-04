from xgboost import XGBRegressor
import pickle

def load_consumption_model() -> XGBRegressor:

    file = open("./app/models/xgb_model.pkl","rb")
    xgb_regressor = pickle.load(file)
    file.close()

    return xgb_regressor 