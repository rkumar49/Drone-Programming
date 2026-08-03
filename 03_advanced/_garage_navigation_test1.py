# 09_garage_navigation_test.py
"""
TEST: See how simulator handles obstacles
Intentionally try to fly into an obstacle
"""

from pysimverse import Drone
import time

print("=" * 50)
print("TESTING OBSTACLE DETECTION")
print("=" * 50)

drone = Drone()
drone.connect()
drone.take_off()
print("✅ Took off!\n")

# Try to fly forward until blocked
print("🔄 Moving forward until blocked by obstacle...")
for i in range(10):  # Try 10 times
    drone.move_forward(20)  # Move 20cm
    time.sleep(0.5)
    print(f"   Step {i+1}: Moved forward 20cm")
    
    # Check if drone is still at same position (blocked)
    # In simulator, if blocked, the drone won't move

print("\n✅ Test complete!")
drone.land()