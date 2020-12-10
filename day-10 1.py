f = open('input.txt', 'r')
jolts = list(map(int, f.read().split('\n')))
f.close()

jolts = sorted(jolts)
jolts.insert(0, 0)

one_diff = 0
three_diff = 1

for i in range(len(jolts)-1):
    if jolts[i+1]-jolts[i] == 1:
        one_diff += 1

    elif jolts[i+1]-jolts[i] == 3:
        three_diff += 1

print(one_diff * three_diff)
