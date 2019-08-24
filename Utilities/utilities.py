import logging
import os

import math
from typing import List, Iterator
from Graph_Objects import Node
from random import randint
from itertools import cycle

from Graph_Objects.buidling_sizes import Size


logger = logging.getLogger(__name__)


def set_up_logger(log_name: str):
    logging.basicConfig(filename=os.getcwd() + log_name,
                        filemode='w',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.INFO)

    os.chmod(os.getcwd() + log_name, 777)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logging.getLogger("").addHandler(console)


def get_building_size(size: Size) -> List:
    if size == Size.LARGE:
        return [90 / 60, 100 / 60, 110 / 60, 120 / 60, 130 / 60, 140 / 60, 150 / 60, 160 / 60, 170 / 60, 180 / 60]
    elif size == Size.MEDIUM:
        return [50 / 60, 1, 70 / 60, 80 / 60, 90 / 60]
    elif size == Size.SMALL:
        return [20 / 60, 30 / 60, 10 / 60, 40 / 60]
    else:
        logger.error('Size is not supported')
        raise ValueError('Size is not supported')


def print_total_time_distance(amount_of_total, logger: logging):
    logger.info(f"total distance (meters): {amount_of_total}")
    logger.info(f"total time in minutes: {weight_on_sub_path(amount_of_total)}\n")


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
