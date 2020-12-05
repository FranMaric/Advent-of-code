f=open('input.txt','r')
data=f.read()
f.close()

data=[i.replace('\n',' ') for i in data.split('\n\n')]

should_contain=('byr','iyr','eyr','hgt','hcl','ecl','pid')

valid_counter=0
for passport in data:
    valid=True
    for i in should_contain:
        if i not in passport:
            valid=False
    if valid:
        valid_counter+=1
        
print(valid_counter)