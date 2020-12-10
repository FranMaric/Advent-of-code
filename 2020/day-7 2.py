f = open('input.txt', 'r')
ulaz = f.read().split('\n')
f.close()

bags = {}

for i in range(len(ulaz)):
    bag, contains = ulaz[i].split(' bags contain ')
    if ', ' not in contains:
        if contains == 'no other bags.':
            bags[bag] = {}
            continue
        else:
            contains = [contains]
    else:
        contains = contains.split(', ')

    content = {}

    for k in range(len(contains)):
        contains[k] = contains[k].split(' ')
        content[' '.join(contains[k][1:-1])] = int(contains[k][0])

    bags[bag] = content

the_one = 'shiny gold'
global_counter = 0


def recursion(looking_in, multiplier=1):
    global global_counter
    for bag in bags[looking_in].keys():
        global_counter += bags[looking_in][bag]*multiplier
        recursion(bag, multiplier*bags[looking_in][bag])


recursion(the_one)

print(global_counter)
