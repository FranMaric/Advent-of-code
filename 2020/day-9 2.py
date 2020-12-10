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
        invalid = data[i]
        invalid_index = i
        break

data.pop(invalid_index)

for length in range(2, invalid_index+1):
    for start in range(0, invalid_index-length+1):
        suma = 0
        for j in range(start, start+length):
            suma += data[j]
        if suma == invalid:
            candidats = [data[j] for j in range(start, start+length)]
            print(min(candidats)+max(candidats))

for length in range(2, len(data)-invalid_index-1):
    for start in range(invalid_index+1, len(data)-length):
        suma = 0
        for j in range(start, start+length):
            suma += data[j]
        if suma == invalid:
            candidats = [data[j] for j in range(start, start+length)]
            print(min(candidats)+max(candidats))
