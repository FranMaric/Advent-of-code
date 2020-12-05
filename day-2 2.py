lines=open('input.txt','r').read().split('\n')
valid=0

for line in lines:
    line=line.split(' ')
    length=line[0].split('-')
    line[1]=line[1].replace(':','')
    
    if line[2][int(length[0])-1]==line[1] and line[2][int(length[1])-1]!=line[1] or line[2][int(length[0])-1]!=line[1] and line[2][int(length[1])-1]==line[1]:
        valid+=1
        
print(valid)
    