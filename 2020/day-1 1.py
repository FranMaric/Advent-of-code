file=open('input.txt', 'r').read()

brojevi=list(map(int, file.split('\n')))

for i in range(len(brojevi)):
    for j in range(len(brojevi)):
        if brojevi[i]+brojevi[j]==2020:
            print('Rjesnje:',brojevi[i]*brojevi[j])
            quit()