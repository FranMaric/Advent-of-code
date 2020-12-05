f=open('input.txt','r')
data=f.read()
f.close()

data=[i.replace('\n',' ') for i in data.split('\n\n')]

should_contain=('byr','iyr','eyr','hgt','hcl','ecl','pid')

valid_counter=0

def extract(what, from_where):
    if not what in from_where:
        return '0'
    output=from_where.split(what+':')[1].split(' ')
    if type(output)==list:
        return output[0]
    else:
        return output

for passport in data:
    if not 1920<=int(extract('byr', passport))<=2020:
        continue
    if not 2010<=int(extract('iyr', passport))<=2020:
        continue    
    if not 2020<=int(extract('eyr', passport))<=2030:
        continue
    
    if 'hgt:' not in passport:
        continue
    height=extract('hgt', passport)
    
    if 'cm' in height:
        if not 150<=int(height.replace('cm',''))<=193:
            continue
    elif 'in' in height:
        if not 59<=int(height.replace('in',''))<=76:
            continue
    else:
        continue
    
    if 'hcl:' not in passport:
        continue
    hcl=extract('hcl', passport)
    if hcl[0]!='#' or len(hcl)!=7:
        continue
    for i in hcl[1:]:
        if i not in '01234567890abcdef':
            hcl='kurac'
            break
    if hcl=='kurac':
        continue
    
    if not extract('ecl', passport) in 'amb blu brn gry grn hzl oth':
        continue
    if len(extract('pid', passport))!=9:
        continue
    
    valid_counter+=1
    
print(valid_counter)