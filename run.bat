@echo off
echo ========================================
echo Steganography  - Launcher
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://python.org
    pause
    exit /b 1
)

echo Python detected: 
python --version
echo.

REM Check if requirements are installed
echo Checking dependencies...
python -c "import PIL, numpy, scipy, cv2, moviepy" >nul 2>&1
if errorlevel 1 (
    echo.
    echo Some dependencies are missing.
    echo Installing required packages...
    echo.
    pip install -r requirements.txt
    if errorlevel 1 (
        echo.
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
    echo.
    echo Dependencies installed successfully!
    echo.
)

echo Starting Steganography Analyzer GUI...
echo.
python main_gui.py

if errorlevel 1 (
    echo.
    echo ERROR: Application failed to start
    echo Check the error message above for details
    pause
    exit /b 1
)
