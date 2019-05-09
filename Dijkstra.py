"""
Dijkstra grid based planning
author: Atsushi Sakai(@Atsushi_twi)
"""

import matplotlib.pyplot as plt
import math
import numpy as np
from Utilities.KDTree import KDTree
import time
import random
import yaml

show_animation = True

N_SAMPLE = 500  # number of sample_points
N_KNN = 10  # number of edge from one sampled point
MAX_EDGE_LEN = 30.0  # [m] Maximum edge length


class Node:

    def __init__(self, x, y, cost, pind):
        self.x = x
        self.y = y
        self.cost = cost
        self.pind = pind

    def __str__(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.cost) + "," + str(self.pind)


def dijkstra_planning(sx, sy, gx, gy, ox, oy, reso, rr):
    """
    gx: goal x position [m]
    gx: goal x position [m]
    ox: x position list of Obstacles [m]
    oy: y position list of Obstacles [m]
    reso: grid resolution [m]
    rr: robot radius[m]
    """

    nstart = Node(round(sx / reso), round(sy / reso), 0.0, -1)
    ngoal = Node(round(gx / reso), round(gy / reso), 0.0, -1)
    ox = [iox / reso for iox in ox]
    oy = [ioy / reso for ioy in oy]

    obmap, minx, miny, maxx, maxy, xw, yw = calc_obstacle_map(ox, oy, reso, rr)

    motion = get_motion_model()
    obkdtree = KDTree(np.vstack((ox, oy)).T)
    sox, soy = sample_points((sx, sy), (gx, gy), rr, ox, oy, obkdtree)
    openset, closedset = dict(), dict()
    openset[calc_index(nstart, xw, minx, miny)] = nstart

    while 1:
        c_id = min(openset, key=lambda o: openset[o].cost)
        current = openset[c_id]
        #  print("current", current)

        # # show graph
        # if show_animation:
        #     plt.plot(current.x * reso, current.y * reso, "xc")
        #     if len(closedset.keys()) % 10 == 0:
        #         plt.pause(0.001)

        if current.x == ngoal.x and current.y == ngoal.y:
            print("Find goal")
            ngoal.pind = current.pind
            ngoal.cost = current.cost
            break

        # Remove the item from the open set
        openset.pop(c_id)
        # Add it to the closed set
        closedset[c_id] = current

        # expand search grid based on motion model
        for i, _ in enumerate(motion):
            node = Node(current.x + motion[i][0], current.y + motion[i][1],
                        current.cost + motion[i][2], c_id)
            print(motion[i][2])
            n_id = calc_index(node, xw, minx, miny)

            if not verify_node(node, obmap, minx, miny, maxx, maxy):
                continue

            if n_id in closedset:
                continue
            # Otherwise if it is already in the open set
            if n_id in openset:
                if openset[n_id].cost > node.cost:
                    openset[n_id].cost = node.cost
                    openset[n_id].pind = c_id
            else:
                openset[n_id] = node

    rx, ry = calc_final_path(ngoal, closedset, reso)

    return rx, ry


def calc_final_path(ngoal, closedset, reso):
    # generate final course
    rx, ry = [ngoal.x * reso], [ngoal.y * reso]
    pind = ngoal.pind

    while pind != -1:
        n = closedset[pind]
        rx.append(n.x * reso)
        ry.append(n.y * reso)
        print(f"COST IS: {n.cost}")
        pind = n.pind

    return rx, ry


def verify_node(node, obmap, minx, miny, maxx, maxy):


    if node.x < minx:
        return False
    elif node.y < miny:
        return False
    elif node.x > maxx:
        return False
    elif node.y > maxy:
        return False
    # if obmap[node.x][node.y]:
    #     return False

    return True


def calc_obstacle_map(ox, oy, reso, vr):

    minx = round(min(ox))
    miny = round(min(oy))
    maxx = round(max(ox))
    maxy = round(max(oy))
    #  print("minx:", minx)
    #  print("miny:", miny)
    #  print("maxx:", maxx)
    #  print("maxy:", maxy)

    xwidth = round(maxx - minx)
    ywidth = round(maxy - miny)
    #  print("xwidth:", xwidth)
    #  print("ywidth:", ywidth)

    # obstacle map generation
    obmap = [[False for i in range(ywidth)] for i in range(xwidth)]
    for ix in range(xwidth):
        x = ix + minx
        for iy in range(ywidth):
            y = iy + miny
            #  print(x, y)
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


def main():
    print(__file__ + " start!!")
    yaml_file = open('floors.yaml', 'r')
    coordinates_dict = yaml.load(yaml_file, Loader=yaml.FullLoader)
    # start and goal position
    floor = 1
    sx = coordinates_dict['Building']['BUILDING_8_HIT']['Floors'][str(floor)]['start_x'][0]
    sy = coordinates_dict['Building']['BUILDING_8_HIT']['Floors'][str(floor)]['start_y'][0]
    gx = coordinates_dict['Building']['BUILDING_8_HIT']['Floors'][str(floor)]['goal_x'][1]
    gy = coordinates_dict['Building']['BUILDING_8_HIT']['Floors'][str(floor)]['goal_y'][1]
    grid_size = 1.0  # [m]
    robot_size = 1.0  # [m]

    obstacle_x = []
    obstacle_y = []

    for i in range(60):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in range(60):
        obstacle_x.append(60.0)
        obstacle_y.append(i)
    for i in range(35):
        obstacle_x.append(i)
        obstacle_y.append(60.0)
    for i in range(45, 61):
        obstacle_x.append(i)
        obstacle_y.append(60.0)

    for i in range(10):
        obstacle_x.append(0)
        obstacle_y.append(i)
    for i in range(18, 61):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    # bottom left class
    for i in range(11):
        obstacle_x.append(i)
        obstacle_y.append(8.0)
    for i in range(10):
        obstacle_x.append(10.0)
        obstacle_y.append(i)

    # bottom stairs
    for i in range(11, 20):
        obstacle_x.append(i)
        obstacle_y.append(4.0)
    for i in range(5):
        obstacle_x.append(19)
        obstacle_y.append(i)

    # elevator
    for i in range(25, 35):
        obstacle_x.append(i)
        obstacle_y.append(3.0)
    for i in range(4):
        obstacle_x.append(25)
        obstacle_y.append(i)
    for i in range(4):
        obstacle_x.append(34)
        obstacle_y.append(i)

    # bottom right class
    for i in range(50, 60):
        obstacle_x.append(i)
        obstacle_y.append(10.0)
    for i in range(10):
        obstacle_x.append(50.0)
        obstacle_y.append(i)

    # toilet near bottom right class
    for i in range(47, 50):
        obstacle_x.append(i)
        obstacle_y.append(7)
    for i in range(8):
        obstacle_x.append(47)
        obstacle_y.append(i)

    # mid left class
    for i in range(10):
        obstacle_x.append(i)
        obstacle_y.append(20.0)
    for i in range(10):
        obstacle_x.append(i)
        obstacle_y.append(35.0)
    for i in range(20, 36):
        obstacle_x.append(10)
        obstacle_y.append(i)
    for i in range(10):
        obstacle_x.append(i)
        obstacle_y.append(28)

    # top left stairs
    for i in range(20, 33):
        obstacle_x.append(14.0)
        obstacle_y.append(i)
    for i in range(10, 14):
        obstacle_x.append(i)
        obstacle_y.append(20)

    # right class
    for i in range(25, 45):
        obstacle_x.append(50)
        obstacle_y.append(i)
    for i in range(11):
        obstacle_x.append(60 - i)
        obstacle_y.append(25.0)
    for i in range(11):
        obstacle_x.append(60 - i)
        obstacle_y.append(45.0)

    if show_animation:
        plt.plot(obstacle_x, obstacle_y, ".k")
        plt.plot(sx, sy, "^r")
        plt.plot(gx, gy, "^c")
        plt.grid(True)
        plt.axis("equal")

    rx, ry = dijkstra_planning(sx, sy, gx, gy, obstacle_x, obstacle_y, grid_size, robot_size)

    if show_animation:
        plt.plot(rx, ry, "-r")
        plt.show()


if __name__ == '__main__':
    average = 0
    f = True
    it = 0
    for i in range(1):
        start_time = time.time()

        while f:
            main()
            if start_time > 0:
                it += 1
                f = False
                continue
            else:
                f = True
        end_time = time.time()
        average += (end_time - start_time)
    average /= 1
    print(average)

