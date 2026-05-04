@echo off
echo ==========================================
echo Yield Prediction Project Setup
echo ==========================================

:: Create virtual environment with a shorter name 'v'
if not exist v (
    echo Creating virtual environment...
    python -m venv v
)

:: Activate virtual environment and install requirements
echo Activating virtual environment and installing dependencies...
call v\Scripts\activate
python -m pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt

echo.
echo ==========================================
echo Setup Complete!
echo To activate the environment, run: v\Scripts\activate
echo To train the model, run: python scripts\train_pipeline.py
echo To start the web app, run: python app.py
echo ==========================================
pause
