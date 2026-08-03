# 01_connect_and_takeoff.py
"""
CONCEPT: Connecting to drone, arming, takeoff, and landing
This is the "Hello World" of drone programming
"""

from pysimverse import Drone
import time

print("=" * 50)
print("DRONE PROGRAMMING - LESSON 1: CONNECT & TAKEOFF")
print("=" * 50)

# Step 1: Create drone object
drone = Drone()
print("✅ Drone object created")

# Step 2: Connect to simulator
print("🔄 Connecting to drone simulator...")
drone.connect()
print("✅ Connected successfully!")

# Step 3: Takeoff
print("🔄 Taking off...")
drone.take_off()
print("✅ Drone is airborne!")

# Step 4: Hover for 3 seconds
print("⏳ Hovering for 3 seconds...")
time.sleep(3)

# Step 5: Land
print("🔄 Landing...")
drone.land()
print("✅ Drone has landed safely!")

print("\n🎯 LESSON 1 COMPLETE!")
print("Key Learnings:")
print("  - Drone() creates a drone object")
print("  - connect() establishes connection")
print("  - take_off() makes drone fly")
print("  - land() brings drone back down")