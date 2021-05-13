S = list(input())
Ncnt, Ecnt, Wcnt, Scnt = 0, 0, 0, 0

for i in S:
    if i == 'N':
        Ncnt += 1
    elif i == 'E':
        Ecnt += 1
    elif i == 'W':
        Wcnt += 1
    else:
        Scnt += 1

if (Ncnt > 0 and Scnt == 0) or (Scnt > 0 and Ncnt == 0) or (Ecnt > 0 and Wcnt == 0) or (Wcnt > 0 and Ecnt == 0):
    print('No')
else:
    print('Yes')