#!/usr/bin/env python3
"""
Script to create sample face images for testing the attendance system.
This script will capture images from the webcam to create known face samples.
"""

import cv2
import os
import time

def create_sample_faces():
    """
    Interactive script to capture face images for the attendance system
    """
    print("=" * 60)
    print("Sample Face Image Creator")
    print("=" * 60)
    print("This script will help you create face images for the attendance system.")
    print("Press 'c' to capture an image, 'q' to quit")
    print("=" * 60)
    
    # Create known_faces directory if it doesn't exist
    if not os.path.exists('known_faces'):
        os.makedirs('known_faces')
        print("Created 'known_faces' directory")
    
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return
    
    print("Webcam initialized successfully")
    print("Position your face in the camera and press 'c' to capture")
    print("Press 'q' to quit")
    
    image_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            break
        
        # Display the frame
        cv2.imshow('Capture Face Images', frame)
        
        # Wait for key press
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('c'):
            # Capture image
            image_count += 1
            name = input(f"\nEnter name for person {image_count} (or press Enter for 'person{image_count}'): ").strip()
            
            if not name:
                name = f"person{image_count}"
            
            # Save the image
            filename = f"known_faces/{name}.jpg"
            cv2.imwrite(filename, frame)
            print(f"✓ Saved image as '{filename}'")
            
            # Ask if user wants to capture more
            more = input("Capture another person? (y/n): ").lower().strip()
            if more != 'y':
                break
                
        elif key == ord('q'):
            break
    
    # Clean up
    cap.release()
    cv2.destroyAllWindows()
    
    print(f"\n✓ Created {image_count} face image(s) in the 'known_faces' folder")
    print("You can now run the attendance system with: python attendance_system.py")

def list_existing_faces():
    """
    List existing face images in the known_faces directory
    """
    known_faces_dir = "known_faces"
    
    if not os.path.exists(known_faces_dir):
        print("No 'known_faces' directory found")
        return
    
    image_files = [f for f in os.listdir(known_faces_dir) 
                   if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not image_files:
        print("No face images found in 'known_faces' directory")
    else:
        print(f"Found {len(image_files)} face image(s):")
        for file in image_files:
            print(f"  - {file}")

def main():
    """
    Main function
    """
    print("Sample Face Image Creator for AI Attendance System")
    print()
    
    # List existing faces
    list_existing_faces()
    print()
    
    # Ask user what they want to do
    choice = input("Do you want to create new face images? (y/n): ").lower().strip()
    
    if choice == 'y':
        create_sample_faces()
    else:
        print("No new images will be created.")
        print("Make sure you have face images in the 'known_faces' folder before running the attendance system.")

if __name__ == "__main__":
    main() 