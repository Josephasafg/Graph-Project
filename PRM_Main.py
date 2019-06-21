import math
import numpy as np
import matplotlib.pyplot as plt
from Utilities import utilities
from Utilities import dijkstra_utilities
from Utilities import mapping_utility_methods
from Graph_Objects.KDTree import KDTree
from Graph_Objects.Graph import Graph
from Utilities.time_utilities import timer
from Utilities.time_utilities import calculate_average_time
from Graph_Objects.Node import Node
from Utilities.utilities import randomize_dynamic_graph_size

# global parameters
TOTAL_TIME = 0
RUNNING_ALGORITHM = "prm_dijkstra"
X_LIST = list()
Y_LIST = list()
Z_LIST = list()
SHOW_ANIMATION = True


def _get_algorithm_function(algorithm_name):
    if algorithm_name == 'prm_dijkstra':
        return prm_dijkstra
    elif algorithm_name == 'prm_a_star':
        return prm_a_star
    elif algorithm_name == 'dijkstra':
        return dijkstra
    else:
        raise ValueError("This algorithm can't be found!")


@timer
def prm_planning(obstacle_x, obstacle_y, robot_radius, algorithm_name, data_graph, random_graph_size):
    result_tuple_list = list()
    total_distance_list = list()
    goal_list_tuple = list()
    algorithms = _get_algorithm_function(algorithm_name)

    start_node = data_graph.starting_point
    my_indexes = data_graph.get_element_indexes(
        data_graph.coordinate['Building'][data_graph.model_name]['Floors']['goal_z'], random_graph_size)

    nodes_to_check = 1
    for index in my_indexes:
        goal_tuple = (data_graph.coordinate['Building'][data_graph.model_name]['Floors']
                      ['goal_x'][index] * random_graph_size,
                      data_graph.coordinate['Building'][data_graph.model_name]['Floors']
                      ['goal_y'][index] * random_graph_size,
                      data_graph.coordinate['Building'][data_graph.model_name]['Floors']
                      ['goal_z'][index] * random_graph_size)
        print(f"Checking exit #{nodes_to_check}.\n")
        nodes_to_check += 1

        goal_node = Node(goal_tuple[0], goal_tuple[1], 0.0, -1)

        if algorithm_name == 'dijkstra':
            result_x, result_y, total_distance, return_code = algorithms(start_node, goal_node,
                                                                         obstacle_x, obstacle_y)
        else:
            obstacle_kdtree = KDTree(np.vstack((obstacle_x, obstacle_y)).T)
            sample_x, sample_y = mapping_utility_methods.sample_points\
                (start_node, goal_node, robot_radius, obstacle_x,
                    obstacle_y, obstacle_kdtree, random_graph_size)

            road_map = mapping_utility_methods.generate_roadmap(sample_x, sample_y, robot_radius,
                                                                obstacle_kdtree, random_graph_size)

            result_x, result_y, total_distance, return_code = algorithms(start_node,
                                                                         goal_node, sample_x, sample_y, road_map)

        result_tuple_list.append((result_x, result_y, return_code))
        total_distance_list.append(total_distance)
        goal_list_tuple.append(goal_tuple)

    try:
        min_index, min_distance = utilities.find_min_time(total_distance_list)
        data_graph.goal_point = Node(goal_list_tuple[min_index][0], goal_list_tuple[min_index][1], 0.0, -1)
        data_graph.goal_point.z = goal_list_tuple[min_index][2]
        # data_graph.goal_point = goal_list_tuple[min_index]

        print(f"Closest exit point is: {data_graph.goal_point}")

        total_time_to_escape = start_node.calculate_time_to_escape(utilities.weight_on_sub_path(min_distance))
        print(f"Total time to escape per capacity-\nCapacity: {start_node.capacity}\nTime: {total_time_to_escape} minutes\n")
    except ValueError as ve:
        raise ValueError(ve)

    return result_tuple_list[min_index][0], result_tuple_list[min_index][1],\
        min_index, min_distance, result_tuple_list[min_index][2]


def prm_a_star(start_node, goal_node, sample_x, sample_y, road_map):
    open_set, closed_set = dict(), dict()
    open_set[len(road_map) - 2] = start_node
    break_flag = 0
    while True:
        if not open_set:
            print("Cannot find path")
            break_flag = 1
            break

        current_id = min(open_set, key=lambda o: open_set[o].cost +
                         utilities.calc_heuristic(goal_node, open_set[o]))
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
    utilities.print_total_time_distance(total_distance)

    return result_x, result_y, total_distance, break_flag


def prm_dijkstra(start_node, goal_node, sample_x, sample_y, road_map):
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
            goal_node.pind = current.pind
            goal_node.cost = current.cost
            goal_node.z = start_node.z
            print(f"Exit point is found! {goal_node}")
            break

        # Remove the item from the open set
        open_set.pop(current_id)
        # Add it to the closed set
        closed_set[current_id] = current

        for i in range(len(road_map[current_id])):
            neighbour_id = road_map[current_id][i]
            distance_x = sample_x[neighbour_id] - current.x
            distance_y = sample_y[neighbour_id] - current.y
            distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

            node = Node(sample_x[neighbour_id], sample_y[neighbour_id], distance, current_id)

            if neighbour_id in closed_set:
                continue

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

    utilities.print_total_time_distance(amount_of_total)

    return result_x, result_y, amount_of_total, flag


def dijkstra(start_node, goal_node, obstacle_x, obstacle_y):
    grid_resolution = 1.0
    robot_radius = 1.0

    obstacle_map, min_x, min_y, max_x, max_y, x_width, y_width = dijkstra_utilities.calc_obstacle_map(obstacle_x, obstacle_y,
                                                                                        grid_resolution, robot_radius)

    motion_model = dijkstra_utilities.get_motion_model()

    open_set, closed_set = dict(), dict()
    open_set[dijkstra_utilities.calc_index(start_node, x_width, min_x, min_y)] = start_node

    flag = 0
    while True:
        if not open_set:
            print("Cannot find path")
            flag = 1
            break

        c_id = min(open_set, key=lambda o: open_set[o].cost)
        current = open_set[c_id]

        if current.x == goal_node.x and current.y == goal_node.y:
            print("Find goal")
            goal_node.pind = current.pind
            goal_node.cost = current.cost
            break

        # Remove the item from the open set
        open_set.pop(c_id)
        # Add it to the closed set
        closed_set[c_id] = current

        for i, _ in enumerate(motion_model):
            node = Node(current.x + motion_model[i][0], current.y + motion_model[i][1],
                        current.cost + motion_model[i][2], c_id)
            node_id = dijkstra_utilities.calc_index(node, x_width, min_x, min_y)

            if not dijkstra_utilities.verify_node(node, obstacle_map, min_x, min_y, max_x, max_y):
                continue

            if node_id in closed_set:
                continue
            
            if node_id in open_set:
                if open_set[node_id].cost > node.cost:
                    open_set[node_id].cost = node.cost
                    open_set[node_id].pind = c_id
            else:
                open_set[node_id] = node

    result_x, result_y, amount_of_total = dijkstra_utilities.calc_final_path(goal_node, closed_set)
    utilities.print_total_time_distance(amount_of_total)

    return result_x, result_y, amount_of_total, flag


def main(data_graph, algorithm_name, random_graph_size):
    robot_size = 1.0 * random_graph_size

    obstacle_x, obstacle_y = list(), list()

    current_floor = mapping_utility_methods._get_building_model(data_graph.model_name,
                                                                round(data_graph.current_floor/random_graph_size))
    obstacle_x, obstacle_y = current_floor(obstacle_x, obstacle_y, random_graph_size)

    result_x, result_y, min_index, current_min_time, return_code = prm_planning(obstacle_x, obstacle_y, robot_size,
                                                                                algorithm_name, data_graph,
                                                                                random_graph_size)

    #  current_min_time needs to be min distance
    data_graph.total_min_time += current_min_time
    if SHOW_ANIMATION:
        plt.plot(obstacle_x, obstacle_y, ".k")
        plt.plot(data_graph.starting_point.x, data_graph.starting_point.y, "^r")
        plt.plot(data_graph.goal_point.x,
                 data_graph.goal_point.y, "^g")
        plt.grid(True)
        plt.axis("equal")

    assert result_x, 'Cannot find path'

    lower_height = float(graph.get_lower_floor_height())
    for _ in range(len(result_x)):
        Z_LIST.append(lower_height)

    X_LIST.extend(result_x)
    Y_LIST.extend(result_y)
    if SHOW_ANIMATION:
        plt.plot(result_x, result_y, "-r")
        plt.show()

    if return_code != 0:
        return False

    return True


if __name__ == '__main__':
    average_of_run = 0
    graph = Graph('floors.yaml', 'BUILDING_8_HIT')
    amount_of_graphs = 2
    amount_of_plots = 0
    for i in range(amount_of_graphs):
        print("Evaluating a new building...\n")
        exit_flag = True
        tries = 0
        graph_size = randomize_dynamic_graph_size()

        # graph_size = 1 / 3
        # graph.randomize_graph_selection()
        print(f"Current building being evaluated - {graph.model_name}")
        graph.get_prioritized_points(graph_size, RUNNING_ALGORITHM)

        for current_index in range(len(graph.starting_nodes)):
            print(f"Evaluating a new starting point for building {graph.model_name}...\n")
            amount_of_plots += 1
            graph.current_floor = graph.starting_nodes[current_index].z
            print(f"Current floor height is: {graph.current_floor} meters")
            graph.list_of_height = list(graph.get_height_no_duplicates(graph_size))
            working_height_set = sorted(set(graph.list_of_height), reverse=True)

            graph.starting_point = Node(graph.starting_nodes[current_index].x, graph.starting_nodes[current_index].y, 0.0, -1, True)
            graph.starting_point.z = graph.starting_nodes[current_index].z

            while exit_flag:
                print(f"***********************************************************")
                print(f"Starting point number {graph.starting_point}")
                if tries > 10:
                    break
                exit_flag = main(graph, RUNNING_ALGORITHM, graph_size)

                if not exit_flag:
                    print(f'Returned from floor {graph.current_floor} unsuccessfully')
                    print(f"***********************************************************")
                    tries += 1
                    amount_of_plots += 1
                    exit_flag = True
                    continue
                else:
                    print(f"***********************************************************")
                    print(f'Returned successfully from floor (height) - {graph.current_floor} meters')
                    tries = 1
                    if (current_index == len(graph.starting_nodes) - 1) or (graph.current_floor > 0.0):
                        if not graph.list_of_height:
                            break
                        else:
                            del graph.list_of_height[0]
                            if not graph.list_of_height:
                                break
                        graph.current_floor = graph.list_of_height[0]
                    else:
                        break

                if graph.current_floor < 0:
                    break
                else:
                    graph.starting_point.x = graph.goal_point.x
                    graph.starting_point.y = graph.goal_point.y - (4.0 * graph_size)
                    graph.starting_point.z = graph.current_floor
                    graph.total_min_time += graph.calc_height_distance()

            graph.list_of_height = list(working_height_set)
            print(f"Total time to escape building {graph.model_name} in minutes per {graph.starting_point.capacity} "
                  f"people: {graph.total_min_time} minutes")
            print("---------------------------------------------------------")
            mapping_utility_methods.create_3d_graph(X_LIST, Y_LIST, Z_LIST)
            X_LIST, Y_LIST, Z_LIST = graph.clear_x_y_z_lists(X_LIST, Y_LIST, Z_LIST)
            graph.total_min_time = 0
        graph.starting_nodes.clear()
    average_of_run /= amount_of_graphs
    print("Average Time per one floor - ")
    calculate_average_time(amount_of_plots)
    print("Average Time per one Building - ")
    calculate_average_time(amount_of_graphs)
    exit(0)
