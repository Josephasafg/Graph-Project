import math
from typing import List, Iterator
from Graph_Objects import Node
from random import randint
from itertools import cycle

from Graph_Objects.buidling_sizes import Size


def get_building_size(size: Size) -> List:
    if size == Size.LARGE:
        return [90 / 60, 100 / 60, 110 / 60, 120 / 60, 130 / 60, 140 / 60, 150 / 60, 160 / 60, 170 / 60, 180 / 60]
    elif size == Size.MEDIUM:
        return [5 / 6, 1, 7 / 6, 4 / 3, 3 / 2]
    elif size == Size.SMALL:
        return [1 / 3, 1 / 2, 1 / 6, 2 / 3]
    else:
        raise ValueError('Size is not supported')


def print_total_time_distance(amount_of_total):
    print(f"total distance (meters): {amount_of_total}")
    print(f"total time in minutes: {weight_on_sub_path(amount_of_total)}\n")


def randomize_dynamic_graph_size(size: Size) -> List:
    building_sizes = get_building_size(size)
    choose_random_index = randint(0, len(building_sizes))
    return building_sizes[choose_random_index]


def create_size_cycle(size: Size) -> Iterator[float]:
    building_sizes = get_building_size(size)
    cycle_list = cycle(building_sizes)
    return cycle_list


def find_min_time(time_list: List):
    if all(item == 0 for item in time_list):
        return 0, 0
    minimum = min(m for m in time_list if m != 0)
    return time_list.index(minimum), minimum


#   400 meters per minute = 24 KMH
def weight_on_sub_path(distance: int, average_speed=250.0):
    return distance / average_speed


def calc_heuristic(n1: Node, n2: Node):
    factored_weight = 1.0
    distance = factored_weight * math.sqrt((n1.x - n2.x) ** 2 + (n1.y - n2.y) ** 2)
    return distance


def create_graph_list() -> Iterator[str]:
    return cycle(['BUILDING_8_HIT', 'OUTLINE_OBSTACLES_DEMO_BUILDING_1',
                  'OUTLINE_OBSTACLES_DEMO_BUILDING_2', 'OUTLINE_OBSTACLES_DEMO_BUILDING_3',
                  'OUTLINE_OBSTACLES_DEMO_BUILDING_4', 'OUTLINE_OBSTACLES_DEMO_BUILDING_5',
                  'OUTLINE_OBSTACLES_DEMO_BUILDING_6', 'OUTLINE_OBSTACLES_DEMO_BUILDING_7',
                  'OUTLINE_OBSTACLES_DEMO_BUILDING_8', 'OUTLINE_OBSTACLES_DEMO_BUILDING_9',
                  'OUTLINE_OBSTACLES_DEMO_BUILDING_10'])
