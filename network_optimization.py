import joblib
import pandas as pd
import numpy as np
from config import *

class NetworkOptimizer:
    def __init__(self):
        self.model = None
        self.scaler = None

    def load_model(self):
        self.model = joblib.load(NET_OPT_MODEL_PATH)
        self.scaler = joblib.load(SCALER_PATH)
        return self.model is not None and self.scaler is not None

    def optimize_bandwidth(self, network_conditions):
        """Predict optimal bandwidth for given network conditions"""
        if not self.model or not self.scaler:
            self.load_model()
        
        # Create input DataFrame with correct feature order
        input_data = {col: [network_conditions.get(col, 0)] for col in FEATURE_COLUMNS}
        input_df = pd.DataFrame(input_data)
        
        # Apply scaling
        input_df[FEATURE_COLUMNS] = self.scaler.transform(input_df[FEATURE_COLUMNS])
        
        return self.model.predict(input_df)[0]