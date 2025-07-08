#!/bin/bash

echo "========================================"
echo "AI Face Detection Attendance System"
echo "========================================"
echo

echo "Checking Python installation..."
python3 --version
if [ $? -ne 0 ]; then
    echo "Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3.7 or higher"
    exit 1
fi

echo
echo "Installing dependencies..."
pip3 install -r requirements.txt

echo
echo "Running installation test..."
python3 test_installation.py

echo
echo "Starting attendance system..."
python3 attendance_system.py 