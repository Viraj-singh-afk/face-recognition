# Setup Instructions

> **Warning:**
> - For best results, use Python 3.8–3.11. Python 3.12+ and 3.13+ may not work with face-recognition due to dlib build issues.
> - On Windows, you may need to install CMake and Visual Studio Build Tools if you see errors about dlib or CMake during installation.

## Prerequisites

Before running the AI Face Detection Attendance System, you need to install Python 3.7 or higher.

### Installing Python

**Windows:**
1. Download Python from https://www.python.org/downloads/
2. During installation, make sure to check "Add Python to PATH"
3. Verify installation by opening Command Prompt and typing: `python --version`

**macOS:**
1. Install using Homebrew: `brew install python3`
2. Or download from https://www.python.org/downloads/

**Linux:**
1. Install using package manager: `sudo apt-get install python3 python3-pip`
2. Or download from https://www.python.org/downloads/

## Installation Steps

1. **Open Command Prompt/Terminal** in the project directory

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Test the installation**:
   ```bash
   python test_installation.py
   ```

4. **Create face images** (optional):
   ```bash
   python create_sample_faces.py
   ```

5. **Start the system**:
   ```bash
   python attendance_system.py
   ```

## Quick Start (Windows)

If you have Python installed, simply double-click `run_attendance_system.bat` to automatically:
- Install all dependencies
- Test the installation
- Start the attendance system

## Quick Start (Mac/Linux)

If you have Python installed:
1. Open terminal in the project directory
2. Run: `chmod +x run_attendance_system.sh`
3. Run: `./run_attendance_system.sh`

## System Features

✅ **Real-time Face Detection** - Uses OpenCV to access webcam and detect faces
✅ **Face Recognition** - Uses face_recognition library to identify known faces  
✅ **Attendance Logging** - Automatically logs to CSV files with timestamps
✅ **Duplicate Prevention** - Avoids duplicate entries during one session
✅ **Visual Feedback** - Shows camera feed with rectangles and names around faces
✅ **GUI Interface** - Simple Tkinter GUI to start/stop attendance sessions
✅ **Session Management** - Clear session data and manage attendance tracking

## File Structure

```
face_attendance_system/
├── attendance_system.py      # Main application
├── requirements.txt          # Python dependencies
├── test_installation.py     # Installation test script
├── create_sample_faces.py   # Face image creator
├── run_attendance_system.bat # Windows launcher
├── run_attendance_system.sh # Unix launcher
├── README.md               # Detailed documentation
├── QUICK_START.md         # Quick start guide
├── SETUP_INSTRUCTIONS.md  # This file
├── known_faces/           # Add face images here
└── attendance_logs/       # Generated attendance files
```

## Usage

1. **Add face images** to the `known_faces` folder
2. **Run the system**: `python attendance_system.py`
3. **Click "Start Attendance"** to begin monitoring
4. **View logs** in the `attendance_logs` folder

## Troubleshooting

- **Python not found**: Install Python and add to PATH
- **Dependencies fail**: Try `pip install --upgrade pip` first
- **Webcam issues**: Make sure no other app is using the camera
- **Face recognition problems**: Use better lighting and clearer photos

## Support

For detailed documentation, see `README.md`
For quick setup, see `QUICK_START.md` 