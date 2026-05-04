import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split

# Add root directory to path to import src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocessing import clean_data, preprocess_features
from src.model import YieldModel

def run_training():
    data_path = os.path.join('data', 'yield_df.csv')
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found. Please ensure the data file is in the 'data/' directory.")
        return

    print("Loading data...")
    df = pd.read_csv(data_path)

    print("Cleaning data...")
    df = clean_data(df)

    print("Preprocessing features...")
    X, y = preprocess_features(df)

    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print(f"Training model on {len(X_train)} samples...")
    model_wrapper = YieldModel()
    model_wrapper.train(X_train, y_train)

    # Evaluate
    score = model_wrapper.model.score(X_test, y_test)
    print(f"Model R2 Score: {score:.4f}")

    # Save
    if not os.path.exists('models'):
        os.makedirs('models')
        
    model_wrapper.save(os.path.join('models', 'yield_model.pkl'), 
                       os.path.join('models', 'scaler.pkl'))
    print("Training pipeline completed successfully.")

if __name__ == "__main__":
    run_training()
