# 03_combination_moves.py
"""
CONCEPT: Combining movements to create flight patterns
Learn to create square, rectangle, and L-shape patterns
"""

from pysimverse import Drone
import time

print("=" * 50)
print("DRONE PROGRAMMING - LESSON 3: COMBINATION MOVES")
print("=" * 50)

drone = Drone()
drone.connect()
drone.take_off()
print("✅ Took off!\n")

# Pattern 1: Square (4 sides, each 200 cm)
print("🔄 Pattern 1: SQUARE (200cm x 200cm)")
for i in range(4):
    drone.move_forward(100)
    time.sleep(0.5)
    drone.move_right(100)
    time.sleep(0.5)
print("✅ Square complete!\n")
time.sleep(1)

# Pattern 2: Rectangle (300cm x 150cm)
print("🔄 Pattern 2: RECTANGLE (300cm x 150cm)")
drone.move_forward(150)
time.sleep(0.5)
drone.move_right(150)
time.sleep(0.5)
drone.move_backward(150)
time.sleep(0.5)
drone.move_left(150)
print("✅ Rectangle complete!\n")
time.sleep(1)

# Pattern 3: L-Shape
print("🔄 Pattern 3: L-SHAPE")
drone.move_forward(100)
time.sleep(0.5)
drone.move_right(100)
time.sleep(0.5)
print("✅ L-Shape complete!\n")

# Return to center and land
drone.move_left(100)
drone.move_backward(250)
time.sleep(1)

drone.land()
print("\n✅ All patterns complete!")

print("\n🎯 LESSON 3 COMPLETE!")
print("Key Learnings:")
print("  - You can combine movements for complex patterns")
print("  - Use time.sleep() between moves for stability")
print("  - Practice precision with centimeter-level control")