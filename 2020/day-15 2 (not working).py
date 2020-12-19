f = open('input.txt', 'r')
numbers = list(map(int, f.read().split(',')))
f.close()

numbers = [0, 3, 6]

for i in range(len(numbers), 30000000):
    if numbers.count(numbers[i-1]) > 1:
        numbers.append(i-1-numbers[:-1][::-1].index(numbers[i-1]))
    else:
        numbers.append(0)

print(numbers[-1])
