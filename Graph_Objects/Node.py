import random


class Node:
    def __init__(self, x, y, cost=0.0, pind=-1, capacity=False):
        self.x = x
        self.y = y
        self.z = 0
        self.cost = cost
        self.pind = pind
        self.priority = 0

        if capacity:
            self.capacity = self.get_node_capacity()

    def __str__(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.cost) + "," + str(self.pind)

    def calculate_time_to_escape(self, escape_time_per_person):
        return escape_time_per_person * self.capacity

    @staticmethod
    def get_node_capacity():
        return random.randint(1, 50)
