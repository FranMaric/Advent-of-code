f = open('input.txt', 'r')
directions = [[i[0], int(i[1:])] for i in f.read().split('\n')]
f.close()

x, y, rotation = 0, 0, 0

for i in directions:
    if i[0] == 'R':
        rotation -= i[1]/90
        rotation = rotation % 4
        if rotation < 0:
            rotation = 4-rotation
    elif i[0] == 'L':
        rotation += i[1]/90
        rotation = rotation % 4
    elif i[0] == 'F':
        if rotation == 2:
            x -= i[1]
        elif rotation == 0:
            x += i[1]
        elif rotation == 1:
            y += i[1]
        elif rotation == 3:
            y -= i[1]
    elif i[0] == 'N':
        y += i[1]
    elif i[0] == 'S':
        y -= i[1]
    elif i[0] == 'E':
        x += i[1]
    elif i[0] == 'W':
        x -= i[1]


print(abs(x)+abs(y))
