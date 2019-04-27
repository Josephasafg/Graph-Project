import random
import yaml
import math


# test
class Graph:
    def __init__(self, yaml_file, model_name=None, floor_number=-1):
        current_file = open(yaml_file, 'r')
        self.coordinate = yaml.load(current_file, Loader=yaml.FullLoader)
        self.starting_point = tuple()
        self.goal_point = tuple()
        self.current_floor = floor_number
        self.total_min_time = 0
        self.model_name = model_name

    def randomize_start_points(self):
        amount_of_options = len(self.coordinate['Building'][self.model_name]['Floors'][str(self.current_floor)]['start_x'])
        result = random.randint(0, amount_of_options - 1)
        start_x = self.coordinate['Building'][self.model_name]['Floors'][str(self.current_floor)]['start_x'][result]
        start_y = self.coordinate['Building'][self.model_name]['Floors'][str(self.current_floor)]['start_y'][result]
        start_z = self.coordinate['Building'][self.model_name]['Floors'][str(self.current_floor)]['start_z'][result]
        del self.coordinate['Building'][self.model_name]['Floors'][str(self.current_floor)]['start_x'][result]
        del self.coordinate['Building'][self.model_name]['Floors'][str(self.current_floor)]['start_y'][result]
        del self.coordinate['Building'][self.model_name]['Floors'][str(self.current_floor)]['start_z'][result]
        self.starting_point = start_x, start_y, start_z

    def randomize_graph_selection(self):
        random_key = random.choice(list(self.coordinate['Building']))
        # del self.coordinate['Building'][random_key]
        self.model_name = random_key

    def delete_current_model(self):
        del self.coordinate['Building'][self.model_name]

    def randomize_floor_selection(self):
        floor_number = random.choice(list(self.coordinate['Building'][self.model_name]['Floors']))
        self.current_floor = int(floor_number)

    @staticmethod
    def clear_x_y_z_lists(x_list, y_list, z_list):
        x_list.clear()
        y_list.clear()
        z_list.clear()
        return x_list, y_list, z_list

    def calc_height_distance(self):
        height_distance_x = (self.goal_point[0] - self.starting_point[0])**2
        height_distance_y = (self.goal_point[1] - self.starting_point[1]) ** 2
        height_distance_z = (self.goal_point[2] - self.starting_point[2]) ** 2
        total_distance = math.sqrt(height_distance_x + height_distance_y + height_distance_z)
        return total_distance/400

    # def randomize_goal_points(self, floor_number):
    #     amount_of_options = len(self.coordinate['Building']['Floors'][str(floor_number)]['goal_x'])
    #     result = random.randint(0, amount_of_options - 1)
    #     goal_x = self.coordinate['Building']['Floors'][str(floor_number)]['goal_x'][result]
    #     goal_y = self.coordinate['Building']['Floors'][str(floor_number)]['goal_y'][result]
    #     del self.coordinate['Building']['Floors'][str(floor_number)]['goal_x'][result]
    #     del self.coordinate['Building']['Floors'][str(floor_number)]['goal_y'][result]
    #     self.goal_point = goal_x, goal_y

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
            distance_x = abs(self.starting_point[0] - x)**2
            distance_y = abs(self.starting_point[1] - y)**2
            square_result = math.sqrt(distance_x + distance_y)
            min_list.append((x, y, square_result))
        x, y = self.find_min_in_list(min_list)
        return x, y





