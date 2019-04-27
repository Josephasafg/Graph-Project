def outline_obstacles_demo_building_1(obstacle_x, obstacle_y):
    #  outline of room
    for i in range(0, 60):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in range(60):
        obstacle_x.append(60.0)
        obstacle_y.append(i)
    for i in range(61):
        obstacle_x.append(i)
        obstacle_y.append(60.0)
    for i in range(61):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    # outline obstacle top left
    for i in range(0, 6):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(40, 60):
        obstacle_y.append(i)
        obstacle_x.append(6)

    # outline exit/enter 1
    for i in range(0, 3):
        obstacle_y.append(i)
        obstacle_x.append(6)
    for i in range(0, 3):
        obstacle_y.append(i)
        obstacle_x.append(8)

    # outline obst
    for i in range(11, 17):
        obstacle_x.append(i)
        obstacle_y.append(22)
    for i in range(0, 22):
        obstacle_y.append(i)
        obstacle_x.append(11)
    for i in range(0, 22):
        obstacle_y.append(i)
        obstacle_x.append(16)

    # outline obst
    for i in range(30, 45):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(40, 60):
        obstacle_y.append(i)
        obstacle_x.append(30)
    for i in range(40, 60):
        obstacle_y.append(i)
        obstacle_x.append(45)

    # outline obst
    for i in range(40, 60):
        obstacle_x.append(i)
        obstacle_y.append(20)
    for i in range(0, 20):
        obstacle_y.append(i)
        obstacle_x.append(40)

    # outline exit/enter 2
    for i in range(30, 33):
        obstacle_y.append(i)
        obstacle_x.append(40)
    for i in range(40, 43):
        obstacle_x.append(i)
        obstacle_y.append(30)
    for i in range(40, 43):
        obstacle_x.append(i)
        obstacle_y.append(33)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_2(obstacle_x, obstacle_y):
    #  outline of room
    for i in range(0, 60):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in range(0, 60):
        obstacle_y.append(i)
        obstacle_x.append(0.0)
    for i in range(0, 31):
        obstacle_x.append(60.0)
        obstacle_y.append(i)
    for i in range(0, 41):
        obstacle_x.append(i)
        obstacle_y.append(60.0)
    for i in range(40, 60):
        obstacle_x.append(i)
        obstacle_y.append(30)
    for i in range(30, 60):
        obstacle_y.append(i)
        obstacle_x.append(40)

    # outline obstacle top left
    for i in range(0, 12):
        obstacle_x.append(i)
        obstacle_y.append(50)
    for i in range(0, 12):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(40, 51):
        obstacle_y.append(i)
        obstacle_x.append(12)

    # outline obstacle center left
    for i in range(0, 7):
        obstacle_x.append(i)
        obstacle_y.append(13)
    for i in range(13, 25):
        obstacle_y.append(i)
        obstacle_x.append(7)
    for i in range(30, 41):
        obstacle_y.append(i)
        obstacle_x.append(7)

    # outline bottom left
    for i in range(0, 17):
        obstacle_x.append(i)
        obstacle_y.append(13)
    for i in range(7, 14):
        obstacle_y.append(i)
        obstacle_x.append(17)
    for i in range(0, 4):
        obstacle_y.append(i)
        obstacle_x.append(17)

    # outline middle top
    for i in range(30, 34):
        obstacle_y.append(i)
        obstacle_x.append(25)
    for i in range(30, 35):
        obstacle_y.append(i)
        obstacle_x.append(28)
    for i in range(25, 28):
        obstacle_x.append(i)
        obstacle_y.append(30)
    for i in range(25, 28):
        obstacle_x.append(i)
        obstacle_y.append(34)

    # outline middle bottom
    j= 5
    for i in range(30-j, 34-j):
        obstacle_y.append(i)
        obstacle_x.append(25-j)
    for i in range(30-j, 35-j):
        obstacle_y.append(i)
        obstacle_x.append(28-j)
    for i in range(25-j, 28-j):
        obstacle_x.append(i)
        obstacle_y.append(30-j)
    for i in range(25-j, 28-j):
        obstacle_x.append(i)
        obstacle_y.append(34-j)

    # outline exit/enter 1
    for i in range(57, 61):
        obstacle_x.append(i)
        obstacle_y.append(17)
    for i in range(57, 61):
        obstacle_x.append(i)
        obstacle_y.append(14)

    # outline obst next to exit on top
    for i in range(30, 40):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(40, 60):
        obstacle_y.append(i)
        obstacle_x.append(30)

    # outline obst above bottom right
    for i in range(42, 56):
        obstacle_x.append(i)
        obstacle_y.append(20)
    for i in range(20, 30):
        obstacle_y.append(i)
        obstacle_x.append(42)
    for i in range(20, 30):
        obstacle_y.append(i)
        obstacle_x.append(55)

    # outline obst bototm right
    for i in range(42, 56):
        obstacle_x.append(i)
        obstacle_y.append(10)
    for i in range(0, 10):
        obstacle_y.append(i)
        obstacle_x.append(42)
    for i in range(0, 10):
        obstacle_y.append(i)
        obstacle_x.append(55)

    # outline obst bototm left
    for i in range(42, 56):
        obstacle_x.append(i)
        obstacle_y.append(10)
    for i in range(0, 10):
        obstacle_y.append(i)
        obstacle_x.append(42)
    for i in range(0, 10):
        obstacle_y.append(i)
        obstacle_x.append(55)

    # outline exit/enter 2 top
    for i in range(57, 60):
        obstacle_y.append(i)
        obstacle_x.append(27)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_3(obstacle_x, obstacle_y):
    #  outline of room
    for i in range(0, 20):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in range(40, 60):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in range(60):
        obstacle_x.append(60.0)
        obstacle_y.append(i)
    for i in range(61):
        obstacle_x.append(i)
        obstacle_y.append(60.0)
    for i in range(61):
        obstacle_x.append(0.0)
        obstacle_y.append(i)
    for i in range(0,30):
        obstacle_x.append(20)
        obstacle_y.append(i)
    for i in range(0,30):
        obstacle_x.append(40)
        obstacle_y.append(i)
    for i in range(20,41):
        obstacle_x.append(i)
        obstacle_y.append(30)

    # outline obstacle middle bottom 1
    for i in range(20, 26):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(30, 40):
        obstacle_y.append(i)
        obstacle_x.append(20)
    for i in range(30, 40):
        obstacle_y.append(i)
        obstacle_x.append(25)

    # outline obstacle middle bottom 2
    for i in range(35, 41):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(30, 40):
        obstacle_y.append(i)
        obstacle_x.append(35)
    for i in range(30, 40):
        obstacle_y.append(i)
        obstacle_x.append(40)


    # outline obstacle middle top 1
    for i in range(20, 26):
        obstacle_x.append(i)
        obstacle_y.append(50)
    for i in range(50, 60):
        obstacle_y.append(i)
        obstacle_x.append(20)
    for i in range(50, 60):
        obstacle_y.append(i)
        obstacle_x.append(25)

    # outline obstacle middle top 2
    for i in range(35, 41):
        obstacle_x.append(i)
        obstacle_y.append(50)
    for i in range(50, 60):
        obstacle_y.append(i)
        obstacle_x.append(35)
    for i in range(50, 60):
        obstacle_y.append(i)
        obstacle_x.append(40)

    # outline obstacle top left
    for i in range(0, 6):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(40, 60):
        obstacle_y.append(i)
        obstacle_x.append(6)

    # outline exit/enter 1
    for i in range(0, 3):
        obstacle_y.append(i)
        obstacle_x.append(8)
    for i in range(0, 3):
        obstacle_y.append(i)
        obstacle_x.append(11)

    # outline exit/enter 2
    for i in range(0, 3):
        obstacle_y.append(i)
        obstacle_x.append(48)
    for i in range(0, 3):
        obstacle_y.append(i)
        obstacle_x.append(51)

    # outline middle left
    for i in range(0, 7):
        obstacle_x.append(i)
        obstacle_y.append(30)
    for i in range(0, 7):
        obstacle_x.append(i)
        obstacle_y.append(10)
    for i in range(10, 22):
        obstacle_y.append(i)
        obstacle_x.append(7)
    for i in range(26, 31):
        obstacle_y.append(i)
        obstacle_x.append(7)

    # outline obst top left
    for i in range(53, 60):
        obstacle_x.append(i)
        obstacle_y.append(30)
    for i in range(30, 41):
        obstacle_y.append(i)
        obstacle_x.append(53)
    for i in range(44, 60):
        obstacle_y.append(i)
        obstacle_x.append(53)

     # outline obst top left
    for i in range(40, 45):
        obstacle_x.append(i)
        obstacle_y.append(30)
    for i in range(40, 44):
        obstacle_x.append(i)
        obstacle_y.append(10)
    for i in range(10, 30):
        obstacle_y.append(i)
        obstacle_x.append(44)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_4(obstacle_x, obstacle_y):
    #  outline of room
    for i in range(0, 20):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in range(40, 60):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in range(60):
        obstacle_x.append(60.0)
        obstacle_y.append(i)
    for i in range(0,21):
        obstacle_x.append(i)
        obstacle_y.append(60.0)
    for i in range(40,61):
        obstacle_x.append(i)
        obstacle_y.append(60.0)
    for i in range(40,60):
        obstacle_x.append(20)
        obstacle_y.append(i)
    for i in range(40,60):
        obstacle_x.append(40)
        obstacle_y.append(i)
    for i in range(20,41):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(61):
        obstacle_x.append(0.0)
        obstacle_y.append(i)
    for i in range(0,20):
        obstacle_x.append(20)
        obstacle_y.append(i)
    for i in range(0,20):
        obstacle_x.append(40)
        obstacle_y.append(i)
    for i in range(20,41):
        obstacle_x.append(i)
        obstacle_y.append(20)

    # outline obstacle middle bottom
    for i in range(28, 33):
        obstacle_x.append(i)
        obstacle_y.append(34)
    for i in range(34, 41):
        obstacle_y.append(i)
        obstacle_x.append(28)
    for i in range(34, 41):
        obstacle_y.append(i)
        obstacle_x.append(33)


    # outline obstacle middle top
    for i in range(28, 33):
        obstacle_x.append(i)
        obstacle_y.append(28)
    for i in range(20, 29):
        obstacle_y.append(i)
        obstacle_x.append(28)
    for i in range(20, 29):
        obstacle_y.append(i)
        obstacle_x.append(33)

    # outline obstacle top left
    for i in range(0, 9):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(11, 21):
        obstacle_x.append(i)
        obstacle_y.append(40)

    # outline obstacle bottom right
    for i in range(40, 49):
        obstacle_x.append(i)
        obstacle_y.append(20)
    for i in range(51, 61):
        obstacle_x.append(i)
        obstacle_y.append(20)

    # outline exit/enter 1
    for i in range(0, 3):
        obstacle_y.append(i)
        obstacle_x.append(8)
    for i in range(0, 3):
        obstacle_y.append(i)
        obstacle_x.append(11)

    # outline exit/enter 2
    for i in range(57, 61):
        obstacle_y.append(i)
        obstacle_x.append(48)
    for i in range(57, 61):
        obstacle_y.append(i)
        obstacle_x.append(51)

    # outline middle left
    for i in range(0, 7):
        obstacle_x.append(i)
        obstacle_y.append(30)
    for i in range(0, 7):
        obstacle_x.append(i)
        obstacle_y.append(10)
    for i in range(10, 31):
        obstacle_y.append(i)
        obstacle_x.append(7)

    # outline obst top right
    for i in range(53, 60):
        obstacle_x.append(i)
        obstacle_y.append(30)
    for i in range(30, 60):
        obstacle_y.append(i)
        obstacle_x.append(53)


     # outline obst top right small
    for i in range(40, 45):
        obstacle_x.append(i)
        obstacle_y.append(57)
    for i in range(40, 45):
        obstacle_x.append(i)
        obstacle_y.append(42)
    for i in range(42, 58):
        obstacle_y.append(i)
        obstacle_x.append(44)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_5(obstacle_x, obstacle_y):
    #  outline of room
    for i in range(0, 60):
        obstacle_x.append(i)
        obstacle_y.append(60.0)
    for i in range(30, 61):
        obstacle_y.append(i)
        obstacle_x.append(60.0)
    for i in range(30, 61):
        obstacle_y.append(i)
        obstacle_x.append(0.0)
    for i in range(0, 21):
        obstacle_x.append(i)
        obstacle_y.append(30.0)
    for i in range(40, 61):
        obstacle_x.append(i)
        obstacle_y.append(30.0)
    for i in range(0, 31):
        obstacle_y.append(i)
        obstacle_x.append(20.0)
    for i in range(0, 31):
        obstacle_y.append(i)
        obstacle_x.append(40.0)
    for i in range(20, 41):
        obstacle_y.append(0)
        obstacle_x.append(i)

    # outline obstacle top left
    for i in range(0, 12):
        obstacle_x.append(i)
        obstacle_y.append(50)
    for i in range(0, 12):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(40, 51):
        obstacle_y.append(i)
        obstacle_x.append(12)

    # outline obstacle right
    for i in range(45, 49):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(51, 56):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(30, 41):
        obstacle_y.append(i)
        obstacle_x.append(45)
    for i in range(30, 41):
        obstacle_y.append(i)
        obstacle_x.append(56)


    # outline middle top
    for i in range(30, 34):
        obstacle_y.append(i)
        obstacle_x.append(25)
    for i in range(30, 35):
        obstacle_y.append(i)
        obstacle_x.append(28)
    for i in range(25, 28):
        obstacle_x.append(i)
        obstacle_y.append(30)
    for i in range(25, 28):
        obstacle_x.append(i)
        obstacle_y.append(34)

    # outline middle bototm
    for i in range(30, 41):
        obstacle_y.append(20)
        obstacle_x.append(i)
    for i in range(30, 41):
        obstacle_y.append(10)
        obstacle_x.append(i)
    for i in range(10, 21):
        obstacle_x.append(30)
        obstacle_y.append(i)


    # outline exit/enter 1
    for i in range(0, 4):
        obstacle_y.append(i)
        obstacle_x.append(27)
    for i in range(0, 4):
        obstacle_y.append(i)
        obstacle_x.append(31)

    # outline obst next to exit on top
    for i in range(20, 30):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(34, 41):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(40, 61):
        obstacle_y.append(i)
        obstacle_x.append(20)
    for i in range(40, 61):
        obstacle_y.append(i)
        obstacle_x.append(40)

    # outline exit/enter 2 top
    for i in range(57, 61):
        obstacle_x.append(i)
        obstacle_y.append(51)
    for i in range(57, 61):
        obstacle_x.append(i)
        obstacle_y.append(47)

    # outline exit/enter 3 top left
    for i in range(0, 4):
        obstacle_x.append(i)
        obstacle_y.append(52)
    for i in range(0, 4):
        obstacle_x.append(i)
        obstacle_y.append(55)


    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_6(obstacle_x, obstacle_y):
    #  outline of room
    for i in range(0, 60):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in range(0, 60):
        obstacle_x.append(i)
        obstacle_y.append(30.0)
    for i in range(0, 31):
        obstacle_y.append(i)
        obstacle_x.append(60.0)
    for i in range(0, 31):
        obstacle_y.append(i)
        obstacle_x.append(0.0)



    # outline obstacle top left
    for i in range(0, 12):
        obstacle_x.append(i)
        obstacle_y.append(20)
    for i in range(0, 12):
        obstacle_x.append(i)
        obstacle_y.append(10)
    for i in range(10, 21):
        obstacle_y.append(i)
        obstacle_x.append(12)

    # outline obstacle left bottom
    for i in range(15, 19):
        obstacle_x.append(i)
        obstacle_y.append(10)
    for i in range(21, 26):
        obstacle_x.append(i)
        obstacle_y.append(10)
    for i in range(0, 11):
        obstacle_y.append(i)
        obstacle_x.append(15)
    for i in range(0, 11):
        obstacle_y.append(i)
        obstacle_x.append(26)


    # outline bottom
    for i in range(0, 4):
        obstacle_y.append(i)
        obstacle_x.append(30)
    for i in range(0, 5):
        obstacle_y.append(i)
        obstacle_x.append(34)
    for i in range(30, 34):
        obstacle_x.append(i)
        obstacle_y.append(0)
    for i in range(30, 34):
        obstacle_x.append(i)
        obstacle_y.append(4)

    # outline top left
    for i in range(45, 61):
        obstacle_y.append(26)
        obstacle_x.append(i)

    # outline completing top left
    for i in range(16, 27):
        obstacle_x.append(45)
        obstacle_y.append(i)
    for i in range(40, 46):
        obstacle_y.append(16)
        obstacle_x.append(i)

        # outline obst bottom right
    for i in range(0, 11):
        obstacle_x.append(40)
        obstacle_y.append(i)
    for i in range(40, 45):
        obstacle_x.append(i)
        obstacle_y.append(10)
    for i in range(48, 61):
        obstacle_x.append(i)
        obstacle_y.append(10)


    # outline obst next to exit on top
    for i in range(20, 30):
        obstacle_x.append(i)
        obstacle_y.append(16)
    for i in range(34, 41):
        obstacle_x.append(i)
        obstacle_y.append(16)
    for i in range(16, 31):
        obstacle_y.append(i)
        obstacle_x.append(20)
    for i in range(16, 31):
        obstacle_y.append(i)
        obstacle_x.append(40)

    # outline exit/enter 2 top
    for i in range(57, 61):
        obstacle_x.append(i)
        obstacle_y.append(21)
    for i in range(57, 61):
        obstacle_x.append(i)
        obstacle_y.append(17)

    # outline exit/enter 3 top left
    for i in range(0, 4):
        obstacle_x.append(i)
        obstacle_y.append(22)
    for i in range(0, 4):
        obstacle_x.append(i)
        obstacle_y.append(25)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_7(obstacle_x, obstacle_y):
    #  outline of room
    for i in range(0, 60):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in range(60):
        obstacle_x.append(60.0)
        obstacle_y.append(i)
    for i in range(61):
        obstacle_x.append(i)
        obstacle_y.append(60.0)
    for i in range(61):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    # outline obstacle triangle left
    j = 0
    # outline obst triangle right
    for i in range(40, 61):
        obstacle_x.append(j+1)
        obstacle_y.append(i)
        j += 1

    # outline exit/enter 1
    for i in range(0, 3):
        obstacle_y.append(i)
        obstacle_x.append(6)
    for i in range(0, 3):
        obstacle_y.append(i)
        obstacle_x.append(8)

    # outline obst around x=10
    for i in range(11, 17):
        obstacle_x.append(i)
        obstacle_y.append(22)
    for i in range(0, 22):
        obstacle_y.append(i)
        obstacle_x.append(11)
    for i in range(0, 22):
        obstacle_y.append(i)
        obstacle_x.append(16)

    # outline obst around x=30
    for i in range(30, 34):
        obstacle_x.append(i)
        obstacle_y.append(22)
    for i in range(37, 41):
        obstacle_x.append(i)
        obstacle_y.append(22)
    for i in range(0, 22):
        obstacle_y.append(i)
        obstacle_x.append(30)
    for i in range(0, 22):
        obstacle_y.append(i)
        obstacle_x.append(40)


    j = 61
    # outline obst triangle right
    for i in range(50, j):
        obstacle_x.append(i)
        obstacle_y.append(j-1)
        j -= 1

    # outline obst rectangle in the middle
    for i in range(30, 40):
        obstacle_x.append(20)
        obstacle_y.append(i)
    for i in range(30, 40):
        obstacle_x.append(25)
        obstacle_y.append(i)
    for i in range(20, 26):
        obstacle_x.append(i)
        obstacle_y.append(30)
    for i in range(20, 26):
        obstacle_x.append(i)
        obstacle_y.append(40)

    # outline obst around x = 0
    for i in range(30, 33):
        obstacle_x.append(10)
        obstacle_y.append(i)
    for i in range(36, 40):
        obstacle_x.append(10)
        obstacle_y.append(i)
    for i in range(0, 11):
        obstacle_x.append(i)
        obstacle_y.append(30)
    for i in range(0, 11):
        obstacle_x.append(i)
        obstacle_y.append(40)


    # outline obst
    for i in range(30, 45):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(40, 60):
        obstacle_y.append(i)
        obstacle_x.append(30)
    for i in range(40, 60):
        obstacle_y.append(i)
        obstacle_x.append(45)

    # outline obst
    for i in range(40, 60):
        obstacle_x.append(i)
        obstacle_y.append(20)
    for i in range(0, 20):
        obstacle_y.append(i)
        obstacle_x.append(40)

    # outline exit/enter 2
    for i in range(57, 61):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(57, 61):
        obstacle_x.append(i)
        obstacle_y.append(37)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_8(obstacle_x, obstacle_y):
    #  outline of room
    for i in range(20, 40):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in range(21,40):
        obstacle_x.append(60.0)
        obstacle_y.append(i)
    for i in range(21,40):
        obstacle_x.append(i)
        obstacle_y.append(60.0)
    for i in range(20,40):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    j = 0
    for i in range(40, 61):
        obstacle_x.append(j+1)
        obstacle_y.append(i)
        j += 1

    j = 61
    for i in range(40, j):
        obstacle_x.append(i)
        obstacle_y.append(j-1)
        j -= 1

    j = 0
    for i in range(40, 61):
        obstacle_x.append(i)
        obstacle_y.append(j+1)
        j += 1

    j = 20
    for i in range(0, j):
        obstacle_x.append(i)
        obstacle_y.append(j-1)
        j -= 1


    # outline exit/enter 1
    for i in range(0, 3):
        obstacle_y.append(i)
        obstacle_x.append(20)
    for i in range(0, 3):
        obstacle_y.append(i)
        obstacle_x.append(23)

    # outline obst around x=10
    for i in range(11, 17):
        obstacle_x.append(i)
        obstacle_y.append(22)
    for i in range(9, 22):
        obstacle_y.append(i)
        obstacle_x.append(11)
    for i in range(3, 22):
        obstacle_y.append(i)
        obstacle_x.append(16)

    # outline obst around x=30
    for i in range(30, 34):
        obstacle_x.append(i)
        obstacle_y.append(22)
    for i in range(37, 41):
        obstacle_x.append(i)
        obstacle_y.append(22)
    for i in range(0, 22):
        obstacle_y.append(i)
        obstacle_x.append(30)
    for i in range(0, 22):
        obstacle_y.append(i)
        obstacle_x.append(40)



    # outline obst rectangle in the middle
    for i in range(25, 40):
        obstacle_x.append(20)
        obstacle_y.append(i)
    for i in range(25, 40):
        obstacle_x.append(25)
        obstacle_y.append(i)
    for i in range(20, 26):
        obstacle_x.append(i)
        obstacle_y.append(25)
    for i in range(20, 26):
        obstacle_x.append(i)
        obstacle_y.append(40)

    # outline obst around x = 0
    for i in range(30, 33):
        obstacle_x.append(10)
        obstacle_y.append(i)
    for i in range(36, 40):
        obstacle_x.append(10)
        obstacle_y.append(i)
    for i in range(0, 11):
        obstacle_x.append(i)
        obstacle_y.append(30)
    for i in range(0, 11):
        obstacle_x.append(i)
        obstacle_y.append(40)


    # outline obst
    for i in range(30, 45):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(40, 60):
        obstacle_y.append(i)
        obstacle_x.append(30)
    for i in range(40, 55):
        obstacle_y.append(i)
        obstacle_x.append(45)

    # outline obst
    for i in range(40, 60):
        obstacle_x.append(i)
        obstacle_y.append(20)
    for i in range(0, 20):
        obstacle_y.append(i)
        obstacle_x.append(40)

    # outline exit/enter 2
    for i in range(57, 61):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(57, 61):
        obstacle_x.append(i)
        obstacle_y.append(37)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_9(obstacle_x, obstacle_y):
    #  outline of room
    for i in range(30, 61):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in range(0,61):
        obstacle_x.append(60.0)
        obstacle_y.append(i)
    for i in range(30,61):
        obstacle_x.append(i)
        obstacle_y.append(60.0)


    j = 0
    for i in range(30, 61):
        obstacle_x.append(j+1)
        obstacle_y.append(i)
        j += 1


    j = 30
    for i in range(0, j):
        obstacle_x.append(i)
        obstacle_y.append(j-1)
        j -= 1


    # outline exit/enter 1
    for i in range(10, 13):
        obstacle_y.append(i)
        obstacle_x.append(20)
    for i in range(7, 13):
        obstacle_y.append(i)
        obstacle_x.append(23)

    # outline obst around x=10
    for i in range(11, 17):
        obstacle_x.append(i)
        obstacle_y.append(22)
    for i in range(18, 22):
        obstacle_y.append(i)
        obstacle_x.append(11)
    for i in range(13, 22):
        obstacle_y.append(i)
        obstacle_x.append(16)

    # outline obst around x=30
    for i in range(30, 34):
        obstacle_x.append(i)
        obstacle_y.append(22)
    for i in range(37, 41):
        obstacle_x.append(i)
        obstacle_y.append(22)
    for i in range(0, 22):
        obstacle_y.append(i)
        obstacle_x.append(30)
    for i in range(0, 22):
        obstacle_y.append(i)
        obstacle_x.append(40)



    # outline obst rectangle in the middle
    for i in range(25, 40):
        obstacle_x.append(20)
        obstacle_y.append(i)
    for i in range(25, 40):
        obstacle_x.append(25)
        obstacle_y.append(i)
    for i in range(20, 26):
        obstacle_x.append(i)
        obstacle_y.append(25)
    for i in range(20, 26):
        obstacle_x.append(i)
        obstacle_y.append(40)


    # outline obst
    for i in range(30, 34):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(37, 45):
        obstacle_x.append(i)
        obstacle_y.append(40)

    for i in range(40, 60):
        obstacle_y.append(i)
        obstacle_x.append(30)
    for i in range(40, 45):
        obstacle_y.append(i)
        obstacle_x.append(45)
    for i in range(48, 60):
        obstacle_y.append(i)
        obstacle_x.append(45)


    # outline obst
    for i in range(40, 60):
        obstacle_x.append(i)
        obstacle_y.append(20)
    for i in range(0, 20):
        obstacle_y.append(i)
        obstacle_x.append(40)

    # outline exit/enter 2
    for i in range(57, 61):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(57, 61):
        obstacle_x.append(i)
        obstacle_y.append(37)

    return obstacle_x, obstacle_y


def outline_obstacles_demo_building_10(obstacle_x, obstacle_y):
    #  outline of room
    for i in range(0, 40):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in range(21,61):
        obstacle_x.append(60.0)
        obstacle_y.append(i)
    for i in range(21,61):
        obstacle_x.append(i)
        obstacle_y.append(60.0)
    for i in range(0,41):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    j = 0
    for i in range(40, 61):
        obstacle_x.append(j+1)
        obstacle_y.append(i)
        j += 1

    j = 0
    for i in range(40, 61):
        obstacle_x.append(i)
        obstacle_y.append(j+1)
        j += 1


    # outline exit/enter 1
    for i in range(0, 3):
        obstacle_y.append(i)
        obstacle_x.append(20)
    for i in range(0, 3):
        obstacle_y.append(i)
        obstacle_x.append(23)

    # outline obst around x=10
    for i in range(0, 17):
        obstacle_x.append(i)
        obstacle_y.append(22)
    for i in range(0, 17):
        obstacle_x.append(i)
        obstacle_y.append(10)
    for i in range(10, 22):
        obstacle_y.append(i)
        obstacle_x.append(16)

    # outline obst around x=30
    for i in range(30, 34):
        obstacle_x.append(i)
        obstacle_y.append(22)
    for i in range(37, 41):
        obstacle_x.append(i)
        obstacle_y.append(22)
    for i in range(0, 22):
        obstacle_y.append(i)
        obstacle_x.append(30)
    for i in range(0, 22):
        obstacle_y.append(i)
        obstacle_x.append(40)


    # outline obst rectangle in the middle
    for i in range(25, 40):
        obstacle_x.append(20)
        obstacle_y.append(i)
    for i in range(25, 40):
        obstacle_x.append(25)
        obstacle_y.append(i)
    for i in range(20, 26):
        obstacle_x.append(i)
        obstacle_y.append(25)
    for i in range(20, 26):
        obstacle_x.append(i)
        obstacle_y.append(40)

    # outline obst around x = 0
    for i in range(30, 33):
        obstacle_x.append(10)
        obstacle_y.append(i)
    for i in range(36, 40):
        obstacle_x.append(10)
        obstacle_y.append(i)
    for i in range(0, 11):
        obstacle_x.append(i)
        obstacle_y.append(30)
    for i in range(0, 11):
        obstacle_x.append(i)
        obstacle_y.append(40)


    # outline obst
    for i in range(30, 36):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(39, 45):
        obstacle_x.append(i)
        obstacle_y.append(40)
    for i in range(40, 60):
        obstacle_y.append(i)
        obstacle_x.append(30)
    for i in range(40, 60):
        obstacle_y.append(i)
        obstacle_x.append(45)

    # outline obst
    for i in range(40, 60):
        obstacle_x.append(i)
        obstacle_y.append(20)
    for i in range(0, 20):
        obstacle_y.append(i)
        obstacle_x.append(40)

    # outline obst
    for i in range(55, 60):
        obstacle_x.append(i)
        obstacle_y.append(25)
    for i in range(55, 60):
        obstacle_x.append(i)
        obstacle_y.append(35)
    for i in range(25, 29):
        obstacle_y.append(i)
        obstacle_x.append(55)
    for i in range(32, 36):
        obstacle_y.append(i)
        obstacle_x.append(55)

    # outline exit/enter 2
    for i in range(57, 61):
        obstacle_y.append(i)
        obstacle_x.append(52)
    for i in range(57, 61):
        obstacle_y.append(i)
        obstacle_x.append(55)

    return obstacle_x, obstacle_y


def outline_obstacles_floor_one_other(obstacle_x, obstacle_y):
    #   Room outline
    for i in range(15):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in range(21, 60):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in range(45):
        obstacle_x.append(60.0)
        obstacle_y.append(i)
    for i in range(50, 60):
        obstacle_x.append(60.0)
        obstacle_y.append(i)
    for i in range(61):
        obstacle_x.append(i)
        obstacle_y.append(60.0)
    for i in range(61):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    # left class
    for i in range(10, 30):
        obstacle_x.append(10.0)
        obstacle_y.append(i)
    for i in range(11):
        obstacle_x.append(i)
        obstacle_y.append(10.0)
    for i in range(11):
        obstacle_x.append(i)
        obstacle_y.append(30)

    ##
    # top left class
    for i in range(11):
        obstacle_x.append(i)
        obstacle_y.append(45.0)
    for i in range(45, 60):
        obstacle_x.append(10.0)
        obstacle_y.append(i)

    # toilet near top left class
    for i in range(11, 16):
        obstacle_x.append(i)
        obstacle_y.append(50.0)
    for i in range(50, 60):
        obstacle_x.append(15)
        obstacle_y.append(i)
    # elevator
    for i in range(25, 36):
        obstacle_x.append(i)
        obstacle_y.append(58.0)
    for i in range(3):
        obstacle_x.append(25)
        obstacle_y.append(60 - i)
    for i in range(3):
        obstacle_x.append(35)
        obstacle_y.append(60 - i)

    # top right stairs
    for i in range(45, 51):
        obstacle_x.append(i)
        obstacle_y.append(58.0)
    for i in range(3):
        obstacle_x.append(45)
        obstacle_y.append(60 - i)
    for i in range(3):
        obstacle_x.append(50)
        obstacle_y.append(60 - i)

    # top right class
    for i in range(51, 60):
        obstacle_x.append(i)
        obstacle_y.append(55.0)
    for i in range(6):
        obstacle_x.append(51)
        obstacle_y.append(60 - i)
    for i in range(6):
        obstacle_x.append(60)
        obstacle_y.append(60 - i)

    # end of building in right corner
    for i in range(50, 60):
        obstacle_x.append(i)
        obstacle_y.append(10)
    for i in range(11):
        obstacle_x.append(50)
        obstacle_y.append(i)

    # stairs + class right side of building
    for i in range(50, 60):
        obstacle_x.append(i)
        obstacle_y.append(20.0)
    for i in range(20, 40):
        obstacle_x.append(50.0)
        obstacle_y.append(i)
    for i in range(50, 60):
        obstacle_x.append(i)
        obstacle_y.append(40.0)

    # obstacles near class
    for i in range(45, 50):
        obstacle_x.append(i)
        obstacle_y.append(20.0)
    for i in range(20, 30):
        obstacle_x.append(45.0)
        obstacle_y.append(i)
    for i in range(45, 50):
        obstacle_x.append(i)
        obstacle_y.append(30.0)

    return obstacle_x, obstacle_y


def outline_obstacles_floor_one(obstacle_x, obstacle_y):
    # Room outline
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
    for i in range(7):
        obstacle_x.append(10.0)
        obstacle_y.append(i)

    # stairs bottom left
    for i in range(16, 21):
        obstacle_x.append(i)
        obstacle_y.append(3)
    for i in range(3, 9):
        obstacle_x.append(16)
        obstacle_y.append(i)
    for i in range(3, 9):
        obstacle_x.append(21)
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
    for i in range(7):
        obstacle_x.append(50.0)
        obstacle_y.append(i)

    # toilet near bottom right class
    # for i in range(47, 50):
    #     obstacle_x.append(i)
    #     obstacle_y.append(7)
    for i in range(8):
        obstacle_x.append(47)
        obstacle_y.append(i)

    # mid left class
    for i in range(10):
        obstacle_x.append(i)
        obstacle_y.append(40.0)
    for i in range(10):
        obstacle_x.append(i)
        obstacle_y.append(55.0)
    for i in range(40, 52):
        obstacle_x.append(10)
        obstacle_y.append(i)
    for i in range(10):
        obstacle_x.append(i)
        obstacle_y.append(48)

    # # top left stairs
        # middle stairs
    for i in range(25, 35):
        obstacle_x.append(10.0)
        obstacle_y.append(i)
    for i in range(25, 35):
        obstacle_x.append(16.0)
        obstacle_y.append(i)
    for i in range(10, 16):
        obstacle_x.append(i)
        obstacle_y.append(25.0)
    # for i in range(20, 33):
    #     obstacle_x.append(20.0)
    #     obstacle_y.append(i)
    # for i in range(20, 25):
    #     obstacle_x.append(i)
    #     obstacle_y.append(20)
    # for i in range(20, 33):
    #     obstacle_x.append(25)
    #     obstacle_y.append(i)

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

    return obstacle_x, obstacle_y


def outline_obstacles_floor_two_and_three(obstacle_x, obstacle_y):
    #   Room outline
    for i in range(60):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in range(60):
        obstacle_x.append(60.0)
        obstacle_y.append(i)
    for i in range(61):
        obstacle_x.append(i)
        obstacle_y.append(60.0)
    for i in range(61):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    # two classes bottom left
    for i in range(10):
        obstacle_x.append(i)
        obstacle_y.append(10.0)
    for i in range(11):
        obstacle_x.append(10.0)
        obstacle_y.append(i)
    for i in range(11):
        obstacle_x.append(15.0)
        obstacle_y.append(i)
    for i in range(11, 15):
        obstacle_x.append(i)
        obstacle_y.append(10.0)

    # stairs bottom left
    for i in range(16, 21):
        obstacle_x.append(i)
        obstacle_y.append(3)
    for i in range(3, 9):
        obstacle_x.append(16)
        obstacle_y.append(i)
    for i in range(3, 9):
        obstacle_x.append(21)
        obstacle_y.append(i)
    # bottom elevator
    for i in range(28, 34):
        obstacle_x.append(i)
        obstacle_y.append(3)
    for i in range(4):
        obstacle_x.append(28)
        obstacle_y.append(i)
    for i in range(4):
        obstacle_x.append(34)
        obstacle_y.append(i)

    # toilets
    for i in range(42, 53):
        obstacle_x.append(i)
        obstacle_y.append(8.0)
    for i in range(8):
        obstacle_x.append(42)
        obstacle_y.append(i)
    for i in range(9):
        obstacle_x.append(53)
        obstacle_y.append(i)

    # faculty offices
    for i in range(56, 60):
        obstacle_x.append(i)
        obstacle_y.append(8.0)
    for i in range(8):
        obstacle_x.append(56.0)
        obstacle_y.append(i)

    # big class number 1
    for i in range(45, 60):
        obstacle_x.append(i)
        obstacle_y.append(20.0)
    for i in range(45, 60):
        obstacle_x.append(i)
        obstacle_y.append(35.0)
    for i in range(20, 33):
        obstacle_x.append(45.0)
        obstacle_y.append(i)

    # big class number 2
    for i in range(45, 60):
        obstacle_x.append(i)
        obstacle_y.append(37.0)
    for i in range(45, 60):
        obstacle_x.append(i)
        obstacle_y.append(52.0)
    for i in range(37, 45):
        obstacle_x.append(45.0)
        obstacle_y.append(i)

    # benches
    for i in range(25, 35):
        obstacle_x.append(i)
        obstacle_y.append(57)
    for i in range(4):
        obstacle_x.append(25)
        obstacle_y.append(60 - i)
    for i in range(4):
        obstacle_x.append(35)
        obstacle_y.append(60 - i)

    # balcony
    for i in range(55, 60):
        obstacle_x.append(5.0)
        obstacle_y.append(i)
    for i in range(5):
        obstacle_x.append(i)
        obstacle_y.append(55.0)
    for i in range(5):
        obstacle_x.append(i)
        obstacle_y.append(60.0)

    # middle stairs
    for i in range(25, 35):
        obstacle_x.append(10.0)
        obstacle_y.append(i)
    for i in range(25, 35):
        obstacle_x.append(16.0)
        obstacle_y.append(i)
    for i in range(10, 16):
        obstacle_x.append(i)
        obstacle_y.append(25.0)

    return obstacle_x, obstacle_y


def outline_obstacles_floor_four(obstacle_x, obstacle_y):
    #  outline of room
    for i in range(0, 60):
        obstacle_x.append(i)
        obstacle_y.append(0.0)
    for i in range(60):
        obstacle_x.append(60.0)
        obstacle_y.append(i)
    for i in range(61):
        obstacle_x.append(i)
        obstacle_y.append(60.0)
    for i in range(61):
        obstacle_x.append(0.0)
        obstacle_y.append(i)

    # stairs bottom left
    for i in range(16, 21):
        obstacle_x.append(i)
        obstacle_y.append(3)
    for i in range(3, 9):
        obstacle_x.append(16)
        obstacle_y.append(i)
    for i in range(3, 9):
        obstacle_x.append(21)
        obstacle_y.append(i)

    # Lecture hall
    for i in range(35, 60):
        obstacle_x.append(i)
        obstacle_y.append(20.0)
    for i in range(35, 60):
        obstacle_x.append(i)
        obstacle_y.append(45.0)
    for i in range(20, 25):
        obstacle_x.append(35)
        obstacle_y.append(i)
    for i in range(29, 42):
        obstacle_x.append(35)
        obstacle_y.append(i)

    # small room under hall
    for i in range(57, 60):
        obstacle_x.append(i)
        obstacle_y.append(15.0)
    for i in range(57, 60):
        obstacle_x.append(i)
        obstacle_y.append(10.0)
    for i in range(10, 15):
        obstacle_x.append(57.0)
        obstacle_y.append(i)

    # toilets
    for i in range(46, 56):
        obstacle_x.append(i)
        obstacle_y.append(7.0)
    for i in range(8):
        obstacle_x.append(46.0)
        obstacle_y.append(i)
    for i in range(8):
        obstacle_x.append(56.0)
        obstacle_y.append(i)

    # elevator
    for i in range(26, 38):
        obstacle_x.append(i)
        obstacle_y.append(3.0)
    for i in range(4):
        obstacle_x.append(26)
        obstacle_y.append(i)
    for i in range(4):
        obstacle_x.append(38)
        obstacle_y.append(i)

    # faculty offices
    for i in range(6):
        obstacle_x.append(i)
        obstacle_y.append(20.0)
    for i in range(21):
        obstacle_x.append(6.0)
        obstacle_y.append(i)

    # more offices
    for i in range(6):
        obstacle_x.append(i)
        obstacle_y.append(50.0)
    for i in range(9):
        obstacle_x.append(i)
        obstacle_y.append(30.0)
    for i in range(30, 51):
        obstacle_x.append(9.0)
        obstacle_y.append(i)

    # stairs near offices
        # middle stairs
    for i in range(25, 35):
        obstacle_x.append(10.0)
        obstacle_y.append(i)
    for i in range(25, 35):
        obstacle_x.append(16.0)
        obstacle_y.append(i)
    for i in range(10, 16):
        obstacle_x.append(i)
        obstacle_y.append(25.0)
    # for i in range(6, 11):
    #     obstacle_x.append(i)
    #     obstacle_y.append(30.0)
    # for i in range(30, 51):
    #     obstacle_x.append(11.0)
    #     obstacle_y.append(i)

    # # exhibit
    # for i in range(6, 12):
    #     obstacle_x.append(i)
    #     obstacle_y.append(26.0)
    # for i in range(26, 30):
    #     obstacle_x.append(6.0)
    #     obstacle_y.append(i)
    # for i in range(26, 30):
    #     obstacle_x.append(11.0)
    #     obstacle_y.append(i)

    # benches - top
    for i in range(20, 33):
        obstacle_x.append(i)
        obstacle_y.append(57.0)
    for i in range(4):
        obstacle_x.append(20)
        obstacle_y.append(60 - i)
        for i in range(4):
            obstacle_x.append(33)
            obstacle_y.append(60 - i)

    return obstacle_x, obstacle_y
