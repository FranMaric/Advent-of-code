matrica=open('input.txt','r').read().split('\n')

counter=0

for i in range(1,len(matrica)):
    if matrica[i][(i*3)%len(matrica[0])]=='#':
        counter+=1

print(counter)