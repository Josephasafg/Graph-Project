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


def verify_node(node, obstacle_map, min_x, min_y, max_x, max_y, grid_resolution):
    point_x = calc_position(node.x, grid_resolution, min_x)
    point_y = calc_position(node.y, grid_resolution, min_y)
    if point_x < min_x:
        return False
    elif point_y < min_y:
        return False
    elif point_x >= max_x:
        return False
    elif point_y >= max_y:
        return False

    try:
        if obstacle_map[int(node.x)][int(node.y)]:
            return False
    except IndexError as e:
        print(e)

    return True


def calc_position(index: int, reso: float, min_p):
    pos = index * reso + min_p
    return pos


def calc_xyindex(position, min_pos, reso):
    return round((position - min_pos) / reso)


def calc_obstacle_map(ox, oy, grid_resolution, robot_radius):
    min_x = round(min(ox))
    min_y = round(min(oy))
    max_x = round(max(ox))
    max_y = round(max(oy))

    x_width = round((max_x - min_x) / grid_resolution)
    y_width = round((max_y - min_y) / grid_resolution)

    # obstacle map generation
    obstacle_map = [[False for _ in arange(y_width)]
                    for _ in arange(x_width)]
    for ix in arange(int(x_width)):
        x = calc_position(ix, grid_resolution, min_x)
        for iy in arange(int(y_width)):
            y = calc_position(iy, grid_resolution, min_y)
            for iox, ioy in zip(ox, oy):
                d = math.sqrt((iox - x)**2 + (ioy - y)**2)
                if d <= robot_radius:
                    obstacle_map[int(ix)][int(iy)] = True
                    break

    return obstacle_map, min_x, min_y, max_x, max_y, x_width, y_width


def calc_index(node, x_width, x_min, y_min):
    return (node.y - y_min) * x_width + (node.x - x_min)


def calc_xyindex(position: int, minp: int, reso: float):
    return round((position - minp)/reso)


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
