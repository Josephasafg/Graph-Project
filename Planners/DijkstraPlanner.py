import logging

import math
from typing import List
from numpy import arange
from Graph_Objects.Node import Node
from Utilities.dijkstra_utilities import get_motion_model
from Utilities.utilities import print_total_time_distance

logger = logging.getLogger(__name__)


class DijkstraPlanner:
    def __init__(self, obstacle_x, obstacle_y, grid_resolution: float, radius: float, size_factor: float):
        self.grid_resolution = grid_resolution
        self.rr = radius
        self.obstacle_map = list()
        self.min_x = 0
        self.min_y = 0
        self.max_x = 0
        self.max_y = 0
        self.x_width = 0
        self.y_width = 0
        self.calc_obstacle_map(obstacle_x, obstacle_y, size_factor)
        self.motion = get_motion_model()

    def planning(self, sx, sy, gx, gy):
        start_node = Node(self.calc_xyindex(math.floor(sx), self.min_x),
                          self.calc_xyindex(math.floor(sy), self.min_y), 0.0, -1)
        goal_node = Node(self.calc_xyindex(math.floor(gx), self.min_x),
                         self.calc_xyindex(math.floor(gy), self.min_y), 0.0, -1)

        open_set, closed_set = dict(), dict()
        open_set[self.calc_grid_index(start_node)] = start_node

        flag = 0
        while True:
            if len(open_set) == 0:
                flag = 1
                logger.info("Open set is empty..")
                break

            c_id = min(open_set, key=lambda o: open_set[o].cost)
            current = open_set[c_id]

            if current.x == goal_node.x and current.y == goal_node.y:
                logger.info("Find goal")
                goal_node.pind = current.pind
                goal_node.cost = current.cost
                break

            # Remove the item from the open set
            del open_set[c_id]

            # Add it to the closed set
            closed_set[c_id] = current

            # expand_grid search grid based on motion model
            for i, _ in enumerate(self.motion):
                node = Node(current.x + self.motion[i][0],
                            current.y + self.motion[i][1],
                            (current.cost + self.motion[i][2]), c_id)
                n_id = self.calc_grid_index(node)

                # If the node is not safe, do nothing
                if not self.verify_node(node):
                    continue

                if n_id in closed_set:
                    continue

                if n_id not in open_set:
                    open_set[n_id] = node  # discovered a new node
                else:
                    if open_set[n_id].cost > node.cost:
                        # This path is the best until now. record it
                        open_set[n_id] = node

        result_x, result_y, amount_of_total = self.calc_final_path(goal_node, closed_set)
        print_total_time_distance(amount_of_total, logger)

        return result_x, result_y, amount_of_total, flag

    def calc_final_path(self, goal_node, closedset):
        # generate final course
        result_x, result_y = [self.calc_grid_position(goal_node.x, self.min_x)], [
            self.calc_grid_position(goal_node.y, self.min_y)]
        total_cost = goal_node.cost

        pind = goal_node.pind
        while pind != -1:
            n = closedset[pind]
            result_x.append(self.calc_grid_position(n.x, self.min_x))
            result_y.append(self.calc_grid_position(n.y, self.min_y))
            total_cost += n.cost
            pind = n.pind

        return result_x, result_y, total_cost

    def calc_grid_position(self, index, minp):
        pos = index * self.grid_resolution + minp
        return pos

    def calc_xyindex(self, position, min_pos):
        return round((position - min_pos) / self.grid_resolution)

    def calc_grid_index(self, node):
        return (node.y - self.min_y) * self.x_width + (node.x - self.min_x)

    def verify_node(self, node):
        point_x = self.calc_grid_position(node.x, self.min_x)
        point_y = self.calc_grid_position(node.y, self.min_y)

        if point_x < self.min_x:
            return False
        elif point_y < self.min_y:
            return False
        elif point_x >= self.max_x:
            return False
        elif point_y >= self.max_y:
            return False

        # collision check
        try:
            if self.obstacle_map[int(node.x)][int(node.y)]:
                return False
        except IndexError:
            pass

        return True

    def calc_obstacle_map(self, obstacle_x, obstacle_y, graph_size_factor):
        self.min_x = round(min(obstacle_x))
        self.min_y = round(min(obstacle_y))
        self.max_x = round(max(obstacle_x))
        self.max_y = round(max(obstacle_y))

        self.x_width = round((self.max_x - self.min_x) / self.grid_resolution) * graph_size_factor
        self.y_width = round((self.max_y - self.min_y) / self.grid_resolution) * graph_size_factor

        # obstacle map generation
        self.obstacle_map = [[False for _ in arange(self.y_width)]
                      for _ in arange(self.x_width)]
        for ix in arange(self.x_width):
            x = self.calc_grid_position(ix, self.min_x)
            for iy in arange(self.y_width):
                y = self.calc_grid_position(iy, self.min_y)
                for i_obstacle_x, i_obstacle_y in zip(obstacle_x, obstacle_y):
                    d = math.sqrt((i_obstacle_x - x) ** 2 + (i_obstacle_y - y) ** 2)
                    if d <= self.rr:
                        self.obstacle_map[int(ix)][int(iy)] = True
                        break


def dijkstra_main(start_node: Node, goal_node: Node, grid_size: float, robot_radius: float,
                  obstacle_x: List, obstacle_y: List, size_factor):
    dijkstra = DijkstraPlanner(obstacle_x, obstacle_y, grid_size, robot_radius, size_factor)
    result_x, result_y, total_amount, return_flag = dijkstra.planning(start_node.x, start_node.y, goal_node.x, goal_node.y)

    return result_x, result_y, total_amount, return_flag
