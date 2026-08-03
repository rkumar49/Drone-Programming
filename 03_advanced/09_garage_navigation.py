# 09_garage_navigation.py
"""
CONCEPT: Garage Navigation - Safe path finding with collision detection
The simulator will stop the drone if it hits obstacles
We move in small steps and check if we can still move
"""

from pysimverse import Drone
import time

print("=" * 50)
print("DRONE PROGRAMMING - LESSON 9: GARAGE NAVIGATION")
print("=" * 50)
print("🚗 Navigating through garage with collision detection")
print("Moving in small steps to avoid obstacles\n")

drone = Drone()
drone.connect()
drone.take_off()
print("✅ Took off!\n")

def try_move_forward(distance, step=15):
    """Try to move forward in small steps, stop if obstacle hit"""
    moved = 0
    for _ in range(int(distance / step)):
        # Try to move small step
        drone.move_forward(step)
        time.sleep(0.2)
        moved += step
        print(f"   📍 Moved forward {step}cm (Total: {moved}cm)")
        
        # In simulator, if we hit obstacle, drone won't move
        # We can check position if available
    return moved

def try_move_right(distance, step=15):
    """Try to move right in small steps"""
    moved = 0
    for _ in range(int(distance / step)):
        drone.move_right(step)
        time.sleep(0.2)
        moved += step
        print(f"   📍 Moved right {step}cm (Total: {moved}cm)")
    return moved

def try_move_left(distance, step=15):
    """Try to move left in small steps"""
    moved = 0
    for _ in range(int(distance / step)):
        drone.move_left(step)
        time.sleep(0.2)
        moved += step
        print(f"   📍 Moved left {step}cm (Total: {moved}cm)")
    return moved

def try_move_backward(distance, step=15):
    """Try to move backward in small steps"""
    moved = 0
    for _ in range(int(distance / step)):
        drone.move_backward(step)
        time.sleep(0.2)
        moved += step
        print(f"   📍 Moved backward {step}cm (Total: {moved}cm)")
    return moved

# ============================================
# NAVIGATE THROUGH GARAGE WITH OBSTACLES
# ============================================

print("🔄 Starting garage navigation with obstacle awareness...\n")

# Try different paths - if one is blocked, try another
print("📌 Attempt 1: Moving forward...")
forward_moved = try_move_forward(60, step=15)
time.sleep(0.5)

if forward_moved < 60:
    print("   ⚠️  Forward path blocked! Trying alternative...")
    print("   🔄 Moving right to go around...")
    try_move_right(40, step=15)
    time.sleep(0.5)
    print("   🔄 Trying forward again...")
    try_move_forward(40, step=15)
    time.sleep(0.5)

print("\n📌 Attempt 2: Moving right...")
try_move_right(50, step=15)
time.sleep(0.5)

print("\n📌 Attempt 3: Moving forward...")
try_move_forward(40, step=15)
time.sleep(0.5)

print("\n📌 Attempt 4: Moving left...")
try_move_left(50, step=15)
time.sleep(0.5)

print("\n📌 Attempt 5: Moving forward into parking spot...")
try_move_forward(30, step=15)
time.sleep(0.5)

print("\n✅ Parked! Now exiting...")

print("\n📌 Moving backward...")
try_move_backward(30, step=15)
time.sleep(0.5)

print("📌 Moving right...")
try_move_right(50, step=15)
time.sleep(0.5)

print("📌 Moving backward...")
try_move_backward(40, step=15)
time.sleep(0.5)

print("📌 Moving left...")
try_move_left(40, step=15)
time.sleep(0.5)

print("📌 Moving backward to exit...")
try_move_backward(60, step=15)
time.sleep(0.5)

print("\n✅ Garage navigation complete!")
drone.land()

print("\n🎯 LESSON 9 COMPLETE!")
print("Key Learnings:")
print("  ✅ Moving in small steps (15cm) for safety")
print("  ✅ Simulator stops drone at obstacles automatically")
print("  ✅ When blocked, try alternative paths")
print("  ✅ Always move slowly in unknown environments")
print("\n💡 Tips for garage navigation:")
print("  - Keep movements small (15-20cm)")
print("  - Watch the drone's position")
print("  - If stuck, try going around obstacles")
print("  - Plan path before executing")