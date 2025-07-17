import pandas as pd
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from config import *

class MLTrainer:
    def __init__(self):
        self.models = {
            'random_forest': RandomForestRegressor(n_estimators=100, random_state=42)
        }
        self.test_data_path = os.path.join(PROCESSED_DATA_DIR, 'test_data.csv')

    def load_data(self):
        return pd.read_csv(os.path.join(PROCESSED_DATA_DIR, 'preprocessed_network_data.csv'))

    def split_data(self, data):
        # Ensure all feature columns exist
        X = data[[col for col in FEATURE_COLUMNS if col in data.columns]]
        y = data[TARGET_COLUMN]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Save test data
        test_data = X_test.copy()
        test_data[TARGET_COLUMN] = y_test
        test_data.to_csv(self.test_data_path, index=False)
        
        return X_train, X_test, y_train, y_test

    def train_models(self, X_train, y_train):
        for name, model in self.models.items():
            model.fit(X_train, y_train)
            print(f"Trained {name} model")

    def evaluate_models(self, X_test, y_test):
        metrics = {}
        for name, model in self.models.items():
            y_pred = model.predict(X_test)
            metrics[name] = {
                'mae': mean_absolute_error(y_test, y_pred),
                'rmse': np.sqrt(mean_squared_error(y_test, y_pred))
            }
        return metrics

    def save_models(self):
        joblib.dump(self.models['random_forest'], RF_MODEL_PATH)
        print(f"Models saved to {MODELS_DIR}")