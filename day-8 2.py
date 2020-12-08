f = open('input.txt', 'r')
instructions = [i.split(' ') for i in f.read().split('\n')]
f.close()

accumulators = []


def run_instructions(instructions):
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

    if i == len(instructions):
        return [True, accumulator]
    return [False]


for j in range(len(instructions)):
    if instructions[j][0] == 'jmp':
        instructions[j][0] = 'nop'
    elif instructions[j][0] == 'nop':
        instructions[j][0] = 'jmp'
    else:
        continue

    halts = run_instructions(instructions)

    if halts[0] == True:
        accumulators.append(halts[1])

    if instructions[j][0] == 'jmp':
        instructions[j][0] = 'nop'
    elif instructions[j][0] == 'nop':
        instructions[j][0] = 'jmp'

print(list(set(accumulators))[0])
