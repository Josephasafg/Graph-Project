import math
from numpy import arange
import numpy as np
import random

show_animation = True

N_SAMPLE = 500  # number of sample_points
N_KNN = 10  # number of edge from one sampled point
MAX_EDGE_LEN = 30.0  # [m] Maximum edge length


def calc_final_path(goal_node, closed_set):
    # generate final course
    result_x, result_y, total_cost = [goal_node.x], [goal_node.y], goal_node.cost
    pind = goal_node.pind

    while pind != -1:
        current_node = closed_set[pind]
        result_x.append(current_node.x)
        result_y.append(current_node.y)
        total_cost += current_node.cost
        pind = current_node.pind

    return result_x, result_y, total_cost


def verify_node(node, obstacle_map, min_x, min_y, max_x, max_y):
    if node.x < min_x:
        return False
    elif node.y < min_y:
        return False
    elif node.x > max_x:
        return False
    elif node.y > max_y:
        return False

    if obstacle_map[int(node.x)][int(node.y)]:
        return False

    return True


def calc_obstacle_map(ox, oy, grid_resolution, robot_radius):
    min_x = int(min(ox))
    min_y = int(min(oy))
    max_x = int(max(ox))
    max_y = int(max(oy))

    x_width = max_x - min_x + 1
    y_width = max_y - min_y + 1

    # obstacle map generation
    obstacle_map = [[False for _ in arange(0, y_width, 0.1)] for _ in arange(0, x_width, 0.1)]
    for ix in arange(x_width):
        x = ix + min_x
        for iy in arange(y_width):
            y = iy + min_y
            for iox, ioy in zip(ox, oy):
                d = math.sqrt((iox - x)**2 + (ioy - y)**2)
                if d <= robot_radius / grid_resolution:
                    obstacle_map[ix][iy] = True
                    break

    return obstacle_map, min_x, min_y, max_x, max_y, x_width, y_width


def calc_index(node, x_width, x_min, y_min):
    return (node.y - y_min) * x_width + (node.x - x_min)


def get_motion_model():
    # dx, dy, cost
    motion = [[1, 0, 1],
              [0, 1, 1],
              [-1, 0, 1],
              [0, -1, 1],
              [-1, -1, math.sqrt(2)],
              [-1, 1, math.sqrt(2)],
              [1, -1, math.sqrt(2)],
              [1, 1, math.sqrt(2)]]

    return motion
