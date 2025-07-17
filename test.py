import pandas as pd
import numpy as np
import os

# Ensure output folder exists
os.makedirs('data/raw', exist_ok=True)

# Generate network data
network_data = pd.DataFrame({
    'timestamp': pd.date_range(start='2023-01-01', periods=1000, freq='s'),
    'network_type': np.random.choice(['4G', '5G', 'WiFi'], 1000),
    'device_type': np.random.choice(['mobile', 'tablet', 'desktop'], 1000),
    'total_data': np.random.uniform(1e6, 1e9, 1000),
    'duration': np.random.uniform(1, 300, 1000),
    'start_time': np.random.uniform(1e9, 1e10, 1000),
    'bandwidth': np.random.uniform(1, 100, 1000),
    'latency': np.random.uniform(1, 500, 1000),
    'bitrate': np.random.uniform(100, 10000, 1000),
    'buffering': np.random.uniform(0, 5000, 1000)
})
network_data['end_time'] = network_data['start_time'] + \
    np.random.uniform(0.1, 5, 1000)
network_data.to_csv('data/raw/network_data.csv', index=False)

# Generate video data
video_data = pd.DataFrame({
    'timestamp': pd.date_range(start='2023-01-01', periods=500, freq='ms'),
    'frame_quality': np.random.uniform(0.7, 1.0, 500),
    'compression_ratio': np.random.uniform(0.1, 0.9, 500),
    'resolution': np.random.choice(['1920x1080', '1280x720', '3840x2160'], 500),
    'bit_depth': np.random.choice([8, 10, 12], 500)
})
video_data.to_csv('data/raw/video_data.csv', index=False)

print("✅ Raw data generated.")
