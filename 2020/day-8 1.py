f = open('input.txt', 'r')
instructions = [i.split(' ') for i in f.read().split('\n')]
f.close()

accumulator = 0
done_instructions = [0 for i in range(len(instructions))]

i = 0
while i < len(instructions) and done_instructions[i] == 0:
    done_instructions[i] = 1
    if instructions[i][0] == 'acc':
        accumulator += int(instructions[i][1])
    elif instructions[i][0] == 'jmp':
        i += int(instructions[i][1])
        continue

    i += 1

print(accumulator)
