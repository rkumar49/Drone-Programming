# 10_hand_gesture_working.py
"""
CONCEPT: Hand Gesture Control Using OpenCV + MediaPipe Alternative
Works without the model file
"""

from pysimverse import Drone
import cv2
import time
import numpy as np

print("=" * 50)
print("DRONE PROGRAMMING - LESSON 10: HAND GESTURE CONTROL")
print("=" * 50)
print("""
✋ Control the drone with your hand:
  - Move hand UP: Drone goes up
  - Move hand DOWN: Drone goes down  
  - Move hand LEFT: Drone goes left
  - Move hand RIGHT: Drone goes right
  - Press 'q' to quit
""")

drone = Drone()
drone.connect()
drone.streamon()
drone.take_off()
print("✅ Took off!\n")

# Simple hand detection using skin color
def detect_hand(frame):
    """Detect hand using skin color detection"""
    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Skin color range (adjust if needed)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    
    # Create mask for skin
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Get largest contour (hand)
        largest = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest)
        
        if area > 1000:  # Minimum hand size
            M = cv2.moments(largest)
            if M["m00"] > 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                return (cx, cy), largest, mask
    
    return None, None, mask

CAM_WIDTH = 640
CAM_HEIGHT = 480
center_x = CAM_WIDTH // 2
center_y = CAM_HEIGHT // 2
threshold = 40
last_command_time = time.time()
command_cooldown = 0.3

print("🎮 Show your hand to the camera...\n")
print("📌 TIP: Good lighting is important!")

while True:
    frame, success = drone.get_frame()
    if not success:
        continue
    
    frame = cv2.resize(frame, (CAM_WIDTH, CAM_HEIGHT))
    frame_copy = frame.copy()
    
    # Detect hand
    hand_pos, contour, mask = detect_hand(frame_copy)
    
    if hand_pos:
        x, y = hand_pos
        dx = x - center_x
        dy = y - center_y
        
        # Draw hand outline
        if contour is not None:
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
        cv2.circle(frame, (x, y), 10, (0, 0, 255), -1)
        
        # Draw crosshair
        cv2.circle(frame, (center_x, center_y), 5, (255, 0, 0), -1)
        cv2.line(frame, (center_x, center_y), (x, y), (0, 255, 255), 2)
        
        # Move drone
        current_time = time.time()
        if current_time - last_command_time > command_cooldown:
            moved = False
            
            if abs(dx) > threshold:
                if dx > 0:
                    drone.move_right(10)
                    print("➡ Right")
                else:
                    drone.move_left(10)
                    print("⬅ Left")
                moved = True
                last_command_time = current_time
            
            if abs(dy) > threshold:
                if dy > 0:
                    drone.move_down(10)
                    print("⬇ Down")
                else:
                    drone.move_up(10)
                    print("⬆ Up")
                moved = True
                last_command_time = current_time
    
    # Show status
    status = "✅ Hand detected" if hand_pos else "❌ Show your hand"
    cv2.putText(frame, status, (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0) if hand_pos else (0, 0, 255), 2)
    cv2.putText(frame, "Press 'q' to quit", (10, 60), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    cv2.imshow("Hand Control", frame)
    cv2.imshow("Hand Mask", mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
drone.land()
print("\n✅ Hand gesture control complete!")