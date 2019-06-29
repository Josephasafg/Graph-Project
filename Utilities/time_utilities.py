import time
import functools
from math import sqrt
from Graph_Objects.Node import Node
global_list = list()
global_list.append(0.0)


def calc_time_constraint(start_node: Node, goal_node: Node) -> float:
    x = (start_node.x - goal_node.x) ** 2
    y = (start_node.y - goal_node.y) ** 2
    z = (start_node.z - goal_node.z) ** 2
    distance = sqrt(x + y + z)
    distance = distance * 1.25
    return distance


def calculate_average_time(tries: int, item: str):
    print(f"Total amount of {item}: {tries}")
    print(f"Average time it took for the algorithm to run for one {item} is: {global_list[0] / tries} seconds\n")


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        global_list.insert(0, global_list[0] + run_time)
        return value
    return wrapper_timer
