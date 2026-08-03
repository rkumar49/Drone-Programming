# first_flight.py
from pysimverse import Drone
import time

# Initialize drone
drone = Drone()
drone.connect()

# Take off
drone.take_off()
time.sleep(2)

# Move around (distances in CENTIMETERS)
drone.set_speed(80)        # 80 cm/s
drone.move_forward(275)    # Move 275 cm forward
drone.move_right(265)      # Move 265 cm right
drone.move_up(50)          # Move up 50 cm

# Land
drone.land()