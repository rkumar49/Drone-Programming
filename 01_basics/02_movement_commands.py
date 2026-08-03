# 02_movement_commands.py
"""
CONCEPT: Basic movement commands
All movements are in CENTIMETERS (cm)
"""

from pysimverse import Drone
import time

print("=" * 50)
print("DRONE PROGRAMMING - LESSON 2: MOVEMENT COMMANDS")
print("=" * 50)

drone = Drone()
drone.connect()
print("✅ Connected!\n")

# Takeoff
drone.take_off()
print("✅ Took off!")
time.sleep(2)

# Demonstration of all movement commands
print("\n🔄 Moving Forward 200 cm (2 meters)")
drone.move_forward(200)
time.sleep(1)

print("🔄 Moving Backward 100 cm (1 meter)")
drone.move_backward(100)
time.sleep(1)

print("🔄 Moving Right 150 cm (1.5 meters)")
drone.move_right(150)
time.sleep(1)

print("🔄 Moving Left 150 cm (1.5 meters)")
drone.move_left(150)
time.sleep(1)

print("🔄 Moving Up 50 cm (0.5 meters)")
drone.move_up(50)
time.sleep(1)

print("🔄 Moving Down 30 cm (0.3 meters)")
drone.move_down(30)
time.sleep(1)

# Return to start and land
drone.move_left(150)  # Center
drone.move_backward(100)  # Return to original position
print("\n✅ Returning to start position...")
time.sleep(1)

drone.land()
print("\n✅ Mission complete!")

print("\n🎯 LESSON 2 COMPLETE!")
print("Key Learnings:")
print("  - All distances are in centimeters (cm)")
print("  - move_forward(), move_backward() - Front/Back")
print("  - move_right(), move_left() - Left/Right")
print("  - move_up(), move_down() - Vertical movement")