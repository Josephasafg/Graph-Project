import random
import yaml
import math
from Graph_Objects.Node import Node


class Graph:
    def __init__(self, yaml_file, model_name=None, floor_number=-1):
        current_file = open(yaml_file, 'r')
        self.__coordinate = yaml.load(current_file, Loader=yaml.FullLoader)
        self.__starting_point = Node()
        self.__goal_point = Node()
        self.__current_floor = floor_number
        self.__total_min_time = 0
        self.__starting_nodes = list()
        self.__model_name = model_name
        self.__list_of_height = list()

    @property
    def list_of_height(self):
        return self.__list_of_height

    @list_of_height.setter
    def list_of_height(self, value):
        self.__list_of_height = value

    @property
    def starting_nodes(self):
        return self.__starting_nodes

    @starting_nodes.setter
    def starting_nodes(self, value):
        self.__starting_nodes = value

    @property
    def total_min_time(self):
        return self.__total_min_time

    @total_min_time.setter
    def total_min_time(self, value):
        self.__total_min_time = value

    @property
    def starting_point(self):
        return self.__starting_point

    @starting_point.setter
    def starting_point(self, value):
        self.__starting_point = value

    @property
    def goal_point(self):
        return self.__goal_point

    @goal_point.setter
    def goal_point(self, value):
        self.__goal_point = value

    @property
    def coordinate(self):
        return self.__coordinate

    @property
    def current_floor(self):
        return self.__current_floor

    @current_floor.setter
    def current_floor(self, value):
        self.__current_floor = value

    @property
    def model_name(self):
        return self.__model_name

    @model_name.setter
    def model_name(self, value):
        self.__model_name = value

    def get_element_indexes(self, my_list, size):
        return filter(lambda a: my_list[a]*size == self.current_floor, range(0, len(my_list)))

    def get_height_no_duplicates(self, size):
        temp_list = list(set(self.coordinate['Building'][self.model_name]['Floors']['goal_z']))
        temp_list.sort(reverse=True)

        clean_list = [x * size for x in temp_list if not x * size > self.current_floor]
        return clean_list

    @staticmethod
    def minimum_from_fire(node, fire_list):
        distance_list = list()
        for fire in fire_list:
            distance_x = (fire.x - node.x) ** 2
            distance_y = (fire.y - node.y) ** 2
            distance_z = (fire.z - node.z) ** 2
            distance = math.sqrt(distance_x + distance_y + distance_z)
            distance_list.append(distance)
        return node, min(distance_list)

    def create_fire_node_list(self, dynamic_size):
        fire_list = list()
        for fire_index in range(len(self.coordinate['Building'][self.model_name]['FIRE']['start_x'])):
            fire_node = Node(self.coordinate['Building'][self.model_name]['FIRE']['start_x'][fire_index] * dynamic_size,
                             self.coordinate['Building'][self.model_name]['FIRE']['start_y'][fire_index] * dynamic_size)
            fire_node.z = self.coordinate['Building'][self.model_name]['FIRE']['start_z'][fire_index] * dynamic_size
            fire_list.append(fire_node)
        return fire_list

    @staticmethod
    def sort_and_extract_starting_nodes_from_tuple_list(list_of_tuple_distance):
        sorted_node_list = list()
        sorted_starting_list = sorted(list_of_tuple_distance, key=lambda tup: tup[1])
        for node in sorted_starting_list:
            sorted_node_list.append(node[0])

        return sorted_node_list

    def prioritize_by_fire(self, dynamic_size):
        fire_list = self.create_fire_node_list(dynamic_size)

        list_of_tuple_distance = list()
        for start_index in range(len(self.coordinate['Building'][self.model_name]['Floors']['start_x'])):
            node = Node(self.coordinate['Building'][self.model_name]['Floors']['start_x'][start_index] * dynamic_size,
                        self.coordinate['Building'][self.model_name]['Floors']['start_y'][start_index] * dynamic_size)
            node.z = self.coordinate['Building'][self.model_name]['Floors']['start_z'][start_index] * dynamic_size

            min_distance_node_tuple = self.minimum_from_fire(node, fire_list)  # type: tuple
            list_of_tuple_distance.append(min_distance_node_tuple)
        self.starting_nodes = self.sort_and_extract_starting_nodes_from_tuple_list(list_of_tuple_distance)

    def sort_starting_point(self):
        self.starting_nodes.sort(key=lambda current_point: current_point.priority, reverse=True)

    def randomize_graph_selection(self):
        random_key = random.choice(list(self.coordinate['Building']))
        self.model_name = random_key

    def delete_current_model(self):
        del self.coordinate['Building'][self.model_name]

    def randomize_floor_selection(self):
        floor_number = random.choice(list(self.coordinate['Building'][self.model_name]['Floors']['start_z']))
        self.current_floor = int(floor_number)

    @staticmethod
    def clear_x_y_z_lists(x_list, y_list, z_list):
        x_list.clear()
        y_list.clear()
        z_list.clear()
        return x_list, y_list, z_list

    def calc_height_distance(self):
        height_distance_x = (self.goal_point.x - self.starting_point.x)**2
        height_distance_y = (self.goal_point.y - self.starting_point.y) ** 2
        height_distance_z = (self.goal_point.z - self.starting_point.z) ** 2
        total_distance = math.sqrt(height_distance_x + height_distance_y + height_distance_z)
        return total_distance/250

    def get_lower_floor_height(self):
        if (not self.list_of_height) or (self.list_of_height[0] == 0):
            return_value = 0
        else:
            return_value = self.list_of_height[1]
        return return_value

    @staticmethod
    def find_min_in_list(minimum_list):
        min_value = minimum_list[0][2]
        x = minimum_list[0][0]
        y = minimum_list[0][1]
        for value in minimum_list:
            if value[2] < min_value:
                x = value[0]
                y = value[1]
                min_value = value[2]
        return x, y

    def choose_next_goal(self, floor_number):
        min_list = list()
        for x, y in zip(self.coordinate['Building'][self.model_name]['Floors'][str(floor_number)]['goal_x'],
                        self.coordinate['Building'][self.model_name]['Floors'][str(floor_number)]['goal_y']):
            distance_x = abs(self.starting_point.x - x)**2
            distance_y = abs(self.starting_point.y - y)**2
            square_result = math.sqrt(distance_x + distance_y)
            min_list.append((x, y, square_result))
        x, y = self.find_min_in_list(min_list)
        return x, y

    def get_prioritized_points(self, dynamic_size, algorithm):
        if algorithm == 'prm_a_star':
            self.prioritize_by_fire(dynamic_size)
        else:
            self.prioritize_starting_points(dynamic_size)

    def prioritize_starting_points(self, dynamic_size):
        amount_of_options = len(self.coordinate['Building'][self.model_name]['Floors']['start_x'])
        for index in range(amount_of_options):
            priority = random.randint(0, 1000)
            current_node = Node(self.coordinate['Building'][self.model_name]['Floors']['start_x'][index] * dynamic_size,
                                self.coordinate['Building'][self.model_name]['Floors']['start_y'][index] * dynamic_size)
            current_node.z = self.coordinate['Building'][self.model_name]['Floors']['start_z'][index] * dynamic_size
            current_node.priority = priority
            self.starting_nodes.append(current_node)
        self.sort_starting_point()

    """May need for future use"""
    # def prioritize_starting_points(self, dynamic_size):
    #     current_floor_list = self.coordinate['Building'][self.model_name]['Floors']['start_z']
    #     my_list_indexes = self.get_element_indexes(current_floor_list, dynamic_size)
    #     for index in my_list_indexes:
    #         priority = random.randint(0, 1000)
    #         current_node = Node(self.coordinate['Building'][self.model_name]['Floors']['start_x'][index] * dynamic_size,
    #                             self.coordinate['Building'][self.model_name]['Floors']['start_y'][index] * dynamic_size)
    #         current_node.z = self.coordinate['Building'][self.model_name]['Floors']['start_z'][index] * dynamic_size
    #         current_node.priority = priority
    #         self.starting_nodes.append(current_node)
    #     self.sort_starting_point()
