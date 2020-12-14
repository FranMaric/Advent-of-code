
def binaryToDecimal(num):
    output = 0
    for i in range(len(num)):
        if num[-(i+1)] == '1':
            output += 2**i
    return output


def decimalToBinary(num):
    return bin(int(num))[2:].zfill(36)


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
        index = int(instruction[0][4:instruction[0].index(']')])
        number = list(decimalToBinary(instruction[1]))
        for i in range(len(mask)):
            if mask[i] != 'X':
                number[i] = mask[i]
        memory[index] = ''.join(number)

suma = 0
for address in memory.keys():
    suma += binaryToDecimal(memory[address])
print(suma)
