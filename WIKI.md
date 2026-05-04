# 📖 Project Wiki: Crop Yield Prediction

Welcome to the comprehensive guide for the **Crop Yield Prediction** project. This project leverages machine learning to predict agricultural yields based on historical data, climatic conditions, and pesticide usage.

---

## 🏛 Architecture & Structure

The project is designed with a **Modular Pattern** to separate data science logic from the application layer.

### 📁 Directory Layout
- **`src/`**: Core logic.
  - `preprocessing.py`: Data cleaning, outlier treatment, and feature engineering.
  - `model.py`: Model wrapper for training, saving, and loading.
- **`scripts/`**: Automation tools.
  - `train_pipeline.py`: End-to-end script to train the model from a CSV file.
- **`server/`**: Web application.
  - `api/`: Modular Flask blueprints for predictions.
  - `static/` & `templates/`: Premium Glassmorphism frontend.
- **`assets/`**: Visualizations, images, and project documentation assets.
- **`data/`**: Local storage for datasets (e.g., `yield_df.csv`).
- **`models/`**: Serialized model files and scalers (`.pkl`).

---

## 🧪 Machine Learning Pipeline

### 1. Data Cleaning
- **Duplicate Removal**: Ensures the model isn't biased by repeated entries.
- **Outlier Treatment**: Average temperature is clipped using the IQR method to prevent extreme climatic anomalies from skewing predictions.

### 2. Feature Engineering
- **One-Hot Encoding**: Categorical variables like `Item` (crop type) are converted into numeric binary columns.
- **Scaling**: `StandardScaler` is used to normalize numeric features, ensuring models like KNN or Linear Regression perform optimally.

### 3. Model Selection
- **Random Forest Regressor**: Chosen as the primary model due to its robustness against non-linear relationships and feature importance insights.
- **Performance**: Achieves an R² score of ~0.97 on the testing set.

---

## 🌐 Web Application

The project features a **Production-Ready Flask Server**.

- **Endpoints**:
  - `GET /`: Home page with prediction form.
  - `POST /api/v1/predict`: Asynchronous endpoint returning JSON predictions.
- **Frontend**:
  - Built with **Glassmorphism** UI principles.
  - Uses modern CSS (Flexbox/Grid) and Vanilla JS for a smooth, no-refresh user experience.

---

## 🚀 Deployment Guide

### Local Setup
```bash
# 1. Setup environment
setup.bat

# 2. Train model
python scripts/train_pipeline.py

# 3. Run App
python app.py
```

### Production
The app is configured for `gunicorn`:
```bash
gunicorn -w 4 app:app
```

---

## 📊 Results & Visualization
The model provides high-accuracy predictions. Key visualizations (EDA) can be found in the `yield.ipynb` notebook, illustrating:
- Correlation between rainfall and yield.
- Impact of pesticide usage on different crop types.
- Temperature trends over the years.

---

*Documentation maintained by the Yield Prediction Team.*
