import cv2
import face_recognition
import numpy as np
import csv
import os
import datetime
import threading
import time
from PIL import Image
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QStatusBar, QMessageBox)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPixmap

class FaceAttendanceSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.known_face_encodings = []
        self.known_face_names = []
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True
        self.attendance_logged = set()
        self.is_running = False
        self.video_capture = None
        self.video_thread = None
        self.timer = QTimer()
        self.create_directories()
        self.load_known_faces()
        self.init_ui()

    def create_directories(self):
        directories = ['known_faces', 'attendance_logs']
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)

    def load_known_faces(self):
        known_faces_dir = "known_faces"
        if not os.path.exists(known_faces_dir):
            return
        image_files = [f for f in os.listdir(known_faces_dir)
                      if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        for image_file in image_files:
            name = os.path.splitext(image_file)[0]
            image_path = os.path.join(known_faces_dir, image_file)
            image = face_recognition.load_image_file(image_path)
            face_encodings = face_recognition.face_encodings(image)
            if face_encodings:
                self.known_face_encodings.append(face_encodings[0])
                self.known_face_names.append(name)

    def init_ui(self):
        self.setWindowTitle("AI Face Detection Attendance System")
        self.setGeometry(100, 100, 900, 700)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        # Title
        title = QLabel("AI Face Detection Attendance System")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 22px; font-weight: bold; margin: 10px;")
        main_layout.addWidget(title)
        # Webcam preview
        self.video_label = QLabel()
        self.video_label.setFixedSize(640, 480)
        self.video_label.setStyleSheet("background: #222; border: 1px solid #888;")
        main_layout.addWidget(self.video_label, alignment=Qt.AlignCenter)
        # Status
        self.status = QLabel("Status: Ready")
        self.status.setStyleSheet("color: #666; font-size: 14px; margin: 8px;")
        main_layout.addWidget(self.status)
        # Buttons
        button_layout = QHBoxLayout()
        self.start_btn = QPushButton("Start Attendance")
        self.start_btn.clicked.connect(self.start_attendance)
        self.stop_btn = QPushButton("Stop Attendance")
        self.stop_btn.clicked.connect(self.stop_attendance)
        self.stop_btn.setEnabled(False)
        self.clear_btn = QPushButton("Clear Session")
        self.clear_btn.clicked.connect(self.clear_session)
        button_layout.addWidget(self.start_btn)
        button_layout.addWidget(self.stop_btn)
        button_layout.addWidget(self.clear_btn)
        main_layout.addLayout(button_layout)
        # Attendance log
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setStyleSheet("background: #fff; font-family: Courier; font-size: 12px;")
        main_layout.addWidget(QLabel("Recent Attendance:"))
        main_layout.addWidget(self.log_text)
        # Instructions
        instructions = QLabel("Instructions:\n1. Add face images to 'known_faces' folder\n2. Click 'Start Attendance' to begin\n3. Attendance will be logged to CSV file")
        instructions.setStyleSheet("color: #888; font-size: 12px; margin: 8px;")
        main_layout.addWidget(instructions)
        central_widget.setLayout(main_layout)
        # Status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Ready")
        # Close event
        self.destroyed.connect(self.on_closing)

    def start_attendance(self):
        if not self.known_face_names:
            QMessageBox.critical(self, "Error", "No known faces loaded. Please add face images to the 'known_faces' folder.")
            return
        self.is_running = True
        self.attendance_logged.clear()
        self.status.setText("Status: Running")
        self.statusBar.showMessage("Attendance running")
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.video_capture = cv2.VideoCapture(0)
        self.timer.timeout.connect(self.run_video_capture)
        self.timer.start(30)

    def stop_attendance(self):
        self.is_running = False
        self.status.setText("Status: Stopped")
        self.statusBar.showMessage("Attendance stopped")
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        if self.video_capture:
            self.video_capture.release()
            self.video_capture = None
        self.video_label.clear()
        self.timer.stop()

    def clear_session(self):
        self.attendance_logged.clear()
        self.log_text.clear()
        self.statusBar.showMessage("Session cleared")

    def run_video_capture(self):
        if not self.is_running or not self.video_capture:
            return
        ret, frame = self.video_capture.read()
        if not ret:
            return
        rgb_frame = frame[:, :, ::-1]
        if self.process_this_frame:
            self.face_locations = face_recognition.face_locations(rgb_frame)
            self.face_encodings = face_recognition.face_encodings(rgb_frame, self.face_locations)
            self.face_names = []
            for face_encoding in self.face_encodings:
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                name = "Unknown"
                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                if len(face_distances) > 0:
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]
                self.face_names.append(name)
                if name != "Unknown" and name not in self.attendance_logged:
                    self.log_attendance(name)
        self.process_this_frame = not self.process_this_frame
        # Draw rectangles and names
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.8, (255, 255, 255), 1)
        # Convert to QImage and display
        rgb_display = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_display.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_display.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.video_label.setPixmap(QPixmap.fromImage(qt_image))

    def log_attendance(self, name):
        now = datetime.datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")
        log_file = os.path.join("attendance_logs", f"attendance_{date_str}.csv")
        new_entry = f"{name},{date_str},{time_str}\n"
        if name not in self.attendance_logged:
            with open(log_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([name, date_str, time_str])
            self.attendance_logged.add(name)
            self.log_text.append(f"{name} - {date_str} {time_str}")
            self.statusBar.showMessage(f"Attendance logged: {name}")

    def on_closing(self):
        self.is_running = False
        if self.video_capture:
            self.video_capture.release()
        self.timer.stop()

    def run(self):
        self.show()


def main():
    import sys
    app = QApplication(sys.argv)
    window = FaceAttendanceSystem()
    window.run()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 