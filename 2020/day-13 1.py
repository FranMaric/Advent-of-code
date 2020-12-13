
f = open(r"C:\Users\fran-\Desktop\Advent-of-code\2020\input.txt", 'r')
data = f.read().split('\n')
f.close()
timestamp = int(data[0])
buses = data[1].split(',')

for i in range(len(buses)-1, -1, -1):
    if buses[i] == 'x':
        buses.pop(i)

buses = list(map(int, buses))

smallestWaitTime = 0
smallestIndex = 0

for i in range(len(buses)):
    d = timestamp
    while d % buses[i] != 0:
        d += 1
    if i == 0 or d-timestamp < smallestWaitTime:
        smallestIndex = i
        smallestWaitTime = d-timestamp

print(smallestWaitTime*buses[smallestIndex])
