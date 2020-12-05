

def convert(string):
    if len(string) != 10:
        return 'Length must be equal to 10 !!!'
    row = [0, 127]
    column = [0, 7]
    for i in range(7):
        if string[i] == 'F':
            row[1] = (row[1]+row[0])//2
        elif string[i] == 'B':
            row[0] = (row[1]+row[0])//2

    for i in range(6, 10):
        if string[i] == 'L':
            column[1] = (column[1]+column[0])//2
        elif string[i] == 'R':
            column[0] = (column[1]+column[0])//2

    return (column[1], row[1])


f = open('input.txt', 'r')
data = f.read().split('\n')
f.close()

output = []

for i in range(len(data)):
    pos = convert(data[i])
    seatID = pos[1]*8 + pos[0]
    output.append(seatID)

for i in range(min(output), max(output)):
    if i not in output:
        print(i)
