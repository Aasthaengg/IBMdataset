S = input()
I = []
for TS in S:
    if TS=='0':
        I.append('0')
    elif TS=='1':
        I.append('1')
    elif TS=='B' and len(I)>=1:
        del I[-1]
print(''.join(I))