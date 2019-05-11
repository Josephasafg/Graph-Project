import math
import numpy as np
import matplotlib.pyplot as plt
from Utilities import mapping_utility_methods
from Utilities.KDTree import KDTree
from Graph import Graph
from Utilities.timer_decorator import timer
from Utilities.timer_decorator import calculate_average_time
from Node import Node
from Utilities.utilities import randomize_dynamic_graph_size

# parameter
TOTAL_TIME = 0
ALGORITHM = "a_star"
X = list()
Y = list()
Z = list()
SHOW_ANIMATION = True


def _get_algorithm_function(algorithm_name):
    if algorithm_name == 'dijkstra':
        return dijkstra_planning
    elif algorithm_name == 'a_star':
        return a_star_planning
    else:
        raise ValueError("This algorithm can't be found!")


@timer
def prm_planning(obstacle_x, obstacle_y, robot_radius, algorithm_name, data_graph, random_graph_size):
    result_tuple_list = list()
    total_distance_list = list()
    goal_list_tuple = list()
    obkdtree = KDTree(np.vstack((obstacle_x, obstacle_y)).T)
    algorithms = _get_algorithm_function(algorithm_name)
    start_node = None

    for index in range(len(data_graph.coordinate['Building'][data_graph.model_name]['Floors'][str(data_graph.current_floor)]['goal_x'])):
        goal_tuple = (data_graph.coordinate['Building'][data_graph.model_name]['Floors'][str(data_graph.current_floor)]
                      ['goal_x'][index] * random_graph_size,
                      data_graph.coordinate['Building'][data_graph.model_name]['Floors'][str(data_graph.current_floor)]
                      ['goal_y'][index] * random_graph_size,
                      data_graph.coordinate['Building'][data_graph.model_name]['Floors'][str(data_graph.current_floor)]
                      ['goal_z'][index] * random_graph_size)

        sample_x, sample_y = mapping_utility_methods.sample_points\
            (data_graph.starting_point, goal_tuple, robot_radius, obstacle_x,
                obstacle_y, obkdtree, random_graph_size)

        # if SHOW_ANIMATION:
        #     plt.plot(sample_x, sample_y, ".b")

        road_map = mapping_utility_methods.generate_roadmap(sample_x, sample_y, robot_radius,
                                                            obkdtree, random_graph_size)

        start_node = Node(data_graph.starting_point[0], data_graph.starting_point[1], 0.0, -1, True)
        goal_node = Node(goal_tuple[0], goal_tuple[1], 0.0, -1)

        result_x, result_y, total_distance, return_code = algorithms(start_node,
                                                                     goal_node, sample_x, sample_y, road_map)
        result_tuple_list.append((result_x, result_y, return_code))
        total_distance_list.append(total_distance)
        goal_list_tuple.append(goal_tuple)
        # print(f"result x:{len(result_x)}, y:{len(result_y)}")

    min_index, min_distance = mapping_utility_methods.find_min_time(total_distance_list)
    data_graph.goal_point = goal_list_tuple[min_index]

    total_time_to_escape = start_node.calculate_time_to_escape(mapping_utility_methods.weight_on_sub_path(min_distance))
    print(f"Total time to escape.\nCapacity: {start_node.capacity}\nTime: {total_time_to_escape} minutes\n")

    return result_tuple_list[min_index][0], result_tuple_list[min_index][1],\
        min_index, min_distance, result_tuple_list[min_index][2]


def a_star_planning(start_node, goal_node, sample_x, sample_y, road_map):
    open_set, closed_set = dict(), dict()
    open_set[len(road_map) - 2] = start_node
    break_flag = 0
    while True:
        if not open_set:
            print("Cannot find path")
            break_flag = 1
            break

        current_id = min(open_set, key=lambda o: open_set[o].cost +
                         mapping_utility_methods.calc_heuristic(goal_node, open_set[o]))
        current = open_set[current_id]

        if current_id == (len(road_map) - 1):
            print("Find goal")
            goal_node.pind = current.pind
            goal_node.cost = current.cost
            break

        # Remove the item from the open set
        open_set.pop(current_id)
        # Add it to the closed set
        closed_set[current_id] = current

        # expand search grid based on motion model
        for i in range(len(road_map[current_id])):
            neighbour_id = road_map[current_id][i]
            dx = sample_x[neighbour_id] - current.x
            dy = sample_y[neighbour_id] - current.y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            node = Node(sample_x[neighbour_id], sample_y[neighbour_id], distance, current_id)

            if neighbour_id in closed_set:
                continue

            if neighbour_id not in open_set:
                open_set[neighbour_id] = node  # Discover a new node
            else:
                if open_set[neighbour_id].cost >= node.cost:
                    # This path is the best until now. record it!
                    open_set[neighbour_id] = node

    result_x, result_y, total = [goal_node.x], [goal_node.y], [goal_node.cost]
    pind = goal_node.pind
    while pind != -1:
        n = closed_set[pind]
        result_x.append(n.x)
        result_y.append(n.y)
        total.append(n.cost)
        pind = n.pind

    total_distance = 0
    for value in total:
        total_distance += value
    print(f"total distance (meters): {total_distance}")
    print(f"Total time in minutes per person: {mapping_utility_methods.weight_on_sub_path(total_distance)}")

    return result_x, result_y, total_distance, break_flag


def dijkstra_planning(start_node, goal_node, sample_x, sample_y, road_map):
    open_set, closed_set = dict(), dict()
    open_set[len(road_map) - 2] = start_node

    flag = 0
    while True:
        if not open_set:
            print("Cannot find path")
            flag = 1
            break

        current_id = min(open_set, key=lambda o: open_set[o].cost)
        current = open_set[current_id]

        if current_id == (len(road_map) - 1):
            print("Goal is found!")
            goal_node.pind = current.pind
            goal_node.cost = current.cost
            break

        # Remove the item from the open set
        open_set.pop(current_id)
        # Add it to the closed set
        closed_set[current_id] = current

        # expand search grid based on motion model
        for i in range(len(road_map[current_id])):
            neighbour_id = road_map[current_id][i]
            distance_x = sample_x[neighbour_id] - current.x
            distance_y = sample_y[neighbour_id] - current.y
            # total_time = weight_on_sub_path(math.sqrt(distance_x**2 + distance_y**2))
            distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

            node = Node(sample_x[neighbour_id], sample_y[neighbour_id], distance, current_id)

            if neighbour_id in closed_set:
                continue
            # Otherwise if it is already in the open set
            if neighbour_id in open_set:
                if open_set[neighbour_id].cost > node.cost:
                    open_set[neighbour_id].cost = node.cost
                    open_set[neighbour_id].pind = current_id
            else:
                open_set[neighbour_id] = node

    # generate final course
    result_x, result_y, total = [goal_node.x], [goal_node.y], [goal_node.cost]
    pind = goal_node.pind

    while pind != -1:
        n = closed_set[pind]
        result_x.append(n.x)
        result_y.append(n.y)
        total.append(n.cost)
        pind = n.pind

    amount_of_total = 0
    for value in total:
        amount_of_total += value
    print(f"total distance (meters): {amount_of_total}")
    print(f"total time in minutes: {mapping_utility_methods.weight_on_sub_path(amount_of_total)}")

    return result_x, result_y, amount_of_total, flag



def main(data_graph, algorithm_name, random_graph_size):
    # print(__file__ + " start!!")
    robot_size = 1.0 * random_graph_size

    obstacle_x, obstacle_y = list(), list()

    current_floor = mapping_utility_methods._get_building_model(data_graph.model_name, data_graph.current_floor)
    obstacle_x, obstacle_y = current_floor(obstacle_x, obstacle_y, random_graph_size)

    result_x, result_y, min_index, current_min_time, return_code = prm_planning(obstacle_x, obstacle_y, robot_size,
                                                                                algorithm_name, data_graph,
                                                                                random_graph_size)

    data_graph.total_min_time += current_min_time
    # if SHOW_ANIMATION and return_code == 0:
    if SHOW_ANIMATION:
        plt.plot(obstacle_x, obstacle_y, ".k")
        plt.plot(data_graph.starting_point[0], data_graph.starting_point[1], "^r")
        plt.plot(graph.coordinate['Building'][data_graph.model_name]['Floors'][str(data_graph.current_floor)]['goal_x']
                 [min_index] * random_graph_size,
                 graph.coordinate['Building'][data_graph.model_name]['Floors'][str(data_graph.current_floor)]['goal_y']
                 [min_index] * random_graph_size, "^g")
        plt.grid(True)
        plt.axis("equal")

    assert result_x, 'Cannot find path'

    #   todo change to floor's actual height
    for i in range(len(result_x)):
        Z.append(float((60 * random_graph_size) * (data_graph.current_floor-1)))

    X.extend(result_x)
    Y.extend(result_y)
    if SHOW_ANIMATION:
        plt.plot(result_x, result_y, "-r")
        plt.show()

    if return_code != 0:
        return False

    data_graph.goal_point = data_graph.coordinate['Building'][data_graph.model_name]['Floors'][str(data_graph.current_floor)]['goal_x'][min_index] * random_graph_size, \
        data_graph.coordinate['Building'][data_graph.model_name]['Floors'][str(data_graph.current_floor)]['goal_y'][min_index] * random_graph_size,\
        data_graph.coordinate['Building'][data_graph.model_name]['Floors'][str(data_graph.current_floor)]['goal_z'][min_index] * random_graph_size

    return True


if __name__ == '__main__':
    average_of_run = 0
    graph = Graph('floors.yaml')
    amount = 2
    amount_of_plots = 0
    for i in range(amount):
        exit_flag = True
        tries = 0
        graph_size = randomize_dynamic_graph_size()
        graph.randomize_graph_selection()
        graph.randomize_floor_selection()
        graph.prioritize_starting_points(graph_size)

        current_floor = graph.current_floor
        for c_index in range(len(graph.starting_nodes)):
            amount_of_plots += 1
            graph.current_floor = current_floor  # todo put this somewhere else
            graph.starting_point = graph.starting_nodes[c_index].x, graph.starting_nodes[c_index].y, \
                                   graph.starting_nodes[c_index].z
            print(f"starting point number {graph.starting_point}")
            # start_time = time.time()
            while exit_flag:
                if tries > 10:
                    break
                exit_flag = main(graph, ALGORITHM, graph_size)

                if not exit_flag:
                    print(f'Returned from floor {graph.current_floor} unsuccessfully')
                    tries += 1
                    amount_of_plots += 1
                    exit_flag = True
                    continue
                else:
                    print(f'Returned successfully from floor {graph.current_floor}')
                    tries = 1
                    if c_index == len(graph.starting_nodes) - 1 or graph.current_floor > 1:
                        graph.current_floor -= 1
                    else:
                        break

                if graph.current_floor < 1:
                    break
                else:
                    graph.starting_point = graph.goal_point[0], graph.goal_point[1] - (3.5 * graph_size), \
                                           graph.coordinate['Building'][graph.model_name]['Floors'][str(graph.current_floor)]['start_z'][0] * graph_size
                    graph.total_min_time += graph.calc_height_distance()

            # average_of_run += (end_time - start_time)
            print(f"Graph total distance is: {graph.total_min_time}")
            mapping_utility_methods.create_3d_graph(X, Y, Z)
            X, Y, Z = graph.clear_x_y_z_lists(X, Y, Z)
            graph.total_min_time = 0
        graph.starting_nodes.clear()
        # graph.delete_current_model()
    average_of_run /= amount
    calculate_average_time(amount_of_plots)
    print(f"Finished Experiment on {ALGORITHM} algorithm. Average is: {average_of_run}")
    exit(0)
