matrica=open('input.txt','r').read().split('\n')

counter=[0,0,0,0,0]

for i in range(1,len(matrica)):
    if matrica[i][i%len(matrica[0])]=='#':
        counter[0]+=1
        
    if matrica[i][(i*3)%len(matrica[0])]=='#':
        counter[1]+=1
        
    if matrica[i][(i*5)%len(matrica[0])]=='#':
        counter[2]+=1
        
    if matrica[i][(i*7)%len(matrica[0])]=='#':
        counter[3]+=1

for i in range(2,len(matrica),2):
    if matrica[i][(i//2)%len(matrica[0])]=='#':
        counter[4]+=1
rez=1
for i in range(len(counter)):
    rez*=counter[i]

print(rez)