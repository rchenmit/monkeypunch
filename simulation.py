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
    random_index = random.randint(0, len(list_of_cars)-1)
    return list_of_cars[random_index]
    

time_now = 0


# initialize the cars in the simulation, store in a list
l_cars_before_entering_road = [car.car(str(x)) for x in range(10)] ## all the cars in the simulation
l_cars_after_leaving_road = []

#priority queue for the road
road_A = [] #it's an empty list for now, we'll modify this by using the heapq methods

seconds_to_simulate = 60
## loop through the time (in seconds), and update the priority queue at each time, 
time_to_stop_simulation = time_now + seconds_to_simulate
while time_now < time_to_stop_simulation:
    # for each item in the priority queue (road_X), decrease the key (representing the seconds) by one
    for queue_tuple in road_A:
        queue_tuple[1].total_travel_time += 1
        if queue_tuple[1].time_to_intersection == 0:
            road_A.remove(queue_tuple)
            l_cars_after_leaving_road.append(queue_tuple[1])
        else:
            queue_tuple[1].time_to_intersection -= 1

    #decide whether a car is coming or not
    if len(l_cars_before_entering_road) == 0:
        continue
    else:
        bool_whether_car_coming = pick_whether_theres_a_car_coming()
        # if there happens to be a car coming, pick which lucky car gets to come through
        if bool_whether_car_coming:
            car_that_comes = pick_which_car(l_cars_before_entering_road)
            l_cars_before_entering_road.remove(car_that_comes)
            heapq.heappush(road_A, (car_that_comes.time_to_intersection, car_that_comes))
    
    # update the time
    time_now += 1
    
    # print the contents of the road right now:
    print "time right now: " + str(time_now) + "--------------------------------------------"
    if len(road_A) > 0:
        for queue_tuple in road_A:
            print "Car on road A: name = " + queue_tuple[1].name + "; Time Left Til Intersection: " +  str(queue_tuple[1].time_to_intersection) + " seconds"
    print "cars already passed: " 
    print [car.name + "," for car in l_cars_after_leaving_road]

seconds_taken_per_car = []
for car in l_cars_after_leaving_road:
    seconds_taken_per_car.append(car.total_travel_time)
avg_seconds_taken_per_car = np.mean(seconds_taken_per_car)

#now, the simulation has ended; print a summary
print "--------------------------------------------------------------------------------------------------------"
print "The simulation has ended"
print "SUMMARY OF SIMULATION: ---------------------------------------------------------"
print "Time simulated (s): " + str(seconds_to_simulate)
print "Average time car took to pass through the road (s): " + str(avg_seconds_taken_per_car)

#### sample output from running this simulation:
#time right now: 1--------------------------------------------
#cars already passed: 
#[]
#time right now: 2--------------------------------------------
#Car on road A: name = 2; Time Left Til Intersection: 7 seconds
#cars already passed: 
#[]
#time right now: 3--------------------------------------------
#Car on road A: name = 2; Time Left Til Intersection: 6 seconds
#cars already passed: 
#[]
#time right now: 4--------------------------------------------
#Car on road A: name = 2; Time Left Til Intersection: 5 seconds
#cars already passed: 
#[]
#time right now: 5--------------------------------------------
#Car on road A: name = 2; Time Left Til Intersection: 4 seconds
#cars already passed: 
#[]
#time right now: 6--------------------------------------------
#Car on road A: name = 2; Time Left Til Intersection: 3 seconds
#cars already passed: 
#[]
#time right now: 7--------------------------------------------
#Car on road A: name = 2; Time Left Til Intersection: 2 seconds
#cars already passed: 
#[]
#time right now: 8--------------------------------------------
#Car on road A: name = 2; Time Left Til Intersection: 1 seconds
#cars already passed: 
#[]
#time right now: 9--------------------------------------------
#Car on road A: name = 2; Time Left Til Intersection: 0 seconds
#cars already passed: 
#[]
#time right now: 10--------------------------------------------
#cars already passed: 
#['2,']
#time right now: 11--------------------------------------------
#cars already passed: 
#['2,']
#time right now: 12--------------------------------------------
#cars already passed: 
#['2,']
#time right now: 13--------------------------------------------
#Car on road A: name = 5; Time Left Til Intersection: 6 seconds
#cars already passed: 
#['2,']
#time right now: 14--------------------------------------------
#Car on road A: name = 5; Time Left Til Intersection: 5 seconds
#cars already passed: 
#['2,']
#time right now: 15--------------------------------------------
#Car on road A: name = 5; Time Left Til Intersection: 4 seconds
#cars already passed: 
#['2,']
#time right now: 16--------------------------------------------
#Car on road A: name = 5; Time Left Til Intersection: 3 seconds
#cars already passed: 
#['2,']
#time right now: 17--------------------------------------------
#Car on road A: name = 5; Time Left Til Intersection: 2 seconds
#cars already passed: 
#['2,']
#time right now: 18--------------------------------------------
#Car on road A: name = 5; Time Left Til Intersection: 1 seconds
#cars already passed: 
#['2,']
#time right now: 19--------------------------------------------
#Car on road A: name = 5; Time Left Til Intersection: 0 seconds
#cars already passed: 
#['2,']
#time right now: 20--------------------------------------------
#cars already passed: 
#['2,', '5,']
#time right now: 21--------------------------------------------
#cars already passed: 
#['2,', '5,']
#time right now: 22--------------------------------------------
#cars already passed: 
#['2,', '5,']
#time right now: 23--------------------------------------------
#cars already passed: 
#['2,', '5,']
#time right now: 24--------------------------------------------
#cars already passed: 
#['2,', '5,']
#time right now: 25--------------------------------------------
#cars already passed: 
#['2,', '5,']
#time right now: 26--------------------------------------------
#cars already passed: 
#['2,', '5,']
#time right now: 27--------------------------------------------
#cars already passed: 
#['2,', '5,']
#time right now: 28--------------------------------------------
#cars already passed: 
#['2,', '5,']
#time right now: 29--------------------------------------------
#cars already passed: 
#['2,', '5,']
#time right now: 30--------------------------------------------
#Car on road A: name = 0; Time Left Til Intersection: 6 seconds
#cars already passed: 
#['2,', '5,']
#time right now: 31--------------------------------------------
#Car on road A: name = 0; Time Left Til Intersection: 5 seconds
#cars already passed: 
#['2,', '5,']
#time right now: 32--------------------------------------------
#Car on road A: name = 0; Time Left Til Intersection: 4 seconds
#cars already passed: 
#['2,', '5,']
#time right now: 33--------------------------------------------
#Car on road A: name = 0; Time Left Til Intersection: 3 seconds
#cars already passed: 
#['2,', '5,']
#time right now: 34--------------------------------------------
#Car on road A: name = 0; Time Left Til Intersection: 2 seconds
#cars already passed: 
#['2,', '5,']
#time right now: 35--------------------------------------------
#Car on road A: name = 0; Time Left Til Intersection: 1 seconds
#cars already passed: 
#['2,', '5,']
#time right now: 36--------------------------------------------
#Car on road A: name = 0; Time Left Til Intersection: 0 seconds
#Car on road A: name = 8; Time Left Til Intersection: 10 seconds
#cars already passed: 
#['2,', '5,']
#time right now: 37--------------------------------------------
#Car on road A: name = 8; Time Left Til Intersection: 10 seconds
#cars already passed: 
#['2,', '5,', '0,']
#time right now: 38--------------------------------------------
#Car on road A: name = 8; Time Left Til Intersection: 9 seconds
#cars already passed: 
#['2,', '5,', '0,']
#time right now: 39--------------------------------------------
#Car on road A: name = 8; Time Left Til Intersection: 8 seconds
#cars already passed: 
#['2,', '5,', '0,']
#time right now: 40--------------------------------------------
#Car on road A: name = 8; Time Left Til Intersection: 7 seconds
#cars already passed: 
#['2,', '5,', '0,']
#time right now: 41--------------------------------------------
#Car on road A: name = 8; Time Left Til Intersection: 6 seconds
#cars already passed: 
#['2,', '5,', '0,']
#time right now: 42--------------------------------------------
#Car on road A: name = 8; Time Left Til Intersection: 5 seconds
#cars already passed: 
#['2,', '5,', '0,']
#time right now: 43--------------------------------------------
#Car on road A: name = 8; Time Left Til Intersection: 4 seconds
#cars already passed: 
#['2,', '5,', '0,']
#time right now: 44--------------------------------------------
#Car on road A: name = 8; Time Left Til Intersection: 3 seconds
#cars already passed: 
#['2,', '5,', '0,']
#time right now: 45--------------------------------------------
#Car on road A: name = 8; Time Left Til Intersection: 2 seconds
#cars already passed: 
#['2,', '5,', '0,']
#time right now: 46--------------------------------------------
#Car on road A: name = 8; Time Left Til Intersection: 1 seconds
#cars already passed: 
#['2,', '5,', '0,']
#time right now: 47--------------------------------------------
#Car on road A: name = 7; Time Left Til Intersection: 5 seconds
#Car on road A: name = 8; Time Left Til Intersection: 0 seconds
#cars already passed: 
#['2,', '5,', '0,']
#time right now: 48--------------------------------------------
#Car on road A: name = 7; Time Left Til Intersection: 4 seconds
#cars already passed: 
#['2,', '5,', '0,', '8,']
#time right now: 49--------------------------------------------
#Car on road A: name = 7; Time Left Til Intersection: 3 seconds
#cars already passed: 
#['2,', '5,', '0,', '8,']
#time right now: 50--------------------------------------------
#Car on road A: name = 7; Time Left Til Intersection: 2 seconds
#cars already passed: 
#['2,', '5,', '0,', '8,']
#time right now: 51--------------------------------------------
#Car on road A: name = 7; Time Left Til Intersection: 1 seconds
#cars already passed: 
#['2,', '5,', '0,', '8,']
#time right now: 52--------------------------------------------
#Car on road A: name = 7; Time Left Til Intersection: 0 seconds
#cars already passed: 
#['2,', '5,', '0,', '8,']
#time right now: 53--------------------------------------------
#cars already passed: 
#['2,', '5,', '0,', '8,', '7,']
#time right now: 54--------------------------------------------
#cars already passed: 
#['2,', '5,', '0,', '8,', '7,']
#time right now: 55--------------------------------------------
#cars already passed: 
#['2,', '5,', '0,', '8,', '7,']
#time right now: 56--------------------------------------------
#cars already passed: 
#['2,', '5,', '0,', '8,', '7,']
#time right now: 57--------------------------------------------
#cars already passed: 
#['2,', '5,', '0,', '8,', '7,']
#time right now: 58--------------------------------------------
#cars already passed: 
#['2,', '5,', '0,', '8,', '7,']
#time right now: 59--------------------------------------------
#cars already passed: 
#['2,', '5,', '0,', '8,', '7,']
#time right now: 60--------------------------------------------
#cars already passed: 
#['2,', '5,', '0,', '8,', '7,']
#--------------------------------------------------------------------------------------------------------
#The simulation has ended
#SUMMARY OF SIMULATION: ---------------------------------------------------------
#Time simulated (s): 60
#Average time car took to pass through the road (s): 7.5
