import copy


def rotateFromTo(previous, nextt):
    prevWaypoint = copy.deepcopy(waypoint)

    waypoint[0] = sign[previous][nextt][0] * \
        prevWaypoint[converter[previous][nextt][0]]
    waypoint[1] = sign[previous][nextt][1] * \
        prevWaypoint[converter[previous][nextt][1]]


f = open('input.txt', 'r')
directions = [[i[0], int(i[1:])] for i in f.read().split('\n')]
f.close()

converter = [[[0, 1], [1, 0], [0, 1], [1, 0]],
             [[1, 0], [0, 1], [1, 0], [0, 1]],
             [[0, 1], [1, 0], [0, 1], [1, 0]],
             [[1, 0], [0, 1], [1, 0], [0, 1]]]

sign = [[[1, 1], [-1, 1], [-1, -1], [1, -1]],
        [[1, -1], [1, 1], [-1, 1], [-1, -1]],
        [[-1, -1], [1, -1], [1, 1], [-1, 1]],
        [[-1, 1], [-1, -1], [1, -1], [1, 1]]]


x, y, rotation = 0, 0, 0
waypoint = [10, 1]

for i in directions:
    if i[0] == 'R':
        previousRotation = rotation
        rotation -= i[1]//90
        rotation = rotation % 4
        if rotation < 0:
            rotation = 4-rotation
        rotateFromTo(previousRotation, rotation)

    elif i[0] == 'L':
        previousRotation = rotation
        rotation += i[1]//90
        rotation = rotation % 4
        rotateFromTo(previousRotation, rotation)

    elif i[0] == 'F':
        x += i[1]*waypoint[0]
        y += i[1]*waypoint[1]

    elif i[0] == 'N':
        waypoint[1] += i[1]
    elif i[0] == 'S':
        waypoint[1] -= i[1]
    elif i[0] == 'E':
        waypoint[0] += i[1]
    elif i[0] == 'W':
        waypoint[0] -= i[1]


print(abs(x)+abs(y))
