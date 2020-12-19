f = open('input.txt', 'r')
numbers = list(map(int, f.read().split(',')))
f.close()

for i in range(len(numbers), 2020):
    if numbers.count(numbers[i-1]) > 1:
        for index in range(i-2, -1, -1):
            if numbers[index] == numbers[i-1]:
                numbers.append(i-1-index)
                break
    else:
        numbers.append(0)

print(numbers[-1])
