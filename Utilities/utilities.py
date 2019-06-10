import math
from random import randint
from random import uniform


def randomize_dynamic_graph_size():
    return randint(1, 3)


def find_min_time(time_list):
    return time_list.index(min(time_list)), min(time_list)


#   400 meters per minute = 24 KMH
def weight_on_sub_path(distance, average_speed=250.0):
    return distance / average_speed


def calc_heuristic(n1, n2):
    factored_weight = 1.0
    distance = factored_weight * math.sqrt((n1.x - n2.x)**2 + (n1.y - n2.y)**2)
    return distance
