class Node:
    def __init__(self, x, y, cost=0.0, pind=-1):
        self.x = x
        self.y = y
        self.z = 0
        self.cost = cost
        self.pind = pind
        self.priority = 0


    def __str__(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.cost) + "," + str(self.pind)
