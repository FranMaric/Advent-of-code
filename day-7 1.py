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


def this_in_this(looking_for, looking_in):
    if looking_for in bags[looking_in].keys():
        return True

    for bag in bags[looking_in].keys():
        if this_in_this(looking_for, bag):
            return True


counter = 0
for i in bags.keys():
    if this_in_this(the_one, i):
        counter += 1

print(counter)
