# 06_waypoints.py
"""
CONCEPT: Autonomous navigation with waypoints
Create a flight path with predefined points
"""

from pysimverse import Drone
import time

print("=" * 50)
print("DRONE PROGRAMMING - LESSON 6: WAYPOINT NAVIGATION")
print("=" * 50)

# Define waypoints as (x, y, z) in cm
# x = forward/backward, y = left/right, z = up/down
waypoints = [
    (0, 0, 0),      # Start
    (200, 0, 50),   # Forward 2m, Up 0.5m
    (200, 200, 50), # Right 2m
    (0, 200, 100),  # Back 2m, Up 1m
    (0, 0, 100),    # Left 2m
    (0, 0, 0),      # Return to start
]

drone = Drone()
drone.connect()
drone.take_off()
print(f"✅ Took off!\n")

print("🔄 Navigating waypoints...")
for i, (x, y, z) in enumerate(waypoints):
    print(f"📍 Waypoint {i+1}: Forward={x}cm, Right={y}cm, Up={z}cm")
    
    # Move to waypoint (using relative movements from current position)
    if x > 0:
        drone.move_forward(x)
    elif x < 0:
        drone.move_backward(-x)
    
    if y > 0:
        drone.move_right(y)
    elif y < 0:
        drone.move_left(-y)
    
    if z > 0:
        drone.move_up(z)
    elif z < 0:
        drone.move_down(-z)
    
    time.sleep(1)  # Pause at each waypoint

print("\n✅ Waypoint navigation complete!")
drone.land()

print("\n🎯 LESSON 6 COMPLETE!")
print("Key Learnings:")
print("  - Waypoints define a flight path")
print("  - Sequential navigation")
print("  - Pausing at waypoints for stability")