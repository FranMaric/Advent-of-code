f = open('input.txt', 'r')
answers = [i.replace(' ', '').replace('\n', '')
           for i in f.read().split('\n\n')]
f.close()

counter = 0

for answer in answers:
    counter += len(set(answer))

print(counter)
