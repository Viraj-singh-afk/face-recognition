#!/usr/bin/env python3
"""
Test script to verify that all dependencies are properly installed
and the face attendance system can run correctly.
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing module imports...")
    
    try:
        import cv2
        print("✓ OpenCV imported successfully")
    except ImportError as e:
        print(f"✗ OpenCV import failed: {e}")
        return False
    
    try:
        import face_recognition
        print("✓ face_recognition imported successfully")
    except ImportError as e:
        print(f"✗ face_recognition import failed: {e}")
        return False
    
    try:
        import numpy as np
        print("✓ NumPy imported successfully")
    except ImportError as e:
        print(f"✗ NumPy import failed: {e}")
        return False
    
    try:
        from PIL import Image
        print("✓ Pillow imported successfully")
    except ImportError as e:
        print(f"✗ Pillow import failed: {e}")
        return False
    
    try:
        import tkinter
        print("✓ Tkinter imported successfully")
    except ImportError as e:
        print(f"✗ Tkinter import failed: {e}")
        return False
    
    return True

def test_webcam():
    """Test if webcam can be accessed"""
    print("\nTesting webcam access...")
    
    try:
        import cv2
        cap = cv2.VideoCapture(0)
        
        if cap.isOpened():
            print("✓ Webcam accessed successfully")
            ret, frame = cap.read()
            if ret:
                print("✓ Webcam can capture frames")
            else:
                print("✗ Webcam cannot capture frames")
                cap.release()
                return False
            cap.release()
        else:
            print("✗ Could not access webcam")
            return False
            
    except Exception as e:
        print(f"✗ Webcam test failed: {e}")
        return False
    
    return True

def test_face_recognition():
    """Test if face recognition library works"""
    print("\nTesting face recognition...")
    
    try:
        import face_recognition
        import numpy as np
        
        # Create a simple test image (random array)
        test_image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        
        # Try to find faces (should return empty list for random image)
        face_locations = face_recognition.face_locations(test_image)
        face_encodings = face_recognition.face_encodings(test_image)
        
        print("✓ face_recognition library working correctly")
        return True
        
    except Exception as e:
        print(f"✗ face_recognition test failed: {e}")
        return False

def test_directories():
    """Test if required directories exist or can be created"""
    print("\nTesting directory creation...")
    
    directories = ['known_faces', 'attendance_logs']
    
    for directory in directories:
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
                print(f"✓ Created directory: {directory}")
            except Exception as e:
                print(f"✗ Failed to create directory {directory}: {e}")
                return False
        else:
            print(f"✓ Directory exists: {directory}")
    
    return True

def test_known_faces():
    """Test if known_faces directory has images"""
    print("\nTesting known faces...")
    
    known_faces_dir = "known_faces"
    
    if not os.path.exists(known_faces_dir):
        print("✗ known_faces directory does not exist")
        return False
    
    image_files = [f for f in os.listdir(known_faces_dir) 
                   if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not image_files:
        print("⚠ No face images found in known_faces directory")
        print("  Please add some face images to test recognition")
        return True  # This is not a critical error
    else:
        print(f"✓ Found {len(image_files)} face image(s)")
        return True

def main():
    """Run all tests"""
    print("=" * 50)
    print("AI Face Detection Attendance System - Installation Test")
    print("=" * 50)
    
    all_tests_passed = True
    
    # Test imports
    if not test_imports():
        all_tests_passed = False
    
    # Test webcam
    if not test_webcam():
        all_tests_passed = False
    
    # Test face recognition
    if not test_face_recognition():
        all_tests_passed = False
    
    # Test directories
    if not test_directories():
        all_tests_passed = False
    
    # Test known faces
    if not test_known_faces():
        all_tests_passed = False
    
    print("\n" + "=" * 50)
    if all_tests_passed:
        print("✓ All tests passed! The system should work correctly.")
        print("\nNext steps:")
        print("1. Add face images to the 'known_faces' folder")
        print("2. Run: python attendance_system.py")
    else:
        print("✗ Some tests failed. Please check the errors above.")
        print("\nCommon solutions:")
        print("1. Install missing dependencies: pip install -r requirements.txt")
        print("2. Make sure your webcam is connected and working")
        print("3. Check if another application is using the webcam")
    print("=" * 50)

if __name__ == "__main__":
    main() 