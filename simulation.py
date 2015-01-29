# main driver for the simulation

import car
import numpy as np
import random

def pick_whether_theres_a_car_coming():
    rand_number = random.random()
    




time_now = 9

carA = car.car('A')
carB = car.car('B')


seconds_to_simulate = 60
## loop through the time (in seconds), and update the priority queue at each time, 
time_to_stop_simulation = time_now + seconds_to_simulate
while time_now < time_to_stop_simulation:
    
