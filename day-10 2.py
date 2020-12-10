f = open('input.txt', 'r')
jolts = list(map(int, f.read().split('\n')))
f.close()

jolts = sorted(jolts)

memo = {}


def recursion(index):
    if index == len(jolts)-1:
        return True

    for i in range(1, 4):
        if jolts[index]+i in jolts:
            recursion(jolts.index(jolts[index]+i))


output = recursion(0)


print(output)
