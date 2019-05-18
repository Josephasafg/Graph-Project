import math
import random
import numpy as np
import matplotlib.pyplot as plt
from Utilities.KDTree import KDTree
from Utilities import building_models
from mpl_toolkits.mplot3d import Axes3D

N_SAMPLE = 500
MAX_EDGE_LEN = 30.0
N_KNN = 10  # number of edge from one sampled point


def _get_building_model(model_name, floor_number=''):
    if model_name == 'OUTLINE_OBSTACLES_DEMO_BUILDING_1':
        return building_models.outline_obstacles_demo_building_1
    elif model_name == 'OUTLINE_OBSTACLES_DEMO_BUILDING_2':
        return building_models.outline_obstacles_demo_building_2
    elif model_name == 'OUTLINE_OBSTACLES_DEMO_BUILDING_3':
        return building_models.outline_obstacles_demo_building_3
    elif model_name == 'OUTLINE_OBSTACLES_DEMO_BUILDING_4':
        return building_models.outline_obstacles_demo_building_4
    elif model_name == 'OUTLINE_OBSTACLES_DEMO_BUILDING_5':
        return building_models.outline_obstacles_demo_building_5
    elif model_name == 'OUTLINE_OBSTACLES_DEMO_BUILDING_6':
        return building_models.outline_obstacles_demo_building_6
    elif model_name == 'OUTLINE_OBSTACLES_DEMO_BUILDING_7':
        return building_models.outline_obstacles_demo_building_7
    elif model_name == 'OUTLINE_OBSTACLES_DEMO_BUILDING_8':
        return building_models.outline_obstacles_demo_building_8
    elif model_name == 'OUTLINE_OBSTACLES_DEMO_BUILDING_9':
        return building_models.outline_obstacles_demo_building_9
    elif model_name == 'OUTLINE_OBSTACLES_DEMO_BUILDING_10':
        return building_models.outline_obstacles_demo_building_10
    elif model_name == 'BUILDING_8_HIT':
        return _get_floor_function_building_8_hit(floor_number)
    else:
        raise ValueError('This building does not exist here...')


def _get_floor_function_building_8_hit(i_floor_number):
    if i_floor_number == 0.0:
        return building_models.outline_obstacles_floor_one
    elif i_floor_number == 60.0:
        return building_models.outline_obstacles_floor_two_and_three
    elif i_floor_number == 120.0:
        return building_models.outline_obstacles_floor_two_and_three
    elif i_floor_number == 180.0:
        return building_models.outline_obstacles_floor_four
    else:
        raise ValueError(i_floor_number)


def find_min_time(time_list):
    return time_list.index(min(time_list)), min(time_list)


def create_3d_graph(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(x, y, z)
    ax.scatter(x, y, z, zdir='z', lw=2, c='r', marker='*')
    plt.show()


#   400 meters per minute = 24 KMH
def weight_on_sub_path(distance, average_speed=250.0):
    return distance / average_speed


def calc_heuristic(n1, n2):
    factored_weight = 1.0
    distance = factored_weight * math.sqrt((n1.x - n2.x)**2 + (n1.y - n2.y)**2)
    return distance


def is_collision(start_x, start_y, goal_x, goal_y, robot_radius, okdtree, random_graph_size):
    x = start_x
    y = start_y
    dx = goal_x - start_x
    dy = goal_y - start_y
    yaw = math.atan2(goal_y - start_y, goal_x - start_x)
    d = math.sqrt(dx**2 + dy**2)

    if d >= (MAX_EDGE_LEN * random_graph_size):
        return True

    D = robot_radius
    nstep = round(d / D)

    for i in range(nstep):
        idxs, dist = okdtree.search(np.array([x, y]).reshape(2, 1))
        if dist[0] <= robot_radius:
            return True  # collision
        x += D * math.cos(yaw)
        y += D * math.sin(yaw)

    # goal point check
    idxs, dist = okdtree.search(np.array([goal_x, goal_y]).reshape(2, 1))
    if dist[0] <= robot_radius:
        return True  # collision

    return False  # OK


def generate_roadmap(sample_x, sample_y, robot_radius, obkdtree, random_graph_size):
    """
    Road map generation
    sample_x: [m] x positions of sampled points
    sample_y: [m] y positions of sampled points
    robot_radius: Robot Radius[m]
    obkdtree: KDTree object of obstacles
    """

    road_map = []
    nsample = len(sample_x)
    skdtree = KDTree(np.vstack((sample_x, sample_y)).T)

    for (i, ix, iy) in zip(range(nsample), sample_x, sample_y):

        index, dists = skdtree.search(
            np.array([ix, iy]).reshape(2, 1), k=nsample)
        inds = index[0]
        edge_id = []

        for ii in range(1, len(inds)):
            nx = sample_x[inds[ii]]
            ny = sample_y[inds[ii]]

            if not is_collision(ix, iy, nx, ny, robot_radius, obkdtree, random_graph_size):
                edge_id.append(inds[ii])

            if len(edge_id) >= N_KNN:
                break

        road_map.append(edge_id)

    return road_map


def plot_road_map(road_map, sample_x, sample_y):  # pragma: no cover

    for i, _ in enumerate(road_map):
        for ii in range(len(road_map[i])):
            ind = road_map[i][ii]

            plt.plot([sample_x[i], sample_x[ind]],
                     [sample_y[i], sample_y[ind]], "-k")


def sample_points(start_tuple, goal_tuple, robot_radius, obstacle_x, obstacle_y, obkdtree, random_graph_size):
    max_x = max(obstacle_x)
    max_y = max(obstacle_y)
    min_x = min(obstacle_x)
    min_y = min(obstacle_y)
    sample_x, sample_y = list(), list()

    while len(sample_x) <= (N_SAMPLE * random_graph_size):
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
