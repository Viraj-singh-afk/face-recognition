@echo off
echo ========================================
echo AI Face Detection Attendance System
echo ========================================
echo.

echo Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7 or higher
    pause
    exit /b 1
)

echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Running installation test...
python test_installation.py

echo.
echo Starting attendance system...
python attendance_system.py

pause 