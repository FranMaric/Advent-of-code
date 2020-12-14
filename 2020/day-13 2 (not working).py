
f = open(r"C:\Users\fran-\Desktop\Advent-of-code\2020\input.txt", 'r')
data = f.read().split('\n')
f.close()

buses = data[1].split(',')

for i in range(len(buses)):
    try:
        buses[i] = int(buses[i])
    except:
        pass

start = 100000000000000

indexes = [i for i in range(len(buses)) if buses[i] != 'x']

while True:
    found = True
    for i in indexes:
        if (start+i) % buses[i] != 0:
            found = False
            break

    if found:
        print(start)
        break

    start += buses[indexes[0]]
