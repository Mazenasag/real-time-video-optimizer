import os

# Directory paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')
COMPRESSED_DATA_DIR = os.path.join(DATA_DIR, 'compressed')
MODELS_DIR = os.path.join(BASE_DIR, 'models')

# File paths
NETWORK_DATA_PATH = os.path.join(RAW_DATA_DIR, 'network_data.csv')
VIDEO_DATA_PATH = os.path.join(RAW_DATA_DIR, 'video_data.csv')
INPUT_VIDEO_PATH = os.path.join(RAW_DATA_DIR, 'input_video.mp4')
COMPRESSED_VIDEO_PATH = os.path.join(COMPRESSED_DATA_DIR, 'optimized_video.mp4')

# Model paths
LINEAR_MODEL_PATH = os.path.join(MODELS_DIR, 'linear_regression_model.pkl')
RF_MODEL_PATH = os.path.join(MODELS_DIR, 'random_forest_model.pkl')
NET_OPT_MODEL_PATH = os.path.join(MODELS_DIR, 'network_optimization_model.pkl')
SCALER_PATH = os.path.join(MODELS_DIR, 'scaler.pkl')  # ✅ FIXED

# Feature columns to normalize
FEATURE_COLUMNS = ['total_data', 'duration', 'avg_bitrate', 'latency']

# Preprocessing config
FEATURE_COLUMNS = [
    'receiving_rate',
    'packet_delay',
    'packet_loss_ratio',
    'rtt',
    'bandwidth_usage',
    'throughput',
    'error_rate',
    'jitter'
]

NORMALIZATION_COLUMNS = FEATURE_COLUMNS
TARGET_COLUMN = 'actual_bandwidth'



