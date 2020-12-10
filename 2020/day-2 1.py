lines=open('input.txt','r').read().split('\n')
valid=0

for line in lines:
    line=line.split(' ')
    length=line[0].split('-')
    line[1]=line[1].replace(':','')
    if int(length[0])<=line[2].count(line[1])<=int(length[1]):
        valid+=1
print(valid)
    