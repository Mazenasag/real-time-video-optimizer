# import os
# import pandas as pd
# import numpy as np
# import joblib
# from sklearn.preprocessing import StandardScaler
# from sklearn.impute import SimpleImputer
# from config import *

# class DataPreprocessor:
#     def __init__(self):
#         self.scaler = StandardScaler()
#         self.imputer = SimpleImputer(strategy='mean')
#         self.fitted = False

#     def load_data(self, filepath):
#         return pd.read_csv(filepath)

#     def clean_data(self, data):
#         data = data.drop_duplicates()
#         data = pd.DataFrame(self.imputer.fit_transform(data), columns=data.columns)
#         return data

#     def normalize_data(self, data, columns):
#         # Only normalize specified columns that exist
#         existing_cols = [col for col in columns if col in data.columns]
#         if existing_cols:
#             data[existing_cols] = self.scaler.fit_transform(data[existing_cols])
#             joblib.dump(self.scaler, SCALER_PATH)  # Save scaler
#             self.fitted = True
#         return data

#     def add_interaction_features(self, data, feature_cols):
#         # Add pairwise product features (interaction terms)
#         for i in range(len(feature_cols)):
#             for j in range(i+1, len(feature_cols)):
#                 col1, col2 = feature_cols[i], feature_cols[j]
#                 new_col = f"{col1}_x_{col2}"
#                 data[new_col] = data[col1] * data[col2]
#         return data

#     def add_polynomial_features(self, data, feature_cols):
#         # Add squared terms
#         for col in feature_cols:
#             data[f"{col}_sq"] = data[col] ** 2
#         return data

#     def print_feature_correlations(self, data, target_col):
#         corr = data.corr()
#         print("\nCorrelation of features with target:")
#         print(corr[target_col].sort_values(ascending=False))

#     def preprocess_network(self):
#         data = self.load_data(NETWORK_DATA_PATH)
#         data = self.clean_data(data)

#         # Add feature engineering steps before normalization
#         data = self.add_interaction_features(data, FEATURE_COLUMNS)
#         data = self.add_polynomial_features(data, FEATURE_COLUMNS)

#         # Normalize original and newly created features except target column
#         all_features = [col for col in data.columns if col != TARGET_COLUMN]
#         data = self.normalize_data(data, all_features)

#         self.print_feature_correlations(data, TARGET_COLUMN)

#         # Ensure output directory exists
#         os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
#         output_path = os.path.join(PROCESSED_DATA_DIR, 'preprocessed_network_data.csv')
#         data.to_csv(output_path, index=False)

#         return data


# if __name__ == "__main__":
#     preprocessor = DataPreprocessor()
#     processed_data = preprocessor.preprocess_network()
#     print("✅ Preprocessing complete. Processed data shape:", processed_data.shape)
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from config import *

class DataPreprocessor:
    def __init__(self, correlation_threshold=0.01):  # ⬅️ Lowered threshold to include more features
        self.scaler = StandardScaler()
        self.imputer = SimpleImputer(strategy='mean')
        self.fitted = False
        self.correlation_threshold = correlation_threshold
        self.selected_features = []

    def load_data(self, filepath):
        return pd.read_csv(filepath)

    def clean_data(self, data):
        data = data.drop_duplicates()
        data = pd.DataFrame(self.imputer.fit_transform(data), columns=data.columns)
        return data

    def select_features_by_correlation(self, data, target_column):
        correlation = data.corr()[target_column].abs()
        self.selected_features = correlation[correlation >= self.correlation_threshold].index.tolist()
        if target_column not in self.selected_features:
            self.selected_features.append(target_column)
        return data[self.selected_features]

    def normalize_data(self, data, exclude_columns=[]):
        columns_to_scale = [col for col in data.columns if col not in exclude_columns]
        data[columns_to_scale] = self.scaler.fit_transform(data[columns_to_scale])
        joblib.dump(self.scaler, SCALER_PATH)
        self.fitted = True
        return data

    def preprocess_network(self):
        data = self.load_data(NETWORK_DATA_PATH)
        data = self.clean_data(data)
        data = self.select_features_by_correlation(data, TARGET_COLUMN)
        data = self.normalize_data(data, exclude_columns=[TARGET_COLUMN])

        os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
        output_path = os.path.join(PROCESSED_DATA_DIR, 'preprocessed_network_data.csv')
        data.to_csv(output_path, index=False)

        print(f"\n✅ Selected features ({len(self.selected_features)-1}): {self.selected_features[:-1]}")
        print(f"✅ Saved to: {output_path}")
        return data

if __name__ == "__main__":
    preprocessor = DataPreprocessor()
    processed_data = preprocessor.preprocess_network()
    print("✅ Preprocessing complete. Processed data shape:", processed_data.shape)

