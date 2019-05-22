import math
import numpy as np
import matplotlib.pyplot as plt
from Utilities import dijkstra_utilities
from Utilities import mapping_utility_methods
from Graph_Objects.KDTree import KDTree
from Graph_Objects.Graph import Graph
from Utilities.timer_decorator import timer
from Utilities.timer_decorator import calculate_average_time
from Graph_Objects.Node import Node
from Utilities.utilities import randomize_dynamic_graph_size

# parameter
TOTAL_TIME = 0
ALGORITHM = "prm_dijkstra"
X = list()
Y = list()
Z = list()
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

    start_node = Node(data_graph.starting_point[0], data_graph.starting_point[1], 0.0, -1, True)
    my_indexes = data_graph.get_element_indexes(data_graph.coordinate['Building'][data_graph.model_name]['Floors']['goal_z'])

    for index in my_indexes:
        goal_tuple = (data_graph.coordinate['Building'][data_graph.model_name]['Floors']
                      ['goal_x'][index] * random_graph_size,
                      data_graph.coordinate['Building'][data_graph.model_name]['Floors']
                      ['goal_y'][index] * random_graph_size,
                      data_graph.coordinate['Building'][data_graph.model_name]['Floors']
                      ['goal_z'][index] * random_graph_size)

        goal_node = Node(goal_tuple[0], goal_tuple[1], 0.0, -1)

        if algorithm_name == 'dijkstra':
            result_x, result_y, total_distance, return_code = algorithms(start_node, goal_node,
                                                                         obstacle_x, obstacle_y)
        else:
            obkdtree = KDTree(np.vstack((obstacle_x, obstacle_y)).T)
            sample_x, sample_y = mapping_utility_methods.sample_points\
                (data_graph.starting_point, goal_tuple, robot_radius, obstacle_x,
                    obstacle_y, obkdtree, random_graph_size)

            road_map = mapping_utility_methods.generate_roadmap(sample_x, sample_y, robot_radius,
                                                                obkdtree, random_graph_size)

            result_x, result_y, total_distance, return_code = algorithms(start_node,
                                                                         goal_node, sample_x, sample_y, road_map)

        result_tuple_list.append((result_x, result_y, return_code))
        total_distance_list.append(total_distance)
        goal_list_tuple.append(goal_tuple)

    min_index, min_distance = mapping_utility_methods.find_min_time(total_distance_list)
    data_graph.goal_point = goal_list_tuple[min_index]

    print(f"My goal is: {data_graph.goal_point}")

    total_time_to_escape = start_node.calculate_time_to_escape(mapping_utility_methods.weight_on_sub_path(min_distance))
    print(f"Total time to escape.\nCapacity: {start_node.capacity}\nTime: {total_time_to_escape} minutes\n")

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
    print(f"=================================================================================")

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
    print(f"total time in minutes: {mapping_utility_methods.weight_on_sub_path(amount_of_total)}\n")
    print(f"=================================================================================")

    return result_x, result_y, amount_of_total, flag


def dijkstra(start_node, goal_node, obstacle_x, obstacle_y):
    grid_resolution = 1.0
    robot_radius = 1.0
    # obstacle_x = [iox / grid_resolution for iox in obstacle_x]
    # obstacle_y = [ioy / grid_resolution for ioy in obstacle_y]

    obmap, minx, miny, maxx, maxy, xw, yw = dijkstra_utilities.calc_obstacle_map(obstacle_x, obstacle_y,
                                                                                 grid_resolution, robot_radius)

    motion = dijkstra_utilities.get_motion_model()

    open_set, closed_set = dict(), dict()
    open_set[dijkstra_utilities.calc_index(start_node, xw, minx, miny)] = start_node

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

        # expand search grid based on motion model
        for i, _ in enumerate(motion):
            # current.cost + motion[i][2]
            # distance_x = motion[i][0] - current.x
            # distance_y = motion[i][1] - current.y
            # distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
            # TODO: distance is longer, usually 4 times longer. this calculation is better. Try to check if consistent
            node = Node(current.x + motion[i][0], current.y + motion[i][1], current.cost + motion[i][2], c_id)
            node_id = dijkstra_utilities.calc_index(node, xw, minx, miny)

            if not dijkstra_utilities.verify_node(node, obmap, minx, miny, maxx, maxy):
                continue

            if node_id in closed_set:
                continue
            # Otherwise if it is already in the open set
            if node_id in open_set:
                if open_set[node_id].cost > node.cost:
                    open_set[node_id].cost = node.cost
                    open_set[node_id].pind = c_id
            else:
                open_set[node_id] = node

    result_x, result_y, amount_of_total = dijkstra_utilities.calc_final_path(goal_node, closed_set)

    print(f"total distance (meters): {amount_of_total}")
    print(f"total time in minutes: {mapping_utility_methods.weight_on_sub_path(amount_of_total)}")
    print(f"=================================================================================")

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
    if SHOW_ANIMATION:
        plt.plot(obstacle_x, obstacle_y, ".k")
        plt.plot(data_graph.starting_point[0], data_graph.starting_point[1], "^r")
        plt.plot(data_graph.goal_point[0],
                 data_graph.goal_point[1], "^g")
        plt.grid(True)
        plt.axis("equal")

    assert result_x, 'Cannot find path'

    lower_height = float(graph.get_lower_floor_height())
    for i in range(len(result_x)):
        Z.append(lower_height)
        # Z.append(float((60 * random_graph_size) * (data_graph.current_floor-1)))

    X.extend(result_x)
    Y.extend(result_y)
    if SHOW_ANIMATION:
        plt.plot(result_x, result_y, "-r")
        plt.show()

    if return_code != 0:
        return False

    # data_graph.goal_point = data_graph.coordinate['Building'][data_graph.model_name]['Floors']['goal_x'][min_index] * random_graph_size, \
    #     data_graph.coordinate['Building'][data_graph.model_name]['Floors']['goal_y'][min_index] * random_graph_size,\
    #     data_graph.coordinate['Building'][data_graph.model_name]['Floors']['goal_z'][min_index] * random_graph_size

    return True


if __name__ == '__main__':
    average_of_run = 0
    graph = Graph('floors.yaml')
    amount = 100
    amount_of_plots = 0
    for i in range(amount):
        exit_flag = True
        tries = 0
        graph_size = randomize_dynamic_graph_size()

        # graph_size = 1.0
        graph.randomize_graph_selection()
        print(f"Building {graph.model_name}")

        graph.randomize_floor_selection()
        graph.prioritize_starting_points(graph_size)

        graph.list_of_height = list(graph.get_height_no_duplicates())
        working_height_set = sorted(set(graph.list_of_height), reverse=True)

        current_floor = graph.current_floor
        for c_index in range(len(graph.starting_nodes)):
            amount_of_plots += 1
            graph.current_floor = current_floor  # todo put this somewhere else
            graph.starting_point = graph.starting_nodes[c_index].x, graph.starting_nodes[c_index].y, \
                                   graph.starting_nodes[c_index].z

            while exit_flag:
                print(f"starting point number {graph.starting_point}")
                print(f"***********************************************")
                if tries > 10:
                    break
                exit_flag = main(graph, ALGORITHM, graph_size)

                if not exit_flag:
                    print(f'Returned from floor {graph.current_floor} unsuccessfully')
                    print(f"***********************************************")
                    tries += 1
                    amount_of_plots += 1
                    exit_flag = True
                    continue
                else:
                    print(f'Returned successfully from floor {graph.current_floor}')
                    tries = 1
                    if c_index == len(graph.starting_nodes) - 1 or graph.current_floor > 0.0:
                        if not graph.list_of_height:
                            break
                        del graph.list_of_height[0]

                        if not graph.list_of_height:
                            break
                        graph.current_floor = graph.list_of_height[0]
                    else:
                        break

                if graph.current_floor < 0:
                    break
                else:
                    graph.starting_point = graph.goal_point[0], graph.goal_point[1] - (4.0 * graph_size), \
                                           graph.current_floor * graph_size
                    graph.total_min_time += graph.calc_height_distance()

            graph.list_of_height = list(working_height_set)
            print(f"Graph total distance is: {graph.total_min_time}")
            mapping_utility_methods.create_3d_graph(X, Y, Z)
            X, Y, Z = graph.clear_x_y_z_lists(X, Y, Z)
            graph.total_min_time = 0
        graph.starting_nodes.clear()
    average_of_run /= amount
    calculate_average_time(amount_of_plots)
    print(f"Finished Experiment on {ALGORITHM} algorithm. Average is: {average_of_run}")
    exit(0)
