# utils/helpers.py
import os
import pandas as pd
import numpy as np
from config import *

def create_directories():
    """Create required directories"""
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
    os.makedirs(COMPRESSED_DATA_DIR, exist_ok=True)
    os.makedirs(MODELS_DIR, exist_ok=True)

def generate_sample_data():
    """Generate sample network and video data"""
    # Network data
    network_data = pd.DataFrame({
        'timestamp': pd.date_range(start='2023-01-01', periods=1000, freq='s'),
        'network_type': np.random.choice(['4G', '5G', 'WiFi'], 1000),
        'device_type': np.random.choice(['mobile', 'tablet', 'desktop'], 1000),
        'total_data': np.random.uniform(1e6, 1e9, 1000),
        'duration': np.random.uniform(1, 300, 1000),
        'start_time': np.random.uniform(1e9, 1e10, 1000),
        'end_time': np.random.uniform(1e9, 1e10, 1000),
        'bandwidth': np.random.uniform(1, 100, 1000),
        'latency': np.random.uniform(1, 500, 1000),
        'bitrate': np.random.uniform(100, 10000, 1000),
        'buffering': np.random.uniform(0, 5000, 1000)
    })
    network_data.to_csv(NETWORK_DATA_PATH, index=False)
    
    # Video metadata
    video_data = pd.DataFrame({
        'timestamp': pd.date_range(start='2023-01-01', periods=500, freq='ms'),
        'frame_quality': np.random.uniform(0.7, 1.0, 500),
        'compression_ratio': np.random.uniform(0.1, 0.9, 500),
        'resolution': np.random.choice(['1920x1080', '1280x720', '3840x2160'], 500),
        'bit_depth': np.random.choice([8, 10, 12], 500)
    })
    video_data.to_csv(VIDEO_DATA_PATH, index=False)
    
    print(f"Sample data generated in {RAW_DATA_DIR}/")