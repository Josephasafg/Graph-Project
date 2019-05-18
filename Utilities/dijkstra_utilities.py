import matplotlib.pyplot as plt
import math
from numpy import arange
import numpy as np
import time
import random
import yaml
from Graph import Graph
from Node import Node
from Utilities.KDTree import KDTree


show_animation = True

N_SAMPLE = 500  # number of sample_points
N_KNN = 10  # number of edge from one sampled point
MAX_EDGE_LEN = 30.0  # [m] Maximum edge length


def calc_final_path(goal_node, closedset):
    # generate final course
    result_x, result_y, total_cost = [goal_node.x], [goal_node.y], goal_node.cost
    pind = goal_node.pind

    while pind != -1:
        current_node = closedset[pind]
        result_x.append(current_node.x)
        result_y.append(current_node.y)
        total_cost += current_node.cost
        pind = current_node.pind

    return result_x, result_y, total_cost


def verify_node(node, obmap, minx, miny, maxx, maxy):
    if node.x < minx:
        return False
    elif node.y < miny:
        return False
    elif node.x > maxx:
        return False
    elif node.y > maxy:
        return False

    if obmap[int(node.x)][int(node.y)]:
        return False

    return True


def calc_obstacle_map(ox, oy, reso, vr):

    minx = int(min(ox))
    miny = int(min(oy))
    maxx = int(max(ox))
    maxy = int(max(oy))

    xwidth = maxx - minx + 1
    ywidth = maxy - miny + 1

    # obstacle map generation
    obmap = [[False for i in arange(0, ywidth, 0.1)] for i in arange(0, xwidth, 0.1)]
    for ix in arange(xwidth):
        x = ix + minx
        for iy in arange(ywidth):
            y = iy + miny
            for iox, ioy in zip(ox, oy):
                d = math.sqrt((iox - x)**2 + (ioy - y)**2)
                if d <= vr / reso:
                    obmap[ix][iy] = True
                    break

    return obmap, minx, miny, maxx, maxy, xwidth, ywidth


def calc_index(node, xwidth, xmin, ymin):
    return (node.y - ymin) * xwidth + (node.x - xmin)


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


def sample_points(start_tuple, goal_tuple, robot_radius, obstacle_x, obstacle_y, obkdtree):
    max_x = max(obstacle_x)
    max_y = max(obstacle_y)
    min_x = min(obstacle_x)
    min_y = min(obstacle_y)
    sample_x, sample_y = list(), list()

    while len(sample_x) <= N_SAMPLE:
        random_x = (random.random() - min_x) * (max_x - min_x)
        random_y = (random.random() - min_y) * (max_y - min_y)
        index, dist = obkdtree.search(np.array([random_x, random_y]).reshape(2, 1))

        if dist[0] >= robot_radius:
            sample_x.append(random_x)
            sample_y.append(random_y)

    sample_x.append(start_tuple[0])
    sample_y.append(start_tuple[1])
    sample_x.append(goal_tuple[0])
    sample_y.append(goal_tuple[1])
    return sample_x, sample_y
