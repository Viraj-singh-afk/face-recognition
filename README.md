# AI Face Detection Attendance System

A Python-based AI face detection attendance system that uses computer vision to automatically log attendance when known faces are detected through a webcam.

## Features

- **Real-time Face Detection**: Uses OpenCV to access webcam and detect faces in real-time
- **Face Recognition**: Uses the `face_recognition` library to identify known faces
- **Attendance Logging**: Automatically logs attendance to CSV files with timestamps
- **Duplicate Prevention**: Avoids duplicate entries during one session
- **Visual Feedback**: Shows real-time camera feed with rectangles and names around detected faces
- **GUI Interface**: Simple Tkinter GUI to start/stop attendance sessions
- **Session Management**: Clear session data and manage attendance tracking

## Requirements

- Python 3.7 or higher
- Webcam
- Good lighting conditions for accurate face recognition

## Installation

1. **Clone or download the project files**

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add face images to the `known_faces` folder**:
   - Create a folder named `known_faces` in the project directory
   - Add photos of people you want to recognize
   - Name the files with the person's name (e.g., `john_doe.jpg`, `jane_smith.png`)
   - Make sure each image contains a clear, front-facing photo of the person
   - Supported formats: JPG, JPEG, PNG

## Usage

1. **Prepare face images**:
   - Add photos to the `known_faces` folder
   - Use clear, well-lit photos with faces clearly visible
   - Name files descriptively (e.g., `student1.jpg`, `teacher_smith.jpg`)

2. **Run the system**:
   ```bash
   python attendance_system.py
   ```

3. **Using the GUI**:
   - The system will automatically load known faces on startup
   - Click "Start Attendance" to begin monitoring
   - Click "Stop Attendance" to stop monitoring
   - Click "Clear Session" to reset attendance tracking for the current session
   - Press 'q' in the camera window to quit

4. **View attendance logs**:
   - Attendance is automatically saved to CSV files in the `attendance_logs` folder
   - Files are named by date (e.g., `attendance_2024-01-15.csv`)
   - Each entry includes the person's name and timestamp

## File Structure

```
face_attendance_system/
├── attendance_system.py      # Main application file
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── known_faces/             # Folder for face images
│   ├── student1.jpg
│   ├── student2.jpg
│   └── teacher.jpg
└── attendance_logs/         # Generated attendance CSV files
    ├── attendance_2024-01-15.csv
    └── attendance_2024-01-16.csv
```

## How It Works

1. **Face Loading**: The system loads all images from the `known_faces` folder and creates face encodings using the `face_recognition` library.

2. **Real-time Detection**: When started, the system continuously captures video from the webcam and processes frames to detect faces.

3. **Face Recognition**: Detected faces are compared against the known face encodings to identify matches.

4. **Attendance Logging**: When a known face is recognized, the system logs the attendance with a timestamp to a CSV file.

5. **Duplicate Prevention**: The system tracks which faces have already been logged in the current session to prevent duplicate entries.

6. **Visual Feedback**: The camera feed shows green rectangles around detected faces with names displayed below.

## Troubleshooting

### Common Issues:

1. **"No known faces loaded" error**:
   - Make sure you have added images to the `known_faces` folder
   - Ensure images contain clear, front-facing photos
   - Check that image files are in supported formats (JPG, JPEG, PNG)

2. **"Could not open webcam" error**:
   - Make sure your webcam is connected and working
   - Check if another application is using the webcam
   - Try restarting the application

3. **Poor face recognition accuracy**:
   - Use high-quality, well-lit photos for known faces
   - Ensure faces are clearly visible and front-facing
   - Improve lighting conditions in the camera area
   - Make sure faces are not too small or too large in the frame

4. **Performance issues**:
   - The system processes every other frame to improve performance
   - Close other applications to free up system resources
   - Ensure good lighting for faster processing

### Dependencies Installation Issues:

If you encounter issues installing `face_recognition`:

**On Windows:**
```bash
pip install cmake
pip install dlib
pip install face_recognition
```

**On macOS:**
```bash
brew install cmake
pip install dlib
pip install face_recognition
```

**On Linux:**
```bash
sudo apt-get install cmake
pip install dlib
pip install face_recognition
```

## Customization

### Adding New Features:

1. **Custom attendance formats**: Modify the `log_attendance` method to change CSV format
2. **Additional GUI elements**: Add new buttons or displays to the `setup_gui` method
3. **Different recognition algorithms**: Modify the face comparison logic in `run_video_capture`
4. **Database integration**: Replace CSV logging with database storage

### Configuration Options:

- **Camera index**: Change `cv2.VideoCapture(0)` to use a different camera
- **Frame processing rate**: Modify the `process_this_frame` logic for different performance
- **Face detection sensitivity**: Adjust the face recognition tolerance in `compare_faces`

## Security and Privacy

- Face data is stored locally and not transmitted
- Attendance logs are stored in CSV format on your local machine
- The system does not require internet connection
- Consider data protection regulations when using in institutional settings

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the system.

## Support

For issues or questions, please check the troubleshooting section above or create an issue in the project repository. 

## Compatibility

- **Recommended Python versions:** 3.8–3.11
- Python 3.12+ and 3.13+ may not work with face-recognition due to dlib build issues.
- If you use Python 3.12+ or 3.13+, you may need to install CMake and Visual Studio Build Tools manually.

## Windows Build Tools

If you see errors about dlib or CMake:
- Download and install [CMake](https://cmake.org/download/) (add to PATH)
- Download and install [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- Restart your computer after installation 