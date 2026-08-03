# 05_keyboard_control.py
"""
CONCEPT: Manual drone control using keyboard
Use arrow keys and WASD to fly manually
"""

from pysimverse import Drone
import cv2
import time

print("=" * 50)
print("DRONE PROGRAMMING - LESSON 5: KEYBOARD CONTROL")
print("=" * 50)
print("""
CONTROLS:
  W - Move Forward    A - Move Left
  S - Move Backward   D - Move Right
  Q - Move Up         E - Move Down
  SPACE - Takeoff     L - Land
  ESC - Exit
""")
print("=" * 50)

drone = Drone()
drone.connect()
drone.take_off()
print("✅ Took off! Use keyboard controls\n")

# Enable camera stream for visual feedback
drone.streamon()
print("📷 Camera stream enabled")

while True:
    # Get keyboard input
    key = cv2.waitKey(1) & 0xFF
    
    # Movement commands (move 20cm each press)
    if key == ord('w') or key == ord('W'):
        drone.move_forward(20)
        print("⬆ Forward 20cm")
    elif key == ord('s') or key == ord('S'):
        drone.move_backward(20)
        print("⬇ Backward 20cm")
    elif key == ord('a') or key == ord('A'):
        drone.move_left(20)
        print("⬅ Left 20cm")
    elif key == ord('d') or key == ord('D'):
        drone.move_right(20)
        print("➡ Right 20cm")
    elif key == ord('q') or key == ord('Q'):
        drone.move_up(20)
        print("⬆ Up 20cm")
    elif key == ord('e') or key == ord('E'):
        drone.move_down(20)
        print("⬇ Down 20cm")
    elif key == ord(' '):  # Spacebar
        drone.take_off()
        print("🛫 Taking off!")
    elif key == ord('l') or key == ord('L'):
        drone.land()
        print("🛬 Landing!")
        break
    elif key == 27:  # ESC key
        print("❌ Exiting...")
        break
    
    # Get and display camera frame
    frame, success = drone.get_frame()
    if success:
        cv2.imshow("Drone Camera", frame)

cv2.destroyAllWindows()
drone.land()
print("\n✅ Keyboard control session complete!")

print("\n🎯 LESSON 5 COMPLETE!")
print("Key Learnings:")
print("  - Manual control using keyboard")
print("  - Real-time camera feed")
print("  - Fine-tuned movements (20cm steps)")