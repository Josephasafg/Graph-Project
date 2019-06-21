import math
from numpy import arange


def outline_obstacles_demo_building_1(obstacle_x, obstacle_y, dynamic_size):
    #  outline of room
    for i in arange(0, 60 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(60 * dynamic_size):
        obstacle_x.append(60.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(61 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * dynamic_size)
    for i in arange(61 * dynamic_size):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    # outline obstacle top left
    for i in arange(0, 6 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(40 * dynamic_size, 60 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(6 * dynamic_size)

    # outline exit/enter 1
    for i in arange(6 * dynamic_size, 10 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(4 * dynamic_size)
    for i in arange(6 * dynamic_size, 10 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(8 * dynamic_size)
    for i in arange(4 * dynamic_size, 8 * dynamic_size):
        obstacle_y.append(6 * dynamic_size)
        obstacle_x.append(i)

    # outline obst
    for i in arange(11 * dynamic_size, 17 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(22 * dynamic_size)
    for i in arange(0 * dynamic_size, 22 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(11 * dynamic_size)
    for i in arange(0 * dynamic_size, 22 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(16 * dynamic_size)

    # outline obst
    for i in arange(30 * dynamic_size, 45 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(40 * dynamic_size, 60 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(30 * dynamic_size)
    for i in arange(40 * dynamic_size, 60 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(45 * dynamic_size)

    # outline obst
    for i in arange(40 * dynamic_size, 60 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(20 * dynamic_size)
    for i in arange(0, 20 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(40 * dynamic_size)

    # outline exit/enter 2
    for i in arange(30 * dynamic_size, 35 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(40 * dynamic_size)
    for i in arange(40 * dynamic_size, 43 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(30 * dynamic_size)
    for i in arange(40 * dynamic_size, 43 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(35 * dynamic_size)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_2(obstacle_x, obstacle_y, dynamic_size):
    #  outline of room
    for i in arange(0, 60 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(0, 60 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(0.0)
    for i in arange(0, 31 * dynamic_size):
        obstacle_x.append(60.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 41 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * dynamic_size)
    for i in arange(40 * dynamic_size, 60 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(30 * dynamic_size)
    for i in arange(30 * dynamic_size, 60 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(40 * dynamic_size)

    # outline obstacle top left
    for i in arange(0, 12 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(50 * dynamic_size)
    for i in arange(0, 12 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(40 * dynamic_size, 51 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(12 * dynamic_size)

    # outline obstacle center left
    for i in arange(0, 7 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(13 * dynamic_size)
    for i in arange(13 * dynamic_size, 25 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(7 * dynamic_size)
    for i in arange(30 * dynamic_size, 41 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(7 * dynamic_size)

    # outline bottom left
    for i in arange(0, 17 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(13 * dynamic_size)
    for i in arange(7 * dynamic_size, 14 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(17 * dynamic_size)
    for i in arange(0, 4 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(17 * dynamic_size)

    # outline middle top
    for i in arange(30 * dynamic_size, 34 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(25 * dynamic_size)
    for i in arange(30 * dynamic_size, 35 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(28 * dynamic_size)
    for i in arange(25 * dynamic_size, 28 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(30 * dynamic_size)
    for i in arange(25 * dynamic_size, 28 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(34 * dynamic_size)

    # outline middle bottom
    j = 5
    for i in arange((30 - j) * dynamic_size, (34 - j) * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append((25 - j) * dynamic_size)
    for i in arange((30 - j) * dynamic_size, (35 - j) * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append((28 - j) * dynamic_size)
    for i in arange((25 - j) * dynamic_size, (28 - j) * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append((30 - j) * dynamic_size)
    for i in arange((25 - j) * dynamic_size, (28 - j) * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append((34 - j) * dynamic_size)

    # outline exit/enter 1
    for i in arange(54 * dynamic_size, 58 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(17 * dynamic_size)
    for i in arange(54 * dynamic_size, 58 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(13 * dynamic_size)
    for i in arange(13 * dynamic_size, 17 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(57 * dynamic_size)

    # outline obst next to exit on top
    for i in arange(30 * dynamic_size, 40 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(40 * dynamic_size, 60 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(30 * dynamic_size)

    # outline obst above bottom right
    for i in arange(42 * dynamic_size, 56 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(22 * dynamic_size)
    for i in arange(22 * dynamic_size, 30 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(42 * dynamic_size)
    for i in arange(22 * dynamic_size, 30 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(55 * dynamic_size)

    # outline obst bototm right
    for i in arange(42 * dynamic_size, 56 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(8 * dynamic_size)
    for i in arange(0, 8 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(42 * dynamic_size)
    for i in arange(0, 8 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(55 * dynamic_size)

    # outline exit/enter 2 top
    for i in arange(52 * dynamic_size, 56 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(27 * dynamic_size)
    for i in arange(52 * dynamic_size, 56 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(24 * dynamic_size)
    for i in arange(24 * dynamic_size, 28 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(52 * dynamic_size)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_3(obstacle_x, obstacle_y, dynamic_size):
    #  outline of room
    for i in arange(0, 20 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(40 * dynamic_size, 60 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(60 * dynamic_size):
        obstacle_x.append(60.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(61 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * dynamic_size)
    for i in arange(61 * dynamic_size):
        obstacle_x.append(0.0)
        obstacle_y.append(i)
    for i in arange(0, 30 * dynamic_size):
        obstacle_x.append(20 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 30 * dynamic_size):
        obstacle_x.append(40 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(20 * dynamic_size, 41 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(30 * dynamic_size)

    # outline obstacle middle bottom 1
    for i in arange(20 * dynamic_size, 26 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(30 * dynamic_size, 40 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(20 * dynamic_size)
    for i in arange(30 * dynamic_size, 40 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(25 * dynamic_size)

    # outline obstacle middle bottom 2
    for i in arange(35 * dynamic_size, 41 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(30 * dynamic_size, 40 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(35 * dynamic_size)
    for i in arange(30 * dynamic_size, 40 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(40 * dynamic_size)

    # outline obstacle middle top 1
    for i in arange(20 * dynamic_size, 26 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(50 * dynamic_size)
    for i in arange(50 * dynamic_size, 60 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(20 * dynamic_size)
    for i in arange(50 * dynamic_size, 60 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(25 * dynamic_size)

    # outline obstacle middle top 2
    for i in arange(35 * dynamic_size, 41 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(50 * dynamic_size)
    for i in arange(50 * dynamic_size, 60 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(35 * dynamic_size)
    for i in arange(50 * dynamic_size, 60 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(40 * dynamic_size)

    # outline obstacle top left
    for i in arange(0, 6 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(40 * dynamic_size, 60 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(6 * dynamic_size)

    # outline exit/enter 1
    for i in arange(6 * dynamic_size, 10 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(11 * dynamic_size)
    for i in arange(6 * dynamic_size, 10 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(16 * dynamic_size)
    for i in arange(11 * dynamic_size, 17 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(6 * dynamic_size)

    # outline exit/enter 2
    for i in arange(6 * dynamic_size, 10 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(49 * dynamic_size)
    for i in arange(6 * dynamic_size, 10 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(54 * dynamic_size)
    for i in arange(49 * dynamic_size, 54 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(6 * dynamic_size)

    # outline middle left
    for i in arange(0, 7 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(30 * dynamic_size)
    for i in arange(0, 7 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(10 * dynamic_size)
    for i in arange(10 * dynamic_size, 22 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(7 * dynamic_size)
    for i in arange(26 * dynamic_size, 31 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(7 * dynamic_size)

    # outline obst top right
    for i in arange(53 * dynamic_size, 60 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(30 * dynamic_size)
    for i in arange(30 * dynamic_size, 41 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(53 * dynamic_size)
    for i in arange(46 * dynamic_size, 60 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(53 * dynamic_size)

    #   outline obst top left
    for i in arange(40 * dynamic_size, 45 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(30 * dynamic_size)
    for i in arange(40 * dynamic_size, 44 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(10 * dynamic_size)
    for i in arange(10 * dynamic_size, 30 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(44 * dynamic_size)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_4(obstacle_x, obstacle_y, dynamic_size):
    #  outline of room
    for i in arange(0, 20 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(40 * dynamic_size, 60 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(60 * dynamic_size):
        obstacle_x.append(60.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 21 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * dynamic_size)
    for i in arange(40 * dynamic_size, 61 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * dynamic_size)
    for i in arange(40 * dynamic_size, 60 * dynamic_size):
        obstacle_x.append(20 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(40 * dynamic_size, 60 * dynamic_size):
        obstacle_x.append(40 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(20 * dynamic_size, 41 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(61 * dynamic_size):
        obstacle_x.append(0.0)
        obstacle_y.append(i)
    for i in arange(0 * dynamic_size, 20 * dynamic_size):
        obstacle_x.append(20 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 20 * dynamic_size):
        obstacle_x.append(40 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(20 * dynamic_size, 41 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(20 * dynamic_size)

    # outline obstacle middle bottom
    for i in arange(28 * dynamic_size, 33 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(34 * dynamic_size)
    for i in arange(34 * dynamic_size, 41 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(28 * dynamic_size)
    for i in arange(34 * dynamic_size, 41 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(33 * dynamic_size)

    # outline obstacle middle top
    for i in arange(28 * dynamic_size, 33 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(28 * dynamic_size)
    for i in arange(20 * dynamic_size, 29 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(28 * dynamic_size)
    for i in arange(20 * dynamic_size, 29 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(33 * dynamic_size)

    # outline obstacle top left
    for i in arange(0, 9 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(14 * dynamic_size, 21 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)

    # outline obstacle bottom right
    for i in arange(40 * dynamic_size, 49 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(20 * dynamic_size)
    for i in arange(53 * dynamic_size, 61 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(20 * dynamic_size)

    # outline exit/enter 1
    for i in arange(5 * dynamic_size, 9 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(11 * dynamic_size)
    for i in arange(5 * dynamic_size, 9 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(16 * dynamic_size)
    for i in arange(11 * dynamic_size, 17 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(5 * dynamic_size)

    # outline exit/enter 2
    for i in arange(54 * dynamic_size, 58 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(47 * dynamic_size)
    for i in arange(54 * dynamic_size, 58 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(51 * dynamic_size)
    for i in arange(54 * dynamic_size, 58 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(51 * dynamic_size)

    # outline middle left
    for i in arange(0, 7 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(30 * dynamic_size)
    for i in arange(0, 7 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(10 * dynamic_size)
    for i in arange(47 * dynamic_size, 52 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(58 * dynamic_size)

    # outline obst top right
    for i in arange(53 * dynamic_size, 60 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(30 * dynamic_size)
    for i in arange(30 * dynamic_size, 60 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(53 * dynamic_size)

    # outline obst top right small
    for i in arange(40 * dynamic_size, 45 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(57 * dynamic_size)
    for i in arange(40 * dynamic_size, 45 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(42 * dynamic_size)
    for i in arange(42 * dynamic_size, 58 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(44 * dynamic_size)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_5(obstacle_x, obstacle_y, dynamic_size):
    #  outline of room
    for i in arange(0, 60 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * dynamic_size)
    for i in arange(30 * dynamic_size, 61 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(60.0 * dynamic_size)
    for i in arange(30 * dynamic_size, 61 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(0.0)
    for i in arange(0, 21 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(30.0 * dynamic_size)
    for i in arange(40 * dynamic_size, 61 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(30.0 * dynamic_size)
    for i in arange(0, 31 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(20.0 * dynamic_size)
    for i in arange(0, 31 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(40.0 * dynamic_size)
    for i in arange(20 * dynamic_size, 41 * dynamic_size):
        obstacle_y.append(0)
        obstacle_x.append(i)

    # outline obstacle top left
    for i in arange(0, 12 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(50 * dynamic_size)
    for i in arange(0, 12 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(40 * dynamic_size, 51 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(12 * dynamic_size)

    # outline obstacle right
    for i in arange(45 * dynamic_size, 49 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(53 * dynamic_size, 56 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(30 * dynamic_size, 41 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(45 * dynamic_size)
    for i in arange(30 * dynamic_size, 41 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(56 * dynamic_size)

    # outline middle top
    for i in arange(30 * dynamic_size, 34 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(25 * dynamic_size)
    for i in arange(30 * dynamic_size, 35 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(28 * dynamic_size)
    for i in arange(25 * dynamic_size, 28 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(30 * dynamic_size)
    for i in arange(25 * dynamic_size, 28 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(34 * dynamic_size)

    # outline middle bottom
    for i in arange(30 * dynamic_size, 41 * dynamic_size):
        obstacle_y.append(20 * dynamic_size)
        obstacle_x.append(i)
    for i in arange(30 * dynamic_size, 41 * dynamic_size):
        obstacle_y.append(10 * dynamic_size)
        obstacle_x.append(i)
    for i in arange(10 * dynamic_size, 21 * dynamic_size):
        obstacle_x.append(30 * dynamic_size)
        obstacle_y.append(i)

    # outline exit/enter 1
    for i in arange(3 * dynamic_size, 6 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(23 * dynamic_size)
    for i in arange(3 * dynamic_size, 6 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(27 * dynamic_size)
    for i in arange(23 * dynamic_size, 28 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(2 * dynamic_size)

    # outline obst next to exit on top
    for i in arange(20 * dynamic_size, 30 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(34 * dynamic_size, 41 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(40 * dynamic_size, 61 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(20 * dynamic_size)
    for i in arange(40 * dynamic_size, 61 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(40 * dynamic_size)

    # outline exit/enter2 top
    for i in arange(55 * dynamic_size, 58 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(53 * dynamic_size)
    for i in arange(55 * dynamic_size, 58 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(58 * dynamic_size)
    for i in arange(53 * dynamic_size, 59 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(58 * dynamic_size)

    # outline exit/enter 3 top left
    for i in arange(2 * dynamic_size, 5 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(53 * dynamic_size)
    for i in arange(2 * dynamic_size, 5 * dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(57 * dynamic_size)
    for i in arange(53 * dynamic_size, 58 * dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(2 * dynamic_size)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_6(obstacle_x, obstacle_y, dynamic_size):
    #  outline of room
    for i in arange(0, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(0, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(30.0 * dynamic_size)
    for i in arange(0, 31 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(60.0 * dynamic_size)
    for i in arange(0, 31 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(0.0)

    # outline obstacle top left
    for i in arange(0, 9 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(20 * dynamic_size)
    for i in arange(0, 12 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(10 * dynamic_size)
    for i in arange(10 * dynamic_size, 21 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(9 * dynamic_size)

    # outline obstacle left bottom
    for i in arange(15 * dynamic_size, 19 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(10 * dynamic_size)
    for i in arange(21 * dynamic_size, 26 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(10 * dynamic_size)
    for i in arange(0, 11 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(15 * dynamic_size)
    for i in arange(0, 11 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(26 * dynamic_size)

    # outline bottom
    for i in arange(0, 4 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(30 * dynamic_size)
    for i in arange(0, 5 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(34 * dynamic_size)
    for i in arange(30 * dynamic_size, 34 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(0)
    for i in arange(30 * dynamic_size, 34 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(4 * dynamic_size)

    # outline top left
    for i in arange(45 * dynamic_size, 61 * dynamic_size, dynamic_size):
        obstacle_y.append(26 * dynamic_size)
        obstacle_x.append(i)

    # outline completing top left
    for i in arange(16 * dynamic_size, 27 * dynamic_size, dynamic_size):
        obstacle_x.append(45 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(40 * dynamic_size, 46 * dynamic_size, dynamic_size):
        obstacle_y.append(16 * dynamic_size)
        obstacle_x.append(i)

    # outline obst bottom right
    for i in arange(0, 11 * dynamic_size, dynamic_size):
        obstacle_x.append(40 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(40 * dynamic_size, 45 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(10 * dynamic_size)
    for i in arange(48 * dynamic_size, 61 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(10 * dynamic_size)

    # outline obst next to exit on top
    for i in arange(20 * dynamic_size, 30 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(16 * dynamic_size)
    for i in arange(34 * dynamic_size, 41 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(16 * dynamic_size)
    for i in arange(16 * dynamic_size, 31 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(20 * dynamic_size)
    for i in arange(16 * dynamic_size, 31 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(40 * dynamic_size)

    # outline exit/enter 2 top
    for i in arange(54 * dynamic_size, 58 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(21 * dynamic_size)
    for i in arange(54 * dynamic_size, 58 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(17 * dynamic_size)
    for i in arange(17 * dynamic_size, 22 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(58 * dynamic_size)

    # outline exit/enter 1 top left
    for i in arange(2 * dynamic_size, 6 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(24 * dynamic_size)
    for i in arange(2 * dynamic_size, 6 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(28 * dynamic_size)
    for i in arange(24 * dynamic_size, 28 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(2 * dynamic_size)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_7(obstacle_x, obstacle_y, dynamic_size):
    #  outline of room
    for i in arange(0, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(0, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(60.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 61 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * dynamic_size)
    for i in arange(0, 61 * dynamic_size, dynamic_size):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    # outline obstacle triangle left
    j = 0
    # outline obst triangle right
    for i in arange(40 * dynamic_size, 61 * dynamic_size, dynamic_size):
        obstacle_x.append((j+1) * dynamic_size)
        obstacle_y.append(i)
        j += (1 * dynamic_size)

    # outline exit/enter 1
    for i in arange(3 * dynamic_size, 6 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(4 * dynamic_size)
    for i in arange(3 * dynamic_size, 6 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(8 * dynamic_size)
    for i in arange(4 * dynamic_size, 9 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(2 * dynamic_size)

    # outline obst around x=10
    for i in arange(11 * dynamic_size, 17 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(22 * dynamic_size)
    for i in arange(0, 22 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(11 * dynamic_size)
    for i in arange(0, 22 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(16 * dynamic_size)

    # outline obst around x=30
    for i in arange(30 * dynamic_size, 34 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(22 * dynamic_size)
    for i in arange(37 * dynamic_size, 41 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(22 * dynamic_size)
    for i in arange(0, 22 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(30 * dynamic_size)
    for i in arange(0, 22 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(40 * dynamic_size)

    j = 61 * dynamic_size
    # outline obst triangle right
    for i in arange(50 * dynamic_size, j, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(j - (1 * dynamic_size))
        j -= (1 * dynamic_size)

    # outline obst rectangle in the middle
    for i in arange(30 * dynamic_size, 40 * dynamic_size, dynamic_size):
        obstacle_x.append(20 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(30 * dynamic_size, 40 * dynamic_size, dynamic_size):
        obstacle_x.append(25 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(20 * dynamic_size, 26 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(30 * dynamic_size)
    for i in arange(20 * dynamic_size, 26 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)

    # outline obst around x = 0
    for i in arange(30 * dynamic_size, 33 * dynamic_size, dynamic_size):
        obstacle_x.append(10 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(36 * dynamic_size, 40 * dynamic_size, dynamic_size):
        obstacle_x.append(10 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 11 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(30 * dynamic_size)
    for i in arange(0, 11 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)

    # outline obst
    for i in arange(30 * dynamic_size, 45 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(40 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(30 * dynamic_size)
    for i in arange(40 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(45 * dynamic_size)

    # outline obst
    for i in arange(40 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(20 * dynamic_size)
    for i in arange(0, 20 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(40 * dynamic_size)

    # outline exit/enter 2
    for i in arange(54 * dynamic_size, 57 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(42 * dynamic_size)
    for i in arange(54 * dynamic_size, 57 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(37 * dynamic_size)
    for i in arange(37 * dynamic_size, 43 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(57 * dynamic_size)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_8(obstacle_x, obstacle_y, dynamic_size):
    #  outline of room
    for i in arange(20 * dynamic_size, 40 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(21 * dynamic_size, 40 * dynamic_size, dynamic_size):
        obstacle_x.append(60.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(21 * dynamic_size,40 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * dynamic_size)
    for i in arange(20 * dynamic_size,40 * dynamic_size, dynamic_size):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    j = 0
    for i in arange(40 * dynamic_size, 61 * dynamic_size, dynamic_size):
        obstacle_x.append(j + (1 * dynamic_size))
        obstacle_y.append(i)
        j += (1 * dynamic_size)

    j = 61 * dynamic_size
    for i in arange(40 * dynamic_size, j, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(j - (1 * dynamic_size))
        j -= (1 * dynamic_size)

    j = 0
    for i in arange(40 * dynamic_size, 61 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(j + (1 * dynamic_size))
        j += (1 * dynamic_size)

    j = 20 * dynamic_size
    for i in arange(0, j, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(j - (1 * dynamic_size))
        j -= (1 * dynamic_size)

    # outline exit/enter 1
    for i in arange(2 * dynamic_size, 6 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(20 * dynamic_size)
    for i in arange(2 * dynamic_size, 6 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(25 * dynamic_size)
    for i in arange(20 * dynamic_size, 26 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(2 * dynamic_size)

    # outline obst around x=10
    for i in arange(11 * dynamic_size, 17 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(22 * dynamic_size)
    for i in arange(9 * dynamic_size, 22 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(11 * dynamic_size)
    for i in arange(3 * dynamic_size, 22 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(16 * dynamic_size)

    # outline obst around x=30
    for i in arange(30 * dynamic_size, 34 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(22 * dynamic_size)
    for i in arange(37 * dynamic_size, 41 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(22 * dynamic_size)
    for i in arange(0, 22 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(30 * dynamic_size)
    for i in arange(0, 22 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(40 * dynamic_size)

    # outline obst rectangle in the middle
    for i in arange(25 * dynamic_size, 40 * dynamic_size, dynamic_size):
        obstacle_x.append(20 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(25 * dynamic_size, 40 * dynamic_size, dynamic_size):
        obstacle_x.append(25 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(20 * dynamic_size, 26 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(25 * dynamic_size)
    for i in arange(20 * dynamic_size, 26 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)

    # outline obst around x = 0
    for i in arange(30 * dynamic_size, 33 * dynamic_size, dynamic_size):
        obstacle_x.append(10 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(37 * dynamic_size, 40 * dynamic_size, dynamic_size):
        obstacle_x.append(10 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 11 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(30 * dynamic_size)
    for i in arange(0, 11 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)

    # outline obst
    for i in arange(30 * dynamic_size, 45 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(40 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(30 * dynamic_size)
    for i in arange(40 * dynamic_size, 55 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(45 * dynamic_size)

    # outline obst
    for i in arange(40 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(20 * dynamic_size)
    for i in arange(0, 20 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(40 * dynamic_size)

    # outline exit/enter 2
    for i in arange(55 * dynamic_size, 59 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(39 * dynamic_size)
    for i in arange(55 * dynamic_size, 59 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(34 * dynamic_size)
    for i in arange(34 * dynamic_size, 39 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(58 * dynamic_size)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_9(obstacle_x, obstacle_y, dynamic_size):
    #  outline of room
    for i in arange(30 * dynamic_size, 61 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(0, 61 * dynamic_size, dynamic_size):
        obstacle_x.append(60.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(30 * dynamic_size, 61 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * dynamic_size)

    j = 0.0
    for i in arange(30 * dynamic_size, 61 * dynamic_size, dynamic_size):
        obstacle_x.append(j+(1 * dynamic_size))
        obstacle_y.append(i)
        j = j + (1 * dynamic_size)

    j = 30 * dynamic_size
    for i in arange(0, j, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(j- (1 * dynamic_size))
        j -= (1 * dynamic_size)

    # outline exit/enter 1
    for i in arange(9 * dynamic_size, 13 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(22 * dynamic_size)
    for i in arange(9 * dynamic_size, 13 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(26 * dynamic_size)
    for i in arange(22 * dynamic_size, 27 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(8 * dynamic_size)

    # outline obst around x=10
    for i in arange(11 * dynamic_size, 17 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(22 * dynamic_size)
    for i in arange(18 * dynamic_size, 22 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(11 * dynamic_size)
    for i in arange(13 * dynamic_size, 22 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(16 * dynamic_size)

    # outline obst around x=30
    for i in arange(30 * dynamic_size, 34 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(22 * dynamic_size)
    for i in arange(37 * dynamic_size, 41 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(22 * dynamic_size)
    for i in arange(0, 22 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(30 * dynamic_size)
    for i in arange(0, 22 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(40 * dynamic_size)

    # outline obst rectangle in the middle
    for i in arange(25 * dynamic_size, 40 * dynamic_size, dynamic_size):
        obstacle_x.append(20 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(25 * dynamic_size, 40 * dynamic_size, dynamic_size):
        obstacle_x.append(25 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(20 * dynamic_size, 26 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(25 * dynamic_size)
    for i in arange(20 * dynamic_size, 26 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)

    # outline obst
    for i in arange(30 * dynamic_size, 34 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(37 * dynamic_size, 45 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)

    for i in arange(40 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(30 * dynamic_size)
    for i in arange(40 * dynamic_size, 45 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(45 * dynamic_size)
    for i in arange(49 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(45 * dynamic_size)

    # outline obst
    for i in arange(40 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(20 * dynamic_size)
    for i in arange(0, 20 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(40 * dynamic_size)

    # outline exit/enter 2
    for i in arange(55 * dynamic_size, 59 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(55 * dynamic_size, 59 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(35 * dynamic_size)
    for i in arange(35 * dynamic_size, 41 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(58 * dynamic_size)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_10(obstacle_x, obstacle_y, dynamic_size):
    #  outline of room
    for i in arange(0, 40 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(21 * dynamic_size, 61 * dynamic_size, dynamic_size):
        obstacle_x.append(60.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(21 * dynamic_size, 61 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * dynamic_size)
    for i in arange(0, 41 * dynamic_size, dynamic_size):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    j = 0 * dynamic_size
    for i in arange(40 * dynamic_size, 61 * dynamic_size, dynamic_size):
        obstacle_x.append(j+1)
        obstacle_y.append(i)
        j += 1 * dynamic_size

    j = 0 * dynamic_size
    for i in arange(40 * dynamic_size, 61 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(j+1)
        j += 1 * dynamic_size

    # outline exit/enter 1
    for i in arange(3 * dynamic_size, 6 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(20 * dynamic_size)
    for i in arange(3 * dynamic_size, 6 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(24 * dynamic_size)
    for i in arange(20 * dynamic_size, 25 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(2 * dynamic_size)

    # outline obst around x=10
    for i in arange(0, 17 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(22 * dynamic_size)
    for i in arange(0, 17 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(10 * dynamic_size)
    for i in arange(10 * dynamic_size, 22 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(16 * dynamic_size)

    # outline obst around x=30
    for i in arange(30 * dynamic_size, 34 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(22 * dynamic_size)
    for i in arange(37 * dynamic_size, 41 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(22 * dynamic_size)
    for i in arange(0, 22 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(30 * dynamic_size)
    for i in arange(0, 22 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(40 * dynamic_size)

    # outline obst rectangle in the middle
    for i in arange(25 * dynamic_size, 40 * dynamic_size, dynamic_size):
        obstacle_x.append(20 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(25 * dynamic_size, 40 * dynamic_size, dynamic_size):
        obstacle_x.append(25 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(20 * dynamic_size, 26 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(25 * dynamic_size)
    for i in arange(20 * dynamic_size, 26 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)

    # outline obst around x = 0
    for i in arange(30 * dynamic_size, 33 * dynamic_size, dynamic_size):
        obstacle_x.append(10 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(36 * dynamic_size, 40 * dynamic_size, dynamic_size):
        obstacle_x.append(10 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 11 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(30 * dynamic_size)
    for i in arange(0, 11 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)

    # outline obst
    for i in arange(30 * dynamic_size, 36 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(39 * dynamic_size, 45 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40 * dynamic_size)
    for i in arange(40 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(30 * dynamic_size)
    for i in arange(40 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(45 * dynamic_size)

    # outline obst
    for i in arange(40 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(20 * dynamic_size)
    for i in arange(0, 20 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(40 * dynamic_size)

    # outline obst
    for i in arange(55 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(25 * dynamic_size)
    for i in arange(55 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(35 * dynamic_size)
    for i in arange(25 * dynamic_size, 29 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(55 * dynamic_size)
    for i in arange(32 * dynamic_size, 36 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(55 * dynamic_size)

    # outline exit/enter 2
    for i in arange(55 * dynamic_size, 58 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(50 * dynamic_size)
    for i in arange(55 * dynamic_size, 58 * dynamic_size, dynamic_size):
        obstacle_y.append(i)
        obstacle_x.append(55 * dynamic_size)
    for i in arange(50 * dynamic_size, 56 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(58 * dynamic_size)

    return obstacle_x, obstacle_y


def outline_obstacles_floor_one_other(obstacle_x, obstacle_y, dynamic_size):
    #   Room outline
    for i in arange(15):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(21, 60):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(45):
        obstacle_x.append(60.0)
        obstacle_y.append(i)
    for i in arange(50, 60):
        obstacle_x.append(60.0)
        obstacle_y.append(i)
    for i in arange(61):
        obstacle_x.append(i)
        obstacle_y.append(60.0)
    for i in arange(61):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    # left class
    for i in arange(10, 30):
        obstacle_x.append(10.0)
        obstacle_y.append(i)
    for i in arange(11):
        obstacle_x.append(i)
        obstacle_y.append(10.0)
    for i in arange(11):
        obstacle_x.append(i)
        obstacle_y.append(30)

    ##
    # top left class
    for i in arange(11):
        obstacle_x.append(i)
        obstacle_y.append(45.0)
    for i in arange(45, 60):
        obstacle_x.append(10.0)
        obstacle_y.append(i)

    # toilet near top left class
    for i in arange(11, 16):
        obstacle_x.append(i)
        obstacle_y.append(50.0)
    for i in arange(50, 60):
        obstacle_x.append(15)
        obstacle_y.append(i)
    # elevator
    for i in arange(25, 36):
        obstacle_x.append(i)
        obstacle_y.append(58.0)
    for i in arange(3):
        obstacle_x.append(25)
        obstacle_y.append(60 - i)
    for i in arange(3):
        obstacle_x.append(35)
        obstacle_y.append(60 - i)

    # top right stairs
    for i in arange(45, 51):
        obstacle_x.append(i)
        obstacle_y.append(58.0)
    for i in arange(3):
        obstacle_x.append(45)
        obstacle_y.append(60 - i)
    for i in arange(3):
        obstacle_x.append(50)
        obstacle_y.append(60 - i)

    # top right class
    for i in arange(51, 60):
        obstacle_x.append(i)
        obstacle_y.append(55.0)
    for i in arange(6):
        obstacle_x.append(51)
        obstacle_y.append(60 - i)
    for i in arange(6):
        obstacle_x.append(60)
        obstacle_y.append(60 - i)

    # end of building in right corner
    for i in arange(50, 60):
        obstacle_x.append(i)
        obstacle_y.append(10)
    for i in arange(11):
        obstacle_x.append(50)
        obstacle_y.append(i)

    # stairs + class right side of building
    for i in arange(50, 60):
        obstacle_x.append(i)
        obstacle_y.append(20.0)
    for i in arange(20, 40):
        obstacle_x.append(50.0)
        obstacle_y.append(i)
    for i in arange(50, 60):
        obstacle_x.append(i)
        obstacle_y.append(40.0)

    # obstacles near class
    for i in arange(45, 50):
        obstacle_x.append(i)
        obstacle_y.append(20.0)
    for i in arange(20, 30):
        obstacle_x.append(45.0)
        obstacle_y.append(i)
    for i in arange(45, 50):
        obstacle_x.append(i)
        obstacle_y.append(30.0)

    return obstacle_x, obstacle_y


def outline_obstacles_floor_one(obstacle_x, obstacle_y, dynamic_size):
    # Room outline
    for i in arange(0, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(0, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(60.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 35 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * dynamic_size)
    for i in arange(45 * dynamic_size, 61 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * dynamic_size)

    for i in arange(0, 10 * dynamic_size, dynamic_size):
        obstacle_x.append(0)
        obstacle_y.append(i)
    for i in arange(18 * dynamic_size, 61 * dynamic_size, dynamic_size):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    # bottom left class
    for i in arange(0, 11 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(8.0 * dynamic_size)
    for i in arange(0, 7 * dynamic_size, dynamic_size):
        obstacle_x.append(10.0 * dynamic_size)
        obstacle_y.append(i)

    # stairs bottom left
    for i in arange(16 * dynamic_size, 21 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(6 * dynamic_size)
    for i in arange(6 * dynamic_size, 10 * dynamic_size, dynamic_size):
        obstacle_x.append(16 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(6 * dynamic_size, 10 * dynamic_size, dynamic_size):
        obstacle_x.append(21 * dynamic_size)
        obstacle_y.append(i)

    for i in arange(25 * dynamic_size, 35 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(3.0 * dynamic_size)
    for i in arange(0, 4 * dynamic_size, dynamic_size):
        obstacle_x.append(25 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 4 * dynamic_size, dynamic_size):
        obstacle_x.append(34 * dynamic_size)
        obstacle_y.append(i)

    # bottom right class
    for i in arange(50 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(10.0 * dynamic_size)
    for i in arange(0, 7 * dynamic_size, dynamic_size):
        obstacle_x.append(50.0 * dynamic_size)
        obstacle_y.append(i)

    # toilet near bottom right class
    # for i in arange(47, 50):
    #     obstacle_x.append(i)
    #     obstacle_y.append(7)
    for i in arange(0, 8 * dynamic_size, dynamic_size):
        obstacle_x.append(47 * dynamic_size)
        obstacle_y.append(i)

    # mid left class
    for i in arange(0, 10 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(40.0 * dynamic_size)
    for i in arange(0, 10 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(55.0 * dynamic_size)
    for i in arange(40 * dynamic_size, 52 * dynamic_size, dynamic_size):
        obstacle_x.append(10 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 10 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(48 * dynamic_size)

    # # top left stairs
        # middle stairs
    for i in arange(25 * dynamic_size, 35 * dynamic_size, dynamic_size):
        obstacle_x.append(10.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(25 * dynamic_size, 35 * dynamic_size, dynamic_size):
        obstacle_x.append(16.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(10 * dynamic_size, 16 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(25.0 * dynamic_size)
    # for i in arange(20, 33):
    #     obstacle_x.append(20.0)
    #     obstacle_y.append(i)
    # for i in arange(20, 25):
    #     obstacle_x.append(i)
    #     obstacle_y.append(20)
    # for i in arange(20, 33):
    #     obstacle_x.append(25)
    #     obstacle_y.append(i)

    # right class
    for i in arange(25 * dynamic_size, 45 * dynamic_size, dynamic_size):
        obstacle_x.append(50 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 11 * dynamic_size, dynamic_size):
        obstacle_x.append((60 - i) * dynamic_size)
        obstacle_y.append(25.0 * dynamic_size)
    for i in arange(0, 11 * dynamic_size, dynamic_size):
        obstacle_x.append((60 - i) * dynamic_size)
        obstacle_y.append(45.0 * dynamic_size)

    return obstacle_x, obstacle_y


def outline_obstacles_floor_two_and_three(obstacle_x, obstacle_y, dynamic_size):
    #   Room outline
    for i in arange(0, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(0, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(60.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 61 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * dynamic_size)
    for i in arange(0, 61 * dynamic_size, dynamic_size):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    # two classes bottom left
    for i in arange(0, 10 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(10.0 * dynamic_size)
    for i in arange(0, 11 * dynamic_size, dynamic_size):
        obstacle_x.append(10.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 11 * dynamic_size, dynamic_size):
        obstacle_x.append(15.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(11 * dynamic_size, 15 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(10.0 * dynamic_size)

    # stairs bottom left
    for i in arange(16 * dynamic_size, 21 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(6 * dynamic_size)
    for i in arange(6 * dynamic_size, 10 * dynamic_size, dynamic_size):
        obstacle_x.append(16 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(6 * dynamic_size, 10 * dynamic_size, dynamic_size):
        obstacle_x.append(21 * dynamic_size)
        obstacle_y.append(i)
    # bottom elevator
    for i in arange(28 * dynamic_size, 34 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(3 * dynamic_size)
    for i in arange(4 * dynamic_size, dynamic_size):
        obstacle_x.append(28 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 4 * dynamic_size, dynamic_size):
        obstacle_x.append(34 * dynamic_size)
        obstacle_y.append(i)

    # toilets
    for i in arange(42 * dynamic_size, 53 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(8.0 * dynamic_size)
    for i in arange(0, 8 * dynamic_size, dynamic_size):
        obstacle_x.append(42 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 9 * dynamic_size, dynamic_size):
        obstacle_x.append(53 * dynamic_size)
        obstacle_y.append(i)

    # faculty offices
    for i in arange(56 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(8.0 * dynamic_size)
    for i in arange(0, 8 * dynamic_size, dynamic_size):
        obstacle_x.append(56.0 * dynamic_size)
        obstacle_y.append(i)

    # big class number 1
    for i in arange(45 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(20.0 * dynamic_size)
    for i in arange(45 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(35.0 * dynamic_size)
    for i in arange(20 * dynamic_size, 33 * dynamic_size, dynamic_size):
        obstacle_x.append(45.0 * dynamic_size)
        obstacle_y.append(i)

    # big class number 2
    for i in arange(45 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(37.0 * dynamic_size)
    for i in arange(45 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(52.0 * dynamic_size)
    for i in arange(37 * dynamic_size, 45 * dynamic_size, dynamic_size):
        obstacle_x.append(45.0 * dynamic_size)
        obstacle_y.append(i)

    # benches
    for i in arange(25 * dynamic_size, 35 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(57 * dynamic_size)
    for i in arange(0, 4 * dynamic_size, dynamic_size):
        obstacle_x.append(25 * dynamic_size)
        obstacle_y.append((60 - i) * dynamic_size)
    for i in arange(0, 4 * dynamic_size, dynamic_size):
        obstacle_x.append(35 * dynamic_size)
        obstacle_y.append((60 - i) * dynamic_size)

    # balcony
    for i in arange(55 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(5.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 5 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(55.0 * dynamic_size)
    for i in arange(0, 5 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * dynamic_size)

    # middle stairs
    for i in arange(25 * dynamic_size, 35 * dynamic_size, dynamic_size):
        obstacle_x.append(10.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(25 * dynamic_size, 35 * dynamic_size, dynamic_size):
        obstacle_x.append(16.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(10 * dynamic_size, 16 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(25.0 * dynamic_size)

    return obstacle_x, obstacle_y


def outline_obstacles_floor_four(obstacle_x, obstacle_y, dynamic_size):
    #  outline of room
    for i in arange(0, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(0, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(60.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 61 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * dynamic_size)
    for i in arange(0, 61 * dynamic_size, dynamic_size):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    # stairs bottom left
    for i in arange(16 * dynamic_size, 21 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(3 * dynamic_size)
    for i in arange(3 * dynamic_size, 9 * dynamic_size, dynamic_size):
        obstacle_x.append(16 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(3 * dynamic_size, 9 * dynamic_size, dynamic_size):
        obstacle_x.append(21 * dynamic_size)
        obstacle_y.append(i)

    # Lecture hall
    for i in arange(35 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(20.0 * dynamic_size)
    for i in arange(35 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(45.0 * dynamic_size)
    for i in arange(20 * dynamic_size, 25 * dynamic_size, dynamic_size):
        obstacle_x.append(35 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(29 * dynamic_size, 42 * dynamic_size, dynamic_size):
        obstacle_x.append(35 * dynamic_size)
        obstacle_y.append(i)

    # small room under hall
    for i in arange(57 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(15.0 * dynamic_size)
    for i in arange(57 * dynamic_size, 60 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(10.0 * dynamic_size)
    for i in arange(10 * dynamic_size, 15 * dynamic_size, dynamic_size):
        obstacle_x.append(57.0 * dynamic_size)
        obstacle_y.append(i)

    # toilets
    for i in arange(46 * dynamic_size, 56 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(7.0 * dynamic_size)
    for i in arange(0, 8 * dynamic_size, dynamic_size):
        obstacle_x.append(46.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 8 * dynamic_size, dynamic_size):
        obstacle_x.append(56.0 * dynamic_size)
        obstacle_y.append(i)

    # elevator
    for i in arange(26 * dynamic_size, 38 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(3.0 * dynamic_size)
    for i in arange(0, 4 * dynamic_size, dynamic_size):
        obstacle_x.append(26 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(0, 4 * dynamic_size, dynamic_size):
        obstacle_x.append(38 * dynamic_size)
        obstacle_y.append(i)

    # faculty offices
    for i in arange(0, 6 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(20.0 * dynamic_size)
    for i in arange(0, 21 * dynamic_size, dynamic_size):
        obstacle_x.append(6.0 * dynamic_size)
        obstacle_y.append(i)

    # more offices
    for i in arange(0, 6 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(50.0 * dynamic_size)
    for i in arange(0, 9 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(30.0 * dynamic_size)
    for i in arange(30 * dynamic_size, 51 * dynamic_size, dynamic_size):
        obstacle_x.append(9.0 * dynamic_size)
        obstacle_y.append(i)

    # stairs near offices
        # middle stairs
    for i in arange(25 * dynamic_size, 35 * dynamic_size, dynamic_size):
        obstacle_x.append(10.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(25 * dynamic_size, 35 * dynamic_size, dynamic_size):
        obstacle_x.append(16.0 * dynamic_size)
        obstacle_y.append(i)
    for i in arange(10 * dynamic_size, 16 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(25.0 * dynamic_size)

    # benches - top
    for i in arange(20 * dynamic_size, 33 * dynamic_size, dynamic_size):
        obstacle_x.append(i)
        obstacle_y.append(57.0 * dynamic_size)
    for i in arange(0, 4 * dynamic_size, dynamic_size):
        obstacle_x.append(20 * dynamic_size)
        obstacle_y.append((60 - i) * dynamic_size)
    for i in arange(4 * dynamic_size, dynamic_size):
        obstacle_x.append(33 * dynamic_size)
        obstacle_y.append((60 - i) * dynamic_size)

    return obstacle_x, obstacle_y
