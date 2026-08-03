# 04_speed_control.py
"""
CONCEPT: Speed control with set_speed()
Default speed is around 80 cm/s
"""

from pysimverse import Drone
import time

print("=" * 50)
print("DRONE PROGRAMMING - LESSON 4: SPEED CONTROL")
print("=" * 50)

drone = Drone()
drone.connect()
drone.take_off()
print("✅ Took off!\n")

# Test different speeds
speeds = [40, 80, 120, 160]  # cm/s

for speed in speeds:
    print(f"🔄 Testing speed: {speed} cm/s")
    drone.set_speed(speed)
    
    # Move forward 200cm at this speed
    print(f"   Flying forward 200cm at {speed} cm/s...")
    drone.move_forward(200)
    time.sleep(0.5)
    
    # Move back to start
    drone.move_backward(200)
    time.sleep(0.5)

print("\n✅ All speeds tested!")

# Return to default speed
drone.set_speed(80)
print("⚡ Speed reset to default (80 cm/s)")

time.sleep(1)
drone.land()
print("\n✅ Mission complete!")

print("\n🎯 LESSON 4 COMPLETE!")
print("Key Learnings:")
print("  - set_speed() controls drone speed (cm/s)")
print("  - Default speed: ~80 cm/s")
print("  - Slower speeds = more precision")
print("  - Faster speeds = quicker movements")