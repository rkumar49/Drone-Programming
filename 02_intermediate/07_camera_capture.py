# 07_camera_capture.py
"""
CONCEPT: Capturing images with drone camera
Learn to use OpenCV for image processing
"""

from pysimverse import Drone
import cv2
import time
import os

print("=" * 50)
print("DRONE PROGRAMMING - LESSON 7: CAMERA CAPTURE")
print("=" * 50)

# Create folder for captures
os.makedirs("captures", exist_ok=True)

drone = Drone()
drone.connect()

# Enable camera stream
drone.streamon()
print("📷 Camera stream enabled")

drone.take_off()
print("✅ Took off!\n")

# Take photos at different positions
# Use separate commands for each direction
print("📸 Capturing images at different positions...\n")

# Position 1: Front
print("📸 Position 1: Front")
drone.move_forward(80)
time.sleep(0.5)
frame, success = drone.get_frame()
if success:
    cv2.imwrite("captures/photo_Front_1.jpg", frame)
    print("   ✅ Saved: captures/photo_Front_1.jpg")
drone.move_backward(80)
time.sleep(0.5)
print("   ↩️ Returned to center\n")

# Position 2: Right
print("📸 Position 2: Right")
drone.move_right(80)
time.sleep(0.5)
frame, success = drone.get_frame()
if success:
    cv2.imwrite("captures/photo_Right_2.jpg", frame)
    print("   ✅ Saved: captures/photo_Right_2.jpg")
drone.move_left(80)
time.sleep(0.5)
print("   ↩️ Returned to center\n")

# Position 3: Left
print("📸 Position 3: Left")
drone.move_left(80)
time.sleep(0.5)
frame, success = drone.get_frame()
if success:
    cv2.imwrite("captures/photo_Left_3.jpg", frame)
    print("   ✅ Saved: captures/photo_Left_3.jpg")
drone.move_right(80)
time.sleep(0.5)
print("   ↩️ Returned to center\n")

# Position 4: Above
print("📸 Position 4: Above")
drone.move_up(80)
time.sleep(0.5)
frame, success = drone.get_frame()
if success:
    cv2.imwrite("captures/photo_Above_4.jpg", frame)
    print("   ✅ Saved: captures/photo_Above_4.jpg")
drone.move_down(80)
time.sleep(0.5)
print("   ↩️ Returned to center\n")

# Land safely
print("\n✅ All photos captured!")
drone.land()

print("\n🎯 LESSON 7 COMPLETE!")
print("Key Learnings:")
print("  - Enabling camera stream")
print("  - Capturing images from drone")
print("  - Saving images to disk")
print(f"  - Photos saved in 'captures' folder")