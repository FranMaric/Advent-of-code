f = open('input.txt', 'r')
data = list(map(int, f.read().split('\n')))
f.close()

preamble = 25

for i in range(preamble, len(data)):
    start = 0 if i-preamble < 0 else i-preamble

    found_one = False
    for num1 in data[start:i]:
        for num2 in data[start:i]:
            if num1+num2 == data[i]:
                found_one = True
                break
    if not found_one:
        print(data[i])
        break
