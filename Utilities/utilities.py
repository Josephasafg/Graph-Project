import math
from typing import List
from Graph_Objects import Node
from random import randint
from random import uniform


def print_total_time_distance(amount_of_total):
    print(f"total distance (meters): {amount_of_total}")
    print(f"total time in minutes: {weight_on_sub_path(amount_of_total)}\n")
    # print(f"============================================================")


def randomize_dynamic_graph_size():
    # small_sizes = [1/3, 1/2, 1/6, 2/3]
    # large_sizes = [50/60, 60/60, 70/60, 80/60, 90/60]
    choose_random_index = randint(0, 3)
    # return small_sizes[choose_random_index]
    return randint(1, 3)


def find_min_time(time_list: List):
    return time_list.index(min(time_list)), min(time_list)


#   400 meters per minute = 24 KMH
def weight_on_sub_path(distance: int, average_speed=250.0):
    return distance / average_speed


def calc_heuristic(n1: Node, n2: Node):
    factored_weight = 1.0
    distance = factored_weight * math.sqrt((n1.x - n2.x)**2 + (n1.y - n2.y)**2)
    return distance
