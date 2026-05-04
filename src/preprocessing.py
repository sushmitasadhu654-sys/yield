import pandas as pd
import numpy as np

def clean_data(df):
    """
    Cleans the yield dataset based on the notebook logic.
    """
    # 1. Drop unnecessary columns
    if 'Unnamed: 0' in df.columns:
        df = df.drop('Unnamed: 0', axis=1)
        
    # 2. Handle duplicates
    df = df.drop_duplicates()
    
    # 3. Handle outliers for avg_temp (from notebook)
    Q1 = df['avg_temp'].quantile(0.25)
    Q3 = df['avg_temp'].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df['avg_temp'] = df['avg_temp'].clip(lower, upper)
    
    return df

def preprocess_features(df):
    """
    Performs one-hot encoding for the Item column.
    Note: Area is usually ignored in the notebook features for simplicity in the basic RF model.
    """
    # One-hot encoding for Item
    df = pd.get_dummies(df, columns=['Item'], prefix='Item')
    
    # Target and Features
    # Ensuring we have the columns expected by the model
    target = 'hg/ha_yield'
    
    # The notebook defines X explicitly:
    feature_cols = [
        'Year', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp',
        'Item_Maize', 'Item_Plantains and others', 'Item_Potatoes', 'Item_Rice, paddy',
        'Item_Sorghum', 'Item_Soybeans', 'Item_Sweet potatoes', 'Item_Wheat', 'Item_Yams'
    ]
    
    # Check which features are present (after dummies)
    available_features = [col for col in feature_cols if col in df.columns]
    
    X = df[available_features]
    y = df[target]
    
    return X, y
