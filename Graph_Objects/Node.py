import random


class Node:
    def __init__(self, x=0, y=0, cost=0.0, pind=-1, capacity=False):
        self.__x = x
        self.__y = y
        self.__z = 0
        self._cost = cost
        self._pind = pind
        self.__priority = 0

        if capacity:
            self.__capacity = self.get_node_capacity()

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, value):
        self.__priority = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, value):
        self.__z = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    @property
    def capacity(self):
        return self.__capacity

    @property
    def pind(self):
        return self._pind

    @pind.setter
    def pind(self, value):
        self._pind = value

    def __str__(self):
        return f"({str(self.x)}, {str(self.y)}, {str(self.z)})"

    def calculate_time_to_escape(self, escape_time_per_person):
        return escape_time_per_person * self.capacity

    @staticmethod
    def get_node_capacity():
        # return 24
        return random.randint(1, 50)
