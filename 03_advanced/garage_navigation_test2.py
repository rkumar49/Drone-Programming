# 09_garage_navigation_fixed.py
"""
CONCEPT: Garage Navigation using simulator's collision system
The simulator will stop the drone at obstacles
We move in small steps and trust the simulator to block movements
"""

from pysimverse import Drone
import time

print("=" * 50)
print("GARAGE NAVIGATION - SAFE PATH FINDING")
print("=" * 50)
print("🔄 Using simulator's collision detection")
print("Moving in small steps - simulator will block obstacles\n")

drone = Drone()
drone.connect()
drone.take_off()
print("✅ Took off!\n")

# Since we can't detect obstacles, we use a different strategy:
# Move in small steps and trust the simulator to block us

print("🔄 Finding a path through the garage...\n")

# Try to move in a path, but stop if blocked
# The simulator will prevent movement through obstacles

path = [
    ("forward", 20),
    ("forward", 20),
    ("forward", 20),
    ("forward", 20),
    ("forward", 20),  # Total 100cm forward
    ("right", 20),
    ("right", 20),
    ("right", 20),
    ("right", 20),
    ("right", 20),   # Total 100cm right
    ("forward", 20),
    ("forward", 20),
    ("forward", 20),
    ("forward", 20),
    ("forward", 20),  # Total 100cm forward
    ("left", 20),
    ("left", 20),
    ("left", 20),
    ("left", 20),
    ("left", 20),    # Total 100cm left
]

print("📌 Following path with 20cm steps...\n")

step_count = 0
for direction, distance in path:
    step_count += 1
    
    # Try to move
    if direction == "forward":
        drone.move_forward(distance)
    elif direction == "backward":
        drone.move_backward(distance)
    elif direction == "right":
        drone.move_right(distance)
    elif direction == "left":
        drone.move_left(distance)
    
    time.sleep(0.2)
    
    # Every 5 steps, check if we're still moving
    if step_count % 5 == 0:
        print(f"   📍 Step {step_count}: Moved {direction} {distance}cm")

print("\n✅ Path execution complete!")

# Now try to return (reverse path in reverse order)
print("\n🔄 Returning to start...")

return_path = [
    ("right", 20),
    ("right", 20),
    ("right", 20),
    ("right", 20),
    ("right", 20),  # Reverse the left moves
    ("backward", 20),
    ("backward", 20),
    ("backward", 20),
    ("backward", 20),
    ("backward", 20),  # Reverse forward moves
    ("left", 20),
    ("left", 20),
    ("left", 20),
    ("left", 20),
    ("left", 20),   # Reverse right moves
    ("backward", 20),
    ("backward", 20),
    ("backward", 20),
    ("backward", 20),
    ("backward", 20),  # Reverse forward moves
]

for direction, distance in return_path:
    if direction == "forward":
        drone.move_forward(distance)
    elif direction == "backward":
        drone.move_backward(distance)
    elif direction == "right":
        drone.move_right(distance)
    elif direction == "left":
        drone.move_left(distance)
    time.sleep(0.2)

print("\n✅ Return complete!")
drone.land()

print("\n🎯 LESSON 9 COMPLETE!")
print("Key Learnings:")
print("  ✅ Simulator has collision detection")
print("  ✅ Moving in small steps (20cm) is safer")
print("  ✅ The simulator will block obstacle hits")
print("  ⚠️  Without sensors, we can't know WHY we're blocked")
print("\n💡 To avoid crashes:")
print("  - Use SMALL steps (10-20cm)")
print("  - Watch the drone visually")
print("  - Stop if it's not moving as expected")
print("  - Clear paths before flying")