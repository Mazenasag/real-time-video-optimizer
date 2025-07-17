import os
from utils.helpers import create_directories
from data_preprocessing import DataPreprocessor
from machine_learning import MLTrainer
from network_optimization import NetworkOptimizer
from evaluation import Evaluator
from config import *

def main():
    # Setup environment
    create_directories()
    
    # Step 1: Data preprocessing
    print("\n=== Data Preprocessing ===")
    preprocessor = DataPreprocessor()
    network_data = preprocessor.preprocess_network()
    print("Data preprocessing complete")
    
    # Step 2: Machine learning training
    print("\n=== Machine Learning Training ===")
    ml_trainer = MLTrainer()
    data = ml_trainer.load_data()
    X_train, X_test, y_train, y_test = ml_trainer.split_data(data)
    ml_trainer.train_models(X_train, y_train)
    ml_trainer.save_models()
    
    # Step 3: Network optimization
    print("\n=== Network Optimization ===")
    net_optimizer = NetworkOptimizer()
    
    # Simulate current network conditions
    current_conditions = {
        'receiving_rate': 850,
        'packet_delay': 42,
        'packet_loss_ratio': 0.02,
        'rtt': 75,
        'bandwidth_usage': 450000000,
        'throughput': 3800,
        'error_rate': 0.015,
        'jitter': 8
    }
    
    # Predict optimal bandwidth
    predicted_bandwidth = net_optimizer.optimize_bandwidth(current_conditions)
    print(f"Predicted optimal bandwidth: {predicted_bandwidth:.2f} Mbps")
    
    # Step 4: Evaluation
    print("\n=== Evaluation ===")
    evaluator = Evaluator()
    evaluator.load_models()
    
    # Model evaluation
    model_metrics = evaluator.evaluate_models()
    print("\nModel Evaluation Results:")
    for model, metrics in model_metrics.items():
        print(f"{model.upper()}: MAE={metrics['mae']:.2f}, RMSE={metrics['rmse']:.2f}")

if __name__ == "__main__":
    main()