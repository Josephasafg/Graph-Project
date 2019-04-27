from numpy import arange

DEFAULT = 1.0


def outline_obstacles_demo_building_1(obstacle_x, obstacle_y):
    #  outline of room
    for i in arange(0, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(60 * DEFAULT):
        obstacle_x.append(60.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * DEFAULT)
    for i in arange(61 * DEFAULT):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    # outline obstacle top left
    for i in arange(0, 6 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(6 * DEFAULT)

    # outline exit/enter 1
    for i in arange(0, 3 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(6 * DEFAULT)
    for i in arange(0, 3 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(8 * DEFAULT)

    # outline obst
    for i in arange(11 * DEFAULT, 17 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(22 * DEFAULT)
    for i in arange(0, 22 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(11 * DEFAULT)
    for i in arange(0, 22 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(16 * DEFAULT)

    # outline obst
    for i in arange(30 * DEFAULT, 45 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(30 * DEFAULT)
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(45 * DEFAULT)

    # outline obst
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(20 * DEFAULT)
    for i in arange(0, 20 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(40 * DEFAULT)

    # outline exit/enter 2
    for i in arange(30 * DEFAULT, 33 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(40 * DEFAULT)
    for i in arange(40 * DEFAULT, 43 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(30 * DEFAULT)
    for i in arange(40 * DEFAULT, 43 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(33 * DEFAULT)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_2(obstacle_x, obstacle_y):
    #  outline of room
    for i in arange(0, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(0, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(0.0)
    for i in arange(0, 31 * DEFAULT):
        obstacle_x.append(60.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(0, 41 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * DEFAULT)
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(30 * DEFAULT)
    for i in arange(30 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(40 * DEFAULT)

    # outline obstacle top left
    for i in arange(0, 12 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(50 * DEFAULT)
    for i in arange(0, 12 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(40 * DEFAULT, 51 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(12 * DEFAULT)

    # outline obstacle center left
    for i in arange(0, 7 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(13 * DEFAULT)
    for i in arange(13 * DEFAULT, 25 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(7 * DEFAULT)
    for i in arange(30 * DEFAULT, 41 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(7 * DEFAULT)

    # outline bottom left
    for i in arange(0, 17 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(13 * DEFAULT)
    for i in arange(7 * DEFAULT, 14 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(17 * DEFAULT)
    for i in arange(0, 4 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(17 * DEFAULT)

    # outline middle top
    for i in arange(30 * DEFAULT, 34 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(25 * DEFAULT)
    for i in arange(30 * DEFAULT, 35 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(28 * DEFAULT)
    for i in arange(25 * DEFAULT, 28 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(30 * DEFAULT)
    for i in arange(25 * DEFAULT, 28 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(34 * DEFAULT)

    # outline middle bottom
    j = 5
    for i in arange((30-j) * DEFAULT, (34-j) * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append((25-j) * DEFAULT)
    for i in arange((30-j) * DEFAULT, (35-j) * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append((28-j) * DEFAULT)
    for i in arange((25-j) * DEFAULT, (28-j) * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append((30-j) * DEFAULT)
    for i in arange((25-j) * DEFAULT, (28-j) * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append((34-j) * DEFAULT)

    # outline exit/enter 1
    for i in arange(57 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(17 * DEFAULT)
    for i in arange(57 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(14 * DEFAULT)

    # outline obst next to exit on top
    for i in arange(30 * DEFAULT, 40 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(30 * DEFAULT)

    # outline obst above bottom right
    for i in arange(42 * DEFAULT, 56 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(20 * DEFAULT)
    for i in arange(20 * DEFAULT, 30 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(42 * DEFAULT)
    for i in arange(20 * DEFAULT, 30 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(55 * DEFAULT)

    # outline obst bototm right
    for i in arange(42 * DEFAULT, 56 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(10 * DEFAULT)
    for i in arange(0, 10 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(42 * DEFAULT)
    for i in arange(0, 10 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(55 * DEFAULT)

    # outline obst bototm left
    for i in arange(42 * DEFAULT, 56 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(10 * DEFAULT)
    for i in arange(0, 10 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(42 * DEFAULT)
    for i in arange(0, 10 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(55 * DEFAULT)

    # outline exit/enter 2 top
    for i in arange(57 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(27 * DEFAULT)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_3(obstacle_x, obstacle_y):
    #  outline of room
    for i in arange(0, 20 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(60 * DEFAULT):
        obstacle_x.append(60.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * DEFAULT)
    for i in arange(61 * DEFAULT):
        obstacle_x.append(0.0)
        obstacle_y.append(i)
    for i in arange(0, 30 * DEFAULT):
        obstacle_x.append(20 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(0, 30 * DEFAULT):
        obstacle_x.append(40 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(20 * DEFAULT, 41 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(30 * DEFAULT)

    # outline obstacle middle bottom 1
    for i in arange(20 * DEFAULT, 26 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(30 * DEFAULT, 40 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(20 * DEFAULT)
    for i in arange(30 * DEFAULT, 40 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(25 * DEFAULT)

    # outline obstacle middle bottom 2
    for i in arange(35 * DEFAULT, 41 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(30 * DEFAULT, 40 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(35 * DEFAULT)
    for i in arange(30 * DEFAULT, 40 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(40 * DEFAULT)

    # outline obstacle middle top 1
    for i in arange(20 * DEFAULT, 26 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(50 * DEFAULT)
    for i in arange(50 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(20 * DEFAULT)
    for i in arange(50 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(25 * DEFAULT)

    # outline obstacle middle top 2
    for i in arange(35 * DEFAULT, 41 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(50 * DEFAULT)
    for i in arange(50 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(35 * DEFAULT)
    for i in arange(50 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(40 * DEFAULT)

    # outline obstacle top left
    for i in arange(0, 6 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(6 * DEFAULT)

    # outline exit/enter 1
    for i in arange(0, 5 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(8 * DEFAULT)
    for i in arange(0, 5 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(11 * DEFAULT)

    # outline exit/enter 2
    for i in arange(0, 5 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(48 * DEFAULT)
    for i in arange(0, 5 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(51 * DEFAULT)

    # outline middle left
    for i in arange(0, 7 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(30 * DEFAULT)
    for i in arange(0, 7 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(10 * DEFAULT)
    for i in arange(10 * DEFAULT, 22 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(7 * DEFAULT)
    for i in arange(26 * DEFAULT, 31 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(7 * DEFAULT)

    # outline obst top left
    for i in arange(53 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(30 * DEFAULT)
    for i in arange(30 * DEFAULT, 41 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(53 * DEFAULT)
    for i in arange(44 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(53 * DEFAULT)

    #   outline obst top left
    for i in arange(40 * DEFAULT, 45 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(30 * DEFAULT)
    for i in arange(40 * DEFAULT, 44 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(10 * DEFAULT)
    for i in arange(10 * DEFAULT, 30 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(44 * DEFAULT)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_4(obstacle_x, obstacle_y):
    #  outline of room
    for i in arange(0, 20* DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(60 * DEFAULT):
        obstacle_x.append(60.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(0, 21 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * DEFAULT)
    for i in arange(40 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * DEFAULT)
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(20 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(40 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(20 * DEFAULT, 41 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(61 * DEFAULT):
        obstacle_x.append(0.0)
        obstacle_y.append(i)
    for i in arange(0 * DEFAULT, 20 * DEFAULT):
        obstacle_x.append(20 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(0, 20 * DEFAULT):
        obstacle_x.append(40 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(20 * DEFAULT, 41 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(20 * DEFAULT)

    # outline obstacle middle bottom
    for i in arange(28 * DEFAULT, 33 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(34 * DEFAULT)
    for i in arange(34 * DEFAULT, 41 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(28 * DEFAULT)
    for i in arange(34 * DEFAULT, 41 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(33 * DEFAULT)

    # outline obstacle middle top
    for i in arange(28 * DEFAULT, 33 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(28 * DEFAULT)
    for i in arange(20 * DEFAULT, 29 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(28 * DEFAULT)
    for i in arange(20 * DEFAULT, 29 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(33 * DEFAULT)

    # outline obstacle top left
    for i in arange(0, 9 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(11 * DEFAULT, 21 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)

    # outline obstacle bottom right
    for i in arange(40 * DEFAULT, 49 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(20 * DEFAULT)
    for i in arange(51 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(20 * DEFAULT)

    # outline exit/enter 1
    for i in arange(0, 3 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(8 * DEFAULT)
    for i in arange(0, 3 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(11 * DEFAULT)

    # outline exit/enter 2
    for i in arange(57 * DEFAULT, 61 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(48 * DEFAULT)
    for i in arange(57 * DEFAULT, 61 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(51 * DEFAULT)

    # outline middle left
    for i in arange(0, 7 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(30 * DEFAULT)
    for i in arange(0, 7 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(10 * DEFAULT)
    for i in arange(10 * DEFAULT, 31 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(7 * DEFAULT)

    # outline obst top right
    for i in arange(53 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(30 * DEFAULT)
    for i in arange(30 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(53 * DEFAULT)

    # outline obst top right small
    for i in arange(40 * DEFAULT, 45 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(57 * DEFAULT)
    for i in arange(40 * DEFAULT, 45 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(42 * DEFAULT)
    for i in arange(42 * DEFAULT, 58 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(44 * DEFAULT)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_5(obstacle_x, obstacle_y):
    #  outline of room
    for i in arange(0, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * DEFAULT)
    for i in arange(30 * DEFAULT, 61 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(60.0 * DEFAULT)
    for i in arange(30 * DEFAULT, 61 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(0.0)
    for i in arange(0, 21 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(30.0 * DEFAULT)
    for i in arange(40 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(30.0 * DEFAULT)
    for i in arange(0, 31 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(20.0 * DEFAULT)
    for i in arange(0, 31 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(40.0 * DEFAULT)
    for i in arange(20 * DEFAULT, 41 * DEFAULT):
        obstacle_y.append(0)
        obstacle_x.append(i)

    # outline obstacle top left
    for i in arange(0, 12 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(50 * DEFAULT)
    for i in arange(0, 12 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(40 * DEFAULT, 51 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(12 * DEFAULT)

    # outline obstacle right
    for i in arange(45 * DEFAULT, 49 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(51 * DEFAULT, 56 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(30 * DEFAULT, 41 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(45 * DEFAULT)
    for i in arange(30 * DEFAULT, 41 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(56 * DEFAULT)

    # outline middle top
    for i in arange(30 * DEFAULT, 34 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(25 * DEFAULT)
    for i in arange(30 * DEFAULT, 35 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(28 * DEFAULT)
    for i in arange(25 * DEFAULT, 28 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(30 * DEFAULT)
    for i in arange(25 * DEFAULT, 28 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(34 * DEFAULT)

    # outline middle bottom
    for i in arange(30 * DEFAULT, 41 * DEFAULT):
        obstacle_y.append(20 * DEFAULT)
        obstacle_x.append(i)
    for i in arange(30 * DEFAULT, 41 * DEFAULT):
        obstacle_y.append(10 * DEFAULT)
        obstacle_x.append(i)
    for i in arange(10 * DEFAULT, 21 * DEFAULT):
        obstacle_x.append(30 * DEFAULT)
        obstacle_y.append(i)

    # outline exit/enter 1
    for i in arange(0, 4 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(27 * DEFAULT)
    for i in arange(0, 4 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(31 * DEFAULT)

    # outline obst next to exit on top
    for i in arange(20 * DEFAULT, 30 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(34 * DEFAULT, 41 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(40 * DEFAULT, 61 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(20 * DEFAULT)
    for i in arange(40 * DEFAULT, 61 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(40 * DEFAULT)

    # outline exit/enter 2 top
    for i in arange(57 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(51 * DEFAULT)
    for i in arange(57 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(47 * DEFAULT)

    # outline exit/enter 3 top left
    for i in arange(0, 4 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(52 * DEFAULT)
    for i in arange(0, 4 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(55 * DEFAULT)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_6(obstacle_x, obstacle_y):
    #  outline of room
    for i in arange(0, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(0, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(30.0 * DEFAULT)
    for i in arange(0, 31 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(60.0 * DEFAULT)
    for i in arange(0, 31 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(0.0)

    # outline obstacle top left
    for i in arange(0, 12 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(20 * DEFAULT)
    for i in arange(0, 12 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(10 * DEFAULT)
    for i in arange(10 * DEFAULT, 21 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(12 * DEFAULT)

    # outline obstacle left bottom
    for i in arange(15 * DEFAULT, 19 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(10 * DEFAULT)
    for i in arange(21 * DEFAULT, 26 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(10 * DEFAULT)
    for i in arange(0, 11 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(15 * DEFAULT)
    for i in arange(0, 11 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(26 * DEFAULT)

    # outline bottom
    for i in arange(0, 4 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(30 * DEFAULT)
    for i in arange(0, 5 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(34 * DEFAULT)
    for i in arange(30 * DEFAULT, 34 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(0)
    for i in arange(30 * DEFAULT, 34 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(4 * DEFAULT)

    # outline top left
    for i in arange(45 * DEFAULT, 61 * DEFAULT):
        obstacle_y.append(26 * DEFAULT)
        obstacle_x.append(i)

    # outline completing top left
    for i in arange(16 * DEFAULT, 27 * DEFAULT):
        obstacle_x.append(45 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(40 * DEFAULT, 46 * DEFAULT):
        obstacle_y.append(16 * DEFAULT)
        obstacle_x.append(i)

    # outline obst bottom right
    for i in arange(0, 11 * DEFAULT):
        obstacle_x.append(40 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(40 * DEFAULT, 45 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(10 * DEFAULT)
    for i in arange(48 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(10 * DEFAULT)

    # outline obst next to exit on top
    for i in arange(20 * DEFAULT, 30 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(16 * DEFAULT)
    for i in arange(34 * DEFAULT, 41 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(16 * DEFAULT)
    for i in arange(16 * DEFAULT, 31 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(20 * DEFAULT)
    for i in arange(16 * DEFAULT, 31 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(40 * DEFAULT)

    # outline exit/enter 2 top
    for i in arange(55 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(21 * DEFAULT)
    for i in arange(55 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(17 * DEFAULT)

    # outline exit/enter 3 top left
    for i in arange(0, 4 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(22 * DEFAULT)
    for i in arange(0, 4 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(25 * DEFAULT)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_7(obstacle_x, obstacle_y):
    #  outline of room
    for i in arange(0, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(60 * DEFAULT):
        obstacle_x.append(60.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * DEFAULT)
    for i in arange(61 * DEFAULT):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    # outline obstacle triangle left
    j = 0
    # outline obst triangle right
    for i in arange(40 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append((j+1) * DEFAULT)
        obstacle_y.append(i)
        j += 1

    # outline exit/enter 1
    for i in arange(0, 3 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(6 * DEFAULT)
    for i in arange(0, 3 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(8 * DEFAULT)

    # outline obst around x=10
    for i in arange(11 * DEFAULT, 17 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(22 * DEFAULT)
    for i in arange(0, 22 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(11 * DEFAULT)
    for i in arange(0, 22 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(16 * DEFAULT)

    # outline obst around x=30
    for i in arange(30 * DEFAULT, 34 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(22 * DEFAULT)
    for i in arange(37 * DEFAULT, 41 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(22 * DEFAULT)
    for i in arange(0, 22 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(30 * DEFAULT)
    for i in arange(0, 22 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(40 * DEFAULT)

    j = 61
    # outline obst triangle right
    for i in arange(50 * DEFAULT, j * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(j-1)
        j -= 1

    # outline obst rectangle in the middle
    for i in arange(30 * DEFAULT, 40 * DEFAULT):
        obstacle_x.append(20 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(30 * DEFAULT, 40 * DEFAULT):
        obstacle_x.append(25 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(20 * DEFAULT, 26 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(30 * DEFAULT)
    for i in arange(20 * DEFAULT, 26 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)

    # outline obst around x = 0
    for i in arange(30 * DEFAULT, 33 * DEFAULT):
        obstacle_x.append(10 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(36 * DEFAULT, 40 * DEFAULT):
        obstacle_x.append(10 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(0, 11 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(30 * DEFAULT)
    for i in arange(0, 11 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)

    # outline obst
    for i in arange(30 * DEFAULT, 45 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(30 * DEFAULT)
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(45 * DEFAULT)

    # outline obst
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(20 * DEFAULT)
    for i in arange(0, 20 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(40 * DEFAULT)

    # outline exit/enter 2
    for i in arange(57 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(57 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(37 * DEFAULT)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_8(obstacle_x, obstacle_y):
    #  outline of room
    for i in arange(20 * DEFAULT, 40 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(21 * DEFAULT,40 * DEFAULT):
        obstacle_x.append(60.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(21 * DEFAULT,40 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * DEFAULT)
    for i in arange(20 * DEFAULT,40 * DEFAULT):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    j = 0
    for i in arange(40 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(j+1)
        obstacle_y.append(i)
        j += 1

    j = 61 * DEFAULT
    for i in arange(40 * DEFAULT, j):
        obstacle_x.append(i)
        obstacle_y.append(j-1)
        j -= 1

    j = 0
    for i in arange(40 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(j+1)
        j += 1

    j = 20 * DEFAULT
    for i in arange(0, j):
        obstacle_x.append(i)
        obstacle_y.append(j-1)
        j -= 1

    # outline exit/enter 1
    for i in arange(0, 3 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(20 * DEFAULT)
    for i in arange(0, 3 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(23 * DEFAULT)

    # outline obst around x=10
    for i in arange(11 * DEFAULT, 17 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(22 * DEFAULT)
    for i in arange(9 * DEFAULT, 22 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(11 * DEFAULT)
    for i in arange(3 * DEFAULT, 22 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(16 * DEFAULT)

    # outline obst around x=30
    for i in arange(30 * DEFAULT, 34 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(22 * DEFAULT)
    for i in arange(37 * DEFAULT, 41 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(22 * DEFAULT)
    for i in arange(0, 22 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(30 * DEFAULT)
    for i in arange(0, 22 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(40 * DEFAULT)

    # outline obst rectangle in the middle
    for i in arange(25 * DEFAULT, 40 * DEFAULT):
        obstacle_x.append(20 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(25 * DEFAULT, 40 * DEFAULT):
        obstacle_x.append(25 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(20 * DEFAULT, 26 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(25 * DEFAULT)
    for i in arange(20 * DEFAULT, 26 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)

    # outline obst around x = 0
    for i in arange(30 * DEFAULT, 33 * DEFAULT):
        obstacle_x.append(10 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(36 * DEFAULT, 40 * DEFAULT):
        obstacle_x.append(10 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(0, 11 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(30 * DEFAULT)
    for i in arange(0, 11 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)


    # outline obst
    for i in arange(30 * DEFAULT, 45 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(30 * DEFAULT)
    for i in arange(40 * DEFAULT, 55 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(45 * DEFAULT)

    # outline obst
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(20 * DEFAULT)
    for i in arange(0, 20 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(40 * DEFAULT)

    # outline exit/enter 2
    for i in arange(57 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(57 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(37 * DEFAULT)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_9(obstacle_x, obstacle_y):
    #  outline of room
    for i in arange(30 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(0, 61 * DEFAULT):
        obstacle_x.append(60.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(30 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * DEFAULT)

    j = 0
    for i in arange(30 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(j+1)
        obstacle_y.append(i)
        j += 1

    j = 30 * DEFAULT
    for i in arange(0, j):
        obstacle_x.append(i)
        obstacle_y.append(j-1)
        j -= 1

    # outline exit/enter 1
    for i in arange(10 * DEFAULT, 13 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(20 * DEFAULT)
    for i in arange(7 * DEFAULT, 13 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(23 * DEFAULT)

    # outline obst around x=10
    for i in arange(11 * DEFAULT, 17 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(22 * DEFAULT)
    for i in arange(18 * DEFAULT, 22 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(11 * DEFAULT)
    for i in arange(13 * DEFAULT, 22 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(16 * DEFAULT)

    # outline obst around x=30
    for i in arange(30 * DEFAULT, 34 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(22 * DEFAULT)
    for i in arange(37 * DEFAULT, 41 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(22 * DEFAULT)
    for i in arange(0, 22 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(30 * DEFAULT)
    for i in arange(0, 22 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(40 * DEFAULT)

    # outline obst rectangle in the middle
    for i in arange(25 * DEFAULT, 40 * DEFAULT):
        obstacle_x.append(20 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(25 * DEFAULT, 40 * DEFAULT):
        obstacle_x.append(25 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(20 * DEFAULT, 26 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(25 * DEFAULT)
    for i in arange(20 * DEFAULT, 26 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)

    # outline obst
    for i in arange(30 * DEFAULT, 34 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(37 * DEFAULT, 45 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)

    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(30 * DEFAULT)
    for i in arange(40 * DEFAULT, 45 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(45 * DEFAULT)
    for i in arange(48 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(45 * DEFAULT)


    # outline obst
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(20 * DEFAULT)
    for i in arange(0, 20 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(40 * DEFAULT)

    # outline exit/enter 2
    for i in arange(57 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(57 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(37 * DEFAULT)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_10(obstacle_x, obstacle_y):
    #  outline of room
    for i in arange(0, 40 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(21 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(60.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(21 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * DEFAULT)
    for i in arange(0, 41 * DEFAULT):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    j = 0 * DEFAULT
    for i in arange(40 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(j+1)
        obstacle_y.append(i)
        j += 1

    j = 0 * DEFAULT
    for i in arange(40 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(j+1)
        j += 1

    # outline exit/enter 1
    for i in arange(0, 3 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(20 * DEFAULT)
    for i in arange(0, 3 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(23 * DEFAULT)

    # outline obst around x=10
    for i in arange(0, 17 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(22 * DEFAULT)
    for i in arange(0, 17 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(10 * DEFAULT)
    for i in arange(10 * DEFAULT, 22 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(16 * DEFAULT)

    # outline obst around x=30
    for i in arange(30 * DEFAULT, 34 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(22 * DEFAULT)
    for i in arange(37 * DEFAULT, 41 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(22 * DEFAULT)
    for i in arange(0, 22 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(30 * DEFAULT)
    for i in arange(0, 22 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(40 * DEFAULT)

    # outline obst rectangle in the middle
    for i in arange(25 * DEFAULT, 40 * DEFAULT):
        obstacle_x.append(20 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(25 * DEFAULT, 40 * DEFAULT):
        obstacle_x.append(25 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(20 * DEFAULT, 26 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(25 * DEFAULT)
    for i in arange(20 * DEFAULT, 26 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)

    # outline obst around x = 0
    for i in arange(30 * DEFAULT, 33 * DEFAULT):
        obstacle_x.append(10 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(36 * DEFAULT, 40 * DEFAULT):
        obstacle_x.append(10 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(0, 11 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(30 * DEFAULT)
    for i in arange(0, 11 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)

    # outline obst
    for i in arange(30 * DEFAULT, 36 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(39 * DEFAULT, 45 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40 * DEFAULT)
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(30 * DEFAULT)
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(45 * DEFAULT)

    # outline obst
    for i in arange(40 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(20 * DEFAULT)
    for i in arange(0, 20 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(40 * DEFAULT)

    # outline obst
    for i in arange(55 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(25 * DEFAULT)
    for i in arange(55 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(35 * DEFAULT)
    for i in arange(25 * DEFAULT, 29 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(55 * DEFAULT)
    for i in arange(32 * DEFAULT, 36 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(55 * DEFAULT)

    # outline exit/enter 2
    for i in arange(57 * DEFAULT, 61 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(52 * DEFAULT)
    for i in arange(57 * DEFAULT, 61 * DEFAULT):
        obstacle_y.append(i)
        obstacle_x.append(55 * DEFAULT)

    return obstacle_x, obstacle_y


def outline_obstacles_floor_one_other(obstacle_x, obstacle_y):
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


def outline_obstacles_floor_one(obstacle_x, obstacle_y):
    # Room outline
    for i in arange(60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(60 * DEFAULT):
        obstacle_x.append(60.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(35 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * DEFAULT)
    for i in arange(45 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * DEFAULT)

    for i in arange(10 * DEFAULT):
        obstacle_x.append(0)
        obstacle_y.append(i)
    for i in arange(18 * DEFAULT, 61 * DEFAULT):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    # bottom left class
    for i in arange(11 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(8.0 * DEFAULT)
    for i in arange(7 * DEFAULT):
        obstacle_x.append(10.0 * DEFAULT)
        obstacle_y.append(i)

    # stairs bottom left
    for i in arange(16 * DEFAULT, 21 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(3 * DEFAULT)
    for i in arange(3 * DEFAULT, 9 * DEFAULT):
        obstacle_x.append(16 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(3 * DEFAULT, 9 * DEFAULT):
        obstacle_x.append(21 * DEFAULT)
        obstacle_y.append(i)
    # elevator
    for i in arange(25 * DEFAULT, 35 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(3.0 * DEFAULT)
    for i in arange(4 * DEFAULT):
        obstacle_x.append(25 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(4 * DEFAULT):
        obstacle_x.append(34 * DEFAULT)
        obstacle_y.append(i)

    # bottom right class
    for i in arange(50 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(10.0 * DEFAULT)
    for i in arange(7 * DEFAULT):
        obstacle_x.append(50.0 * DEFAULT)
        obstacle_y.append(i)

    # toilet near bottom right class
    # for i in arange(47, 50):
    #     obstacle_x.append(i)
    #     obstacle_y.append(7)
    for i in arange(8 * DEFAULT):
        obstacle_x.append(47 * DEFAULT)
        obstacle_y.append(i)

    # mid left class
    for i in arange(10 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(40.0 * DEFAULT)
    for i in arange(10 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(55.0 * DEFAULT)
    for i in arange(40 * DEFAULT, 52 * DEFAULT):
        obstacle_x.append(10 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(10 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(48 * DEFAULT)

    # # top left stairs
        # middle stairs
    for i in arange(25 * DEFAULT, 35 * DEFAULT):
        obstacle_x.append(10.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(25 * DEFAULT, 35 * DEFAULT):
        obstacle_x.append(16.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(10 * DEFAULT, 16 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(25.0 * DEFAULT)
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
    for i in arange(25 * DEFAULT, 45 * DEFAULT):
        obstacle_x.append(50 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(11 * DEFAULT):
        obstacle_x.append((60 - i) * DEFAULT)
        obstacle_y.append(25.0 * DEFAULT)
    for i in arange(11 * DEFAULT):
        obstacle_x.append((60 - i) * DEFAULT)
        obstacle_y.append(45.0 * DEFAULT)

    return obstacle_x, obstacle_y


def outline_obstacles_floor_two_and_three(obstacle_x, obstacle_y):
    #   Room outline
    for i in arange(60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(60 * DEFAULT):
        obstacle_x.append(60.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * DEFAULT)
    for i in arange(61 * DEFAULT):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    # two classes bottom left
    for i in arange(10 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(10.0 * DEFAULT)
    for i in arange(11 * DEFAULT):
        obstacle_x.append(10.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(11 * DEFAULT):
        obstacle_x.append(15.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(11 * DEFAULT, 15 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(10.0 * DEFAULT)

    # stairs bottom left
    for i in arange(16 * DEFAULT, 21 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(3 * DEFAULT)
    for i in arange(3 * DEFAULT, 9 * DEFAULT):
        obstacle_x.append(16 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(3 * DEFAULT, 9 * DEFAULT):
        obstacle_x.append(21 * DEFAULT)
        obstacle_y.append(i)
    # bottom elevator
    for i in arange(28 * DEFAULT, 34 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(3 * DEFAULT)
    for i in arange(4 * DEFAULT):
        obstacle_x.append(28 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(4 * DEFAULT):
        obstacle_x.append(34 * DEFAULT)
        obstacle_y.append(i)

    # toilets
    for i in arange(42 * DEFAULT, 53 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(8.0 * DEFAULT)
    for i in arange(8 * DEFAULT):
        obstacle_x.append(42 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(9 * DEFAULT):
        obstacle_x.append(53 * DEFAULT)
        obstacle_y.append(i)

    # faculty offices
    for i in arange(56 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(8.0 * DEFAULT)
    for i in arange(8 * DEFAULT):
        obstacle_x.append(56.0 * DEFAULT)
        obstacle_y.append(i)

    # big class number 1
    for i in arange(45 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(20.0 * DEFAULT)
    for i in arange(45 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(35.0 * DEFAULT)
    for i in arange(20 * DEFAULT, 33 * DEFAULT):
        obstacle_x.append(45.0 * DEFAULT)
        obstacle_y.append(i)

    # big class number 2
    for i in arange(45 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(37.0 * DEFAULT)
    for i in arange(45 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(52.0 * DEFAULT)
    for i in arange(37 * DEFAULT, 45 * DEFAULT):
        obstacle_x.append(45.0 * DEFAULT)
        obstacle_y.append(i)

    # benches
    for i in arange(25 * DEFAULT, 35 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(57 * DEFAULT)
    for i in arange(4 * DEFAULT):
        obstacle_x.append(25 * DEFAULT)
        obstacle_y.append((60 - i) * DEFAULT)
    for i in arange(4 * DEFAULT):
        obstacle_x.append(35 * DEFAULT)
        obstacle_y.append((60 - i) * DEFAULT)

    # balcony
    for i in arange(55 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(5.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(5 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(55.0 * DEFAULT)
    for i in arange(5 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * DEFAULT)

    # middle stairs
    for i in arange(25 * DEFAULT, 35 * DEFAULT):
        obstacle_x.append(10.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(25 * DEFAULT, 35 * DEFAULT):
        obstacle_x.append(16.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(10 * DEFAULT, 16 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(25.0 * DEFAULT)

    return obstacle_x, obstacle_y


def outline_obstacles_floor_four(obstacle_x, obstacle_y):
    #  outline of room
    for i in arange(0, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in arange(60 * DEFAULT):
        obstacle_x.append(60.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(61 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(60.0 * DEFAULT)
    for i in arange(61 * DEFAULT):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    # stairs bottom left
    for i in arange(16 * DEFAULT, 21 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(3 * DEFAULT)
    for i in arange(3 * DEFAULT, 9 * DEFAULT):
        obstacle_x.append(16 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(3 * DEFAULT, 9 * DEFAULT):
        obstacle_x.append(21 * DEFAULT)
        obstacle_y.append(i)

    # Lecture hall
    for i in arange(35 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(20.0 * DEFAULT)
    for i in arange(35 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(45.0 * DEFAULT)
    for i in arange(20 * DEFAULT, 25 * DEFAULT):
        obstacle_x.append(35 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(29 * DEFAULT, 42 * DEFAULT):
        obstacle_x.append(35 * DEFAULT)
        obstacle_y.append(i)

    # small room under hall
    for i in arange(57 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(15.0 * DEFAULT)
    for i in arange(57 * DEFAULT, 60 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(10.0 * DEFAULT)
    for i in arange(10 * DEFAULT, 15 * DEFAULT):
        obstacle_x.append(57.0 * DEFAULT)
        obstacle_y.append(i)

    # toilets
    for i in arange(46 * DEFAULT, 56 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(7.0 * DEFAULT)
    for i in arange(8 * DEFAULT):
        obstacle_x.append(46.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(8 * DEFAULT):
        obstacle_x.append(56.0 * DEFAULT)
        obstacle_y.append(i)

    # elevator
    for i in arange(26 * DEFAULT, 38 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(3.0 * DEFAULT)
    for i in arange(4 * DEFAULT):
        obstacle_x.append(26 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(4 * DEFAULT):
        obstacle_x.append(38 * DEFAULT)
        obstacle_y.append(i)

    # faculty offices
    for i in arange(6 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(20.0 * DEFAULT)
    for i in arange(21 * DEFAULT):
        obstacle_x.append(6.0 * DEFAULT)
        obstacle_y.append(i)

    # more offices
    for i in arange(6 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(50.0 * DEFAULT)
    for i in arange(9 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(30.0 * DEFAULT)
    for i in arange(30 * DEFAULT, 51 * DEFAULT):
        obstacle_x.append(9.0 * DEFAULT)
        obstacle_y.append(i)

    # stairs near offices
        # middle stairs
    for i in arange(25 * DEFAULT, 35 * DEFAULT):
        obstacle_x.append(10.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(25 * DEFAULT, 35 * DEFAULT):
        obstacle_x.append(16.0 * DEFAULT)
        obstacle_y.append(i)
    for i in arange(10 * DEFAULT, 16 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(25.0 * DEFAULT)
    # for i in arange(6, 11):
    #     obstacle_x.append(i)
    #     obstacle_y.append(30.0)
    # for i in arange(30, 51):
    #     obstacle_x.append(11.0)
    #     obstacle_y.append(i)

    # # exhibit
    # for i in arange(6, 12):
    #     obstacle_x.append(i)
    #     obstacle_y.append(26.0)
    # for i in arange(26, 30):
    #     obstacle_x.append(6.0)
    #     obstacle_y.append(i)
    # for i in arange(26, 30):
    #     obstacle_x.append(11.0)
    #     obstacle_y.append(i)

    # benches - top
    for i in arange(20 * DEFAULT, 33 * DEFAULT):
        obstacle_x.append(i)
        obstacle_y.append(57.0 * DEFAULT)
    for i in arange(4 * DEFAULT):
        obstacle_x.append(20 * DEFAULT)
        obstacle_y.append((60 - i) * DEFAULT)
        for i in arange(4 * DEFAULT):
            obstacle_x.append(33 * DEFAULT)
            obstacle_y.append((60 - i) * DEFAULT)

    return obstacle_x, obstacle_y
