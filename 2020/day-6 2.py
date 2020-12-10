f = open('input.txt', 'r')
answers = [i.replace(' ', '').split('\n')
           for i in f.read().split('\n\n')]
f.close()

counter = 0

for answer in answers:
    for i in range(len(answer[0])):
        add_one = True
        for j in range(len(answer)):
            if answer[0][i] not in answer[j]:
                add_one = False
        if add_one:
            counter += 1

print(counter)
