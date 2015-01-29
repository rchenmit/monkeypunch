# class for car

import random

class car:
    def __init__(self, name):
        self.enter_time = None
        self.exit_time = None
        self.total_travel_time = 0
        self.name = name
        self.time_to_intersection = random.randint(5, 10)


            