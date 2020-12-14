
def binaryToDecimal(num):
    output = 0
    for i in range(len(num)):
        if num[-(i+1)] == '1':
            output += 2**i
    return output


def decimalToBinary(num, zfill=36):
    return bin(int(num))[2:].zfill(zfill)


f = open('input.txt', 'r')
instructions = f.read().split('\n')
f.close()

mask = ''

memory = {}

for instruction in instructions:
    instruction = instruction.split(' = ')
    if instruction[0] == 'mask':
        mask = instruction[1]
    else:
        address = list(decimalToBinary(
            instruction[0][4:instruction[0].index(']')]))
        number = list(decimalToBinary(instruction[1]))

        for i in range(len(mask)):
            if mask[i] == '1':
                address[i] = '1'

        x_count = mask.count('X')
        if x_count > 0:
            for i in range(2**x_count):
                i = decimalToBinary(i, zfill=x_count)

                indexCounter = 0
                for j in range(len(address)):
                    if mask[j] == 'X':
                        address[j] = i[indexCounter]
                        indexCounter += 1

                memory[''.join(address)] = ''.join(number)
        else:
            memory[''.join(address)] = ''.join(number)

suma = 0
for address in memory.keys():
    suma += binaryToDecimal(memory[address])
print(suma)
