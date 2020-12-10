file=open('input.txt', 'r').read()

brojevi=list(map(int, file.split('\n')))

for i in range(len(brojevi)):
    for j in range(len(brojevi)):
        for k in range(len(brojevi)):
            if brojevi[i]+brojevi[j]+brojevi[k]==2020:
                print('Rjesnje:',brojevi[i]*brojevi[j]*brojevi[k])
                quit()