import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error
from config import *

class Evaluator:
    def __init__(self):
        self.models = {}
        
    def load_models(self):
        self.models['random_forest'] = joblib.load(RF_MODEL_PATH)
        return len(self.models) > 0

    def load_test_data(self):
        return pd.read_csv(os.path.join(PROCESSED_DATA_DIR, 'test_data.csv'))

    def evaluate_models(self):
        test_data = self.load_test_data()
        X_test = test_data[FEATURE_COLUMNS]
        y_test = test_data[TARGET_COLUMN]
        
        metrics = {}
        for name, model in self.models.items():
            y_pred = model.predict(X_test)
            metrics[name] = {
                'mae': mean_absolute_error(y_test, y_pred),
                'rmse': np.sqrt(mean_squared_error(y_test, y_pred))
            }
        return metrics