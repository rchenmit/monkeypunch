# main driver for the simulation

import car
import numpy as np
import random
import heapq

def pick_whether_theres_a_car_coming():
    rand_number = random.random()
    if rand_number < 0.1:
        return True
    else:
        return False
    
def pick_which_car(list_of_cars):
    random_index = random.randint(0, len(list_of_cars))
    return list_of_cars[random_index]
    

time_now = 9


# initialize the cars in the simulation, store in a list
l_cars_in_simulation = [car.car(str(x)) for x in range(10)] ## all the cars in the simulation

#priority queue for the road
road_A = [] #it's an empty list for now, we'll modify this by using the heapq methods

seconds_to_simulate = 60
## loop through the time (in seconds), and update the priority queue at each time, 
time_to_stop_simulation = time_now + seconds_to_simulate
while time_now < time_to_stop_simulation:
    # for each item in the priority queue (road_X), decrease the key (representing the seconds) by one
    
    #decide whether a car is coming or not
    bool_whether_car_coming = pick_whether_theres_a_car_coming()
    # if there happens to be a car coming, pick which lucky car gets to come through
    if bool_whether_car_coming:
        car_that_comes = pick_which_car(l_cars_in_simulation)
        l_cars_in_simulation.remove(car_that_comes)
    heapq.heappush(road_A, (car_that_comes.time_to_intersection, car_that_comes))
    
    