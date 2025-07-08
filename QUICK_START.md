# Quick Start Guide

## Windows Users

1. **Double-click** `run_attendance_system.bat` to automatically install dependencies and start the system

## Mac/Linux Users

1. **Open terminal** in the project directory
2. **Run**: `chmod +x run_attendance_system.sh`
3. **Run**: `./run_attendance_system.sh`

## Manual Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Test installation**:
   ```bash
   python test_installation.py
   ```

3. **Create face images** (optional):
   ```bash
   python create_sample_faces.py
   ```

4. **Start the system**:
   ```bash
   python attendance_system.py
   ```

## First Time Setup

1. **Add face images** to the `known_faces` folder:
   - Use clear, front-facing photos
   - Name files descriptively (e.g., `john_doe.jpg`)
   - Supported formats: JPG, JPEG, PNG

2. **Run the system** and click "Start Attendance"

3. **View attendance logs** in the `attendance_logs` folder

## Troubleshooting

- **Webcam not working**: Make sure no other app is using the camera
- **Face recognition issues**: Use better lighting and clearer photos
- **Installation problems**: See the main README.md for detailed troubleshooting

## System Requirements

- Python 3.7+
- Webcam
- Good lighting
- 4GB+ RAM recommended 