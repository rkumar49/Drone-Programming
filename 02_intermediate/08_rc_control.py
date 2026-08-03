# 08_rc_control.py
"""
CONCEPT: RC (Radio Control) style control
Using send_rc_control() for smooth continuous movement
"""

from pysimverse import Drone
import time

print("=" * 50)
print("DRONE PROGRAMMING - LESSON 8: RC CONTROL")
print("=" * 50)

drone = Drone()
drone.connect()
drone.take_off()
print("✅ Took off!\n")

print("🔄 Testing RC controls...")
print("Values: -100 to 100 (negative = reverse/left/down)")

# RC Control format: send_rc_control(left_right, forward_backward, up_down, yaw)
# Values range: -100 to 100

# Test 1: Forward
print("\n📡 Forward at 50% power")
drone.send_rc_control(0, 50, 0, 0)
time.sleep(2)

# Test 2: Right
print("📡 Right at 50% power")
drone.send_rc_control(50, 0, 0, 0)
time.sleep(2)

# Test 3: Up
print("📡 Up at 50% power")
drone.send_rc_control(0, 0, 50, 0)
time.sleep(2)

# Test 4: Yaw (rotation)
print("📡 Yaw right at 50%")
drone.send_rc_control(0, 0, 0, 50)
time.sleep(2)

# Stop all movement
print("\n⏹ Stopping all movement")
drone.send_rc_control(0, 0, 0, 0)
time.sleep(1)

# Return and land
print("🔄 Returning to start...")
drone.move_backward(100)
drone.move_left(100)
drone.move_down(50)

drone.land()
print("\n✅ RC control test complete!")

print("\n🎯 LESSON 8 COMPLETE!")
print("Key Learnings:")
print("  - send_rc_control() for smooth continuous control")
print("  - Values: -100 to 100")
print("  - Useful for fine-tuned manual control")
print("  - Send 0,0,0,0 to stop all movement")